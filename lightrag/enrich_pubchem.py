"""Enrich existing PCM_RAG chemical entities with PubChem facts.

Shape 1 enrichment (see PLAN.md). Reads the persisted LightRAG graph, picks
chemical-entity candidates, LLM-judges them, resolves each to a PubChem CID,
and APPENDS a delimited PubChem-facts block onto the entity's description via
the running LightRAG server (/graph/entity/edit). Additive + idempotent:
original description text is preserved above the marker; re-runs replace the
block, never stack.

PRECONDITIONS:
  - LightRAG server UP and IDLE (no ingest running) at LIGHTRAG_URL.
  - ZAI_API_KEY set (glm-5.3 judge via z.ai).
  - Ollama UP at OLLAMA_URL for any write run (the server re-embeds edited descriptions;
    checked fail-fast, exit 3). Not needed for --dry-run / --selftest.

USAGE:
  python enrich_pubchem.py            # full run (writes to graph)
  python enrich_pubchem.py --dry-run  # enumerate+judge+fetch, NO writes
  python enrich_pubchem.py --refresh  # re-enrich nodes already marked
  python enrich_pubchem.py --limit 10 # cap candidates (testing)
  python enrich_pubchem.py --fix-blocks            # clean existing blocks (strip/rewrite), needs no ZAI key
  python enrich_pubchem.py --fix-blocks --dry-run  # same, log only, NO writes
  python enrich_pubchem.py --max-glm-tokens 500000  # stop cleanly once GLM has used N tokens (0 = no cap)
  python enrich_pubchem.py --ignore-resume  # start although RESUME.json says a quota stop is still active
  python enrich_pubchem.py --selftest # offline asserts, no network, no graph

EXIT CODES:
  0  ok
  1  fatal precondition (missing key / graphml)
  2  judge_error abort (>10% of names failed to judge)
  3  Ollama unreachable (write runs)
  4  stopped on GLM quota or --max-glm-tokens budget (resume later): judge.json is saved and
     data/enrich_cache/RESUME.json says when to re-run; stops BEFORE any PubChem fetch or graph write.
     Re-run the same command after reset_at; judged names, PubChem cache and graph markers skip finished work.
"""
import argparse
import asyncio
import json
import os
import re
import sys
import time
import xml.etree.ElementTree as ET
from datetime import datetime
from pathlib import Path

import httpx


# Force UTF-8 output encoding on Windows (handles chemical names with subscripts)
for _s in (sys.stdout, sys.stderr):
    if (getattr(_s, "encoding", "") or "").lower() not in ("utf-8", "utf8"):
        _s.reconfigure(encoding="utf-8", errors="replace")

# ---------------------------------------------------------------- config
SCRIPT_DIR = Path(__file__).parent
GRAPHML = SCRIPT_DIR / "data" / "rag_storage" / "graph_chunk_entity_relation.graphml"
CACHE_DIR = SCRIPT_DIR / "data" / "enrich_cache"
JUDGE_CACHE = CACHE_DIR / "judge.json"
RESUME_FILE = "RESUME.json"  # under CACHE_DIR; written on a GLM quota/budget stop (exit 4)
FACTS_VERSION = 3  # bump when fact parsing changes; stale-version CID cache files are re-fetched

LIGHTRAG_URL = os.environ.get("LIGHTRAG_URL", "http://127.0.0.1:9622")
def _load_lightrag_key():
    k = os.environ.get("LIGHTRAG_API_KEY")
    if k:
        return k
    envf = SCRIPT_DIR / ".env"
    if envf.exists():
        for line in envf.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line.startswith("LIGHTRAG_API_KEY="):
                return line.split("=", 1)[1].strip().strip('"').strip("'")
    raise SystemExit("LIGHTRAG_API_KEY not set (env var or lightrag/.env)")


LIGHTRAG_KEY = _load_lightrag_key()

OLLAMA_URL = os.environ.get("OLLAMA_URL", "http://127.0.0.1:11434")

ZAI_KEY = os.environ.get("ZAI_API_KEY", "")
ZAI_BASE = "https://api.z.ai/api/coding/paas/v4"
JUDGE_MODEL = "glm-5.3"

PUBCHEM = "https://pubchem.ncbi.nlm.nih.gov"
PUBCHEM_HEADERS = {
    "User-Agent": "PCM-RAG-enrich/1.0 (LightRAG PubChem enrichment; contact ilpin301@gmail.com)",
    "From": "ilpin301@gmail.com",
}

MARK_START = "<!--PUBCHEM_START-->"
MARK_END = "<!--PUBCHEM_END-->"
BLOCK_RE = re.compile(r"<!--PUBCHEM_START-->.*?<!--PUBCHEM_END-->", re.DOTALL)

TYPE_PATH = {"naturalobject", "material", "substance"}
REGEX_TYPES = {"concept", "artifact"}

# chemical-name regex (candidate-widener over concept/artifact; judge is real gate)
CHEM_TOKENS = re.compile(
    r"\b(acid|hydrate|paraffin|wax|glycol|erythritol|eutectic|oxide|nitrate|"
    r"sulfate|sulphate|chloride|carbonate|hydroxide|stearic|palmitic|lauric|"
    r"myristic|capric|oleic|PEG|Ag2O|Al2O3|CuO|ZnO|graphene oxide)\b",
    re.IGNORECASE,
)
CHEM_FORMULA = re.compile(r"^[A-Z][a-z]?\d|·|H2O|Na2|CaCl2")

GRAPHML_NS = "{http://graphml.graphdrawing.org/xmlns}"

# global PubChem throttle: flat 0.8s between calls
# (~1.25 req/s = 375 calls/5 min, under both the 5/s and 400/5-min caps)
PUBCHEM_MIN_INTERVAL = 0.8
_last_pubchem_call = 0.0


class FetchFailed(Exception):
    """PubChem fetch gave up after retries (network/429/503) - NOT the same as unresolved."""


def log(msg):
    print(msg, flush=True)


