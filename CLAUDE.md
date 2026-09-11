# PCM_RAG

## RAG Ingest Rules
- **One SOURCE per ingest run.** If `IN\` has several new files, ingest them one at a time:
  full cycle per source (probe, launch, verify, error-correction pass, cleanup, ledger, memory),
  and only then start the next. Never batch several sources into one list file - a failure then
  cannot be attributed and the delete/re-ingest repair costs minutes per document. Slices of ONE
  source still go in ONE run. A failed or lossy source STOPS the queue; report and wait.
- Always launch ingests via the ragkit launcher, detached, never inline:
  `& $env:RAGKIT_HOME\ingest.ps1 -Root X:\RAG_MAIN\PCM_RAG -ListFile <utf8 list>`. It produces
  `lightrag\LOG\ingest_run.log`, which progress checks depend on, and it owns `docker compose`
  `stop`/`start` - do not stop the container yourself. This base has no launcher of its own any more.
- Delete/wipe `ingest_run.log` ONLY after the run reports `EXITCODE=0`, never before the run starts.
- Probe every PDF before routing: use full image detection (embedded images AND vector figures), not just `page.get_images()`. Image-heavy → MinerU/VLM path; text-only → text path.
- Slice PDFs over the MinerU size/page limit before ingest; delete slice PDFs only after all slices are confirmed processed.
- Verify every ingest with: doc count delta, graph node delta, vector sanity check, and one targeted query.
- Record every ingested SOURCE in `lightrag\INGESTED_SOURCES.txt`, not the slice names.

## This base
- Server `pcm_rag-lightrag-1`, port 9622, `COMPOSE_PROJECT_NAME=pcm_rag` in `lightrag\.env`.
- The tooling lives in the ragkit repo, not here: `rag_ingest.py`, `ingest_merged.py`,
  `check_vectors.py`, `ingest_triage.py` and the launcher are all under `$env:RAGKIT_HOME`.
  The RAG skills are user-level too. Nothing RAG-specific is version-controlled in this repo
  except `.env`, the compose file, `IN\`, `FOUND\`, the ledger and `keepawake.ps1`.
- The store (`lightrag\data\rag_storage\`) is NOT in git. It is backed up to Google Drive with
  `rag_sync.ps1`. Never `git add -A` here.
- `rag_sync.ps1 push` must run from a native PowerShell. Invoked from Git Bash, `tar` resolves
  to the msys build, which reads `C:\...` as a remote host and fails with
  `Cannot connect to C: resolve failed`.

## Vector storage: Qdrant (since 2026-09-09)
- Vectors are NOT in `lightrag\data
ag_storage` any more. They live in the docker named volume
  `pcm_rag_qdrant_storage` (ext4 inside the WSL VHDX), served by `pcm_rag-qdrant-1` on
  `127.0.0.1:6333`. `LIGHTRAG_VECTOR_STORAGE=QdrantVectorDBStorage` in `lightrag\.env`.
- **Host-side URLs must be `127.0.0.1`, never `localhost`.** localhost resolves to `::1` first and
  the failed IPv6 attempt costs ~2 s per request - it looks like slow throughput, not a DNS problem.
  The container uses `http://qdrant:6333` via docker DNS; compose sets it and wins because LightRAG
  calls `load_dotenv(override=False)`.
- Do NOT stop the whole compose project to ingest. Qdrant is a server the host ingest talks to;
  `ingest.ps1` stops only the `lightrag` service.
- `rag_sync.ps1 push` exports a Qdrant snapshot per collection into `data\qdrant_snapshots\` and
  tars it alongside `rag_storage`; `pull` uploads them back. A backup taken any other way contains
  no vectors.
- The old `vdb_*.json` files are still present but are DEAD - nothing reads them. They are kept only
  as a rollback until a proving ingest has run. Do not trust them as a source of truth, and do not
  let `check_vectors.py` be pointed at them (it switches on `LIGHTRAG_VECTOR_STORAGE` by itself).
- Verified at migration: recall@10 vs exact cosine 1.0000 / 0.9980 / 0.9970; retrieval identical to
  the pre-migration baseline (jaccard 1.000 over 10 questions).
