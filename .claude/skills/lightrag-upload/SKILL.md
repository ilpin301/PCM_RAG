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