def require_ollama():
    """Fail fast before any graph write: the server embeds edited descriptions via Ollama, and with
    Ollama down the graph is written but the vector upserts stay queued in the server's memory."""
    try:
        httpx.get(f"{OLLAMA_URL}/api/version", timeout=5, trust_env=False).raise_for_status()
    except Exception:
        log(f"FATAL: Ollama not reachable at {OLLAMA_URL} - the server needs it to embed "
            "edited descriptions; start Ollama first")
        sys.exit(3)


# ---------------------------------------------------------------- step 1: enumerate
def _find_key(root, attr_name):
    """graphml <key> id for node attr `attr_name`, or None."""
    for k in root.iter(GRAPHML_NS + "key"):
        if k.get("for") == "node" and k.get("attr.name") == attr_name:
            return k.get("id")
    return None


def _find_type_key(root):
    """graphml <key> id for node attr 'entity_type', or None."""
    return _find_key(root, "entity_type")


def enumerate_candidates():
    """Union of TYPE path and chemical-regex-over-concept/artifact path, deduped by name."""
    if not GRAPHML.exists():
        log(f"FATAL: graphml not found at {GRAPHML}")
        sys.exit(1)
    root = ET.parse(GRAPHML).getroot()
    k_type = _find_type_key(root)
    if not k_type:
        log("FATAL: no node <key> with attr.name='entity_type' in graphml")
        sys.exit(1)
    cands = {}
    for node in root.iter(GRAPHML_NS + "node"):
        name = node.get("id")
        etype = None
        for data in node.findall(GRAPHML_NS + "data"):
            if data.get("key") == k_type:
                etype = data.text
                break
        if not name or not etype:
            continue
        if etype in TYPE_PATH:
            cands[name] = etype
        elif etype in REGEX_TYPES and (CHEM_TOKENS.search(name) or CHEM_FORMULA.search(name)):
            cands[name] = etype
    log(f"[enumerate] {len(cands)} candidates (type-path + regex-path, deduped)")
    return cands


# ---------------------------------------------------------------- step 2: LLM judge
JUDGE_SYSTEM = (
    "You classify entity names from a phase-change-material knowledge graph. "
    "Decide whether each name denotes a DISCRETE, PURE chemical compound whose "
    "thermophysical properties are relevant to PCM research and are lookupable in PubChem.\n\n"
    "Reply with EXACTLY ONE line:\n"
    "  COMPOUND: <canonical PubChem-lookupable name>\n"
    "  or\n"
    "  SKIP\n\n"
    "Rules:\n"
    "- SKIP abstractions/categories/processes (e.g. 'CO2 Emissions', 'Eutectic Structures', "
    "'Sp2 Bonds', 'Carbonate Group').\n"
    "- SKIP any SYSTEM / COMPOSITE / DERIVATIVE, even if a single base compound and CID are "
    "extractable. Trigger tokens: PCM, PCMs, Eutectic, Hybrid, infused, Nano-PCM, Ne-PCM, "
    "Doped, Composite, Mixture, Blend, Bi-, or any multi-element hyphenated token like X-Y or "
    "X-Y-Z (e.g. 'Al2O3-CuO'). Examples: 'Lauric Acid PCMs' -> SKIP; "
    "'Al2O3 Nanoparticle-infused Ne-PCM' -> SKIP. Reason: pure-compound data on a composite "
    "node = wrong thermophysics.\n"
    "- ALLOW extracting the base compound ONLY for pure-material FORM suffixes that do not change "
    "thermophysics: Nanoparticles, Powder, Nanofluid, Nanowire "
    "(e.g. 'Ag2O Nanoparticles' -> COMPOUND: silver(I) oxide).\n"
    "- Normalize messy names to a clean canonical name "
    "(e.g. 'Paraffin-based 116 Wax' -> COMPOUND: paraffin wax).\n"
    "- Bare elements/metals used as PCMs are compounds for our purpose "
    "(e.g. 'Gallium' -> COMPOUND: gallium)."
)


def load_judge_cache():
    if JUDGE_CACHE.exists():
        return json.loads(JUDGE_CACHE.read_text(encoding="utf-8"))
    return {}


def save_judge_cache(cache):
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    JUDGE_CACHE.write_text(json.dumps(cache, ensure_ascii=False, indent=2), encoding="utf-8")


RULE_SKIP_RE = re.compile(
    r"\b(portlandite|ettringite|tobermorite|monosulfate|alite|belite|C-S-H|"
    r"calcium silicate hydrate)\b",
    re.IGNORECASE,
)


def _rule_skip(name):
    """Deterministic pre-judge skip: single-char names (ambiguous), cement hydration phases.
    Two-char names stay allowed: they include real elements (Cu, Ge, Sb, Te, Si, Se, Sn, Bi)."""
    n = (name or "").strip()
    return len(n) == 1 or bool(RULE_SKIP_RE.search(n))


QUOTA_CODES = {"1308", "1309", "1310", "1113"}  # 5h/weekly/monthly usage limit, insufficient balance
QUOTA_MSG_RE = re.compile(r"usage limit|quota|insufficient balance|limit will reset", re.IGNORECASE)
RESET_AT_RE = re.compile(r"\d{4}-\d{2}-\d{2}[ T]\d{2}:\d{2}(:\d{2})?")
SAVE_EVERY = 25  # judge.json is saved every N new verdicts (plus in judge_all's finally)

# GLM run state: stop = None | "glm_quota" | "glm_budget"; single-threaded asyncio, plain dict is enough
_glm = {"tokens": 0, "max": 0, "stop": None, "reset_at": None, "new": 0}
_not_judged = set()  # names skipped because the stop flag was set (NOT judge errors)


