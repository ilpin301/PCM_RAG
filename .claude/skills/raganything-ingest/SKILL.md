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

- Parse cache + text-phase LLM cache persist after each call — re-runs replay them free.
- Multimodal VLM descriptions may NOT hit cache — expect those to re-run.
- **VDB files (`vdb_*.json`) only exist after a clean `EXITCODE=0` finish.** A killed run can leave them missing → queries return `[no-context]`. Fix: run ingest to clean completion.
- Killed runs leave `dup-*` FAILED stubs in doc status and can leave real docs stuck in `handling`. Cleanup (server MUST be stopped for direct file edit): fix `"handling"` → `"processed"` and delete `dup-*` entries in `data\rag_storage\kv_store_doc_status.json`, or delete stubs via API:
  `Invoke-RestMethod http://localhost:9622/documents/delete_document -Method Delete -Headers $h -Body '{"doc_ids":["dup-XXXX"]}'` (header `X-API-Key` + `Content-Type: application/json`).

## Notes

- First run downloads MinerU models (~a few GB) — slow once, cached after.
- MinerU uses GPU (CUDA) automatically when available; `MINERU_DEVICE_MODE='cuda'` pins it.
- Ollama must be up before ANY ingest: `curl.exe -s http://localhost:11434/api/version`.
- Verify afterwards with lightrag-status skill (documents should appear PROCESSED), then test one query.
- If rag_ingest.py is missing, tell the user setup step 5 of F:\____IL_AI\PCM_RAG\INSTALL.md is incomplete.
