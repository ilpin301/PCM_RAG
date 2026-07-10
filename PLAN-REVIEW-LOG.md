# Plan Review Log: OpenAlex enrichment of ref_text nodes
Act 1 (grill) complete — plan locked with the user. MAX_ROUNDS=5.

## Round 1 — GLM
(Note: review ran via direct z.ai API with PLAN.md + enrich_pubchem.py inlined — claude-CLI path was blocked by z.ai rate-limiting of Claude-Code-tagged traffic, error 1302/1305. GLM remained read-only by construction: no tools at all.)

**Adversarial Review: OpenAlex Enrichment Plan**

### [HIGH] JSON Injection via Title/Author Values
The `format_block` stage injects OpenAlex `title` and `author` strings directly into the graph entity description without sanitization. A malicious or malformed OpenAlex response containing `-->` would prematurely close the HTML comment, allowing arbitrary text/graph poisoning. The PubChem sibling avoids this mostly because formulas/SMILES are structured, but free-text titles are a prime injection vector.
*Fix:* Sanitize all OpenAlex strings by stripping/replacing `<!--`, `-->`, and newlines before injecting them into the `format_block` template.

### [HIGH] Extraction Stage Lacks Persisted Cache
Step 2 (Extract stage) performs LLM calls via glm-5.2 but the plan does not mention saving these results to disk (unlike the judge cache and `openalex_cache.json`). If the script crashes, fails, or is restarted during extraction (which will take significant time for 494 nodes), it must re-run all extraction LLM calls, wasting time and API quota.
*Fix:* Add an `extract_cache.json` to disk exactly like the PubChem `judge.json` and check it before making LLM calls in Step 2.

### [MED] Judge Cache Poisoning via Race Condition
If the script crashes during the judge/extraction phase after a node resolves but before the cache file is written, or if multiple instances are run accidentally, overlapping concurrent writes to `judge.json`/`extract_cache.json` will corrupt the JSON file, losing all cached progress. 
*Fix:* Write cache files atomically (write to `<file>.tmp`, then `os.replace()` to the final path).

### [MED] Missing `publication_year` Array Edge Case
The OpenAlex filter `publication_year:Y-1|Y|Y+1` fails if `Y` is missing or unparseable from the extraction stage. The plan says nodes lacking a year are skipped, but doesn't enforce that the `Y` passed to the search URL is a valid 4-digit integer. If the LLM hallucinates `Y="twenty-twenty"`, the URL will be malformed.
*Fix:* Validate that `Y` is a 4-digit integer before constructing the OpenAlex filter; skip the node if invalid.

### [MED] No DOI Sanity Check
OpenAlex DOIs are injected as `https://doi.org/...`. If the API returns a malformed or missing DOI (e.g., `null` or just `10.xxxx/yyy` without the prefix), the formatted block will contain broken links.
*Fix:* Ensure the DOI string starts with `https://doi.org/` or `http://doi.org/` before injecting; prepend the prefix if missing, or write `none` if invalid.

### [LOW] Match Rate Validation Gap
The plan estimates a 20-40% unresolved fraction but provides no early-exit validation. If the extraction/judge logic is fundamentally flawed (e.g., 0% match rate), the script will happily spin through all 494 nodes doing nothing useful.
*Fix:* Add a `--limit` check during early testing phases to abort if the match rate is exactly 0% after the first 20 nodes.

### [LOW] Hardcoded Snapshot Date
The `format_block` hardcodes "as of 2026-07" for `cited_by_count`. If this script is run in August 2026, the date will be wrong and misleading.
*Fix:* Dynamically generate the date string in `format_block` using `datetime.now().strftime("%Y-%m")`.

VERDICT: REVISE

### Claude's response (Round 1)
All 7 findings accepted, none rejected:
- [HIGH] marker injection → sanitize `<!--`/`-->`/newlines from all OpenAlex strings (plan step 5).
- [HIGH] extraction cache → `extract_cache.json` persisted like the OpenAlex JSON cache (plan step 3).
- [MED] atomic cache writes → tmp + `os.replace` (plan step 3).
- [MED] year validation → 4-digit int 1900–2026 gate (plan step 2).
- [MED] DOI sanity → prefix check / prepend / `none` (plan step 5).
- [LOW] 0%-match early-abort warning after first 20 (plan step 7).
- [LOW] dynamic as-of date (plan step 5).

## Round 2 — GLM
**Adversarial Re-Review: OpenAlex Enrichment Plan (Revised)**

All prior [HIGH] and [MED] findings (JSON injection, missing extraction cache, atomic cache writes, year validation, DOI normalization) have been addressed. The revised plan is structurally sound, respects the LightRAG API limits, and maintains the safety gates required to prevent graph poisoning. 

No new [HIGH] issues found.

### Remaining [LOW] (Non-blocking follow-ups)

*   **[LOW] Check-then-act race condition on write:** In Step 6, reading the fresh description, stripping the old block, and writing via `/graph/entity/edit` is not atomic. If the LightRAG server somehow processes another concurrent edit to the same `ref_text` node in the exact millisecond between your read and write, that concurrent update could be lost. Given the script uses a sequential loop for writes and preconditions state the server is "idle", this is practically impossible, but technically exists.
    *Fix:* If LightRAG supported ETags/If-Match headers, use them. Since it likely doesn't, rely on the "server idle" precondition and document this limitation.

*   **[LOW] OA PDF URL validation:** Step 5 mentions validating the DOI prefix, but the Open-access PDF URL (`<url|none>`) is not explicitly mentioned in the sanitization/validation step. A malformed `oa_url` could still slip through. 
    *Fix:* Ensure the OA PDF URL starts with `http(s)://` before injection, otherwise default to `none`.

VERDICT: APPROVED

### Non-blocking follow-ups
- [LOW] check-then-act race on /graph/entity/edit: accepted as documented limitation — mitigated by server-idle precondition + sequential writes; LightRAG has no ETag/If-Match support.
- [LOW] OA PDF URL validation: incorporated into PLAN.md step 5 (inject only if starts with http(s)://, else `none`).

### Resolution
APPROVED in 2 rounds. Plan locked pending user sign-off; no code written during review.
