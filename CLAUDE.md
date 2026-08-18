# PCM_RAG

## RAG Ingest Rules
- Always launch ingests via `ingest_resume.ps1` (detached), never inline — the wrapper produces `ingest_run.log` needed for progress checks.
- Delete/wipe `ingest_run.log` ONLY after the run reports `EXITCODE=0`, never before the run starts.
- Probe every PDF before routing: use full image detection (embedded images AND vector figures), not just `page.get_images()`. Image-heavy → MinerU/VLM path; text-only → text path.
- Slice PDFs over the MinerU size/page limit before ingest; delete slice PDFs only after all slices are confirmed processed.
- Verify every ingest with: doc count delta, graph node delta, vector sanity check, and one targeted query.
