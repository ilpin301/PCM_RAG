---
name: il-check-rag-base
description: Parallel read-only integrity audit of the PCM_RAG LightRAG store - orphaned vectors, stuck docs, page-coverage gaps, chunk consistency, Drive-snapshot cross-check, leftover slices. Produces one ranked report plus dry-run repair scripts, executes nothing. Use when the user says "check the rag base", "audit the rag", "/il-check-rag-base", after a crash/BSOD, or after a killed ingest.
---

# il-check-rag-base

Read-only. **This skill never repairs anything.** It fans six independent invariant checks out to
subagents, reconciles their findings into one ranked report, and writes idempotent repair scripts
with a dry-run mode for the user to approve separately.

Paths:
- storage: `F:\____IL_AI\PCM_RAG\lightrag\data\rag_storage`
- Drive snapshot: `J:\My Drive\RAG\PCM_RAG\rag_storage.tgz` (J: is the streaming mount, not G:/H:)
- source folder: `F:\____IL_AI\PCM_RAG\IN\`
- logs: `F:\____IL_AI\PCM_RAG\lightrag\LOG`
- python: `F:\____IL_AI\RAG\lightrag\.venv-rag\Scripts\python.exe`

## Step 0 — preflight (READ THIS, two views of the truth disagree)

Confirm no ingest is in flight: no `LOG\ingest_run.log`, no `rag_ingest.py` python process. If one is
running, STOP and tell the user — the JSON stores are mid-write and every finding would be noise.

**Neither the API nor the JSON files alone tell the truth. Both were wrong here on 2026-08-18:**

| view | blind spot |
|---|---|
| `GET /documents` | **omits `handling` rows entirely.** It showed 66 clean docs while one was stuck half-ingested. A doc can be broken and simply not appear. |
| `kv_store_*.json` read while the container is UP | **stale.** LightRAG holds doc_status in memory and flushes on shutdown, so the file shows the pre-flush state. |

So, before auditing:

```powershell
Set-Location F:\____IL_AI\PCM_RAG\lightrag
docker compose stop          # forces the flush; the JSON files are only authoritative once stopped
```

Audit the stopped store, and treat any doc count that differs from `/documents` as a finding, not noise
(the difference IS the hidden `handling` row). Restart with `docker compose start` when done. If the
user will not allow stopping the container, say so in the report and mark invariants B, D and E
`severity:info — unverified (stale store)`; do not present their numbers as fact.

## Step 1 — dispatch the auditors in parallel

Spawn six subagents in ONE message (see `superpowers:dispatching-parallel-agents`). Each owns exactly
one invariant, is told **read-only, propose nothing, fix nothing**, and returns structured JSON:

```json
{"invariant":"A","severity":"critical|warning|info","findings":[{"what":"...","evidence":"...","count":N}]}
```

- **A — orphaned vectors.** Every id in `vdb_chunks.json` / `vdb_entities.json` /
  `vdb_relationships.json` must trace to a live parent in `kv_store_text_chunks.json` /
  `kv_store_full_entities.json` / `kv_store_full_relations.json`. Report ids with no parent, and the
  reverse (parents with no vector).
  Complementary second probe, also required:

  ```powershell
  $env:NO_PROXY='*'; & F:\____IL_AI\RAG\lightrag\.venv-rag\Scripts\python.exe F:\____IL_AI\PCM_RAG\lightrag\check_vectors.py
  ```

  Exit `0` = healthy, `3` = problems; one line per store with row count, matrix row count, nonfinite
  count and zero count. The two probes see different damage and neither replaces the other: the
  set-difference above finds records **missing** a vector or **stale** vectors whose parent is gone;
  `check_vectors.py` finds vectors that **exist but are poisoned** (NaN / all-zero) or a matrix
  **misaligned** with the record list. A corrupt embedding model returns all-zero vectors,
  normalizing yields NaN, and one NaN poisons the whole nano-vectordb matrix at load time — retrieval
  then silently returns nothing while every id still traces to a live parent. Run both.
- **B — stuck / broken doc status.** In `kv_store_doc_status.json` (container STOPPED — see Step 0):
  anything in `handling`, `pending`, `processing`, or `failed`; every `dup-*` stub; docs present in
  `doc_status` but absent from `kv_store_full_docs.json` (and vice versa). Also diff the file's doc
  count against `GET /documents` — a positive difference is a hidden `handling` doc.
  **A `dup-*` stub is never harmless.** It is the shadow of a real doc stuck `handling`: deleting the
  stub alone regenerates it on the next run. Report the underlying doc id, not the stub.
- **C — page-coverage gaps.** For each PDF-derived doc, compare pages actually represented against
  the source PDF page count in `IN\`. Distinguish **benign** blanks (front matter, cover, blank
  verso, pure-image plate with no text) from a **genuine** un-ingested tail (e.g. a slice that never
  finished). Only genuine gaps are `critical`; say explicitly which category each gap is.
- **D — chunk-count consistency.** Chunks per doc vs its page count; flag docs whose ratio is a
  strong outlier versus the corpus median (truncated ingest), and docs with zero chunks.
- **E — Drive snapshot cross-check.** Compare the live store against
  `J:\My Drive\RAG\PCM_RAG\rag_storage.tgz` — doc list and per-doc chunk counts. Report docs present
  in the backup but missing live (possible data loss) and live-only docs (expected: ingested since the
  snapshot). Extract the tgz to the scratchpad, never over the live store. If J: is not mounted,
  return `severity:info` saying the check was skipped — do not guess.
- **F — filesystem leftovers.** Leftover slice PDFs (`*-NN-MM.pdf`) in `IN\` whose source is already
  ingested, stale `ingest_FAILED_*.log` / `ingest_CRASHED_*.log` / `LAST_FAILURE.txt`, orphaned
  `data\mineru_output` folders with no matching doc.

**Known standing gaps — do NOT report these as crash damage.** Measured 2026-08-18 after a clean
re-ingest: ~199 graph entities and ~439 graph edges have no vector, and 9 `kv_store_text_chunks`
entries have no `vdb_chunks` vector. A clean run barely moved them (234->199, 441->439, 9->9), so
they are a standing property of this store. Report the current numbers and whether they moved
relative to this baseline; only a large jump is a finding.

Give each agent the concrete file paths and the venv python above. Big JSON stores (`vdb_*.json` is
hundreds of MB) must be streamed or read with `ijson`/targeted `python -c` — never cat into context.

## Step 2 — reconcile

As coordinator, merge the six JSON payloads into ONE markdown report ranked by severity:

- `critical` — real data loss or an unqueryable store: missing `vdb_*.json`, docs in the backup but
  not live, genuine un-ingested page ranges, zero-chunk docs.
- `warning` — self-inflicted but harmless-to-queries: stuck `handling` rows, `dup-*` stubs, orphaned
  vectors, outlier chunk ratios.
- `info` — cosmetic: leftover slices, stale logs, skipped checks.

Each row: invariant, what, evidence (file + id/count), severity. Deduplicate findings that two agents
report from different angles (a killed run shows up in B, C and D at once — say so once, note the
corroboration).

## Step 3 — write dry-run repair scripts (do NOT execute)

One idempotent script per genuine issue, in
`F:\____IL_AI\PCM_RAG\lightrag\repairs\<issue>.ps1` (or `.py`), each defaulting to `-DryRun` and
printing exactly what it would change. Reuse the recovery moves already documented in the
`raganything-ingest` skill (doc-status `handling` -> `processed`, `dup-*` deletion via
`DELETE /documents/delete_document` with a `doc_ids` body, re-ingest to regenerate `vdb_*.json`)
instead of inventing new ones. Note that direct edits to `kv_store_doc_status.json` require the
container stopped.

Deleting a doc is slow and asynchronous: `delete_document` returns `deletion_started` immediately,
then rewrites the graph and the ~460MB relationship vdb. Expect ~6 minutes. Wait on
`/health` -> `pipeline_busy=False` with a silent until-loop, never a chatty poller.

Hand the user the report + the script list and stop. Applying a repair is a separate, explicit go.