def _zai_quota_error(response):
    """(is_quota, reset_at_str|None) for a z.ai reply. 1305 (concurrency) is NOT quota: it backs off."""
    try:
        body = response.json()
    except ValueError:
        return False, None
    if not isinstance(body, dict):
        return False, None
    err = body.get("error") if isinstance(body.get("error"), dict) else body
    code = str(err.get("code", ""))
    msg = str(err.get("message") or err.get("msg") or "")
    if code == "1305":
        return False, None
    if code in QUOTA_CODES or QUOTA_MSG_RE.search(msg):
        m = RESET_AT_RE.search(msg)
        return True, m.group(0) if m else None
    return False, None


def _request_stop(reason, reset_at=None):
    if _glm["stop"] is None:
        _glm["stop"], _glm["reset_at"] = reason, reset_at
        log(f"[judge] STOP requested ({reason}, reset_at={reset_at}); no further z.ai calls")


async def judge_one(client, sem, name, cache, refresh=False):
    """Returns (name, verdict); verdict None = judge error (never cached), or - when the stop flag
    is set - not judged (name goes into _not_judged; NOT a judge error)."""
    if _rule_skip(name):  # first: overrides old cached verdicts, no z.ai call, no cache write
        return name, {"decision": "skip", "canonical": None}
    if name in cache and not (refresh and cache[name].get("decision") == "skip"):
        return name, cache[name]

    def stopped():
        if _glm["stop"]:
            _not_judged.add(name)
            return True
        return False

    if stopped():
        return name, None
    async with sem:
        for attempt in range(4):
            if stopped():  # flag may have been set while this task waited for the semaphore / backed off
                return name, None
            try:
                r = await client.post(
                    f"{ZAI_BASE}/chat/completions",
                    headers={"Authorization": f"Bearer {ZAI_KEY}"},
                    json={
                        "model": JUDGE_MODEL,
                        "temperature": 0,
                        "messages": [
                            {"role": "system", "content": JUDGE_SYSTEM},
                            {"role": "user", "content": f"Entity name: {name}"},
                        ],
                    },
                    timeout=60,
                )
                is_quota, reset_at = _zai_quota_error(r)
                if is_quota:  # usage limit / balance: retrying is pointless, stop cleanly
                    _request_stop("glm_quota", reset_at)
                    _not_judged.add(name)
                    return name, None
                if r.status_code == 429 or "1305" in r.text:
                    await asyncio.sleep(2 * (attempt + 1))  # z.ai concurrency (1305): back off
                    continue
                r.raise_for_status()
                body = r.json()
                _glm["tokens"] += int((body.get("usage") or {}).get("total_tokens") or 0)
                if _glm["max"] and _glm["tokens"] >= _glm["max"]:
                    _request_stop("glm_budget")  # this reply is still used; later calls are not made
                out = body["choices"][0]["message"]["content"].strip()
                verdict = _parse_judge(out)
                if verdict is None:
                    log(f"[judge] unparseable reply for {name!r}: {out[:80]!r}")
                    return name, None
                cache[name] = verdict
                _glm["new"] += 1
                if _glm["new"] % SAVE_EVERY == 0:
                    save_judge_cache(cache)
                return name, verdict
            except Exception as e:
                if attempt == 3:
                    log(f"[judge] ERROR {name!r}: {e}")
                    return name, None
                await asyncio.sleep(2 * (attempt + 1))
    return name, None


JUDGE_RE = re.compile(r"COMPOUND:|\bSKIP\b", re.IGNORECASE)
JUDGE_JUNK = " \t`*\"'"


def _parse_judge(text):
    """First COMPOUND:/SKIP anywhere in the reply wins. None = unparseable."""
    m = JUDGE_RE.search(text or "")
    if not m:
        return None
    if m.group(0).upper() == "SKIP":
        return {"decision": "skip", "canonical": None}
    rest = text[m.end():].split("\n", 1)[0]
    canon = rest.strip(JUDGE_JUNK).rstrip(".").strip(JUDGE_JUNK)
    if not canon:
        return None
    return {"decision": "compound", "canonical": canon}


async def judge_all(names, cache, refresh=False):
    sem = asyncio.Semaphore(2)  # z.ai 1305 is a concurrency limit — never exceed 2
    try:
        async with httpx.AsyncClient(trust_env=False) as client:
            results = await asyncio.gather(
                *(judge_one(client, sem, n, cache, refresh) for n in names))
    finally:  # a crash/kill loses at most SAVE_EVERY verdicts
        save_judge_cache(cache)
    return dict(results)


def _read_resume():
    f = CACHE_DIR / RESUME_FILE
    if not f.exists():
        return None
    try:
        return json.loads(f.read_text(encoding="utf-8"))
    except ValueError:
        return {}  # unreadable marker: treat as a resumable stop


def _resume_gate(ignore):
    """Startup gate: exit 4 while a recorded quota stop is still active; else clear the marker."""
    info = _read_resume()
    if info is None:
        return
    reset_at = info.get("reset_at")
    if reset_at and not ignore:
        try:
            until = datetime.fromisoformat(str(reset_at).replace("T", " "))  # naive, machine-local
        except ValueError:
            until = None
        if until and until > datetime.now():
            log(f"quota stop still active until {reset_at}; not starting "
                "(--ignore-resume to override)")
            sys.exit(4)
    log(f"[resume] previous stop ({info.get('reason')}) is being resumed"
        + (" (gate ignored)" if ignore else "") + "; removing RESUME.json")
    (CACHE_DIR / RESUME_FILE).unlink(missing_ok=True)


def _write_resume_and_exit(names):
    """GLM quota/budget stop: judge.json is already saved. Record RESUME.json, log, exit 4."""
    info = {
        "stopped_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "reason": _glm["stop"],
        "reset_at": _glm["reset_at"],
        "glm_tokens_used": _glm["tokens"],
        "judged_this_run": _glm["new"],
        "not_judged_remaining": len(_not_judged),
        "resume_command": " ".join(["python", "enrich_pubchem.py"] + sys.argv[1:]),
        "note": "judge.json is saved; re-run the same command after reset_at; "
                "PubChem cache and graph markers make the re-run skip finished work",
    }
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    (CACHE_DIR / RESUME_FILE).write_text(json.dumps(info, ensure_ascii=False, indent=2), encoding="utf-8")
    log("\n==== STOP (GLM) ====")
    log(f"  reason: {info['reason']}  reset_at: {info['reset_at']}")
    log(f"  glm tokens used: {info['glm_tokens_used']}  judged this run: {info['judged_this_run']}  "
        f"not judged: {info['not_judged_remaining']} of {len(names)} names")
    log(f"  judge.json saved; no PubChem calls, no graph writes. Resume after reset_at: "
        f"{info['resume_command']}")
    log(f"  details: {CACHE_DIR / RESUME_FILE}")
    sys.exit(4)


