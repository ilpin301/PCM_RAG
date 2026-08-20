---
name: raganything-ingest
description: Ingest non-text documents (scanned PDFs, images, chart/table-heavy PDFs, office docs) into the LightRAG knowledge graph via RAG-Anything + MinerU. Use when the user wants to add a scanned or image-heavy document to the rag.
---

# RAG-Anything Ingest

Pipeline: MinerU parses the document locally (GPU/CUDA when available) → text/images split → GLM-5.2 extracts entities, GLM-4.5V describes images/tables/charts/equations → bge-m3 embeds → merged into the same LightRAG storage the Docker server uses.

## Source folder rule

**Ingest files ONLY from `F:\____IL_AI\PCM_RAG\IN\`.** Never ingest from or touch files in any other folder (FOUND, etc.). If the user points at a file elsewhere, ask them to copy it into `IN\` first.

## Preferred way: detached run (survives session close)

Edit the PDF list inside `F:\____IL_AI\PCM_RAG\lightrag\ingest_resume.ps1`, then:

```powershell
Set-Location F:\____IL_AI\PCM_RAG\lightrag
docker compose stop     # REQUIRED — script writes the same storage files as the container
Start-Process pwsh -ArgumentList "-NoProfile", "-File", "F:\____IL_AI\PCM_RAG\lightrag\ingest_resume.ps1" -WindowStyle Hidden
# Monitor live:
Get-Content F:\____IL_AI\PCM_RAG\lightrag\LOG\ingest_run.log -Wait -Tail 20
```

### Self-terminating watch (for the Monitor tool — bash)

`tail -f` never exits, so the monitor idles until timeout. Use this poll loop instead — it exits on EXITCODE, or when the log is deleted (which the script does on success):

```bash
cd /f/____IL_AI/PCM_RAG/lightrag
until [ -f LOG/ingest_run.log ]; do sleep 2; done
n=0
while :; do
  if [ -f LOG/ingest_run.log ]; then
    tail -n +$((n+1)) LOG/ingest_run.log | grep -E "EXITCODE|Traceback|RetryError|FAILED|Killed|OOM|Error:"
    n=$(wc -l < LOG/ingest_run.log)
    grep -q EXITCODE LOG/ingest_run.log && break
  else
    echo "EXITCODE=0 (log deleted on success)"; break
  fi
  sleep 5
done
```

Success = `EXITCODE=0` at the end of the log. The script auto-runs `docker compose start` afterwards (fails silently if Docker Desktop is down — check `docker ps` and start manually if needed). Log file is deleted automatically on success.

## Inline run (small docs only)

```powershell
Set-Location F:\____IL_AI\PCM_RAG\lightrag
$env:NO_PROXY='*'
$env:TIKTOKEN_CACHE_DIR='C:\Users\il720506\AppData\Local\Temp\data-gym-cache'   # REQUIRED — see below
$env:Path = "F:\____IL_AI\RAG\lightrag\.venv-rag\Scripts;$env:Path"   # raganything checks `mineru --version` on PATH
$env:PYTHONIOENCODING='utf-8'
$env:MINERU_DEVICE_MODE='cuda'
docker compose stop
F:\____IL_AI\RAG\lightrag\.venv-rag\Scripts\python.exe rag_ingest.py "F:\____IL_AI\PCM_RAG\IN\document.pdf"
docker compose start
```

Multiple files: pass several paths, `rag_ingest.py file1.pdf file2.pdf`.

## Required environment variables

- `TIKTOKEN_CACHE_DIR='C:\Users\il720506\AppData\Local\Temp\data-gym-cache'` — without it, tiktoken tries to download `o200k_base.tiktoken` from Azure CDN and TIMES OUT (SOCKS proxy machine). Fatal: `LightRAG initialization failed: HTTPSConnectionPool(host='openaipublic.blob.core.windows.net'...)`.
- `NO_PROXY='*'` — bypass SOCKS system proxy for local/z.ai calls.
- `ZAI_API_KEY` — must be set in the parent process.

## rag_ingest.py contains critical patches — DO NOT regenerate the script

`rag_ingest.py` carries 3 monkey-patches + a VLM semaphore that are REQUIRED (raganything 1.3.1 + lightrag-hku 1.5.4 compatibility):
1. `asdict` → `_build_global_config` redirect in `raganything.modalprocessors`
2. `role_llm_funcs` mirrored into LightRAG instance `__dict__`
3. junk-content filter wrapping `separate_content` in BOTH `raganything.utils` and `raganything.processor` (drops page_number/header/footer — ~38% of multimodal items are junk otherwise)
4. `_VLM_SEMAPHORE = asyncio.Semaphore(2)` — z.ai coding endpoint has a CONCURRENCY limit (error 1305); do not raise above 2

Any edit to the script must preserve all four.

## z.ai 429 behavior

`ERROR: OpenAI API Rate Limit Error ... code 1305` = z.ai concurrency limit, NOT a per-minute rate. "OpenAI" = the openai python client used as transport for z.ai, not OpenAI the service. Occasional 429s are absorbed by retry backoff — normal, ignore. If items log `RetryError` (retries exhausted), those items are SKIPPED (graph gets gaps) but ingest continues; consider re-running later when z.ai load drops.

## Kill/restart is safe and cheap

- Parse cache persists after each call — a re-run skips MinerU entirely (log shows `Parsing (native):`).
- The LLM response cache only replays free **if the run was checkpointed** — LightRAG writes
  `kv_store_llm_response_cache.json` at pipeline end only, so an uncheckpointed crash loses every
  extraction since launch. See "Long runs: checkpointing" below.
- After a successful ingest the response cache is deleted by the cleanup rule, so the NEXT re-run of
  that same document pays full extraction again. Kill/restart is cheap mid-run, not after success.
- Multimodal VLM descriptions may NOT hit cache — expect those to re-run.
- **VDB files (`vdb_*.json`) only exist after a clean `EXITCODE=0` finish.** A killed run can leave them missing → queries return `[no-context]`. Fix: run ingest to clean completion.
- Killed runs leave `dup-*` FAILED stubs in doc status and can leave real docs stuck in `handling`. Cleanup (server MUST be stopped for direct file edit): fix `"handling"` → `"processed"` and delete `dup-*` entries in `data\rag_storage\kv_store_doc_status.json`, or delete stubs via API:
  `Invoke-RestMethod http://localhost:9622/documents/delete_document -Method Delete -Headers $h -Body '{"doc_ids":["dup-XXXX"]}'` (header `X-API-Key` + `Content-Type: application/json`).
  - **Prefer deleting the partial doc over flipping its status.** Flipping `handling` -> `processed`
    marks a half-ingested document as complete and its missing chunks never come back. Delete it via
    `DELETE /documents/delete_document`, sweep orphaned vectors, then re-ingest.

