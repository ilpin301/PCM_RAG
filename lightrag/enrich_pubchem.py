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
  python enrich_pubchem.py --collect FILE [--force]  # NO graph writes: collect {name: {old, new}} into FILE,
                                      # then apply with ingest.ps1 -Root <base> -DescFile FILE
  python enrich_pubchem.py --fix-blocks --collect FILE  # same for block cleanup (no graph writes, no backup file)
  python enrich_pubchem.py --fix-blocks --verify [--collect FILE]  # also GLM-verify each resolved block, strip rejects
  python enrich_pubchem.py --fix-blocks --strip-all --collect FILE [--force]  # strip EVERY block (before an ingest; re-add after)
  python enrich_pubchem.py --scan-leaks  # list descriptions with PubChem/OpenAlex facts outside the blocks
  python enrich_pubchem.py --max-glm-tokens 500000  # stop cleanly once GLM has used N tokens (0 = no cap)
  python enrich_pubchem.py --ignore-resume  # start although RESUME.json says a quota stop is still active
  python enrich_pubchem.py --selftest # offline asserts, no network, no graph

EXIT CODES:
  0  ok
  1  fatal precondition (missing key / graphml; --collect with --dry-run; --collect FILE exists without --force)
  2  judge_error abort (>10% of names failed to judge)
  3  Ollama unreachable (write runs) or LightRAG unreachable (any run)
  4  stopped on GLM quota or --max-glm-tokens budget (resume later): judge.json is saved and
     data/enrich_cache/RESUME.json says when to re-run; stops BEFORE any PubChem fetch or graph write.
     Re-run the same command after reset_at; judged names, PubChem cache and graph markers skip finished work.
     With the verify step (normal runs, --fix-blocks --verify) it can also stop mid-loop; a --collect FILE
     then holds verified entries only - re-collect after reset_at instead of applying it.
  5  PubChem still blocking this IP (429/ServerBusy streak) or link down, after one long pause; partial --collect file is saved - re-run later, caches skip finished work
  7  --scan-leaks found leaked facts outside the blocks