# ---------------------------------------------------------------- step 3: PubChem
async def _sleep(s):
    """All PubChem waits go through here so the selftest can stub them."""
    await asyncio.sleep(s)


async def _throttle():
    global _last_pubchem_call
    now = time.monotonic()
    wait = PUBCHEM_MIN_INTERVAL - (now - _last_pubchem_call)
    if wait > 0:
        await _sleep(wait)
    _last_pubchem_call = time.monotonic()


RETRY_STATUS = (429, 500, 502, 503, 504)
PUBCHEM_ATTEMPTS = 5


def _fault_code(r):
    """PubChem answers throttled/failed calls with a Fault body (any status). Code str, or None."""
    try:
        fault = r.json().get("Fault")
        return str(fault.get("Code", "")) if isinstance(fault, dict) else None
    except (ValueError, AttributeError):
        return None


async def _pubchem_get(client, url):
    """JSON dict; None = 404 / Fault NotFound (genuine not-found); FetchFailed = retries exhausted.
    Any other Fault body (ServerBusy, Timeout, ServerError...) is retried, never passed through."""
    for attempt in range(PUBCHEM_ATTEMPTS):
        await _throttle()
        backoff = 2 ** (attempt + 1)  # 2, 4, 8, 16, 32 s
        try:
            r = await client.get(url, headers=PUBCHEM_HEADERS, timeout=60)
        except httpx.TransportError:  # includes timeouts
            await _sleep(backoff)
            continue
        if r.status_code == 404:
            return None
        fault = _fault_code(r)
        if fault is not None and "NotFound" in fault:
            return None
        if r.status_code in RETRY_STATUS or fault is not None:
            try:
                retry = int(r.headers.get("Retry-After", backoff))
            except ValueError:  # HTTP-date form
                retry = backoff
            await _sleep(retry)
            continue
        r.raise_for_status()
        return r.json()
    raise FetchFailed(url)


def _norm(s):
    return re.sub(r"\s+", " ", (s or "").strip().lower())


def _parse_mp(pugview):
    """First numeric value with unit °C; convert °F/K; range->low; else 'not available'."""
    if not pugview:
        return "not available"
    strings = []

    def walk(node):
        if isinstance(node, dict):
            info = node.get("Information")
            if isinstance(info, list):
                for item in info:
                    val = item.get("Value", {})
                    for sm in val.get("StringWithMarkup", []) or []:
                        if sm.get("String"):
                            strings.append(sm["String"])
                    if "Number" in val:
                        unit = val.get("Unit", "")
                        nums = val["Number"]
                        if not isinstance(nums, list):
                            nums = [nums]
                        for num in nums:
                            strings.append(f"{num} {unit}")
            for sec in node.get("Section", []) or []:
                walk(sec)

    walk(pugview.get("Record", {}))
    for s in strings:
        low = s.lower()
        if "decompos" in low:
            continue
        m = re.search(r"(-?\d+(?:\.\d+)?)\s*(?:-|to|–)?\s*(?:-?\d+(?:\.\d+)?)?\s*°?\s*c\b", low)
        if m:
            return f"{m.group(1)} °C"
    for s in strings:
        low = s.lower()
        if "decompos" in low:
            continue
        m = re.search(r"(-?\d+(?:\.\d+)?)\s*°?\s*f\b", low)
        if m:
            c = (float(m.group(1)) - 32) * 5 / 9
            return f"{c:.1f} °C (converted from °F)"
        m = re.search(r"(-?\d+(?:\.\d+)?)\s*k\b", low)
        if m:
            return f"{float(m.group(1)) - 273.15:.1f} °C (converted from K)"
    return "not available"


async def pubchem_fetch(client, canonical):
    """Resolve canonical name to a confidence-checked CID + facts, or None (unresolved)."""
    cid_json = await _pubchem_get(
        client, f"{PUBCHEM}/rest/pug/compound/name/{httpx.URL(canonical)}/cids/JSON"
    )
    if cid_json is None:
        return None
    try:
        cids = cid_json["IdentifierList"]["CID"]
    except (KeyError, TypeError):  # e.g. a Fault body: throttled/odd reply, NOT not-found
        raise FetchFailed(f"no IdentifierList for {canonical!r}: {str(cid_json)[:120]}")
    if not cids:
        return None
    cid = cids[0]
    cache_file = CACHE_DIR / f"{cid}.json"
    if cache_file.exists():
        facts = json.loads(cache_file.read_text(encoding="utf-8"))
        if facts.get("v") == FACTS_VERSION:
            if _confidence_ok(canonical, facts):
                return facts
            return None
        # stale version: fall through, re-fetch and overwrite
    prop = await _pubchem_get(
        client,
        f"{PUBCHEM}/rest/pug/compound/cid/{cid}/property/"
        f"MolecularFormula,MolecularWeight,IUPACName,CanonicalSMILES/JSON",
    )
    syn = await _pubchem_get(client, f"{PUBCHEM}/rest/pug/compound/cid/{cid}/synonyms/JSON")
    mp = await _pubchem_get(
        client,
        f"{PUBCHEM}/rest/pug_view/data/compound/{cid}/JSON?heading=Melting+Point",
    )
    # a reply lacking the expected structure is a failed fetch, never an empty value (and never cached)
    try:
        p = prop["PropertyTable"]["Properties"][0]
    except (KeyError, IndexError, TypeError):
        raise FetchFailed(f"malformed properties for CID {cid}: {str(prop)[:120]}")
    synonyms = []  # a synonyms 404 (None) is allowed and means []
    if syn is not None:
        try:
            synonyms = syn["InformationList"]["Information"][0]["Synonym"]
        except (KeyError, IndexError, TypeError):
            raise FetchFailed(f"malformed synonyms for CID {cid}: {str(syn)[:120]}")
    try:
        mp_text = _parse_mp(mp)
    except (AttributeError, TypeError, ValueError):  # malformed pug_view = no melting point
        mp_text = "not available"
    facts = {
        "v": FACTS_VERSION,
        "cid": cid,
        "formula": p.get("MolecularFormula", ""),
        "mw": p.get("MolecularWeight", ""),
        "iupac": p.get("IUPACName", ""),
        "smiles": p.get("CanonicalSMILES") or p.get("ConnectivitySMILES") or "",
        "mp": mp_text,
        "synonyms": synonyms,
        "query": canonical,
    }
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    cache_file.write_text(json.dumps(facts, ensure_ascii=False, indent=2), encoding="utf-8")
    if _confidence_ok(canonical, facts):
        return facts
    return None


