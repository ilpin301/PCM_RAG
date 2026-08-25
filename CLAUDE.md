# PCM_RAG

## RAG Ingest Rules
- Always launch ingests via the ragkit launcher, detached, never inline:
  `& $env:RAGKIT_HOME\ingest.ps1 -Root F:\____IL_AI\PCM_RAG -ListFile <utf8 list>`. It produces
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