"""
import argparse
import asyncio
import json
import os
import re
import shutil
import statistics
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
VERIFY_FILE = "verify.json"  # under CACHE_DIR; GLM same-substance verdicts per (name, CID)
CID_LOOKUP_FILE = "cid_lookup.json"  # under CACHE_DIR; name -> CID replies, so an exit-5 re-run skips finished lookups
NOTFOUND_CACHE_TTL_S = 7 * 86400  # a cached name not-found is trusted this long (PubChem adds compounds)
FACTS_VERSION = 4  # 4: mp only from value-first strings / numbers; no majority of agreeing values -> not available

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
OPENALEX_BLOCK_RE = re.compile(r"<!--OPENALEX_START-->.*?<!--OPENALEX_END-->", re.DOTALL)
LEAK_RE = re.compile(r"PubChem|OpenAlex|\bCID\s*[:#]?\s*\d+|\bSMILES\b|\bIUPAC\b|\bInChI(?:Key)?\b|\b[A-Z]{14}-[A-Z]{10}-[A-Z]\b"
                     r"|\b(?:MW|molecular (?:weight|mass))\s*(?:of|is|:|=)?\s*\d+(?:[.,]\d+)?\s*g/mol"
                     r"|\bCited by [\d,]+ \(as of \d{4}-\d{2}\)|\bOpen-access PDF\b|\bW\d{8,}\b"
                     r"|\bmolar mass\b[^.\n]{0,40}?\d+(?:[.,]\d+)?\s*g/mol|\(\d+[.,]\d{2,}\s*g/mol\)",
                     re.IGNORECASE)  # enrichment facts outside a block, incl. paraphrase and reworded forms
# ponytail: "(N g/mol)" needs >=2 decimals so a polymer grade like "PEG (400 g/mol)" is not a leak; PubChem MW has 3


def _leak_text(desc):
    """Description text outside both enrichment blocks."""
    return OPENALEX_BLOCK_RE.sub("", BLOCK_RE.sub("", desc or ""))

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

# global PubChem throttle: adaptive baseline 2.0s between calls (~0.5 req/s); the interval
# grows on 429/ServerBusy responses and pauses the whole run when PubChem blocks the IP
# (dynamic throttling escalates if you keep requesting during a block). The
# X-Throttling-Control response header also lifts it proactively (see _throttle_floor).
PUBCHEM_MIN_INTERVAL = 2.0
_pubchem_interval = PUBCHEM_MIN_INTERVAL  # the live adaptive value
PUBCHEM_MAX_INTERVAL = 16.0
PUBCHEM_BLOCK_STREAK = 3  # consecutive blocked items that trigger a long pause
PUBCHEM_BLOCK_PAUSE_S = 300.0
_last_pubchem_call = 0.0


class FetchFailed(Exception):
    """PubChem fetch gave up after retries (network/429/503) - NOT the same as unresolved."""
    blocked = False  # True when the last attempt signalled PubChem IP throttling (429/ServerBusy/Timeout) or the link is down


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


def require_lightrag(url=LIGHTRAG_URL):
    """Fail fast before the node loop: every node reads its current description from the server,
    so with LightRAG down each one would just log 'All connection attempts failed'."""
    try:
        httpx.get(f"{url}/health", headers={"X-API-Key": LIGHTRAG_KEY}, timeout=10,
                  trust_env=False).raise_for_status()
    except Exception:
        log(f"FATAL: LightRAG not reachable at {url} - start Docker Desktop and "
            "`docker compose up -d` in lightrag/ first (pcm-PubChem-runner Step 0)")
        sys.exit(3)


def _collect_guard(args):
    """--collect startup checks, before any network work. FILE is never merged, only rebuilt;
    with --force the old FILE is first kept as FILE.prev so a smaller partial result cannot destroy it."""
    if not args.collect:
        return
    if args.dry_run:
        log("FATAL: --collect already writes nothing to the graph; drop --dry-run")
        sys.exit(1)
    if os.path.exists(args.collect) and not args.force:
        log(f"FATAL: {args.collect} exists; pass --force to overwrite (a collect file is never merged)")
        sys.exit(1)
    if os.path.exists(args.collect):  # only reached with --force
        shutil.copy2(args.collect, args.collect + ".prev")


def _save_collected(path, obj):
    """Atomic write of the --collect file (tmp + os.replace); parent dir is created if missing."""
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    tmp = p.with_name(p.name + ".tmp")
    tmp.write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding="utf-8")
    os.replace(tmp, p)


NEW_ENTITIES_FILE = "collect_new_entities.json"  # under CACHE_DIR; Claude's review list after a collect


def _save_new_entities(path, collected, verify_keys0):
    """Names to review: collected entities with no verify.json entry when the run STARTED (verify_match
    fills verify.json during the run, so the end state cannot tell). Names from a previous run's file are
    kept while still collected (a resumed run finds them already verified); the rest of the old file is dropped."""
    p = Path(path)
    prev = set(json.loads(p.read_text(encoding="utf-8"))) if p.exists() else set()
    new = sorted(n for n in collected if n not in verify_keys0 or n in prev)
    _save_collected(p, new)
    return new


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

# carbon allotropes/forms: PubChem only has atomic C (CID 5462310, IUPAC "methane", mp 3500 °C) - wrong for all
CARBON_SKIP_RE = re.compile(
    r"^carbon$|\b(graphene|diamond|carbon black|acetylene black|HOPG|carbon nano[ -]?(wires?|tubes?)|"
    r"[MS]?W?CNTs?)\b|graphite\b",
    re.IGNORECASE,
)


def _rule_skip(name):
    """Deterministic pre-judge skip: single-char names (ambiguous), cement hydration phases, carbon allotropes/forms.
    Two-char names stay allowed: they include real elements (Cu, Ge, Sb, Te, Si, Se, Sn, Bi)."""
    n = (name or "").strip()
    return len(n) == 1 or bool(RULE_SKIP_RE.search(n) or CARBON_SKIP_RE.search(n))


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


async def _zai_chat(client, system, user, who):
    """One z.ai chat call with 1305 backoff. Reply text, or None (error / quota / stop flag set).
    Quota sets the stop flag; the token budget is checked after a reply, which is still returned."""
    for attempt in range(4):
        if _glm["stop"]:
            return None
        try:
            r = await client.post(
                f"{ZAI_BASE}/chat/completions",
                headers={"Authorization": f"Bearer {ZAI_KEY}"},
                json={
                    "model": JUDGE_MODEL,
                    "temperature": 0,
                    "messages": [
                        {"role": "system", "content": system},
                        {"role": "user", "content": user},
                    ],
                },
                timeout=60,
            )
            is_quota, reset_at = _zai_quota_error(r)
            if is_quota:  # usage limit / balance: retrying is pointless, stop cleanly
                _request_stop("glm_quota", reset_at)
                return None
            if r.status_code == 429 or "1305" in r.text:
                await asyncio.sleep(2 * (attempt + 1))  # z.ai concurrency (1305): back off
                continue
            r.raise_for_status()
            body = r.json()
            _glm["tokens"] += int((body.get("usage") or {}).get("total_tokens") or 0)
            if _glm["max"] and _glm["tokens"] >= _glm["max"]:
                _request_stop("glm_budget")  # this reply is still used; later calls are not made
            return body["choices"][0]["message"]["content"].strip()
        except Exception as e:
            if attempt == 3:
                log(f"[glm] ERROR {who}: {e}")
                return None
            await asyncio.sleep(2 * (attempt + 1))
    return None


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
        if stopped():  # flag may have been set while this task waited for the semaphore
            return name, None
        out = await _zai_chat(client, JUDGE_SYSTEM, f"Entity name: {name}", f"judge {name!r}")
        if out is None:
            if _glm["stop"]:
                _not_judged.add(name)
            return name, None
        verdict = _parse_judge(out)
        if verdict is None:
            log(f"[judge] unparseable reply for {name!r}: {out[:80]!r}")
            return name, None
        cache[name] = verdict
        _glm["new"] += 1
        if _glm["new"] % SAVE_EVERY == 0:
            save_judge_cache(cache)
        return name, verdict


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


VERIFY_SYSTEM = (
    "You check a PubChem match for an entity name from a phase-change-material knowledge graph. "
    "Given the name and the PubChem record's IUPAC name and molecular formula, decide whether the "
    "record is the SAME substance the name denotes.\n"
    "- Form words (Nanoparticles, Powder, Nanofluid, Nanowire, Flakes) do not change the substance.\n"
    "- A different compound, hydration state or composition is NOT the same "
    "(e.g. 'Graphene Oxide' vs methane CH4 -> NO).\n"
    "Reply with EXACTLY ONE word: YES or NO."
)
VERIFY_RE = re.compile(r"\b(YES|NO)\b", re.IGNORECASE)


def _parse_verify(text):
    """First standalone YES/NO in the reply -> True/False; None = unparseable."""
    m = VERIFY_RE.search(text or "")
    return None if not m else m.group(1).upper() == "YES"


def load_verify_cache():
    f = CACHE_DIR / VERIFY_FILE
    return json.loads(f.read_text(encoding="utf-8")) if f.exists() else {}


def save_verify_cache(cache):
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    (CACHE_DIR / VERIFY_FILE).write_text(json.dumps(cache, ensure_ascii=False, indent=2), encoding="utf-8")


async def verify_match(client, name, facts, cache):
    """GLM yes/no: is PubChem record `facts` the substance `name` denotes? True/False, cached per
    (name, CID) and saved at once; None = not verified (error, unparseable, stop flag), never cached."""
    hit = cache.get(name)
    if hit and hit.get("cid") == facts["cid"]:
        return hit["same"]
    out = await _zai_chat(
        client, VERIFY_SYSTEM,
        f"Entity name: {name}\nPubChem CID {facts['cid']}: IUPAC name {facts.get('iupac') or '(none)'}; "
        f"formula {facts.get('formula') or '(none)'}",
        f"verify {name!r}")
    same = _parse_verify(out)
    if out is not None and same is None:
        log(f"[verify] unparseable reply for {name!r}: {out[:80]!r}")
    if same is not None:
        cache[name] = {"cid": facts["cid"], "same": same}
        save_verify_cache(cache)
    return same


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
        "note": "judge.json and verify.json are saved; re-run the same command after reset_at; "
                "PubChem cache and graph markers make the re-run skip finished work",
    }
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    (CACHE_DIR / RESUME_FILE).write_text(json.dumps(info, ensure_ascii=False, indent=2), encoding="utf-8")
    log("\n==== STOP (GLM) ====")
    log(f"  reason: {info['reason']}  reset_at: {info['reset_at']}")
    log(f"  glm tokens used: {info['glm_tokens_used']}  judged this run: {info['judged_this_run']}  "
        f"not judged: {info['not_judged_remaining']} of {len(names)} names")
    log(f"  judge.json + verify.json saved. Resume after reset_at: {info['resume_command']}")
    log(f"  details: {CACHE_DIR / RESUME_FILE}")
    sys.exit(4)


# ---------------------------------------------------------------- step 3: PubChem
async def _sleep(s):
    """All PubChem waits go through here so the selftest can stub them."""
    await asyncio.sleep(s)


async def _throttle():
    global _pubchem_interval, _last_pubchem_call
    now = time.monotonic()
    wait = _pubchem_interval - (now - _last_pubchem_call)
    if wait > 0:
        await _sleep(wait)
    _last_pubchem_call = time.monotonic()


class _PubchemBreaker:
    """Run-level circuit breaker for PubChem IP blocks: a streak of blocked items
    pauses the whole run once; a second streak after that pause exits 5 so the
    caller's finally-block saves the partial --collect file (hammering during a
    block escalates its duration - PubChem dynamic request throttling)."""
    def __init__(self):
        self.streak = 0
        self.pauses = 0

    def ok(self):
        self.streak = 0

    async def blocked(self):
        self.streak += 1
        if self.streak < PUBCHEM_BLOCK_STREAK:
            return
        self.streak = 0
        if self.pauses >= 1:
            log("PubChem is STILL blocking this IP after a pause; stopping (exit 5). "
                "Partial work is saved and cached; wait ~30-60 min, then re-run the "
                "same command - judge/verify/CID caches skip finished work.")
            sys.exit(5)
        self.pauses += 1
        log(f"PubChem blocked {PUBCHEM_BLOCK_STREAK} items in a row; pausing "
            f"{PUBCHEM_BLOCK_PAUSE_S:.0f}s to let the IP block lift")
        await _sleep(PUBCHEM_BLOCK_PAUSE_S)


RETRY_STATUS = (429, 500, 502, 503, 504)
PUBCHEM_ATTEMPTS = 5
NOTFOUND_RETRY_S = 60  # --fix-blocks: PubChem briefly answers NotFound for names it has (seen in 15-40 s windows)


def _fault_code(r):
    """PubChem answers throttled/failed calls with a Fault body (any status). Code str, or None."""
    try:
        fault = r.json().get("Fault")
        return str(fault.get("Code", "")) if isinstance(fault, dict) else None
    except (ValueError, AttributeError):
        return None


_THROTTLE_RE = re.compile(r"([A-Za-z ]+?)\s+status:\s*(Green|Yellow|Red|Black)\b", re.IGNORECASE)
_OUR_TRAFFIC_FLOOR = {"yellow": 3.0, "red": 8.0, "black": 20.0}
_SERVICE_FLOOR = {"red": 4.0, "black": 8.0}  # global PubChem load, not our traffic: only severe


def _throttle_floor(headers):
    """Minimum interval (s) implied by PubChem's X-Throttling-Control header; 0.0 if absent/odd."""
    try:
        value = headers.get("X-Throttling-Control") if headers is not None else None
        floor = 0.0
        for name, color in _THROTTLE_RE.findall(value or ""):
            table = _SERVICE_FLOOR if name.strip().lower() == "service" else _OUR_TRAFFIC_FLOOR
            floor = max(floor, table.get(color.lower(), 0.0))
        return floor
    except Exception:
        return 0.0