def _confidence_ok(canonical, facts):
    """Accept CID only if normalized query == IUPAC OR == a whole synonym (whole-string)."""
    q = _norm(canonical)
    if q and q == _norm(facts.get("iupac")):
        return True
    for s in facts.get("synonyms", []):
        if q == _norm(s):
            return True
    return False


# ---------------------------------------------------------------- step 4: format
def format_block(facts):
    mp = facts.get("mp") or "not available"
    return (
        f"{MARK_START}\n"
        f"PubChem facts (CID {facts['cid']}): Formula {facts['formula']}. "
        f"MW {facts['mw']} g/mol. IUPAC {facts['iupac']}. SMILES {facts['smiles']}. "
        f"Melting point {mp}. Source: PubChem CID {facts['cid']}.\n"
        f"{MARK_END}"
    )


# ---------------------------------------------------------------- step 5: fresh read + write
async def fresh_description(client, name):
    """Re-read node's current description via /graphs. Returns str, or None if node gone."""
    r = await client.get(
        f"{LIGHTRAG_URL}/graphs",
        params={"label": name, "max_depth": 1, "max_nodes": 10},
        headers={"X-API-Key": LIGHTRAG_KEY},
        timeout=60,
    )
    r.raise_for_status()
    kg = r.json()
    for node in kg.get("nodes", []):
        if node.get("id") == name:
            return node.get("properties", {}).get("description", "") or ""
    return None  # empty KnowledgeGraph => node renamed/deleted => "gone"


async def write_entity(client, name, new_desc):
    r = await client.post(
        f"{LIGHTRAG_URL}/graph/entity/edit",
        headers={"X-API-Key": LIGHTRAG_KEY, "Content-Type": "application/json"},
        json={
            "entity_name": name,
            "updated_data": {"description": new_desc},
            "allow_rename": False,
            "allow_merge": False,
        },
        timeout=120,
    )
    r.raise_for_status()
    return r.json()


# ---------------------------------------------------------------- main
async def run(args):
    _resume_gate(args.ignore_resume)
    _glm["max"] = args.max_glm_tokens
    if not ZAI_KEY:
        log("FATAL: ZAI_API_KEY not set.")
        sys.exit(1)
    if not args.dry_run:
        require_ollama()

    stats = {"enriched": 0, "skipped_judge": 0, "judge_error": 0, "unresolved": 0,
             "fetch_failed": 0, "gone": 0, "already": 0, "error": 0}
    error_names = []

    cands = enumerate_candidates()
    names = list(cands.keys())
    if args.limit:
        names = names[: args.limit]
        log(f"[limit] capped to {len(names)} candidates")

    judge_cache = load_judge_cache()
    log(f"[judge] classifying {len(names)} names (Semaphore 2)...")
    verdicts = await judge_all(names, judge_cache, args.refresh)
    if _glm["stop"]:  # judge.json already saved by judge_all; stop BEFORE any PubChem fetch / graph write
        _write_resume_and_exit(names)

    compounds = [(n, v["canonical"]) for n, v in verdicts.items()
                 if v and v.get("decision") == "compound" and v.get("canonical")]
    stats["judge_error"] = sum(1 for v in verdicts.values() if v is None)
    stats["skipped_judge"] = sum(1 for v in verdicts.values()
                                 if v and v.get("decision") == "skip")
    log(f"[judge] {len(compounds)} compounds, {stats['skipped_judge']} skipped, "
        f"{stats['judge_error']} errors")
    if names and stats["judge_error"] > 0.1 * len(names):
        log(f"ABORT: judge_error {stats['judge_error']} of {len(names)} names (>10%). "
            "No PubChem calls, no writes. Fix the judge (key/quota/reply format) and re-run; "
            "good verdicts are cached.")
        sys.exit(2)

    async with httpx.AsyncClient(trust_env=False) as client:
        for name, canonical in compounds:
            try:
                # skip-check: already enriched (unless --refresh)
                if not args.refresh:
                    desc = await fresh_description(client, name)
                    if desc is None:
                        log(f"[gone] {name!r}")
                        stats["gone"] += 1
                        continue
                    if MARK_START in desc:
                        log(f"[already] {name!r}")
                        stats["already"] += 1
                        continue

                facts = await pubchem_fetch(client, canonical)
                if not facts:
                    log(f"[unresolved] {name!r} (canonical={canonical!r})")
                    stats["unresolved"] += 1
                    continue

                block = format_block(facts)
                if args.dry_run:
                    log(f"[dry-run] would enrich {name!r} -> CID {facts['cid']} "
                        f"mp={facts['mp']}")
                    stats["enriched"] += 1
                    continue

                # fresh read immediately before write (avoid stale clobber)
                desc = await fresh_description(client, name)
                if desc is None:
                    log(f"[gone] {name!r}")
                    stats["gone"] += 1
                    continue
                stripped = BLOCK_RE.sub("", desc).rstrip()
                new_desc = (stripped + "\n\n" + block) if stripped else block
                await write_entity(client, name, new_desc)
                log(f"[enriched] {name!r} -> CID {facts['cid']} mp={facts['mp']}")
                stats["enriched"] += 1
            except FetchFailed:
                log(f"[fetch_failed] {name!r} (canonical={canonical!r})")
                stats["fetch_failed"] += 1
            except Exception as e:
                log(f"[error] {name!r}: {e}")
                stats["error"] += 1
                error_names.append(name)

    log("\n==== SUMMARY ====")
    for k, v in stats.items():
        log(f"  {k}: {v}")
    log(f"  candidates: {len(names)}  compounds: {len(compounds)}")
    if args.dry_run:
        log("  (dry-run: no writes performed)")
    if error_names:
        log("  nodes that hit [error] may carry a marker with a stale vector; "
            "re-run with --refresh:")
        for n in error_names:
            log(f"    {n!r}")


