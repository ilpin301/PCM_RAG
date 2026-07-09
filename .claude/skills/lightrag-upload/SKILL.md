---
name: lightrag-upload
description: Upload text documents (txt, md, normal text PDFs) into the local LightRAG knowledge graph. Use when the user says to add/upload/ingest a text document into the rag. NOT for scanned PDFs, images, or chart-heavy docs — use raganything-ingest for those.
---

# LightRAG Upload

Server: http://localhost:9622 — API key header: `X-API-Key: 0972f90608b9b953493482d2f5ec446d`

```powershell
curl.exe -s -X POST http://localhost:9622/documents/upload -H "X-API-Key: 0972f90608b9b953493482d2f5ec446d" -F "file=@C:\path\to\document.pdf"
```

For multiple files, run one curl per file. After upload, processing (chunking, entity extraction via GLM, embedding via Ollama bge-m3) runs in the background — can take minutes per document. Check progress with the lightrag-status skill. Warn the user that large documents take a while and consume Z.ai tokens.