def _url_kind(url):
    for needle, kind in (("/cids/", "cid"), ("/property/", "props"), ("/synonyms/", "syn"), ("pug_view", "pugview")):
        if needle in url:
            return kind
    return "other"


def _log_fail(url, status, fault, headers, attempt):
    """One diagnostic line per failed PubChem attempt: which endpoint/status/header triggers blocks."""
    h = headers if headers is not None else {}
    log(f'[pubchem-fail] kind={_url_kind(url)} status={status} fault={fault or "-"} '
        f'retry_after={h.get("Retry-After") or "-"} throttle="{h.get("X-Throttling-Control") or "-"}" '
        f'interval={_pubchem_interval:.1f} attempt={attempt + 1}/{PUBCHEM_ATTEMPTS}')


async def _pubchem_get(client, url):
    """JSON dict; None = 404 / Fault NotFound (genuine not-found); FetchFailed = retries exhausted.
    Any other Fault body (ServerBusy, Timeout, ServerError...) is retried, never passed through."""
    global _pubchem_interval
    blocked = False
    for attempt in range(PUBCHEM_ATTEMPTS):
        await _throttle()
        backoff = 2 ** (attempt + 1)  # 2, 4, 8, 16, 32 s
        try:
            r = await client.get(url, headers=PUBCHEM_HEADERS, timeout=60)
        except httpx.TransportError as exc:  # transport error = link down, treated as a block so the breaker pauses instead of burning items
            blocked = True
            _log_fail(url, f"transport:{type(exc).__name__}", None, None, attempt)
            await _sleep(backoff)
            continue
        floor = _throttle_floor(r.headers)  # applied on every exit below, after any decay/doubling
        if r.status_code == 404:
            _pubchem_interval = min(PUBCHEM_MAX_INTERVAL, max(_pubchem_interval, floor))
            return None
        fault = _fault_code(r)
        if fault is not None and "NotFound" in fault:
            _pubchem_interval = min(PUBCHEM_MAX_INTERVAL, max(_pubchem_interval, floor))
            return None
        if r.status_code in RETRY_STATUS or fault is not None:
            # 429/503 or a ServerBusy/Timeout Fault = PubChem throttling this IP: grow the
            # global interval (500/502/504 and other faults are ordinary server hiccups)
            blocked = r.status_code in (429, 503) or (
                fault is not None and ("ServerBusy" in fault or "Timeout" in fault))
            if blocked:
                _pubchem_interval = min(PUBCHEM_MAX_INTERVAL, _pubchem_interval * 2)
            _pubchem_interval = min(PUBCHEM_MAX_INTERVAL, max(_pubchem_interval, floor))
            try:
                retry = int(r.headers.get("Retry-After", backoff))
            except ValueError:  # HTTP-date form
                retry = backoff
            _log_fail(url, r.status_code, fault, r.headers, attempt)
            await _sleep(retry)
            continue
        _pubchem_interval = max(PUBCHEM_MIN_INTERVAL, _pubchem_interval * 0.8)  # relax toward baseline
        _pubchem_interval = min(PUBCHEM_MAX_INTERVAL, max(_pubchem_interval, floor))
        r.raise_for_status()
        return r.json()
    err = FetchFailed(url)
    err.blocked = blocked
    raise err


def _norm(s):
    return re.sub(r"\s+", " ", (s or "").strip().lower())


MP_VALUE_RE = re.compile(
    r"^\s*(?:(?:mp|m\.p\.|melting point|melting pt)\s*[:=]?\s*)?"
    r"(-?\d{1,3}(?:,\d{3})+(?:\.\d+)?|-?\d+(?:\.\d+)?)\s*(?:(?:-|to|–)\s*-?[\d,]+(?:\.\d+)?\s*)?(?:°\s*|deg\s*)?([CFK])\b",
    re.IGNORECASE,
)
NOT_MELT_RE = re.compile(r"decompos|\bdec\b\.?|sublim|\bsubl\b\.?|triple p(?:oin)?t|\bboil", re.IGNORECASE)  # non-melting notes
MP_AGREE_C = 5.0 # values within max(this, MP_AGREE_FRAC of the median in K) of the median agree
MP_AGREE_FRAC = 0.02  # 2 % of absolute temperature: ~6 K near room temperature, ~46 K for Al2O3


def _mp_to_c(value, unit):
    """(°C, suffix) for a value in C/F/K."""
    u = unit.upper()
    if u == "F":
        return (value - 32) * 5 / 9, " (converted from °F)"
    if u == "K":
        return value - 273.15, " (converted from K)"
    return value, ""


def _mp_values(pugview):
    """Measured melting points in PubChem's Melting Point section as [(°C, unit C/F/K, text)], record order.
    A string counts only when it STARTS with the value (after an optional 'mp:' label): narrative
    sentences (e.g. 'At 260 K, a phase transition ...') and decomposition notes are ignored."""
    out = []

    def add(value, unit, raw):
        c, suffix = _mp_to_c(value, unit)
        text = f"{c:.1f} °C{suffix}" if suffix else f"{raw} °C"
        out.append((c, unit.upper(), text))

    def walk(node):
        if isinstance(node, dict):
            info = node.get("Information")
            if isinstance(info, list):
                for item in info:
                    val = item.get("Value", {}) or {}
                    for sm in val.get("StringWithMarkup", []) or []:
                        s = sm.get("String") or ""
                        if NOT_MELT_RE.search(s):
                            continue
                        m = MP_VALUE_RE.match(s)
                        if m:
                            num = m.group(1).replace(",", "")
                            add(float(num), m.group(2), num)
                    if "Number" in val:
                        unit = (val.get("Unit") or "").replace("°", "").strip()
                        if unit.upper() in ("C", "F", "K"):
                            nums = val["Number"] if isinstance(val["Number"], list) else [val["Number"]]
                            for num in nums:
                                add(float(num), unit, num)
            for sec in node.get("Section", []) or []:
                walk(sec)

    if pugview:
        walk(pugview.get("Record", {}))
    return out


def _parse_mp(pugview):
    """Consensus melting point. Uses the °C entries when there are any (PubChem's °F/K entries are
    mostly CAMEO/NIOSH conversions), else the °F/K ones. The first value within the tolerance of the
    median wins, but only when MORE than half of the values agree: a scattered record (polymorphs,
    hydrates, stray numbers) gives 'not available', never a guess or a range."""
    vals = _mp_values(pugview)
    vals = [v for v in vals if v[1] == "C"] or vals
    if not vals:
        return "not available"
    med = statistics.median(c for c, _, _ in vals)
    tol = max(MP_AGREE_C, MP_AGREE_FRAC * (med + 273.15))
    near = [v for v in vals if abs(v[0] - med) <= tol]
    if 2 * len(near) <= len(vals):
        return "not available"
    return near[0][2]