MP_TEXT_RE = re.compile(r"Melting point (.*?)\. Source:", re.DOTALL)


def _block_mp(block):
    """Melting-point text of a PubChem block, '?' if absent."""
    m = MP_TEXT_RE.search(block or "")
    return m.group(1).strip() if m else "?"


def _marked_names():
    """Node names whose graphml description contains MARK_START."""
    if not GRAPHML.exists():
        log(f"FATAL: graphml not found at {GRAPHML}")
        sys.exit(1)
    root = ET.parse(GRAPHML).getroot()
    k_desc = _find_key(root, "description")
    if not k_desc:
        log("FATAL: no node <key> with attr.name='description' in graphml")
        sys.exit(1)
    names = []
    for node in root.iter(GRAPHML_NS + "node"):
        name = node.get("id")
        for data in node.findall(GRAPHML_NS + "data"):
            if data.get("key") == k_desc:
                if name and MARK_START in (data.text or ""):
                    names.append(name)
                break
    return names


async def fix_blocks(args):
    """Clean existing PubChem blocks: strip ONLY rule-skipped nodes, rewrite changed blocks,
    keep unjudged and unresolved. No judge calls, no ZAI key. Backs up descriptions before writes."""
    stats = {k: 0 for k in ("marked", "strip", "rewrite", "same", "keep_unjudged",
                            "keep_unresolved", "block_only", "fetch_failed", "gone", "nomarker", "error")}
    error_names = []
    backup = {}
    backup_file = CACHE_DIR / f"fixblocks_backup_{time.strftime('%Y%m%d-%H%M%S')}.json"
    suffix = " (dry-run)" if args.dry_run else ""
    if not args.dry_run:
        require_ollama()

    names = _marked_names()
    stats["marked"] = len(names)
    log(f"[fix] {len(names)} nodes carry a PubChem block")
    cache = load_judge_cache()

    async with httpx.AsyncClient(trust_env=False) as client:
        for name in names:
            try:
                desc = await fresh_description(client, name)
                if desc is None:
                    log(f"[fix:gone] {name!r}")
                    stats["gone"] += 1
                    continue
                if MARK_START not in desc:
                    log(f"[fix:nomarker] {name!r}")
                    stats["nomarker"] += 1
                    continue

                new_block = None
                if _rule_skip(name):
                    reason = "rule-skip"
                else:
                    v = cache.get(name)
                    if not (v and v.get("decision") == "compound" and v.get("canonical")):
                        log(f"[fix:keep-unjudged] {name!r}")
                        stats["keep_unjudged"] += 1
                        continue
                    facts = await pubchem_fetch(client, v["canonical"])
                    if facts is None:  # resolution failure is never grounds to strip
                        log(f"[fix:keep-unresolved] {name!r} (canonical={v['canonical']!r})")
                        stats["keep_unresolved"] += 1
                        continue
                    else:
                        new_block = format_block(facts)
                        old_block = BLOCK_RE.search(desc).group(0)
                        if new_block == old_block:
                            log(f"[fix:same] {name!r}")
                            stats["same"] += 1
                            continue
                        reason = None

                stripped = BLOCK_RE.sub("", desc).rstrip()
                if new_block is None:
                    if not stripped:  # LightRAG rejects empty descriptions
                        log(f"[fix:block-only] {name!r}")
                        stats["block_only"] += 1
                        continue
                    new_desc = stripped
                    kind = "strip"
                    log(f"[fix:strip] {name!r} ({reason}){suffix}")
                else:
                    new_desc = stripped + "\n\n" + new_block
                    kind = "rewrite"
                    log(f"[fix:rewrite] {name!r} mp: {_block_mp(old_block)} -> "
                        f"{_block_mp(new_block)}{suffix}")

                if not args.dry_run:
                    backup[name] = desc
                    CACHE_DIR.mkdir(parents=True, exist_ok=True)
                    backup_file.write_text(json.dumps(backup, ensure_ascii=False, indent=2),
                                           encoding="utf-8")
                    await write_entity(client, name, new_desc)
                stats[kind] += 1
            except FetchFailed:
                log(f"[fix:fetch_failed] {name!r}")
                stats["fetch_failed"] += 1
            except Exception as e:
                log(f"[fix:error] {name!r}: {e}")
                stats["error"] += 1
                error_names.append(name)

    log("\n==== FIX-BLOCKS SUMMARY ====")
    for k, v in stats.items():
        log(f"  {k}: {v}")
    if args.dry_run:
        log("  (dry-run: no writes performed)")
    if backup:
        log(f"  backup: {backup_file}")
    if error_names:
        log("  nodes that hit [fix:error] (write may be partial; re-run --fix-blocks):")
        for n in error_names:
            log(f"    {n!r}")


