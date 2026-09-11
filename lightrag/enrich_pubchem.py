"""Enrich existing PCM_RAG chemical entities with PubChem facts.

Shape 1 enrichment (see PLAN.md). Reads the persisted LightRAG graph, picks
chemical-entity candidates, LLM-judges them, resolves each to a PubChem CID,
and APPENDS a delimited PubChem-facts block onto the entity's description via
the running LightRAG server (/graph/entity/edit). Additive + idempotent:
original description text is preserved above the marker; re-runs replace the
block, never stack.

PRECONDITIONS:
  - LightRAG server UP and IDLE (no ingest running) at LIGHTRAG_URL.
  - ZAI_API_KEY set (glm-5.2 judge via z.ai).
  - Ollama not required (no embedding done here; server re-embeds on edit).

USAGE:
  python enrich_pubchem.py            # full run (writes to graph)
  python enrich_pubchem.py --dry-run  # enumerate+judge+fetch, NO writes
  python enrich_pubchem.py --refresh  # re-enrich nodes already marked
  python enrich_pubchem.py --limit 10 # cap candidates (testing)
"""
import argparse
import asyncio
import json
import os
import re
import sys
import time
import xml.etree.ElementTree as ET
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

ZAI_KEY = os.environ.get("ZAI_API_KEY", "")
ZAI_BASE = "https://api.z.ai/api/coding/paas/v4"
JUDGE_MODEL = "glm-5.2"

PUBCHEM = "https://pubchem.ncbi.nlm.nih.gov"
PUBCHEM_HEADERS = {
    "User-Agent": "PCM-RAG-enrich/1.0 (LightRAG PubChem enrichment; contact ilpin301@gmail.com)",
    "From": "ilpin301@gmail.com",
}

MARK_START = "<!--PUBCHEM_START-->"
MARK_END = "<!--PUBCHEM_END-->"
BLOCK_RE = re.compile(r"<!--PUBCHEM_START-->.*?<!--PUBCHEM_END-->", re.DOTALL)

# graphml attribute keys (verified): d0=entity_id, d1=entity_type, d2=description
K_TYPE = "d1"

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

# global PubChem throttle: flat 0.75s between calls (~1.33 req/s, under 5/s AND 400/5min)
PUBCHEM_MIN_INTERVAL = 0.75
_last_pubchem_call = 0.0


def log(msg):
    print(msg, flush=True)


# ---------------------------------------------------------------- step 1: enumerate
def enumerate_candidates():
    """Union of TYPE path and chemical-regex-over-concept/artifact path, deduped by name."""
    if not GRAPHML.exists():
        log(f"FATAL: graphml not found at {GRAPHML}")
        sys.exit(1)
    root = ET.parse(GRAPHML).getroot()
    cands = {}
    for node in root.iter(GRAPHML_NS + "node"):
        name = node.get("id")
        etype = None
        for data in node.findall(GRAPHML_NS + "data"):
            if data.get("key") == K_TYPE:
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


async def judge_one(client, sem, name, cache):
    if name in cache:
        return name, cache[name]
    async with sem:
        for attempt in range(4):
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
                if r.status_code == 429 or "1305" in r.text:
                    await asyncio.sleep(2 * (attempt + 1))  # z.ai concurrency (1305): back off
                    continue
                r.raise_for_status()
                out = r.json()["choices"][0]["message"]["content"].strip()
                verdict = _parse_judge(out)
                cache[name] = verdict
                return name, verdict
            except Exception as e:
                if attempt == 3:
                    log(f"[judge] ERROR {name!r}: {e}")
                    return name, None
                await asyncio.sleep(2 * (attempt + 1))
    return name, None


def _parse_judge(text):
    line = text.splitlines()[0].strip() if text else ""
    if line.upper().startswith("COMPOUND:"):
        return {"decision": "compound", "canonical": line.split(":", 1)[1].strip()}
    return {"decision": "skip", "canonical": None}


async def judge_all(names, cache):
    sem = asyncio.Semaphore(2)  # z.ai 1305 is a concurrency limit — never exceed 2
    async with httpx.AsyncClient(trust_env=False) as client:
        results = await asyncio.gather(*(judge_one(client, sem, n, cache) for n in names))
    save_judge_cache(cache)
    return dict(results)