_cid_cache = None  # lazily loaded {norm name: {"r": cid_json | None, "ts": epoch s}}; tests reset it to None


def _cid_cache_load():
    global _cid_cache
    if _cid_cache is None:
        try:
            data = json.loads((CACHE_DIR / CID_LOOKUP_FILE).read_text(encoding="utf-8"))
            _cid_cache = data if isinstance(data, dict) else {}
        except (OSError, ValueError):  # missing or corrupt: start empty, the next store rewrites it
            _cid_cache = {}
    return _cid_cache


def _cid_cache_store(key, result):
    cache = _cid_cache_load()
    cache[key] = {"r": result, "ts": time.time()}
    _save_collected(CACHE_DIR / CID_LOOKUP_FILE, cache)


async def _cid_lookup(client, canonical, notfound_retries=0):
    """Name -> CID JSON via _pubchem_get; a NotFound (None) is retried notfound_retries times after
    NOTFOUND_RETRY_S. Only --fix-blocks retries: its names all resolved once, so a NotFound there is
    usually a PubChem hiccup, while a normal run meets many genuine not-founds.
    Definite answers are cached in cid_lookup.json so a re-run after an exit-5 block skips them; a
    cached not-found is trusted only without retries and for NOTFOUND_CACHE_TTL_S; a FetchFailed
    or a reply without IdentifierList is never cached."""
    key = _norm(canonical)
    hit = _cid_cache_load().get(key)
    if isinstance(hit, dict):
        if isinstance(hit.get("r"), dict):
            return hit["r"]
        if (hit.get("r") is None and notfound_retries == 0
                and time.time() - (hit.get("ts") or 0) < NOTFOUND_CACHE_TTL_S):
            return None
    url = f"{PUBCHEM}/rest/pug/compound/name/{httpx.URL(canonical)}/cids/JSON"
    cid_json = await _pubchem_get(client, url)
    for _ in range(notfound_retries):
        if cid_json is not None:
            break
        await _sleep(NOTFOUND_RETRY_S)
        cid_json = await _pubchem_get(client, url)
    if cid_json is None:
        if notfound_retries == 0:
            _cid_cache_store(key, None)
    elif isinstance(cid_json, dict) and "IdentifierList" in cid_json:
        _cid_cache_store(key, cid_json)
    return cid_json


async def pubchem_fetch(client, canonical, notfound_retries=0):
    """Resolve canonical name to a confidence-checked CID + facts, or None (unresolved)."""
    cid_json = await _cid_lookup(client, canonical, notfound_retries)
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
    require_lightrag()
    if not args.dry_run and not args.collect:
        require_ollama()

    stats = {"enriched": 0, "skipped_judge": 0, "judge_error": 0, "unresolved": 0,
             "rejected": 0, "unverified": 0, "fetch_failed": 0, "gone": 0, "already": 0, "error": 0}
    error_names = []
    collected = {}  # --collect: {name: {"old", "new"}} instead of graph writes

    cands = enumerate_candidates()
    names = list(cands.keys())
    if args.limit:
        names = names[: args.limit]
        log(f"[limit] capped to {len(names)} candidates")

    judge_cache = load_judge_cache()
    verify_cache = load_verify_cache()
    verify_keys0 = set(verify_cache)  # snapshot: verify_match adds entries during this run
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

    breaker = _PubchemBreaker()
    try:
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
                    breaker.ok()  # PubChem answered (facts or None): no IP block
                    if not facts:
                        log(f"[unresolved] {name!r} (canonical={canonical!r})")
                        stats["unresolved"] += 1
                        continue

                    same = await verify_match(client, name, facts, verify_cache)
                    if same is None:
                        log(f"[unverified] {name!r} -> CID {facts['cid']}")
                        stats["unverified"] += 1
                        if _glm["stop"]:
                            break  # GLM quota/budget: nothing further can be verified
                        continue
                    if not same:
                        log(f"[rejected] {name!r} -> CID {facts['cid']} {facts.get('formula')} "
                            f"({facts.get('iupac')})")
                        stats["rejected"] += 1
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
                    if args.collect:
                        collected[name] = {"old": desc, "new": new_desc}
                        log(f"[collected] {name!r} -> CID {facts['cid']} mp={facts['mp']}")
                    else:
                        await write_entity(client, name, new_desc)
                        log(f"[enriched] {name!r} -> CID {facts['cid']} mp={facts['mp']}")
                    stats["enriched"] += 1
                except FetchFailed as e:
                    if e.blocked:
                        await breaker.blocked()
                    log(f"[fetch_failed] {name!r} (canonical={canonical!r})")
                    stats["fetch_failed"] += 1
                except Exception as e:
                    log(f"[error] {name!r}: {e}")
                    stats["error"] += 1
                    error_names.append(name)
    finally:  # a mid-loop kill still leaves a usable partial collect file
        if args.collect:
            _save_collected(args.collect, collected)
            new_ents = _save_new_entities(CACHE_DIR / NEW_ENTITIES_FILE, collected, verify_keys0)

    log("\n==== SUMMARY ====")
    for k, v in stats.items():
        log(f"  {k}: {v}")
    log(f"  candidates: {len(names)}  compounds: {len(compounds)}")
    if args.dry_run:
        log("  (dry-run: no writes performed)")
    if args.collect:
        log(f"  collected: {len(collected)} -> {args.collect}")
        log(f"  new entities for Claude review: {len(new_ents)} -> {CACHE_DIR / NEW_ENTITIES_FILE}")
    if error_names:
        log("  nodes that hit [error] may carry a marker with a stale vector; "
            "re-run with --refresh:")
        for n in error_names:
            log(f"    {n!r}")
    if _glm["stop"]:  # stopped mid-loop on the verify step; a --collect FILE holds verified entries only
        _write_resume_and_exit(names)


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


def scan_leaks():
    """'node <name>' / 'edge <src> -> <tgt>' for every description mentioning PubChem/OpenAlex/CID
    outside the marked blocks: an ingest's LLM merge summary absorbed a block into prose."""
    if not GRAPHML.exists():
        log(f"FATAL: graphml not found at {GRAPHML}")
        sys.exit(1)
    root = ET.parse(GRAPHML).getroot()
    desc_keys = {k.get("id") for k in root.iter(GRAPHML_NS + "key") if k.get("attr.name") == "description"}
    hits = []
    for el in list(root.iter(GRAPHML_NS + "node")) + list(root.iter(GRAPHML_NS + "edge")):
        for data in el.findall(GRAPHML_NS + "data"):
            if data.get("key") in desc_keys and LEAK_RE.search(_leak_text(data.text)):
                hits.append(f"node {el.get('id')}" if el.get("id") is not None
                            else f"edge {el.get('source')} -> {el.get('target')}")
    return hits


