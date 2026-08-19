"""Enrich existing PCM_RAG ref_text entities with OpenAlex bibliographic facts.

Shape 1 enrichment (see PLAN.md, GLM-approved). Reads the persisted LightRAG
graph, picks citation-stub candidates (ref_text + citation-shaped content
nodes), LLM-extracts structured citation fields, searches OpenAlex, LLM-judges
the candidate works under code-enforced hard rules, and APPENDS a delimited
OpenAlex-facts block onto the entity's description via the running LightRAG
server (/graph/entity/edit). Additive + idempotent: original description text
is preserved above the marker; re-runs replace the block, never stack. Uses
different markers than enrich_pubchem.py, so the two enrichers never clobber
each other.

PRECONDITIONS:
  - LightRAG server UP and IDLE (no ingest running) at LIGHTRAG_URL.
  - ZAI_API_KEY set (glm-5.2 extract + judge via z.ai).
  - Ollama not required (no embedding done here; server re-embeds on edit).

USAGE:
  python enrich_openalex.py            # full run (writes to graph)
  python enrich_openalex.py --dry-run  # enumerate+extract+search+judge, NO writes
  python enrich_openalex.py --refresh  # re-enrich nodes already marked
  python enrich_openalex.py --limit 10 # cap candidates (testing)
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


# Force UTF-8 output encoding on Windows (handles diacritics in author names)
for _s in (sys.stdout, sys.stderr):
    if (getattr(_s, "encoding", "") or "").lower() not in ("utf-8", "utf8"):
        _s.reconfigure(encoding="utf-8", errors="replace")

# ---------------------------------------------------------------- config
SCRIPT_DIR = Path(__file__).parent
GRAPHML = SCRIPT_DIR / "data" / "rag_storage" / "graph_chunk_entity_relation.graphml"
CACHE_DIR = SCRIPT_DIR / "data" / "enrich_cache"
EXTRACT_CACHE = CACHE_DIR / "extract_openalex.json"
JUDGE_CACHE = CACHE_DIR / "judge_openalex.json"
SEARCH_CACHE = CACHE_DIR / "search_openalex.json"

LIGHTRAG_URL = os.environ.get("LIGHTRAG_URL", "http://localhost:9622")


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
LLM_MODEL = "glm-5.2"

OPENALEX = "https://api.openalex.org"
MAILTO = "ilpin301@gmail.com"  # polite pool — approved by user


def _load_openalex_key():
    k = os.environ.get("OPENALEX_API_KEY")
    if k:
        return k
    envf = SCRIPT_DIR / ".env"
    if envf.exists():
        for line in envf.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line.startswith("OPENALEX_API_KEY="):
                return line.split("=", 1)[1].strip().strip('"').strip("'")
    return ""


OPENALEX_API_KEY = _load_openalex_key()

MARK_START = "<!--OPENALEX_START-->"
MARK_END = "<!--OPENALEX_END-->"
BLOCK_RE = re.compile(r"<!--OPENALEX_START-->.*?<!--OPENALEX_END-->", re.DOTALL)


class SearchUnavailable(RuntimeError):
	"""OpenAlex search could not be completed (rate-limited / transport failure).

	Raised instead of returning an empty list so a failed search is never
	cached as a legitimate "no hits" result.
	"""


# graphml attribute keys (verified): d0=entity_id, d1=entity_type, d2=description
K_TYPE = "d1"
K_DESC = "d2"

TYPE_PATH = {"ref_text"}
REGEX_TYPES = {"content"}
CITE_RE = re.compile(r"(et al|reference \[|\(\d{4}\))", re.IGNORECASE)
YEAR_RE = re.compile(r"\b(19|20)\d{2}\b")

GRAPHML_NS = "{http://graphml.graphdrawing.org/xmlns}"

# OpenAlex throttle: flat 0.15s between calls (~6.7 req/s, under polite-pool 10/s)
OPENALEX_MIN_INTERVAL = 0.15
_last_openalex_call = 0.0

EXTRACT_BATCH = 20
DESC_TRIM = 800  # chars of description passed to the LLM per node


def log(msg):
    print(msg, flush=True)


# ---------------------------------------------------------------- cache helpers (atomic)
def _load_json(path):
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8"))
    return {}


def _save_json(path, obj):
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding="utf-8")
    os.replace(tmp, path)


# ---------------------------------------------------------------- step 1: enumerate
def enumerate_candidates():
    """ref_text nodes ∪ citation-shaped content nodes, deduped by name.

    Returns {name: {"etype": str, "description": str}}.
    """
    if not GRAPHML.exists():
        log(f"FATAL: graphml not found at {GRAPHML}")
        sys.exit(1)
    root = ET.parse(GRAPHML).getroot()
    cands = {}
    for node in root.iter(GRAPHML_NS + "node"):
        name = node.get("id")
        etype = None
        desc = ""
        for data in node.findall(GRAPHML_NS + "data"):
            if data.get("key") == K_TYPE:
                etype = data.text
            elif data.get("key") == K_DESC:
                desc = data.text or ""
        if not name or not etype:
            continue
        if etype in TYPE_PATH:
            cands[name] = {"etype": etype, "description": desc}
        elif etype in REGEX_TYPES and CITE_RE.search(name) and YEAR_RE.search(name):
            cands[name] = {"etype": etype, "description": desc}
    log(f"[enumerate] {len(cands)} candidates (ref_text + citation-shaped content)")
    return cands


# ---------------------------------------------------------------- step 2: LLM extract
EXTRACT_SYSTEM = (
    "You extract structured citation fields from knowledge-graph reference nodes. "
    "Each input item has an index, a node name, and a description paraphrasing an "
    "academic citation. For EACH item return one JSON object with keys:\n"
    '  "idx": <the input index, integer>\n'
    '  "surname": <first author\'s SURNAME only, string, or null if not stated>\n'
    '  "year": <4-digit publication year, integer, or null if not stated>\n'
    '  "venue": <journal/conference name, string, or null>\n'
    '  "title_guess": <your best reconstruction of the paper title, string, or null>\n'
    '  "keywords": <3-6 space-separated topic words from the description, string>\n'
    "Reply with ONLY a JSON array of these objects — no prose, no code fences. "
    "Never invent a surname or year that is not stated in the name or description."
)


async def _llm_call(client, sem, messages, max_tokens=4000):
    async with sem:
        for attempt in range(4):
            try:
                r = await client.post(
                    f"{ZAI_BASE}/chat/completions",
                    headers={"Authorization": f"Bearer {ZAI_KEY}"},
                    json={
                        "model": LLM_MODEL,
                        "temperature": 0,
                        "max_tokens": max_tokens,
                        "messages": messages,
                    },
                    timeout=120,
                )
                if r.status_code == 429 or "1305" in r.text:
                    await asyncio.sleep(2 * (attempt + 1))  # z.ai concurrency: back off
                    continue
                r.raise_for_status()
                return r.json()["choices"][0]["message"]["content"].strip()
            except Exception:
                if attempt == 3:
                    raise
                await asyncio.sleep(2 * (attempt + 1))
    return None


def _parse_json_array(text):
    """Extract a JSON array from LLM output (tolerates stray prose/fences)."""
    if not text:
        return None
    m = re.search(r"\[.*\]", text, re.DOTALL)
    if not m:
        return None
    try:
        arr = json.loads(m.group(0))
        return arr if isinstance(arr, list) else None
    except json.JSONDecodeError:
        return None


def _valid_year(y):
    try:
        y = int(y)
    except (TypeError, ValueError):
        return None
    return y if 1900 <= y <= 2026 else None


async def extract_all(names, cands, cache):
    """Batch-extract citation fields; per-node fallback on batch parse failure.

    Returns {name: {"surname":..., "year":..., "venue":..., "title_guess":...,
    "keywords":...}} — entry value None means extraction failed/insufficient.
    """
    todo = [n for n in names if n not in cache]
    if todo:
        log(f"[extract] {len(todo)} nodes to extract ({len(names) - len(todo)} cached)")
    sem = asyncio.Semaphore(2)  # z.ai 1305 is a concurrency limit — never exceed 2

    async def do_batch(client, batch):
        items = []
        for i, n in enumerate(batch):
            desc = (cands[n]["description"] or "")[:DESC_TRIM]
            items.append(f"[{i}] NAME: {n}\nDESCRIPTION: {desc}")
        user = "\n\n".join(items)
        try:
            out = await _llm_call(
                client, sem,
                [{"role": "system", "content": EXTRACT_SYSTEM},
                 {"role": "user", "content": user}],
            )
        except Exception as e:
            log(f"[extract] batch ERROR: {e}")
            out = None
        arr = _parse_json_array(out)
        got = {}
        if arr is not None:
            for obj in arr:
                if not isinstance(obj, dict):
                    continue
                try:
                    i = int(obj.get("idx"))
                except (TypeError, ValueError):
                    continue
                if 0 <= i < len(batch):
                    got[batch[i]] = obj
        return got

    async with httpx.AsyncClient(trust_env=False) as client:
        for start in range(0, len(todo), EXTRACT_BATCH):
            batch = todo[start:start + EXTRACT_BATCH]
            got = await do_batch(client, batch)
            missing = [n for n in batch if n not in got]
            if missing:  # batch truncated/unparseable → per-node fallback
                log(f"[extract] fallback: {len(missing)} nodes retried singly")
                for n in missing:
                    got.update(await do_batch(client, [n]))
            for n in batch:
                obj = got.get(n)
                if obj is None:
                    cache[n] = None
                else:
                    year = _valid_year(obj.get("year"))
                    surname = (obj.get("surname") or "").strip() or None
                    if year is None or surname is None:
                        cache[n] = None  # hard requirement: surname + valid year
                    else:
                        cache[n] = {
                            "surname": surname,
                            "year": year,
                            "venue": (obj.get("venue") or "").strip() or None,
                            "title_guess": (obj.get("title_guess") or "").strip() or None,
                            "keywords": (obj.get("keywords") or "").strip(),
                        }
            _save_json(EXTRACT_CACHE, cache)
    return {n: cache.get(n) for n in names}


# ---------------------------------------------------------------- step 3: OpenAlex search
async def _throttle():
    global _last_openalex_call
    now = time.monotonic()
    wait = OPENALEX_MIN_INTERVAL - (now - _last_openalex_call)
    if wait > 0:
        await asyncio.sleep(wait)
    _last_openalex_call = time.monotonic()


async def openalex_search(client, ext, search_cache, name):
    """Search OpenAlex for candidate works. Returns simplified candidate list."""
    if name in search_cache:
        return search_cache[name]
    y = ext["year"]
    surname = ext["surname"].replace(",", " ").replace(":", " ").strip()
    terms = " ".join(t for t in (ext.get("title_guess"), ext.get("keywords")) if t)
    params = {
        "filter": f"publication_year:{y-1}|{y}|{y+1},raw_author_name.search:{surname}",
        "search": terms[:300],
        "per-page": 5,
        "mailto": MAILTO,
    }
    if OPENALEX_API_KEY:
        params["api_key"] = OPENALEX_API_KEY
    works = []
    for attempt in range(4):
        await _throttle()
        try:
            r = await client.get(f"{OPENALEX}/works", params=params, timeout=60)
        except Exception:
            if attempt == 3:
                raise
            await asyncio.sleep(2 * (attempt + 1))
            continue
        if r.status_code in (429, 503):
            await asyncio.sleep(int(r.headers.get("Retry-After", 2 * (attempt + 1))))
            continue
        r.raise_for_status()
        for w in r.json().get("results", []):
            loc = w.get("primary_location") or {}
            src = loc.get("source") or {}
            oa = w.get("open_access") or {}
            works.append({
                "id": (w.get("id") or "").rsplit("/", 1)[-1],
                "title": w.get("display_name") or "",
                "year": w.get("publication_year"),
                "venue": src.get("display_name") or "",
                "doi": w.get("doi") or "",
                "authors": [
                    (a.get("author") or {}).get("display_name") or ""
                    for a in (w.get("authorships") or [])
                ],
                "cited_by_count": w.get("cited_by_count", 0),
                "oa_url": oa.get("oa_url") or "",
            })
        break
    else:
        raise SearchUnavailable(f"OpenAlex search exhausted retries for {name!r}")
    search_cache[name] = works
    _save_json(SEARCH_CACHE, search_cache)
    return works


# ---------------------------------------------------------------- step 4: LLM judge + hard rules
JUDGE_SYSTEM = (
    "You verify whether one of the candidate OpenAlex works IS the exact paper that a "
    "knowledge-graph reference node cites. You get the node's name and description, then "
    "numbered candidates with title, authors, venue, year, DOI.\n\n"
    "Reply with EXACTLY ONE line:\n"
    "  MATCH: <candidate number>\n"
    "  or\n"
    "  SKIP\n\n"
    "Rules:\n"
    "- MATCH only if the candidate is clearly the SAME work: authors, year, and subject "
    "must all be consistent with the reference description.\n"
    "- Venue is a SOFT signal: citation abbreviations often differ from OpenAlex canonical "
    "venue names — a venue mismatch alone does not force SKIP, but never use venue "
    "similarity as the only evidence.\n"
    "- When in doubt, SKIP. A missing enrichment is harmless; a wrong one poisons the graph.\n"
    "- Never pick a review/erratum/preprint duplicate over the work actually described."
)


def _hard_rules_ok(ext, cand):
    """Code-enforced gates the judge cannot override: year ±1, surname in authorship."""
    cy = cand.get("year")
    if not isinstance(cy, int) or abs(cy - ext["year"]) > 1:
        return False
    surname = ext["surname"].lower()
    authors = " ".join(cand.get("authors") or []).lower()
    return surname in authors


async def judge_one(client, sem, name, desc, cands_list, cache):
    if name in cache:
        return cache[name]
    lines = [f"REFERENCE NODE NAME: {name}", f"DESCRIPTION: {desc[:DESC_TRIM]}", "", "CANDIDATES:"]
    for i, c in enumerate(cands_list, 1):
        auth = ", ".join(c["authors"][:5]) + (" et al." if len(c["authors"]) > 5 else "")
        lines.append(
            f"[{i}] TITLE: {c['title']} | AUTHORS: {auth} | VENUE: {c['venue']} | "
            f"YEAR: {c['year']} | DOI: {c['doi'] or 'none'}"
        )
    try:
        out = await _llm_call(
            client, sem,
            [{"role": "system", "content": JUDGE_SYSTEM},
             {"role": "user", "content": "\n".join(lines)}],
            max_tokens=200,
        )
    except Exception as e:
        log(f"[judge] ERROR {name!r}: {e}")
        return None
    verdict = {"decision": "skip", "pick": None}
    line = (out or "").splitlines()[0].strip() if out else ""
    m = re.match(r"MATCH:\s*(\d+)", line, re.IGNORECASE)
    if m:
        i = int(m.group(1))
        if 1 <= i <= len(cands_list):
            verdict = {"decision": "match", "pick": i - 1}
    cache[name] = verdict
    _save_json(JUDGE_CACHE, cache)
    return verdict


# ---------------------------------------------------------------- step 5: format
def _sanitize(s):
    """Strip marker-breaking sequences and newlines from external strings."""
    s = (s or "").replace("<!--", " ").replace("-->", " ")
    return re.sub(r"\s+", " ", s).strip()


def _norm_doi(doi):
    doi = (doi or "").strip()
    if not doi:
        return None
    if doi.startswith("https://doi.org/") or doi.startswith("http://doi.org/"):
        return doi
    if doi.startswith("10."):
        return "https://doi.org/" + doi
    return None


def format_block(work):
    title = _sanitize(work["title"])
    authors = [_sanitize(a) for a in work["authors"][:3] if a]
    auth = ", ".join(authors) + (" et al." if len(work["authors"]) > 3 else "")
    venue = _sanitize(work["venue"]) or "unknown venue"
    doi = _norm_doi(work["doi"]) or "none"
    oa = work.get("oa_url") or ""
    oa = oa if oa.startswith(("http://", "https://")) else "none"
    asof = datetime.now().strftime("%Y-%m")
    wid = _sanitize(work["id"])
    return (
        f"{MARK_START}\n"
        f'OpenAlex reference facts ({wid}): Title: "{title}". Authors: {auth}. '
        f"Venue: {venue}. Year: {work['year']}. DOI: {doi}. "
        f"Cited by {work['cited_by_count']} (as of {asof}). "
        f"Open-access PDF: {oa}. Source: OpenAlex {wid}.\n"
        f"{MARK_END}"
    )


# ---------------------------------------------------------------- step 6: fresh read + write
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

    stats = {"enriched": 0, "skipped_judge": 0, "unresolved": 0,
             "hard_rule_reject": 0, "gone": 0, "already": 0, "error": 0}

    cands = enumerate_candidates()
    names = list(cands.keys())
    if args.limit:
        names = names[: args.limit]
        log(f"[limit] capped to {len(names)} candidates")

    extract_cache = _load_json(EXTRACT_CACHE)
    extracted = await extract_all(names, cands, extract_cache)
    n_ext = sum(1 for v in extracted.values() if v)
    log(f"[extract] {n_ext} extractable, {len(names) - n_ext} unresolved at extraction")

    judge_cache = _load_json(JUDGE_CACHE)
    search_cache = _load_json(SEARCH_CACHE)
    sem = asyncio.Semaphore(2)
    processed = 0

    async with httpx.AsyncClient(trust_env=False) as client:
        async def _process_one(name):
            ext = extracted.get(name)
            if not ext:
                log(f"[unresolved] {name!r} (extraction)")
                stats["unresolved"] += 1
                return

            # skip-check: already enriched (unless --refresh)
            if not args.refresh:
                desc = await fresh_description(client, name)
                if desc is None:
                    log(f"[gone] {name!r}")
                    stats["gone"] += 1
                    return
                if MARK_START in desc:
                    log(f"[already] {name!r}")
                    stats["already"] += 1
                    return

            works = await openalex_search(client, ext, search_cache, name)
            if not works:
                log(f"[unresolved] {name!r} (no OpenAlex hits)")
                stats["unresolved"] += 1
                return

            verdict = await judge_one(
                client, sem, name, cands[name]["description"], works, judge_cache
            )
            if not verdict or verdict.get("decision") != "match":
                log(f"[skipped_judge] {name!r}")
                stats["skipped_judge"] += 1
                return
            work = works[verdict["pick"]]
            if not _hard_rules_ok(ext, work):
                log(f"[hard_rule_reject] {name!r} -> {work['id']} "
                    f"(year/surname gate)")
                stats["hard_rule_reject"] += 1
                return

            block = format_block(work)
            if args.dry_run:
                log(f"[dry-run] would enrich {name!r} -> {work['id']} "
                    f'"{work["title"][:60]}" ({work["year"]})')
                stats["enriched"] += 1
                return

            # fresh read immediately before write (avoid stale clobber)
            desc = await fresh_description(client, name)
            if desc is None:
                log(f"[gone] {name!r}")
                stats["gone"] += 1
                return
            stripped = BLOCK_RE.sub("", desc).rstrip()
            new_desc = (stripped + "\n\n" + block) if stripped else block
            await write_entity(client, name, new_desc)
            log(f"[enriched] {name!r} -> {work['id']} ({work['year']})")
            stats["enriched"] += 1

        for name in names:
            processed += 1
            if processed == 21 and stats["enriched"] == 0:
                log("!!!! WARNING: 0 enriched after first 20 candidates — "
                    "likely systemic extraction/judge failure. Check prompts/API.")
            try:
                await asyncio.wait_for(_process_one(name), timeout=240)
            except asyncio.TimeoutError:
                log(f"[timeout] {name!r} (skipped after 240s)")
                stats["error"] += 1
            except Exception as e:
                log(f"[error] {name!r}: {e}")
                stats["error"] += 1

    log("\n==== SUMMARY ====")
    for k, v in stats.items():
        log(f"  {k}: {v}")
    log(f"  candidates: {len(names)}  extractable: {n_ext}")
    if args.dry_run:
        log("  (dry-run: no writes performed)")


def main():
    ap = argparse.ArgumentParser(description="OpenAlex enrichment of PCM_RAG ref_text entities")
    ap.add_argument("--dry-run", action="store_true", help="extract+search+judge, no graph writes")
    ap.add_argument("--refresh", action="store_true", help="re-enrich nodes already marked")
    ap.add_argument("--limit", type=int, default=0, help="cap number of candidates (testing)")
    args = ap.parse_args()
    asyncio.run(run(args))


if __name__ == "__main__":
    main()
