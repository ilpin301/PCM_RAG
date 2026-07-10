# PCM_RAG — User Guide

GraphRAG knowledge base: documents go in, LightRAG builds a knowledge graph (entities + relationships) plus vector index, you ask questions in natural language and get answers with citations.

## Your two instances

| | PCM_RAG (this one) | Old RAG |
|---|---|---|
| Web UI / API | http://localhost:9622 | http://localhost:9621 |
| API key (`X-API-Key`) | `see lightrag/.env` | `see lightrag/.env` |
| Folder | `F:\____IL_AI\PCM_RAG\lightrag` | `F:\____IL_AI\RAG\lightrag` |
| Container | `pcm_rag-lightrag-1` | `lightrag-lightrag-1` |

Shared by both: Ollama embeddings (bge-m3), Z.ai LLMs (glm-5.2 text, glm-4.5v vision), Python venv at `F:\____IL_AI\RAG\lightrag\.venv-rag`, MinerU model cache, GPU.

## The easy way: talk to Claude Code

Project skills live in `F:\____IL_AI\PCM_RAG\.claude\skills\`. Open Claude Code in `F:\____IL_AI\PCM_RAG` and just say:

- **"ask the rag: what does document X say about Y?"** → lightrag-query skill
- **"upload C:\...\paper.pdf to the rag"** → lightrag-upload skill (text docs)
- **"ingest this scanned PDF into the rag"** → raganything-ingest skill (scans, images, chart-heavy docs)
- **"what's in the rag? did ingestion finish?"** → lightrag-status skill

## The visual way: Web UI

Open **http://localhost:9622** in a browser (login with the API key). You can:
- upload documents (drag & drop), watch processing status
- run queries with mode selection
- **explore the knowledge graph visually** — entities, relationships, clusters
- inspect/delete individual documents

Interactive API reference (all endpoints, try-it-out): **http://localhost:9622/docs**

## The direct way: API commands (PowerShell)

```powershell
$key = (Get-Content F:\____IL_AI\PCM_RAG\lightrag\.env | Select-String '^LIGHTRAG_API_KEY=').Line.Split('=',2)[1].Trim()
$h = @{'X-API-Key'=$key; 'Content-Type'='application/json'}

# Health check
Invoke-RestMethod http://localhost:9622/health -Headers $h

# Ask a question
$body = '{"query":"YOUR QUESTION","mode":"hybrid"}'
(Invoke-RestMethod http://localhost:9622/query -Method Post -Headers $h -Body $body).response

# Upload a file (txt, md, text-based PDF)
curl.exe -s -X POST http://localhost:9622/documents/upload -H "X-API-Key: $key" -F "file=@C:\path\to\document.pdf"

# Insert raw text
$body = '{"text":"...content...","file_source":"note.txt"}'
Invoke-RestMethod http://localhost:9622/documents/text -Method Post -Headers $h -Body $body
# → returns track_id; check progress:
Invoke-RestMethod http://localhost:9622/documents/track_status/<track_id> -Headers $h

# List all documents + statuses (PENDING / PROCESSING / PROCESSED / FAILED)
Invoke-RestMethod http://localhost:9622/documents -Headers $h

# Delete ALL documents (careful — whole graph gone)
Invoke-RestMethod http://localhost:9622/documents -Method Delete -Headers $h
```

## Query modes — which to pick

| Mode | What it does | Use when |
|---|---|---|
| `hybrid` | local + global combined | **default, best for most questions** |
| `local` | entity-focused, digs into specifics | "what is X", details about one thing |
| `global` | relationship/theme-focused | "compare X and Y", big-picture, trends |
| `naive` | plain vector search, no graph | quick lookup, quote finding |
| `mix` | graph + vector combined | broad questions on mixed content |

## Ingesting scanned / image-heavy PDFs (RAG-Anything + MinerU)

**Source folder rule: ingest ONLY from `F:\____IL_AI\PCM_RAG\IN\`** — don't ingest or touch files in other folders; copy documents into `IN\` first.

Web upload handles plain text fine; scans and chart-heavy PDFs need the MinerU pipeline (GPU-parsed, images described by glm-4.5v):

```powershell
# 1. MANDATORY pre-flight: Ollama must be up
curl.exe -s http://localhost:11434/api/version    # no answer → start Ollama first!

# 2. Stop the container (ingest writes the same storage files)
Set-Location F:\____IL_AI\PCM_RAG\lightrag
docker compose stop

# 3. Run ingest (shared venv)
$env:Path = "F:\____IL_AI\RAG\lightrag\.venv-rag\Scripts;$env:Path"
$env:NO_PROXY='*'; $env:PYTHONIOENCODING='utf-8'; $env:MINERU_DEVICE_MODE='cuda'
$env:TIKTOKEN_CACHE_DIR='C:\Users\il720506\AppData\Local\Temp\data-gym-cache'   # required: tiktoken download blocked by proxy
& F:\____IL_AI\RAG\lightrag\.venv-rag\Scripts\python.exe rag_ingest.py "C:\path\doc1.pdf" "C:\path\doc2.pdf"

# 4. Restart server
docker compose start
```

**Long ingests** (hours): edit the PDF list inside `ingest_detached.ps1`, then run it — survives closing the terminal/Claude session. Watch `ingest_run.log`; success = `EXITCODE=0` at the end.

## Operations

```powershell
Set-Location F:\____IL_AI\PCM_RAG\lightrag
docker compose up -d      # start (Docker Desktop must be running — check: docker info)
docker compose stop       # stop (keeps container)
docker compose down       # remove container (data stays — bind mounts)
docker logs pcm_rag-lightrag-1 --tail 50   # server logs
```

Data lives in `F:\____IL_AI\PCM_RAG\lightrag\data\rag_storage` — backup = copy this folder (container stopped).

## Cost control

- Queries: cheap (one glm-5.2 call). Ingestion: expensive part (entity extraction per chunk + vision calls).
- Bulk ingestion: switch `.env` → `LLM_MODEL=glm-5-turbo`, restart container, ingest, switch back to `glm-5.2` for query quality.
- Re-ingesting the same content is cheap — LLM cache replays free. Wiping storage also wipes that cache.

## Rules that keep it alive (violate = broken storage)

1. **Ollama up before ANY ingest** — down = silent embedding failures, dirty storage.
2. **Container STOPPED during `rag_ingest.py`** — both write the same JSON files.
3. **Never change embedding model/dim** after first ingest — old vectors incompatible, full re-ingest required.
4. Prefer clearing via `DELETE /documents` API — direct file deletion in `rag_storage` may be policy-blocked anyway.
5. Failed/killed runs leave `FAILED` doc entries — harmless, visible in status list, delete via UI if annoying.

## More docs

- `F:\____IL_AI\RAG\INSTALL.md` — full as-built install reference
- `F:\____IL_AI\RAG\REPLICATE.md` — how to build another instance (port, COMPOSE_PROJECT_NAME, venv sharing)
- http://localhost:9622/docs — live API reference

## Monitoring live ingest

```powershell
Get-Content F:\____IL_AI\PCM_RAG\lightrag\ingest_run.log -Wait -Tail 20
```

Ctrl+C to stop. Success = `EXITCODE=0` at the end of the log.