async def fix_blocks(args):
    """Clean existing PubChem blocks: strip rule-skipped nodes, rewrite changed blocks, keep unjudged and unresolved. No judge calls. --verify adds one cached GLM yes/no per resolved block (needs ZAI key) and strips rejected blocks. Backs up descriptions before writes."""
    stats = {k: 0 for k in ("marked", "strip", "rewrite", "same", "keep_unjudged",
                            "keep_unresolved", "reject", "keep_unverified", "block_only", "fetch_failed", "gone", "nomarker", "error")}
    error_names = []
    backup = {}
    collected = {}  # --collect: {name: {"old", "new"}} instead of graph writes
    backup_file = CACHE_DIR / f"fixblocks_backup_{time.strftime('%Y%m%d-%H%M%S')}.json"
    suffix = " (dry-run)" if args.dry_run else ""
    if args.verify:
        _resume_gate(args.ignore_resume)
        _glm["max"] = args.max_glm_tokens
        if not ZAI_KEY:
            log("FATAL: --verify needs ZAI_API_KEY.")
            sys.exit(1)
    verify_cache = load_verify_cache() if args.verify else {}
    require_lightrag()
    if not args.dry_run and not args.collect:
        require_ollama()

    names = _marked_names()
    stats["marked"] = len(names)
    log(f"[fix] {len(names)} nodes carry a PubChem block")
    cache = load_judge_cache()

    breaker = _PubchemBreaker()
    try:
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
                    if args.strip_all:
                        reason = "strip-all"
                    elif _rule_skip(name):
                        reason = "rule-skip"
                    else:
                        v = cache.get(name)
                        if not (v and v.get("decision") == "compound" and v.get("canonical")):
                            log(f"[fix:keep-unjudged] {name!r}")
                            stats["keep_unjudged"] += 1
                            continue
                        facts = await pubchem_fetch(client, v["canonical"], notfound_retries=2)
                        breaker.ok()  # PubChem answered (facts or None): no IP block
                        if facts is None:  # resolution failure is never grounds to strip
                            log(f"[fix:keep-unresolved] {name!r} (canonical={v['canonical']!r})")
                            stats["keep_unresolved"] += 1
                            continue
                        ok = await verify_match(client, name, facts, verify_cache) if args.verify else True
                        if ok is None:
                            log(f"[fix:keep-unverified] {name!r}")
                            stats["keep_unverified"] += 1
                            if _glm["stop"]:
                                break  # GLM quota/budget: nothing further can be verified
                            continue
                        if not ok:
                            stats["reject"] += 1
                            reason = (f"verify-reject: CID {facts['cid']} {facts.get('formula')} "
                                      f"({facts.get('iupac')})")
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
                        log(f"{'[collected]' if args.collect else '[fix:strip]'} {name!r} ({reason}){suffix}")
                    else:
                        new_desc = stripped + "\n\n" + new_block
                        kind = "rewrite"
                        log(f"{'[collected]' if args.collect else '[fix:rewrite]'} {name!r} mp: "
                            f"{_block_mp(old_block)} -> {_block_mp(new_block)}{suffix}")

                    if args.collect:  # the collect file itself carries "old": no backup file
                        collected[name] = {"old": desc, "new": new_desc}
                    elif not args.dry_run:
                        backup[name] = desc
                        CACHE_DIR.mkdir(parents=True, exist_ok=True)
                        backup_file.write_text(json.dumps(backup, ensure_ascii=False, indent=2),
                                               encoding="utf-8")
                        await write_entity(client, name, new_desc)
                    stats[kind] += 1
                except FetchFailed as e:
                    if e.blocked:
                        await breaker.blocked()
                    log(f"[fix:fetch_failed] {name!r}")
                    stats["fetch_failed"] += 1
                except Exception as e:
                    log(f"[fix:error] {name!r}: {e}")
                    stats["error"] += 1
                    error_names.append(name)
    finally:  # a mid-loop kill still leaves a usable partial collect file
        if args.collect:
            _save_collected(args.collect, collected)

    log("\n==== FIX-BLOCKS SUMMARY ====")
    for k, v in stats.items():
        log(f"  {k}: {v}")
    if args.dry_run:
        log("  (dry-run: no writes performed)")
    if args.collect:
        log(f"  collected: {len(collected)} -> {args.collect}")
    if backup:
        log(f"  backup: {backup_file}")
    if error_names:
        log("  nodes that hit [fix:error] (write may be partial; re-run --fix-blocks):")
        for n in error_names:
            log(f"    {n!r}")
    if _glm["stop"]:
        _write_resume_and_exit(names)


# ---------------------------------------------------------------- selftest
async def _selftest_pubchem_fetch():
    """pubchem_fetch never turns a bad reply into empty facts or a cache file (caller stubs sleeps)."""
    global CACHE_DIR, _cid_cache
    import tempfile
    timeout = {"Fault": {"Code": "PUGREST.Timeout"}}
    ids = {"IdentifierList": {"CID": [962]}}

    async def fetch(prop, syn):
        global _cid_cache
        _cid_cache = None

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
        _cid_cache = None
        try:
            props = {"PropertyTable": {"Properties": [{"CID": 962, "MolecularFormula": "H2O",
                                                        "ConnectivitySMILES": "O"}]}}
            assert await fetch(props, timeout) == "FetchFailed"
            # nothing cached per CID on a bad synonyms reply (the name lookup file is separate)
            assert not [f for f in CACHE_DIR.glob("*.json") if f.name != CID_LOOKUP_FILE]
            syns = {"InformationList": {"Information": [{"CID": 962, "Synonym": ["water"]}]}}
            facts = await fetch(props, syns)
            assert facts and facts["smiles"] == "O", facts  # ConnectivitySMILES rename
            assert json.loads((CACHE_DIR / "962.json").read_text(encoding="utf-8"))["v"] == FACTS_VERSION
        finally:
            CACHE_DIR = old_dir
            _cid_cache = None


async def _selftest_cid_cache():
    """_cid_lookup name cache: hit skips the request, negative TTL/retry rules, nothing cached on failure."""
    global _cid_cache
    ok = {"IdentifierList": {"CID": [962]}}
    calls = []
    replies = []

    def handler(request):
        calls.append(1)
        status, body = replies.pop(0) if len(replies) > 1 else replies[0]
        return httpx.Response(status, json=body)

    def on_disk():
        return json.loads((CACHE_DIR / CID_LOOKUP_FILE).read_text(encoding="utf-8"))

    async with httpx.AsyncClient(transport=httpx.MockTransport(handler)) as c:
        # (a) a positive answer is fetched once, then served from the cache with zero requests
        (CACHE_DIR / CID_LOOKUP_FILE).unlink(missing_ok=True)  # earlier cases left entries
        _cid_cache = None
        replies[:] = [(200, ok)]
        assert await _cid_lookup(c, "Water", 0) == ok and len(calls) == 1
        assert await _cid_lookup(c, "  water ", 0) == ok and len(calls) == 1  # key = _norm(name)
        _cid_cache = None  # and it was persisted: a fresh load reads it back
        assert await _cid_lookup(c, "water", 2) == ok and len(calls) == 1
        # (b) a genuine not-found is cached negative; notfound_retries>0 ignores it and stores no negative
        _cid_cache = None
        calls.clear()
        replies[:] = [(404, {})]
        assert await _cid_lookup(c, "nosuch", 0) is None and len(calls) == 1
        assert await _cid_lookup(c, "nosuch", 0) is None and len(calls) == 1
        assert on_disk()["nosuch"]["r"] is None
        assert await _cid_lookup(c, "nosuch", 1) is None and len(calls) == 3  # lookup + retry after the sleep
        replies[:] = [(200, ok)]
        assert await _cid_lookup(c, "nosuch", 1) == ok  # positive replaces the negative
        assert await _cid_lookup(c, "nosuch", 0) == ok and len(calls) == 4
        _cid_cache = None
        calls.clear()
        replies[:] = [(404, {})]
        assert await _cid_lookup(c, "neverseen", 1) is None and len(calls) == 2
        assert "neverseen" not in on_disk()  # no negative stored on the retry path
        # (c) an expired negative entry is ignored
        _cid_cache = {"old": {"r": None, "ts": time.time() - NOTFOUND_CACHE_TTL_S - 60}}
        calls.clear()
        assert await _cid_lookup(c, "old", 0) is None and len(calls) == 1
        # (d) a Fault body, a reply without IdentifierList, or FetchFailed writes nothing
        _cid_cache = {}
        (CACHE_DIR / CID_LOOKUP_FILE).unlink()
        for bad in ((200, {"Fault": {"Code": "PUGREST.ServerError"}}), (500, {})):
            replies[:] = [bad]
            try:
                await _cid_lookup(c, "bad", 0)
                raise AssertionError("no FetchFailed")
            except FetchFailed:
                pass
        replies[:] = [(200, {"Other": 1})]
        assert await _cid_lookup(c, "odd", 0) == {"Other": 1}
        assert not (CACHE_DIR / CID_LOOKUP_FILE).exists() and _cid_cache == {}
    # (e) a corrupt or non-dict cache file loads as empty instead of crashing
    for junk in ("{not json", "[1, 2]", ""):
        (CACHE_DIR / CID_LOOKUP_FILE).write_text(junk, encoding="utf-8")
        _cid_cache = None
        assert _cid_cache_load() == {}
    _cid_cache = None


