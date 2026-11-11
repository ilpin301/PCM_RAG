# PCM_RAG

## RAG Ingest Rules
- **One SOURCE per ingest run.** If `IN\` has several new files, ingest them one at a time:
  full cycle per source (probe, launch, verify, error-correction pass, cleanup, ledger, memory),
  and only then start the next. Never batch several sources into one list file - a failure then
  cannot be attributed and the delete/re-ingest repair costs minutes per document. Slices of ONE
  source still go in ONE run. A failed or lossy source STOPS the queue; report and wait.
- **After each source, `rag_sync.ps1 push -WaitUpload` before the next one launches.** The per-source
  cleanup is not done until that push succeeds AND the cloud check below says VERIFIED. If `J:` is missing, Google Drive is not
  running - start `GoogleDriveFS.exe` (newest version folder under
  `C:\Program Files\Google\Drive File Stream` that contains it - not `Drivers`, which sorts last by name), wait for `J:\My Drive` to appear, then push.
  Native PowerShell only. A failed push stops the queue, same as a failed ingest.
  `-WaitUpload` waits up to 1 h for the cloud upload: exit 0 = `rag_sync.ps1 status` confirmed the cloud upload, exit 4 = copied to `J:` but cloud NOT confirmed (keep keepawake and GoogleDriveFS on, stop the queue, report); run it as a background command (the foreground tool cap is 10 min) and read its exit code when the notification arrives.
- **Start Google Drive at the START of a run** (not right before the push) so it warms up while the ingest
  runs. Before `rag_sync.ps1 push`, if `GoogleDriveFS` has been up < 5 min, wait until it has been up 5 min.
  Why: 2026-09-29 a cold-started Drive (~1 min before the push) made the `Copy-Item` overwrite of
  `rag_storage.tgz` on the streaming mount block >4 min while Drive fetched the old ~1 GB archive; warm
  pushes do not download. Evidence is correlation, cause not proven.
- **keepawake runs from the start of the run until the backup is VERIFIED in Google's cloud.** Start
  `lightrag\keepawake.ps1` before anything else; the push runs under it. A plain `rag_sync.ps1 push` (no `-WaitUpload`) exits 1 = PENDING right after copying to the local `J:` mount; never call that 'backed up' and never read the tool's 'completed' notice as backup done. With `-WaitUpload`, exit 0 still needs the independent cloud check below. VERIFIED = the cloud
  `rag_storage.tgz` in this base's Drive folder (Google Drive MCP, filter by the folder's `parentId`, one
  archive per base) has `fileSize` equal to the local file AND `modifiedTime` after the push started.
  Not yet: keep keepawake and GoogleDriveFS up, re-check every ~5 min, give up after 60 min and report.
  Only then stop keepawake and let the next source start (il-rag-ingest Step 8).
  Why: 2026-10-22 keepawake was stopped before the push; Windows slept mid-push (Kernel-Power 42, System
  Idle), and "push OK" was reported while the cloud still held the previous day's archive. 2026-11-11: a plain push exited 1 (PENDING) while the harness reported 'completed (exit code 0)' from the following command, so `-WaitUpload` is now mandatory.
- Always launch ingests via the ragkit launcher, detached, never inline:
  `& $env:RAGKIT_HOME\ingest.ps1 -Root X:\RAG_MAIN\PCM_RAG -ListFile <utf8 list>`. It produces
  `lightrag\LOG\ingest_run.log`, which progress checks depend on, and it owns `docker compose`
  `stop`/`start` - do not stop the container yourself. This base has no launcher of its own any more.
- Delete/wipe `ingest_run.log` ONLY after the run reports `EXITCODE=0`, never before the run starts.
- Probe every PDF before routing: use full image detection (embedded images AND vector figures), not just `page.get_images()`. Image-heavy → MinerU/VLM path; text-only → text path.
- Slice PDFs over the MinerU size/page limit before ingest; delete slice PDFs only after all slices are confirmed processed.
- **After a verified source, delete its parse artifacts.** `lightrag\data\mineru_output\<source-stem>*`
  and `lightrag\data\merged_ingest\<source-stem>\` go **together**, and only once the source passed
  verification and is written to the ledger. `merged_ingest\<src>\parsed\*.json` is the resume cache and
  its `img_path` entries point into `mineru_output`: delete one without the other and a resumed run
  replays a parse cache whose images are gone, so every image caption fails while the run still exits 0.
  Never touch either for a source still in flight or stuck `handling` - that pair is what lets a
  quota-stopped run skip MinerU on relaunch. Left alone they grow without bound: 152 MB across the three
  bases by 2026-09-16.
- Verify every ingest with: doc count delta, graph node delta, vector sanity check, and one targeted query.
- Record every ingested SOURCE in `lightrag\INGESTED_SOURCES.txt`, not the slice names.
- **Enrichment blocks around ingests (leak guard).** LightRAG's merge summary absorbs
  `<!--PUBCHEM_START-->` blocks into plain prose when an ingest re-mentions an enriched entity.
  Before the FIRST source of an ingest queue: `python lightrag\enrich_pubchem.py --fix-blocks --strip-all
  --collect lightrag\data\enrich_cache\pending_strip_all.json --force`, then apply it with
  `ingest.ps1 -DescFile` (NO Drive push after this strip apply - user rule 2026-10-10:
  the stripped state is transient, the pre-strip store is already on Drive, and the
  post-ingest and post-re-apply pushes are the restore points). After the LAST source is verified: pcm-PubChem-runner
  MODE=collect; then Claude reviews the names in
  `lightrag\data\enrich_cache\collect_new_entities.json` that do NOT yet carry `by: claude-review` in
  verify.json. The file holds the collected entities that had no verify.json entry when the collect STARTED,
  PLUS names kept over from the previous file while still collected (already reviewed), so its printed count
  overstates the work (2026-10-10: 326 listed, 1 new; 347 listed, 21 new). Selecting by "no verify.json
  entry now" finds nothing, because the GLM verdict is written to verify.json during collect). Same-substance check; GLM verify
  alone is not enough for NEW entities. Record the verdicts as in plan Task 3 Step 4 (`same` true/false,
  `by: claude-review`, in verify.json); rejected ones go to EXCLUDE; then MODE=apply (re-adds blocks from the judge/verify/PubChem caches).
  Then `python lightrag\enrich_pubchem.py --scan-leaks` must exit 0. Exit 7 = leaked facts: clean them
  as in docs/superpowers/plans/2026-09-30-rag-data-integrity.md Task 4 before anything else.
  `--strip-all` strips only PubChem blocks; OpenAlex reference blocks (`<!--OPENALEX_START-->`,
  ref_text nodes) can be absorbed into prose by an ingest just the same, there is no strip tool for
  them until OpenAlex Task 8 is run, so the post-ingest `--scan-leaks` (it matches the literal word
  OpenAlex too) is the only guard for them; exit 7 -> clean as in Task 4.
- **Jev shadow on every post-ingest PubChem collect.** Run the collect with `--jev-shadow`
  appended (`pcm-PubChem-runner` has no flag pass-through: write "append `--jev-shadow` to the
  enrich_pubchem.py collect command" in its task prompt, or run the collect yourself). Jev
  (TypeSafe `jev-latest`) only records its probability next to the GLM verdict in
  `lightrag\data\enrich_cache\jev_shadow.json`; it never changes a verdict or the graph, and
  Claude still reviews every new entity. After the Claude review, run
  `python lightrag\jev_recalibrate.py` and report its STATUS line. Jev may skip Claude review
  (option b) only after 100 reviewed GLM-yes entities, zero joint false accepts AND the user's
  explicit OK; until then option (a) only (reorder the queue, never skip). Plan:
  `docs/superpowers/plans/2026-11-11-jev-pubchem-verify.md`.

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