# ---------------------------------------------------------------- selftest
async def _selftest_pubchem_fetch():
    """pubchem_fetch never turns a bad reply into empty facts or a cache file (caller stubs sleeps)."""
    global CACHE_DIR
    import tempfile
    timeout = {"Fault": {"Code": "PUGREST.Timeout"}}
    ids = {"IdentifierList": {"CID": [962]}}

    async def fetch(prop, syn):
        def handler(request):
            u = str(request.url)
            if "/name/" in u:
                return httpx.Response(200, json=ids)
            if "/property/" in u:
                return httpx.Response(200, json=prop)
            if "/synonyms/" in u:
                return httpx.Response(200, json=syn)
            return httpx.Response(404, json={})  # pug_view: no melting point

        async with httpx.AsyncClient(transport=httpx.MockTransport(handler)) as c:
            try:
                return await pubchem_fetch(c, "water")
            except FetchFailed:
                return "FetchFailed"

    old_dir = CACHE_DIR
    with tempfile.TemporaryDirectory() as tmp:
        CACHE_DIR = Path(tmp)
        try:
            props = {"PropertyTable": {"Properties": [{"CID": 962, "MolecularFormula": "H2O",
                                                        "ConnectivitySMILES": "O"}]}}
            assert await fetch(props, timeout) == "FetchFailed"
            assert not list(CACHE_DIR.glob("*.json"))  # nothing cached on a bad synonyms reply
            syns = {"InformationList": {"Information": [{"CID": 962, "Synonym": ["water"]}]}}
            facts = await fetch(props, syns)
            assert facts and facts["smiles"] == "O", facts  # ConnectivitySMILES rename
            assert json.loads((CACHE_DIR / "962.json").read_text(encoding="utf-8"))["v"] == FACTS_VERSION
        finally:
            CACHE_DIR = old_dir


async def _selftest_fetch():
    """_pubchem_get retry/None/FetchFailed behaviour against httpx.MockTransport, no network."""
    global PUBCHEM_MIN_INTERVAL, _sleep
    busy = {"Fault": {"Code": "PUGREST.ServerBusy", "Message": "Too many requests"}}
    ok = {"IdentifierList": {"CID": [962]}}

    async def run(*replies):
        it = iter(replies)
        calls = []

        def handler(request):
            calls.append(1)
            status, body = next(it, replies[-1])
            return httpx.Response(status, json=body)

        async with httpx.AsyncClient(transport=httpx.MockTransport(handler)) as c:
            try:
                return await _pubchem_get(c, "http://x/y"), len(calls)
            except FetchFailed:
                return "FetchFailed", len(calls)

    old_int, old_sleep = PUBCHEM_MIN_INTERVAL, _sleep

    async def no_sleep(s):
        pass

    PUBCHEM_MIN_INTERVAL, _sleep = 0, no_sleep
    try:
        assert await run((200, busy), (200, ok)) == (ok, 2)  # ServerBusy Fault on a 200
        assert await run((502, {}), (200, ok)) == (ok, 2)
        assert await run((200, busy)) == ("FetchFailed", PUBCHEM_ATTEMPTS)  # always busy
        assert await run((404, {})) == (None, 1)  # genuine not-found, no retry
        timeout = {"Fault": {"Code": "PUGREST.Timeout"}}
        srverr = {"Fault": {"Code": "PUGREST.ServerError"}}
        assert await run((200, timeout), (200, ok)) == (ok, 2)  # non-busy Fault on a 200 is retried
        assert await run((200, srverr)) == ("FetchFailed", PUBCHEM_ATTEMPTS)
        assert await run((200, {"Fault": {"Code": "PUGREST.NotFound"}})) == (None, 1)
        await _selftest_pubchem_fetch()
    finally:
        PUBCHEM_MIN_INTERVAL, _sleep = old_int, old_sleep


async def _selftest_quota_stop():
    """Quota detection, stop flag / token budget (no HTTP once stopped), RESUME.json + startup gate."""
    global CACHE_DIR
    import tempfile
    from datetime import timedelta
    msg = "Usage limit reached for 5 hour. Your limit will reset at 2026-09-29 23:10:05"
    r1308 = httpx.Response(429, json={"error": {"code": "1308", "message": msg}})
    assert _zai_quota_error(r1308) == (True, "2026-09-29 23:10:05")
    assert _zai_quota_error(httpx.Response(429, json={"error": {"code": "1305", "message": "overloaded"}})) == (False, None)
    r1113 = httpx.Response(429, json={"error": {"code": "1113", "message": "Insufficient balance"}})
    assert _zai_quota_error(r1113) == (True, None)
    assert _zai_quota_error(httpx.Response(429, json={"error": {"code": "1234", "message": "Quota exceeded"}}))[0]
    assert _zai_quota_error(httpx.Response(200, json={"choices": [], "usage": {}})) == (False, None)
    assert _zai_quota_error(httpx.Response(500, text="oops")) == (False, None)

    old_glm, old_nj = dict(_glm), set(_not_judged)
    ok = {"choices": [{"message": {"content": "SKIP"}}], "usage": {"total_tokens": 120}}

    async def judge(handler, names):
        sem = asyncio.Semaphore(2)
        async with httpx.AsyncClient(transport=httpx.MockTransport(handler)) as c:
            return [await judge_one(c, sem, n, {}) for n in names]

    def reset(**kw):
        _glm.update({"tokens": 0, "max": 0, "stop": None, "reset_at": None, "new": 0}, **kw)
        _not_judged.clear()

    try:
        def boom(request):
            raise AssertionError("HTTP call while stop flag set")

        reset(stop="glm_quota")  # stop flag set: no HTTP, marked not-judged
        assert await judge(boom, ["Foo Acid"]) == [("Foo Acid", None)] and _not_judged == {"Foo Acid"}
        reset()
        calls = []

        def quota(request):
            calls.append(1)
            return r1308

        res = await judge(quota, ["Foo Acid", "Bar Acid"])  # 2nd name must not reach z.ai
        assert res == [("Foo Acid", None), ("Bar Acid", None)] and len(calls) == 1, (res, calls)
        assert _glm["stop"] == "glm_quota" and _glm["reset_at"] == "2026-09-29 23:10:05"
        assert _not_judged == {"Foo Acid", "Bar Acid"}
        reset(max=100)
        calls.clear()

        def budget(request):
            calls.append(1)
            return httpx.Response(200, json=ok)

        res = await judge(budget, ["Foo Acid", "Bar Acid"])  # 120 >= 100: 1st judged, then stop
        assert res[0][1] == {"decision": "skip", "canonical": None} and res[1][1] is None and len(calls) == 1
        assert _glm["stop"] == "glm_budget" and _glm["tokens"] == 120 and _not_judged == {"Bar Acid"}

        old_dir, old_argv = CACHE_DIR, sys.argv
        with tempfile.TemporaryDirectory() as tmp:
            CACHE_DIR = Path(tmp)
            try:
                sys.argv = ["enrich_pubchem.py", "--dry-run"]
                reset(stop="glm_quota", reset_at="2026-09-29 23:10:05", tokens=5, new=2)
                _not_judged.add("x")
                try:
                    _write_resume_and_exit(["x", "y"])
                    raise AssertionError("no exit")
                except SystemExit as e:
                    assert e.code == 4
                info = json.loads((CACHE_DIR / RESUME_FILE).read_text(encoding="utf-8"))
                assert info["reason"] == "glm_quota" and info["not_judged_remaining"] == 1
                assert info["resume_command"] == "python enrich_pubchem.py --dry-run", info
                fut = (datetime.now() + timedelta(hours=1)).strftime("%Y-%m-%d %H:%M:%S")
                (CACHE_DIR / RESUME_FILE).write_text(json.dumps({"reset_at": fut}), encoding="utf-8")
                try:
                    _resume_gate(False)
                    raise AssertionError("gate did not stop")
                except SystemExit as e:
                    assert e.code == 4
                assert (CACHE_DIR / RESUME_FILE).exists()
                _resume_gate(True)  # --ignore-resume: proceeds, marker removed
                assert not (CACHE_DIR / RESUME_FILE).exists()
                (CACHE_DIR / RESUME_FILE).write_text(json.dumps({"reset_at": "2020-01-01 00:00:00"}), encoding="utf-8")
                _resume_gate(False)  # reset time passed: resumes
                assert not (CACHE_DIR / RESUME_FILE).exists()
            finally:
                CACHE_DIR, sys.argv = old_dir, old_argv
    finally:
        _glm.clear()
        _glm.update(old_glm)
        _not_judged.clear()
        _not_judged.update(old_nj)