async def _selftest_fetch():
    """_pubchem_get retry/None/FetchFailed behaviour against httpx.MockTransport, no network."""
    global PUBCHEM_MIN_INTERVAL, _sleep, _pubchem_interval, CACHE_DIR, _cid_cache
    import tempfile
    tmpdir = tempfile.TemporaryDirectory()  # _cid_lookup writes cid_lookup.json: keep it off the real cache
    old_dir, CACHE_DIR, _cid_cache = CACHE_DIR, Path(tmpdir.name), None
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

    async def run_exc(*replies):  # like run, but returns the FetchFailed itself (for .blocked)
        it = iter(replies)

        def handler(request):
            status, body = next(it, replies[-1])
            return httpx.Response(status, json=body)

        async with httpx.AsyncClient(transport=httpx.MockTransport(handler)) as c:
            try:
                return await _pubchem_get(c, "http://x/y")
            except FetchFailed as e:
                return e

    old_int, old_sleep, old_pint = PUBCHEM_MIN_INTERVAL, _sleep, _pubchem_interval

    async def no_sleep(s):
        pass

    PUBCHEM_MIN_INTERVAL, _sleep, _pubchem_interval = 0, no_sleep, 0
    try:
        assert [_url_kind(u) for u in (
            "https://x/compound/name/a/cids/JSON", "https://x/compound/cid/1/property/X/JSON",
            "https://x/compound/cid/1/synonyms/JSON", "https://x/rest/pug_view/data/compound/1/JSON",
            "https://x/y")] == ["cid", "props", "syn", "pugview", "other"]
        assert await run((200, busy), (200, ok)) == (ok, 2)  # ServerBusy Fault on a 200
        assert await run((502, {}), (200, ok)) == (ok, 2)
        assert await run((200, busy)) == ("FetchFailed", PUBCHEM_ATTEMPTS)  # always busy
        assert await run((404, {})) == (None, 1)  # genuine not-found, no retry
        timeout = {"Fault": {"Code": "PUGREST.Timeout"}}
        srverr = {"Fault": {"Code": "PUGREST.ServerError"}}
        assert await run((200, timeout), (200, ok)) == (ok, 2)  # non-busy Fault on a 200 is retried
        assert await run((200, srverr)) == ("FetchFailed", PUBCHEM_ATTEMPTS)
        assert await run((200, {"Fault": {"Code": "PUGREST.NotFound"}})) == (None, 1)
        # _cid_lookup: PubChem briefly answers NotFound for names it has; --fix-blocks retries
        seq = iter([(404, {}), (200, ok)])
        lookups = []

        def lookup_handler(request):
            lookups.append(1)
            status, body = next(seq)
            return httpx.Response(status, json=body)

        async with httpx.AsyncClient(transport=httpx.MockTransport(lookup_handler)) as c:
            assert await _cid_lookup(c, "water", 2) == ok and len(lookups) == 2
        seq = iter([(404, {})] * 5)
        lookups.clear()
        _cid_cache = {}  # the positive above would otherwise answer from the cache
        async with httpx.AsyncClient(transport=httpx.MockTransport(lookup_handler)) as c:
            assert await _cid_lookup(c, "water", 0) is None and len(lookups) == 1
            lookups.clear()
            assert await _cid_lookup(c, "water", 2) is None and len(lookups) == 3
        # adaptive interval + blocked flag: 429/ServerBusy grow _pubchem_interval, a success decays it
        base = PUBCHEM_MIN_INTERVAL = _pubchem_interval = old_int  # the real baseline
        e = await run_exc(*[(429, {})] * 5)
        assert type(e) is FetchFailed and e.blocked is True  # a 429 streak = IP block
        assert _pubchem_interval > base
        _pubchem_interval = base
        assert await run((429, {}), (200, ok)) == (ok, 2)
        assert base <= _pubchem_interval <= base * 2  # a success after a 429 decays the doubled value
        for _ in range(4):  # a long 429 run (20 mocked 429s) never pushes the interval past the cap
            await run_exc(*[(429, {})] * 5)
            assert _pubchem_interval <= PUBCHEM_MAX_INTERVAL == 16.0
        _pubchem_interval = base
        # X-Throttling-Control header -> minimum interval
        def tc(c, t, s):
            return {"X-Throttling-Control": f"Request Count status: {c}, Request Time status: {t}, Service status: {s}"}
        assert _throttle_floor((tc("Green (0%)", "Green (0%)", "Yellow (50%)"))) == 0.0
        assert _throttle_floor((tc("Yellow (30%)", "Green (0%)", "Green (0%)"))) == 3.0
        assert _throttle_floor((tc("Green (0%)", "Red (80%)", "Green (0%)"))) == 8.0
        assert _throttle_floor((tc("Black (100%)", "Green (0%)", "Green (0%)"))) == 20.0
        assert _throttle_floor((tc("Green (0%)", "Green (0%)", "Red (80%)"))) == 4.0
        assert _throttle_floor((tc("Green (0%)", "Green (0%)", "Black (100%)"))) == 8.0
        assert _throttle_floor({}) == 0.0 and _throttle_floor(None) == 0.0
        assert _throttle_floor({"X-Throttling-Control": ""}) == 0.0
        assert _throttle_floor({"X-Throttling-Control": "garbage ::: 12"}) == 0.0
        # a success response carrying a Red request-count header lifts the interval past the decay
        _pubchem_interval = base

        def red_handler(request):
            return httpx.Response(200, json=ok, headers=tc("Red (80%)", "Green (0%)", "Green (0%)"))

        async with httpx.AsyncClient(transport=httpx.MockTransport(red_handler)) as c:
            assert await _pubchem_get(c, "http://x/y") == ok
        assert _pubchem_interval >= 8.0
        _pubchem_interval = base
        assert (await run_exc(*[(200, busy)] * 5)).blocked is True  # ServerBusy Fault = block signal
        assert (await run_exc(*[(200, srverr)] * 5)).blocked is False  # a plain Fault is not

        def dead(request):
            raise httpx.ConnectError("no route")

        async with httpx.AsyncClient(transport=httpx.MockTransport(dead)) as c:
            try:
                await _pubchem_get(c, "http://x/y")
                raise AssertionError("no FetchFailed")
            except FetchFailed as e:
                assert e.blocked is True  # transport errors = link down, counted as a block
        PUBCHEM_MIN_INTERVAL = _pubchem_interval = 0
        await _selftest_pubchem_fetch()
        CACHE_DIR, _cid_cache = Path(tmpdir.name), None  # _selftest_pubchem_fetch restored the real dir
        await _selftest_cid_cache()
    finally:
        PUBCHEM_MIN_INTERVAL, _sleep, _pubchem_interval = old_int, old_sleep, old_pint
        CACHE_DIR, _cid_cache = old_dir, None
        tmpdir.cleanup()


