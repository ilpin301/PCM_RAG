---
name: il-rag-ingest
description: Run the full PCM_RAG PDF ingest loop end to end - diff IN/ against the graph, probe each PDF for images AND vector figures, slice oversized PDFs, launch detached via ingest_resume.ps1, wait silently, verify, clean up. Use when the user says "ingest new PDFs from IN", "run the ingest", "/il-rag-ingest", or a close variant.
---

# il-rag-ingest

Orchestrator for the whole ingest procedure. Reads/uses the existing skills rather than
duplicating them: `lightrag-status` (server + doc list), `lightrag-upload` (text-only path),
`raganything-ingest` (MinerU/VLM path details, env vars, failure recovery),
`lightrag-query` (final sanity query).

Hard rules also live in `F:\____IL_AI\PCM_RAG\CLAUDE.md` (`## RAG Ingest Rules`) and the global
`## Background Monitoring`. Do not violate them; this skill is their executable form.

Paths:
- source folder: `F:\____IL_AI\PCM_RAG\IN\` — **ingest ONLY from here**
- project: `F:\____IL_AI\PCM_RAG\lightrag`
- wrapper: `lightrag\ingest_resume.ps1`
- log: `lightrag\LOG\ingest_run.log`
- storage: `lightrag\data\rag_storage`
- server: http://localhost:9622, key from `lightrag\.env` (`LIGHTRAG_API_KEY`) — never hardcode

## Step 0 — preflight

```powershell
$key = (Get-Content F:\____IL_AI\PCM_RAG\lightrag\.env | Select-String '^LIGHTRAG_API_KEY=').Line.Split('=',2)[1].Trim()
curl.exe -s http://localhost:9622/health -H "X-API-Key: $key"
curl.exe -s http://localhost:11434/api/version    # Ollama MUST be up before any ingest
Get-ChildItem F:\____IL_AI\PCM_RAG\lightrag\LOG\ingest_run.log -ErrorAction SilentlyContinue
Get-Content F:\____IL_AI\PCM_RAG\lightrag\LOG\LAST_FAILURE.txt -ErrorAction SilentlyContinue
```

- `ingest_run.log` already present + a live python process => a run is IN FLIGHT. Do not start another;
  attach to it at Step 4 instead.
- `LAST_FAILURE.txt` present => previous run failed. Read it (it already contains `ingest_triage.py`
  output with a verdict + hint) and report before doing anything new.
- **Never wipe `ingest_run.log` before a run.** The wrapper deletes it itself on `EXITCODE=0`.

`GET /documents` **hides `handling` rows**, so a half-ingested doc is invisible there. Cross-check the
store's own count before trusting a clean bill:

```powershell
$fileCount = ((Get-Content F:\____IL_AI\PCM_RAG\lightrag\data
ag_storage\kv_store_doc_status.json -Raw | ConvertFrom-Json).PSObject.Properties | Measure-Object).Count
$apiCount  = (($docs.statuses.PSObject.Properties.Value) | Measure-Object).Count
"file=$fileCount api=$apiCount"   # a positive difference = a hidden 'handling' doc
```

That file is only authoritative with the container STOPPED (LightRAG flushes doc_status on shutdown);
while the server runs it can be stale in the other direction. When the two disagree, stop the
container and re-read before deciding anything.

## Step 1 — diff IN/ against the graph

Two filters, both required. A filename check alone is NOT enough: slices were often ingested under
RENAMED short names (`Electromechanical_Hysteresis_Sb2S3-01-10.pdf` for a source called
`Electromechanical_Hysteresis_in_Phase_Change_Material_Sb2S3.pdf`), so the un-sliced source still
sitting in `IN\` looks new and gets ingested a second time. Content hashing does not help — a slice
is not byte-identical to its source.

```powershell
$key = (Get-Content F:\____IL_AI\PCM_RAG\lightrag\.env | Select-String '^LIGHTRAG_API_KEY=').Line.Split('=',2)[1].Trim()
$docs = (curl.exe -s http://localhost:9622/documents -H "X-API-Key: $key" | ConvertFrom-Json)
$known = $docs.statuses.PSObject.Properties.Value | ForEach-Object { $_.file_path } | Sort-Object -Unique
# ledger of sources already ingested (possibly under renamed slice names)
$ledger = Get-Content F:\____IL_AI\PCM_RAG\lightrag\INGESTED_SOURCES.txt |
          ForEach-Object { ($_ -replace '#.*$','').Trim() } | Where-Object { $_ }
Get-ChildItem F:\____IL_AI\PCM_RAG\IN\*.pdf |
  Where-Object { $known -notcontains $_.Name -and $ledger -notcontains $_.Name }
```

`lightrag\INGESTED_SOURCES.txt` is the ledger: one original source filename per line, `#` comments
ignored. Its comment block also records PARTIAL documents (slice families with a failed or missing
range) — those are deliberately NOT listed as done, and its notes say which page ranges are missing.

Report the genuinely new list. Before ingesting anything from it, sanity-check each candidate against
the ledger comments and against `/documents` for a *renamed* slice family covering the same paper —
if you find one, it is not new; add it to the ledger instead of ingesting it.

A file already PROCESSED is not new. A file in `FAILED` or stuck `handling` is a *repair* case, not a
new ingest — say so and stop for the user's call.

## Step 2 — probe each new PDF (routing)

Full image detection: `get_images()` alone MIS-ROUTES vector-figure PDFs. Always check
`get_drawings()` too.

```powershell
$py = "F:\____IL_AI\RAG\lightrag\.venv-rag\Scripts\python.exe"
& $py -c @'
import sys, fitz
for p in sys.argv[1:]:
    d = fitz.open(p)
    imgs = sum(len(pg.get_images()) for pg in d)
    maxdraw = max((len(pg.get_drawings()) for pg in d), default=0)
    chars = sum(len(pg.get_text()) for pg in d)
    route = "MINERU" if (imgs or maxdraw > 50 or chars/max(d.page_count,1) < 100) else "TEXT"
    print(f"{route} pages={d.page_count} images={imgs} maxdraw={maxdraw} chars/pg={chars//max(d.page_count,1)} {p}")
'@ <pdf paths...>
```

- `MINERU` => this skill's detached path (below).
- `TEXT` => `lightrag-upload` skill instead; far cheaper. Do not push text-only PDFs through MinerU.

## Step 3 — slice oversized PDFs

MinerU on this box fails above roughly 20 pages (5GB VRAM / 32GB RAM). Slice anything over
**10 pages** into `<=10`-page parts, named `<stem>-01-07.pdf` style, written into `IN\`.

```powershell
& $py -c @'
import sys, fitz
src = sys.argv[1]; step = 10
d = fitz.open(src)
for a in range(0, d.page_count, step):
    b = min(a+step, d.page_count) - 1
    out = fitz.open(); out.insert_pdf(d, from_page=a, to_page=b)
    name = src[:-4] + "-%02d-%02d.pdf" % (a+1, b+1)
    out.save(name); print(name)
'@ "F:\____IL_AI\PCM_RAG\IN\big.pdf"
```

Keep the source PDF. Slices are what gets ingested.

## Step 4 — launch detached, then wait silently

Rewrite the `$pdfs = @( ... )` block in `ingest_resume.ps1` with this run's file list — it always holds
the PREVIOUS run's paths, which are usually deleted slices by now, so never launch without rewriting it
and confirming every listed path exists. (The wrapper
carries the required env vars, the `EXITCODE=` marker, the failure triage and `docker compose start`
— do not reimplement it, and do not run `rag_ingest.py` inline.)

```powershell
Set-Location F:\____IL_AI\PCM_RAG\lightrag
docker compose stop     # REQUIRED - script writes the same storage files as the container
Start-Process pwsh -ArgumentList "-NoProfile","-File","F:\____IL_AI\PCM_RAG\lightrag\ingest_resume.ps1" -WindowStyle Hidden
```

Wait with ONE silent one-shot waiter that terminates by itself. Never `tail -f | grep`, never a
poller that emits progress notifications:

```bash
cd /f/____IL_AI/PCM_RAG/lightrag
until [ -f LOG/ingest_run.log ]; do sleep 2; done
while [ -f LOG/ingest_run.log ] && ! grep -q EXITCODE LOG/ingest_run.log; do sleep 20; done
if [ -f LOG/LAST_FAILURE.txt ]; then cat LOG/LAST_FAILURE.txt; else echo "EXITCODE=0"; fi
```

Log deleted + no `LAST_FAILURE.txt` = success (the wrapper deletes the log on `EXITCODE=0`).

**Checkpointing is mandatory for any long run.** LightRAG writes
`kv_store_llm_response_cache.json` only at the end of the pipeline, so without a periodic flush a
crash loses every extraction since launch — verified 2026-08-20: 61 cache saves logged, on-disk
mtime unmoved after 54 minutes. `rag_ingest.py` now runs `periodic_cache_flush(rag, every=300)`
as a background task (cancelled in a `finally`), wired into both `rag_ingest.main()` and
`ingest_merged.insert_merged()`. Before launching any ingest, confirm it is still wired:

```sh
grep -n 'periodic_cache_flush\|flusher' rag_ingest.py ingest_merged.py
```

Expect 5 hits: the definition, plus a create_task/cancel pair in each of the two entry points.
Verify it is actually firing once the run is live — the log prints `--- llm cache flushed to disk`
every 5 minutes, and the cache file's mtime should advance.

## Step 5 — on failure: triage once, then escalate

`LAST_FAILURE.txt` already holds the verdict from `ingest_triage.py`. Known verdicts and the single
fix to attempt before escalating to the user:

| verdict | fix to try once |
|---|---|
| `MINERU_PARSE_FAILED` / `CUDA_OOM` / `HOST_OOM` | slice smaller (5-7 pages) and re-run |
| `LLM_RATE_LIMIT` | wait, re-run as-is (resumable, caches replay); do NOT raise the VLM semaphore above 2 |
| `ENDPOINT_UNREACHABLE` | start Ollama / z.ai reachable, re-run |
| `MULTIMODAL_SERIAL_FALLBACK` | net dropped mid-run — kill and relaunch, do NOT let the serial path grind (see below) |
| `INTERRUPTED` | re-run as-is |
| `UNKNOWN` | do NOT guess a fix — report the log tail and stop |

### Transient network drop: the serial-fallback trap

A brief internet outage during the multimodal phase does not just retry — it destroys the async batch
pass and silently downgrades the whole run to serial. Signature in the log:

```
ERROR: extract LLM func: ... RetryError[<Future ... raised APITimeoutError>]
ERROR: Error in multimodal processing: RetryError[C[111/282]: chunk-...: APITimeoutError]
WARNING: Falling back to individual multimodal processing
INFO: Processing item 1/282: page_footnote content
```

One `APITimeoutError` on one chunk aborts the batched multimodal pass. RAG-Anything catches it and
restarts the multimodal phase from **item 1**, one item at a time, without the async-8 concurrency.

**Nothing is lost, but the run is now uneconomic.** The text phase is already committed (Phase 3 wrote
its entities and relations before multimodal starts), and extraction results live in
`kv_store_llm_response_cache.json`. What is lost is throughput: measured **2.7 min/item** on the serial
path (items 1 to 4 in 8 minutes on 2026-08-20), i.e. roughly **12 hours** for 282 items.

Do NOT let it grind. Once the connection is back:

1. Confirm the endpoint is reachable (HTTP 401 without a key means reachable):

```sh
curl -s --noproxy '*' -o /dev/null -w '%{http_code}\n' --max-time 15 https://api.z.ai/api/paas/v4/
```

2. Kill the run.
3. If the doc registered as `handling`, delete it first — see the `EXITCODE=0` case below.
4. Relaunch unchanged. The parse cache skips MinerU entirely (log shows `Parsing (native):` instead of
   a MinerU invocation), and the LLM response cache is reused for chunks already extracted.

Caveat: LightRAG logs `== LLM cache == saving:` on writes but logs nothing on a hit, so cache-hit rate
on relaunch cannot be read from the log — judge it by how fast the chunk counter climbs.

**Watch for it.** A waiter armed only on `EXITCODE=` will sit through the entire 12-hour serial crawl
without reporting. Arm long-run waiters on the fallback line too:

```sh
until grep -qE 'Falling back to individual multimodal processing|EXITCODE=' LOG/<run>.log; do sleep 60; done
```

Hardening note: `rag_ingest.py` passes no `timeout=` or `max_retries=` to `openai_complete_if_cache`,
so the openai client defaults apply. Raising them would widen the outage a run can absorb; untested.

### The dangerous case: `EXITCODE=0` with no work done

If the doc is already registered (typically stuck `handling` from an earlier killed run),
`rag_ingest.py` writes a fresh `dup-*` FAILED stub and exits **0** in under a minute. The wrapper
deletes the log, the waiter reports success, and nothing was ingested. Signature: finished far too
fast, graph node/edge counts unchanged, `vdb_*.json` byte-identical.

Deleting the `dup-*` stub does NOT fix this — the stub is a shadow of the real doc and comes back.
Repair the underlying doc:

```powershell
# the stuck doc will NOT appear in GET /documents - get its id from the store file
$full = (Get-Content F:\____IL_AI\PCM_RAG\lightrag\data
ag_storage\kv_store_doc_status.json -Raw | ConvertFrom-Json).PSObject.Properties |
        Where-Object { $_.Value.file_path -eq '<slice>.pdf' } | ForEach-Object { $_.Name }
$body = @{ doc_ids = @($full) } | ConvertTo-Json -Compress
Invoke-RestMethod http://localhost:9622/documents/delete_document -Method Delete -Headers $h -Body $body
```

`delete_document` accepts an id that `/documents` does not list. It is async and takes ~6 minutes
(it rewrites the graph and the ~460MB relationship vdb) — wait for `/health` -> `pipeline_busy=False`
with a silent until-loop, verify the doc's chunks are gone from `kv_store_text_chunks.json` and that
the graph counts DROPPED, then re-ingest. Re-ingesting reuses the same doc id (hashed from file path),
which is expected. See [[project_lightrag_delete_endpoint]].

Also check for the rest of the wreckage a killed run leaves: other docs stuck in `handling`, and
missing `vdb_*.json`. Recovery steps are in the `raganything-ingest` skill — reuse them, don't
invent new ones.

## Step 6 — verify (non-optional, all four)

**`EXITCODE=0` is not evidence that anything was ingested** — see the no-op case in Step 5. Only the
deltas below prove work happened. Record the baseline BEFORE launching (`grep -c '<node '` /
`grep -c '<edge '` on the graphml, plus the three `vdb_*.json` sizes and mtimes).

1. **Doc count delta** — `/documents` count before vs after; every new file PROCESSED, none FAILED/handling.
2. **Graph node delta** — `graph_chunk_entity_relation.graphml` node count grew:
   `grep -c '<node ' lightrag/data/rag_storage/graph_chunk_entity_relation.graphml`
3. **Vector sanity** — all three `vdb_chunks.json`, `vdb_entities.json`, `vdb_relationships.json`
   exist, have mtimes AFTER the run start, and GREW. Byte-identical sizes = the run did nothing. Missing/stale vdb => queries
   return `[no-context]`; the run did not finish cleanly.
   Then run `check_vectors.py` — mtime+size say nothing about POISONED vectors:

   ```powershell
   $env:NO_PROXY='*'; & F:\____IL_AI\RAG\lightrag\.venv-rag\Scripts\python.exe F:\____IL_AI\PCM_RAG\lightrag\check_vectors.py
   ```

   Exit `0` = healthy, `3` = problems. One line per store: row count, matrix row count, nonfinite
   count, zero count. A corrupt embedding model returns all-zero vectors; normalizing those yields
   NaN, and NaN poisons the WHOLE nano-vectordb matrix at load time — retrieval then silently returns
   nothing while the ingest still exits 0. It also catches data/matrix row misalignment.
   `ingest_resume.ps1` now runs this itself on the success path and folds a non-zero result into
   `EXITCODE`, so a poisoned store KEEPS its log instead of having it deleted. The manual run above is
   for ad-hoc checks and for verifying a repair.
4. **One targeted query** per ingested doc via `lightrag-query`, asking something only that document
   answers. Answer must cite it.

Report the four numbers. Do not claim success without them.

**Never verify a deletion from `docker logs`.** A waiter polling
`docker logs --tail 200 ... | grep 'Deletion completed'` will hang forever if the container restarts,
because the line scrolls out of the tail window — burned a whole session's waiter on 2026-08-20.
Verify from the store files, which are the actual truth:

```sh
python -c "import json;from collections import Counter;d=json.load(open('data/rag_storage/kv_store_doc_status.json',encoding='utf-8'));print(Counter(v.get('status') for v in d.values()),len(d))"
grep -c '<node ' data/rag_storage/graph_chunk_entity_relation.graphml
```

Expect the deleted doc absent, zero rows in `handling`, and the node count DROPPED.

**Benign warning, do not chase it.** `LLM output format error; found 3/4 fields on ENTITY ...` means
the model emitted a near-miss tuple delimiter, so the record split short and
`_handle_single_entity_extraction` dropped it whole — nothing partial is written. Measured 0.12%
(5 of 4043 entities). Only investigate above a few percent.

## Step 7 — cleanup and bookkeeping

Only after `EXITCODE=0` **and** Step 6 passing:

- delete the slice PDFs (`<stem>-NN-MM.pdf`); keep the source PDF
- append the SOURCE filename (not the slices) to `lightrag\INGESTED_SOURCES.txt`; if any slice of
  it failed, add it as a commented PARTIAL entry naming the missing page range instead
- update `memory\project_ingest_state.md` with the new doc count/state — do this without asking
- `docker ps` to confirm the container came back up (wrapper runs `docker compose start`, which
  fails silently if Docker Desktop is down)

Emit ONE end-of-run summary: files ingested, the four verification numbers, anything skipped and why.

**Always sweep orphaned vectors after a delete.** `DELETE /documents/delete_document` strands
entity vectors that the graph no longer has — observed twice on 2026-08-20 (278 and 275 orphans,
each exactly the `vdb_entities` minus graph-node gap). This is not crash damage; it happens on
clean deletes. After any document deletion:

```sh
python repairs/repair_vdb.py            # dry run: expect TO ADD 0/0/0
python repairs/repair_vdb.py --apply    # writes .bak for all three stores first
python check_vectors.py                 # rows must equal graph nodes / edges
```

## Windows gotchas that cost time

- Any python that prints extracted PDF text needs `PYTHONIOENCODING=utf-8`; the default cp1251 console
  codec raises `UnicodeEncodeError` on the first umlaut and kills the script mid-report.
- `import fitz` warns it is deprecated — use `import pymupdf` in new snippets; both ship in the venv.
- Deleted source PDFs are usually still in git: `git show HEAD:FOUND/<name>.pdf > <scratchpad>/<name>.pdf`
  recovers one for page-count or gap classification without touching the worktree.
- **Upload from PowerShell, never from bash.** `curl.exe -s -X POST .../documents/upload -F "file=@F:\...\x.pdf"`
  run through the Bash tool returns an EMPTY response and uploads nothing — bash mangles the Windows
  path in the `-F` argument, and the server never sees a file. The same command from PowerShell returns
  `{"status":"success",...,"track_id":"upload_..."}`. An empty response body is the tell; always confirm
  the doc count actually rose before waiting on a pipeline that was never given any work.
- Foreground `sleep` is blocked by the harness. Wait with an `until`-loop in a `run_in_background`
  shell, which also satisfies the silent-monitoring rule.

## Keep the machine awake (mandatory)

Any long-running RAG shell process — ingest, parse, insert, delete, enrich, audit — must run with sleep blocked, or the box suspends mid-run and the job dies.

Start this BEFORE launching the process:

```powershell
$ka = Start-Process pwsh -ArgumentList '-NoProfile','-File','F:\____IL_AI\PCM_RAG\lightrag\keepawake.ps1' -PassThru -WindowStyle Hidden
```

Verify it registered (needs an elevated shell to read):

```powershell
powercfg /requests | Select-String -Pattern 'SYSTEM:' -Context 0,2
```

Expect `SYSTEM: [PROCESS] ...pwsh.exe`. If it says `None.`, the block is NOT active — do not start the run.

`keepawake.ps1` holds `SetThreadExecutionState(ES_CONTINUOUS|ES_SYSTEM_REQUIRED|ES_AWAYMODE_REQUIRED)` for as long as it lives, so killing the process releases the block automatically — there is no persistent power setting to restore. Display sleep is deliberately still allowed; only system sleep is blocked.

Stop it as part of the cleanup below, once no RAG process is still running:

```powershell
Stop-Process -Id $ka.Id -Force
```

Gotcha: PowerShell parses `0x80000000` as a signed Int32, so building the flags inline throws on the P/Invoke and the keepawake silently does nothing while still looking alive. Use the script, which casts to `[uint32]`.

## Cleanup after success (mandatory)

When the run finishes SUCCESSFULLY — `EXITCODE=0` and the verification steps passed — do both of these before reporting done:

1. **Kill every shell process started for this run.** Background waiters, `tail -f` tails, monitors, poll loops, and the `keepawake.ps1` process — the user's and yours. Use `TaskStop` on each background task id. Leave nothing running.
2. **Delete the logs the run produced.** `ingest_run.log`, `LOG/*.log` for this run, and any scratchpad task-output files.

Order matters: kill the tails BEFORE deleting the logs, or a live `tail -f` holds the handle.

NEVER do either of these before success. While a run is in flight the log is the only evidence of progress, and on a FAILED or killed run both the logs and the shells must be KEPT for diagnosis.

**Delete the LLM response cache.** Only after `EXITCODE=0` AND every verification step has passed:

```sh
docker stop pcm_rag-lightrag-1     # never delete while the server holds its own in-memory copy
rm data/rag_storage/kv_store_llm_response_cache.json
```

LightRAG recreates the file empty on the next run. This is deliberate, not housekeeping: the cache
exists so a crashed or interrupted run can be replayed without paying for extraction twice, and once
a run has succeeded and verified there is nothing left to replay. It reached ~69 MB / 35k extraction
entries on PCM_RAG before the first cleanup.

Accepted cost: re-ingesting that document later pays full LLM extraction again, and the first queries
after cleanup run cold while the query-mode cache refills.

**Never delete it on failure, and never before verification.** A killed run's cache is the only thing
that makes the relaunch cheap — that is the whole point of [[project_ingest_cache_flush]]. Deleting
early converts a 15-minute relaunch into a full re-extraction.