## Notes

- First run downloads MinerU models (~a few GB) — slow once, cached after.
- MinerU uses GPU (CUDA) automatically when available; `MINERU_DEVICE_MODE='cuda'` pins it.
- Ollama must be up before ANY ingest: `curl.exe -s http://localhost:11434/api/version`.
- Verify afterwards with lightrag-status skill (documents should appear PROCESSED), then test one query.
- If rag_ingest.py is missing, tell the user setup step 5 of F:\____IL_AI\PCM_RAG\INSTALL.md is incomplete.

## Long runs: checkpointing and the serial-fallback trap

Both failure modes below were hit on 2026-08-20 during a 282-item multimodal insert. This skill drives
the same `rag_ingest.py` path, so both apply here.

**Checkpointing is mandatory.** LightRAG persists `kv_store_llm_response_cache.json` only at the end
of the pipeline. Verified: 61 cache saves logged while the on-disk mtime sat unmoved for 54 minutes.
`rag_ingest.py` runs `periodic_cache_flush(rag, every=300)` as a background task, cancelled in a
`finally`. Confirm it is wired before launching:

```sh
grep -n 'periodic_cache_flush\|flusher' rag_ingest.py
```

Once live, the log prints `--- llm cache flushed to disk` every 5 minutes and the cache file's mtime
advances. If it does not, stop and fix that before burning hours of extraction.

**The serial-fallback trap.** A brief internet drop does not just retry — one `APITimeoutError`
aborts the async batch multimodal pass, and RAG-Anything restarts the multimodal phase from item 1,
SERIALLY, without async concurrency. Signature:

```
ERROR: Error in multimodal processing: RetryError[C[111/282]: chunk-...: APITimeoutError]
WARNING: Falling back to individual multimodal processing
INFO: Processing item 1/282: page_footnote content
```

Nothing is lost — the text phase is already committed — but the serial path measured **2.7 min/item**
(~12 h for 282 items). Do not let it grind. Confirm the endpoint is back
(`curl -s --noproxy '*' -o /dev/null -w '%{http_code}\n' --max-time 15 https://api.z.ai/api/paas/v4/`
returning 401 means reachable), kill the run, delete the partial `handling` doc, and relaunch to get
the batch path back.

**Arm waiters on the fallback line, not only on `EXITCODE=`** — otherwise a waiter sits silently
through the entire 12-hour crawl:

```sh
until grep -qE 'Falling back to individual multimodal processing|EXITCODE=' LOG/<run>.log; do sleep 60; done
```

**Sweep orphaned vectors after any delete.** `DELETE /documents/delete_document` strands entity
vectors on every delete, not just after crashes — observed 278, 275, then 272 across three deletes,
each exactly the `vdb_entities` minus graph-node gap. With the container stopped:

```sh
python repairs/repair_vdb.py            # dry run: expect TO ADD 0/0/0
python repairs/repair_vdb.py --apply    # writes .bak for all three stores first
python check_vectors.py                 # entity rows must equal graph nodes
```

**Benign warning, do not chase it.** `LLM output format error; found 3/4 fields on ENTITY ...` means
the model emitted a near-miss tuple delimiter (e.g. `<|# |>` instead of `<|#|>`), so the record split
short. `_handle_single_entity_extraction` returns `None` — the record is dropped whole, nothing
partial or corrupt is written. Measured rate 0.12% (5 of 4043 entities, 6 of ~5000 relations). Only
investigate if it climbs past a few percent.

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