# ---------------------------------------------------------------- step 3: PubChem
async def _throttle():
    global _last_pubchem_call
    now = time.monotonic()
    wait = PUBCHEM_MIN_INTERVAL - (now - _last_pubchem_call)
    if wait > 0:
        await asyncio.sleep(wait)
    _last_pubchem_call = time.monotonic()


async def _pubchem_get(client, url):
    for attempt in range(4):
        await _throttle()
        r = await client.get(url, headers=PUBCHEM_HEADERS, timeout=60)
        if r.status_code == 404:
            return None
        if r.status_code in (429, 503):
            retry = int(r.headers.get("Retry-After", 2 * (attempt + 1)))
            await asyncio.sleep(retry)
            continue
        r.raise_for_status()
        return r.json()
    return None


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
                        for num in val["Number"]:
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
        m = re.search(r"(-?\d+(?:\.\d+)?)\s*°?\s*f\b", low)
        if m:
            c = (float(m.group(1)) - 32) * 5 / 9
            return f"{c:.1f} °C"
        m = re.search(r"(-?\d+(?:\.\d+)?)\s*k\b", low)
        if m:
            return f"{float(m.group(1)) - 273.15:.1f} °C"
    return "not available"


async def pubchem_fetch(client, canonical):
    """Resolve canonical name to a confidence-checked CID + facts, or None (unresolved)."""
    cid_json = await _pubchem_get(
        client, f"{PUBCHEM}/rest/pug/compound/name/{httpx.URL(canonical)}/cids/JSON"
    )
    if not cid_json:
        return None
    try:
        cids = cid_json["IdentifierList"]["CID"]
    except (KeyError, TypeError):
        return None
    if not cids:
        return None
    cid = cids[0]
    cache_file = CACHE_DIR / f"{cid}.json"
    if cache_file.exists():
        facts = json.loads(cache_file.read_text(encoding="utf-8"))
        if _confidence_ok(canonical, facts):
            return facts
        return None
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
    try:
        p = prop["PropertyTable"]["Properties"][0]
    except (KeyError, IndexError, TypeError):
        return None
    synonyms = []
    try:
        synonyms = syn["InformationList"]["Information"][0]["Synonym"]
    except (KeyError, IndexError, TypeError):
        synonyms = []
    facts = {
        "cid": cid,
        "formula": p.get("MolecularFormula", ""),
        "mw": p.get("MolecularWeight", ""),
        "iupac": p.get("IUPACName", ""),
        "smiles": p.get("CanonicalSMILES", ""),
        "mp": _parse_mp(mp),
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
    if not ZAI_KEY:
        log("FATAL: ZAI_API_KEY not set.")
        sys.exit(1)

    stats = {"enriched": 0, "skipped_judge": 0, "unresolved": 0, "gone": 0,
             "already": 0, "error": 0}

    cands = enumerate_candidates()
    names = list(cands.keys())
    if args.limit:
        names = names[: args.limit]
        log(f"[limit] capped to {len(names)} candidates")

    judge_cache = load_judge_cache()
    log(f"[judge] classifying {len(names)} names (Semaphore 2)...")
    verdicts = await judge_all(names, judge_cache)

    compounds = [(n, v["canonical"]) for n, v in verdicts.items()
                 if v and v.get("decision") == "compound" and v.get("canonical")]
    stats["skipped_judge"] = len(names) - len(compounds)
    log(f"[judge] {len(compounds)} compounds, {stats['skipped_judge']} skipped")

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
            except Exception as e:
                log(f"[error] {name!r}: {e}")
                stats["error"] += 1

    log("\n==== SUMMARY ====")
    for k, v in stats.items():
        log(f"  {k}: {v}")
    log(f"  candidates: {len(names)}  compounds: {len(compounds)}")
    if args.dry_run:
        log("  (dry-run: no writes performed)")


def main():
    ap = argparse.ArgumentParser(description="PubChem enrichment of PCM_RAG chemical entities")
    ap.add_argument("--dry-run", action="store_true", help="enumerate+judge+fetch, no graph writes")
    ap.add_argument("--refresh", action="store_true", help="re-enrich nodes already marked")
    ap.add_argument("--limit", type=int, default=0, help="cap number of candidates (testing)")
    args = ap.parse_args()
    asyncio.run(run(args))


if __name__ == "__main__":
    main()
