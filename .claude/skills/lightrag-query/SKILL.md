---
name: lightrag-query
description: Query the local LightRAG knowledge graph (GraphRAG over ingested documents). Use when the user asks a question about their RAG documents, knowledge base, or says "ask the rag", "query lightrag".
---

# LightRAG Query

Server: http://localhost:9622 — API key header required (stored in lightrag/.env as LIGHTRAG_API_KEY — never hardcode)

Query with PowerShell (write JSON body to a temp file first to avoid quoting issues):

```powershell
$key = (Get-Content F:\____IL_AI\PCM_RAG\lightrag\.env | Select-String '^LIGHTRAG_API_KEY=').Line.Split('=',2)[1].Trim()
$body = '{"query":"USER QUESTION HERE","mode":"hybrid"}'
$tmp = New-TemporaryFile; Set-Content $tmp $body -NoNewline
curl.exe -s http://localhost:9622/query -H "Content-Type: application/json" -H "X-API-Key: $key" -d "@$tmp"
```

Modes: `hybrid` (default, best), `local` (entity-focused), `global` (relationship/theme-focused), `naive` (plain vector search), `mix`.

Response JSON has `response` field with the answer including reference markers. Summarize the answer for the user and list the cited sources. If the user asks for raw output, show `response` verbatim.

If connection refused: check `docker ps` — container `lightrag` must be Up; if not, `docker compose up -d` in F:\____IL_AI\PCM_RAG\lightrag.

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