def _selftest():
    p = _parse_judge
    assert p("COMPOUND: gallium") == {"decision": "compound", "canonical": "gallium"}
    assert p("Sure! compound: `silver(I) oxide`.")["canonical"] == "silver(I) oxide"
    assert p("```\nSKIP\n```") == {"decision": "skip", "canonical": None}
    assert p("skip")["decision"] == "skip"
    assert p("no idea") is None
    assert p("COMPOUND:  ") is None

    def pv(value):
        return {"Record": {"Section": [{"Information": [{"Value": value}]}]}}

    assert _parse_mp(pv({"StringWithMarkup": [{"String": "12.3 °C"}]})) == "12.3 °C"
    f = _parse_mp(pv({"Number": 98.6, "Unit": "°F"}))  # scalar, not a list
    assert f == "37.0 °C (converted from °F)", f
    k = _parse_mp(pv({"StringWithMarkup": [{"String": "300 K"}]}))
    assert k == "26.9 °C (converted from K)", k
    assert _parse_mp(None) == "not available"
    d = _parse_mp(pv({"StringWithMarkup": [{"String": "1076 °F (Decomposes) (Loses H2O)"}]}))
    assert d == "not available", d
    for n in ("C", "Portlandite", "C-S-H Gel", "Ettringite Formation"):
        assert _rule_skip(n), n
    for n in ("Cu", "Sb", "O₂", "Gallium", "Paraffin Wax", "CaCO3", "Water"):
        assert not _rule_skip(n), n

    g = (f'<graphml xmlns="{GRAPHML_NS[1:-1]}">'
         '<key id="d1" for="node" attr.name="description"/>'
         '<key id="d7" for="node" attr.name="entity_type"/>'
         '<key id="d9" for="edge" attr.name="entity_type"/></graphml>')
    assert _find_type_key(ET.fromstring(g)) == "d7"
    assert _find_type_key(ET.fromstring(f'<graphml xmlns="{GRAPHML_NS[1:-1]}"/>')) is None
    assert _find_key(ET.fromstring(g), "description") == "d1"
    assert _block_mp(format_block({"cid": 1, "formula": "X", "mw": 1, "iupac": "x",
                                   "smiles": "C", "mp": "12.0 °C"})) == "12.0 °C"
    assert _block_mp("no block") == "?"
    asyncio.run(_selftest_fetch())
    asyncio.run(_selftest_quota_stop())
    print("selftest OK")


def main():
    ap = argparse.ArgumentParser(description="PubChem enrichment of PCM_RAG chemical entities")
    ap.add_argument("--selftest", action="store_true", help="offline asserts, then exit")
    ap.add_argument("--dry-run", action="store_true", help="enumerate+judge+fetch, no graph writes")
    ap.add_argument("--refresh", action="store_true", help="re-enrich nodes already marked")
    ap.add_argument("--limit", type=int, default=0, help="cap number of candidates (testing)")
    ap.add_argument("--fix-blocks", action="store_true",
                    help="clean existing blocks: strip rule-skipped, rewrite changed (no judge calls; --dry-run = log only)")
    ap.add_argument("--max-glm-tokens", type=int, default=0,
                    help="stop cleanly (exit 4) once GLM usage.total_tokens reaches N; 0 = no cap")
    ap.add_argument("--ignore-resume", action="store_true",
                    help="start even if RESUME.json says a quota stop is still active")
    args = ap.parse_args()
    if args.selftest:
        _selftest()
        return
    asyncio.run(fix_blocks(args) if args.fix_blocks else run(args))


if __name__ == "__main__":
    main()
