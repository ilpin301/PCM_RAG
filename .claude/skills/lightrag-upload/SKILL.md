---
name: lightrag-upload
description: Upload text documents (txt, md, normal text PDFs) into the local LightRAG knowledge graph. Use when the user says to add/upload/ingest a text document into the rag. NOT for scanned PDFs, images, or chart-heavy docs — use raganything-ingest for those.
---

# LightRAG Upload

Server: http://localhost:9622 — API key header (stored in lightrag/.env as LIGHTRAG_API_KEY — never hardcode)

```powershell
$key = (Get-Content F:\____IL_AI\PCM_RAG\lightrag\.env | Select-String '^LIGHTRAG_API_KEY=').Line.Split('=',2)[1].Trim()
curl.exe -s -X POST http://localhost:9622/documents/upload -H "X-API-Key: $key" -F "file=@C:\path\to\document.pdf"
```

For multiple files, run one curl per file. After upload, processing (chunking, entity extraction via GLM, embedding via Ollama bge-m3) runs in the background — can take minutes per document. Check progress with the lightrag-status skill. Warn the user that large documents take a while and consume Z.ai tokens.

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