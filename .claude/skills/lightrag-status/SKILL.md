---
name: lightrag-status
description: Check LightRAG server health and list ingested documents with processing status. Use when the user asks what's in the rag, whether ingestion finished, or whether the rag server is running.
---

# LightRAG Status

Server: http://localhost:9622 — API key header: `X-API-Key: 0972f90608b9b953493482d2f5ec446d`

```powershell
# Health
curl.exe -s http://localhost:9622/health -H "X-API-Key: 0972f90608b9b953493482d2f5ec446d"
# Documents + statuses (PENDING / PROCESSING / PROCESSED / FAILED)
curl.exe -s http://localhost:9622/documents -H "X-API-Key: 0972f90608b9b953493482d2f5ec446d"
```

Report to the user: server up/down, document count per status, names of failed docs if any. If server down: `docker ps`, then `docker compose up -d` in F:\____IL_AI\PCM_RAG\lightrag. Full API docs: http://localhost:9622/docs