async def _selftest_breaker():
    """_PubchemBreaker: a blocked streak pauses the run once (via _sleep); a second streak exits 5."""
    global _sleep
    old_sleep = _sleep
    calls = []

    async def rec(s):
        calls.append(s)

    _sleep = rec
    try:
        b = _PubchemBreaker()
        for _ in range(PUBCHEM_BLOCK_STREAK):
            await b.blocked()
        assert calls == [PUBCHEM_BLOCK_PAUSE_S]  # exactly one long pause, no exit
        try:
            for _ in range(PUBCHEM_BLOCK_STREAK):
                await b.blocked()
            raise AssertionError("second streak did not exit")
        except SystemExit as e:
            assert e.code == 5
        assert calls == [PUBCHEM_BLOCK_PAUSE_S]  # the second streak exits instead of pausing again
    finally:
        _sleep = old_sleep


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


async def _selftest_verify():
    """verify_match: verdict cached per (name, CID) and saved, new CID re-asks, stop flag = None, no cache."""
    global CACHE_DIR
    import tempfile
    answer, calls = ["NO"], []

    def handler(request):
        calls.append(1)
        return httpx.Response(200, json={"choices": [{"message": {"content": answer[0]}}],
                                         "usage": {"total_tokens": 10}})

    old_dir, old_glm = CACHE_DIR, dict(_glm)
    with tempfile.TemporaryDirectory() as tmp:
        CACHE_DIR = Path(tmp)
        _glm.update({"tokens": 0, "max": 0, "stop": None, "reset_at": None, "new": 0})
        try:
            async with httpx.AsyncClient(transport=httpx.MockTransport(handler)) as c:
                cache = {}
                go = {"cid": 297, "formula": "CH4", "iupac": "methane"}
                assert await verify_match(c, "Graphene Oxide", go, cache) is False and len(calls) == 1
                assert await verify_match(c, "Graphene Oxide", go, cache) is False and len(calls) == 1
                assert load_verify_cache() == {"Graphene Oxide": {"cid": 297, "same": False}}
                answer[0] = "YES"
                assert await verify_match(c, "Graphene Oxide", dict(go, cid=1), cache) is True
                assert len(calls) == 2
                _glm["stop"] = "glm_quota"
                water = {"cid": 962, "formula": "H2O", "iupac": "oxidane"}
                assert await verify_match(c, "Water", water, cache) is None
                assert len(calls) == 2 and "Water" not in cache
        finally:
            CACHE_DIR = old_dir
            _glm.clear()
            _glm.update(old_glm)


def _selftest():
    global GRAPHML
    import tempfile
    from xml.sax.saxutils import escape
    p = _parse_judge
    assert p("COMPOUND: gallium") == {"decision": "compound", "canonical": "gallium"}
    assert p("Sure! compound: `silver(I) oxide`.")["canonical"] == "silver(I) oxide"
    assert p("```\nSKIP\n```") == {"decision": "skip", "canonical": None}
    assert p("skip")["decision"] == "skip"
    assert p("no idea") is None
    assert p("COMPOUND:  ") is None
    assert _parse_verify("YES") is True and _parse_verify("**yes**") is True
    assert _parse_verify("No.") is False and _parse_verify("maybe") is None and _parse_verify(None) is None

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
    narrative = "At 260 K, a first-order phase transition from fcc to simple cubic is observed."
    assert _parse_mp(pv({"StringWithMarkup": [{"String": narrative}]})) == "not available"
    assert _parse_mp(pv({"StringWithMarkup": [{"String": "MP: 44.2 °C"}]})) == "44.2 °C"
    assert _parse_mp(pv({"StringWithMarkup": [{"String": "about 44 °C"}]})) == "not available"
    assert _parse_mp(pv({"StringWithMarkup": [{"String": "43-45 °C"}]})) == "43 °C"

    def pvs(*strings):
        return {"Record": {"Section": [{"Information": [
            {"Value": {"StringWithMarkup": [{"String": s}]}} for s in strings]}]}}
    assert _parse_mp(pvs("43.8 °C", "111 °F (NTP, 1992)")) == "43.8 °C"  # agree within 5 °C
    assert _parse_mp(pvs("46 °C", "68 °C")) == "not available"  # two values disagree, no majority
    assert _parse_mp(pvs(narrative, "1180 °C")) == "1180 °C"
    assert _parse_mp(pvs("609.6 °F (NTP, 1992)", "610 °F", "32.0691 °C", "321 °C", "321 °C")) == "321 °C"  # outlier
    assert _parse_mp(pvs("1220 °F (NIOSH, 2024)", "660 °C")) == "660 °C"  # °C entries preferred over °F
    assert _parse_mp(pvs("2,446 °C")) == "2446 °C"  # thousands separator
    assert _parse_mp(pvs("3632 °F (NIOSH, 2024)", "2030 °C", "2054 °C", "3632 °F", "2072 °C")) == "2030 °C"  # 2 % of K at high T
    assert _parse_mp(pvs("160 °C", "MP: 150-155 °C", "156 - 157 °C", "150-157 °C", "153 °C")) == "160 °C"
    assert _parse_mp(pvs("greater than 572 °F (NTP, 1992)")) == "not available"  # lower bound only
    assert _parse_mp(pvs("> 300 °C")) == "not available"
    assert _parse_mp(pvs("13.4 °C", "42 - 44 °C")) == "not available"
    assert _block_mp(format_block({"cid": 1, "formula": "X", "mw": 1, "iupac": "x", "smiles": "C",
                                   "mp": "46.0 to 68.0 °C (range of PubChem values)"})) \
        == "46.0 to 68.0 °C (range of PubChem values)"
    for n in ("C", "Portlandite", "C-S-H Gel", "Ettringite Formation", "Graphite", "HOPG", "Carbon", "Nanographite", "Graphene Oxide", "Carbon Black", "Diamond", "Multi-Walled CNTs"):
        assert _rule_skip(n), n
    for n in ("Cu", "Sb", "O₂", "Gallium", "Paraffin Wax", "CaCO3", "Water", "Carbon Dioxide", "Graphitic Carbon Nitride", "Calcium Carbonate", "Fullerene C60"):
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
    with tempfile.TemporaryDirectory() as tmp:  # _save_collected: round trip, parent dir made, no .tmp left
        cf = os.path.join(tmp, "sub", "c.json")
        _save_collected(cf, {"A": {"old": "", "new": "x"}})
        assert json.loads(Path(cf).read_text(encoding="utf-8")) == {"A": {"old": "", "new": "x"}}
        assert os.listdir(os.path.dirname(cf)) == ["c.json"]
    blk = format_block({"cid": 962, "formula": "H2O", "mw": 18, "iupac": "oxidane", "smiles": "O", "mp": "0 °C"})
    assert not LEAK_RE.search(_leak_text("Water is a PCM.\n\n" + blk))
    assert LEAK_RE.search(_leak_text("Ice melts at 0 °C (PubChem CID 962)."))
    assert not LEAK_RE.search(_leak_text("x <!--OPENALEX_START-->OpenAlex W1<!--OPENALEX_END-->"))
    assert LEAK_RE.search(_leak_text("Cited 12 times per OpenAlex."))
    for t in ("Ice (CID: 962).", "Ice (CID#962).", "Its SMILES is O.", "IUPAC name oxidane.", "MW 18.015 g/mol, formula H2O."):
        assert LEAK_RE.search(_leak_text(t)), t
    for t in ("Water is a PCM.", "The molecular weight of the paraffin is 350 g/mol.", "Cited in the CID-Sweden project",
              "Water. " + blk.replace("PubChem", "PubChem facts SMILES IUPAC MW 18 g/mol CID: 962")):
        assert not LEAK_RE.search(_leak_text(t)), t
    assert LEAK_RE.search(_leak_text("PubChem facts: Formula Al."))
    for t in ("InChI=1S/H2O/h1H2.", "InChIKey XLYOFNOQVPJJNP-UHFFFAOYSA-N.", "Key XLYOFNOQVPJJNP-UHFFFAOYSA-N.",
              "The molecular weight of 18.015 g/mol.", "Its molecular mass is 18.015 g/mol.", "Ice (CID : 962).",
              "x <!--OPENALEX_START-->ok<!--OPENALEX_END--> InChI=1S/H2O"):
        assert LEAK_RE.search(_leak_text(t)), t
    for t in ("The molecular weight of polyethylene glycol is high.", "Molecular weight distribution was narrow.",
              "Water. " + blk.replace("PubChem", "PubChem InChI=1S/H2O XLYOFNOQVPJJNP-UHFFFAOYSA-N"),
              "x <!--OPENALEX_START-->InChI=1S/H2O<!--OPENALEX_END-->"):
        assert not LEAK_RE.search(_leak_text(t)), t
    for t in ("Cited by 12 (as of 2026-07).", "cited by 1,204 (as of 2026-07)", "Open-access PDF: https://x.org/a.pdf",
              "Work W2741809807 describes it.", "The molar mass of ice is about 18.015 g/mol.", "Water (18.015 g/mol) melts.",
              "x <!--OPENALEX_START-->ok<!--OPENALEX_END--> Cited by 3 (as of 2026-07)"):
        assert LEAK_RE.search(_leak_text(t)), t
    for t in ("Cited by several authors.", "Cited by 12 groups in 2026.", "An open-access paper.", "The PDF is open access.",
              "Sample W12345 and W1234567 were tested.", "Grade AW12345678 steel.", "The molar mass distribution was narrow.",
              "PEG (400 g/mol) was used.", "Molar mass of the polymer is not reported.",
              "x <!--OPENALEX_START-->Cited by 3 (as of 2026-07). Open-access PDF: u. W2741809807<!--OPENALEX_END-->",
              "Water. " + blk.replace("PubChem", "molar mass 18.015 g/mol (18.015 g/mol)")):
        assert not LEAK_RE.search(_leak_text(t)), t
    mpv = pvs("135 °C (dec.)", "180 °C sublimes", "56.6 °C at the triple point", "99 °C (decomposes)", "58.5 °C")
    assert [v[2] for v in _mp_values(mpv)] == ["58.5 °C"], _mp_values(mpv)
    for marker in ("(dec.)", "dec.", "(dec)", "decomposes", "with decomposition", "sublimes", "sublimation", "(subl.)",
                   "subl.", "at the triple point", "triple pt", "(boils)", "boils at this temperature"):
        assert _mp_values(pvs(f"150 °C {marker}")) == [], marker
    for ok in ("150 °C", "MP: 150 °C", "2,446 °C", "43-45 °C", "111 °F (NTP, 1992)", "300 K"):
        assert len(_mp_values(pvs(ok))) == 1, ok
    old_g = GRAPHML
    with tempfile.TemporaryDirectory() as tmp:
        GRAPHML = Path(tmp) / "g.graphml"
        GRAPHML.write_text(
            f'<graphml xmlns="{GRAPHML_NS[1:-1]}"><key id="d1" for="node" attr.name="description"/>'
            '<key id="e1" for="edge" attr.name="description"/><graph>'
            '<node id="Ice"><data key="d1">Ice (PubChem CID 962) melts at 0 °C.</data></node>'
            f'<node id="Water"><data key="d1">Water.\n\n{escape(blk)}</data></node>'
            '<edge source="Ice" target="Water"><data key="e1">Ice melts to water.</data></edge>'
            '</graph></graphml>', encoding="utf-8")
        try:
            assert scan_leaks() == ["node Ice"], scan_leaks()
        finally:
            GRAPHML = old_g
    try:  # require_lightrag: fail fast when the server is down (a run once logged 551 connection errors)
        require_lightrag("http://127.0.0.1:9")
    except SystemExit as ex:
        assert ex.code == 3, ex.code
    else:
        raise AssertionError("require_lightrag did not exit")
    with tempfile.TemporaryDirectory() as tmp:  # _save_new_entities: only collected names that had no verify entry at start
        nf = Path(tmp) / "sub" / "new.json"
        coll = {"A": {}, "B": {}, "C": {}}
        assert _save_new_entities(nf, coll, {"A"}) == ["B", "C"]
        assert json.loads(nf.read_text(encoding="utf-8")) == ["B", "C"]
        # resumed run: B/C now have verify entries but are still collected -> kept; Z (not collected) dropped
        nf.write_text(json.dumps(["B", "Z"]), encoding="utf-8")
        assert _save_new_entities(nf, coll, {"A", "B", "C"}) == ["B"]
        assert _save_new_entities(nf, {}, set()) == []
        assert os.listdir(nf.parent) == ["new.json"]
    asyncio.run(_selftest_fetch())
    asyncio.run(_selftest_quota_stop())
    asyncio.run(_selftest_verify())
    asyncio.run(_selftest_breaker())
    print("selftest OK")


def main():
    ap = argparse.ArgumentParser(description="PubChem enrichment of PCM_RAG chemical entities")
    ap.add_argument("--selftest", action="store_true", help="offline asserts, then exit")
    ap.add_argument("--dry-run", action="store_true", help="enumerate+judge+fetch, no graph writes")
    ap.add_argument("--refresh", action="store_true", help="re-enrich nodes already marked")
    ap.add_argument("--limit", type=int, default=0, help="cap number of candidates (testing)")
    ap.add_argument("--fix-blocks", action="store_true",
                    help="clean existing blocks: strip rule-skipped, rewrite changed (no judge calls; --dry-run = log only)")
    ap.add_argument("--verify", action="store_true",
                    help="with --fix-blocks: GLM yes/no check of each resolved block, strip rejects (needs ZAI key; cached in verify.json)")
    ap.add_argument("--max-glm-tokens", type=int, default=0,
                    help="stop cleanly (exit 4) once GLM usage.total_tokens reaches N; 0 = no cap")
    ap.add_argument("--ignore-resume", action="store_true",
                    help="start even if RESUME.json says a quota stop is still active")
    ap.add_argument("--collect", metavar="FILE",
                    help="collect new descriptions into FILE (JSON {name: {old, new}}) instead of writing the graph")
    ap.add_argument("--force", action="store_true", help="with --collect: overwrite an existing FILE")
    ap.add_argument("--strip-all", action="store_true",
                    help="with --fix-blocks --collect: strip EVERY PubChem block (before an ingest; re-add after)")
    ap.add_argument("--scan-leaks", action="store_true",
                    help="list descriptions with PubChem/OpenAlex facts outside the blocks; exit 7 if any")
    args = ap.parse_args()
    if args.selftest:
        _selftest()
        return
    if args.scan_leaks:
        hits = scan_leaks()
        for h in hits:
            log(f"[leak] {h}")
        log(f"leaks: {len(hits)}")
        sys.exit(7 if hits else 0)
    if args.strip_all and not (args.fix_blocks and args.collect):
        log("FATAL: --strip-all needs --fix-blocks --collect FILE")
        sys.exit(1)
    _collect_guard(args)
    asyncio.run(fix_blocks(args) if args.fix_blocks else run(args))


if __name__ == "__main__":
    main()
