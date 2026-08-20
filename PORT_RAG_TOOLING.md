# Porting PCM_RAG tooling to another LightRAG project

Written 2026-08-19, from the PCM_RAG work that built `il-rag-ingest` / `il-check-rag-base` and
repaired a vector-store gap. Worked example target: `F:\____IL_AI\MECH_RAG\`.

Read this end to end before copying anything. A blind copy breaks: the projects differ in port,
container name, ingest launcher, and filename encoding.

## 0. What ports and what does not

| Item | Port? | Note |
|---|---|---|
| `.claude/skills/il-rag-ingest/` | yes, with rewrites | the ingest loop; §4 lists every line that must change |
| `.claude/skills/il-check-rag-base/` | yes, with rewrites | the parallel audit; paths + baselines change |
| `lightrag/repairs/repair_vdb.py` | yes | paths only, plus the memory caveat in §5 |
| `lightrag/repairs/cleanup_processed_slices.ps1` | only if the target slices PDFs | pointless where nothing is sliced |
| `lightrag/repairs/delete_dup_stub.ps1` | yes | cheap, and `dup-*` stubs are generic LightRAG behaviour |
| `lightrag/INGESTED_SOURCES.txt` | yes, seeded fresh | never copy PCM's rows; §3 |
| `CLAUDE.md` → `## RAG Ingest Rules` | yes, adapted | §6 |
| `.claude/agents/pcm-PubChem-runner.md` | **NO** | excluded by request; MECH_RAG has no chemistry entities to enrich |
| `.claude/agents/pcm-OpenAlex-runner.md` | **NO** | excluded by request |
| `.claude/skills/raganything-ingest/` | **NO** for MECH_RAG | it already has an equivalent `rag-ingest` skill. Port only to a target that has neither |
| memory files under `~/.claude/projects/.../memory/` | not copied | memory is per-project; write fresh entries for the target as facts are established |

## 1. Substitution table

Everything below is what actually differs. Verify each one against the live target before trusting it.

| | PCM_RAG | MECH_RAG |
|---|---|---|
| project root | `F:\____IL_AI\PCM_RAG` | `F:\____IL_AI\MECH_RAG` |
| container | `pcm_rag-lightrag-1` | `mech_rag-lightrag-1` |
| host port | 9622 | 9623 |
| ingest launcher | `lightrag\ingest_resume.ps1`, inline `$pdfs` array | `lightrag\ingest_detached.ps1 -ListFile`, reads `ingest_list.txt` |
| ingest skill present | `raganything-ingest` | `rag-ingest` |
| vector sanity tool | `lightrag\check_vectors.py` (backported from MECH_RAG, §10) | `lightrag\check_vectors.py` — byte-identical in both, needs no edits when ported |
| `vdb_relationships.json` | ~468 MB | ~1.26 GB |
| root `CLAUDE.md` | exists | does not exist — create one; do NOT edit `lightrag\CLAUDE.md`, that file belongs to upstream LightRAG |
| Drive snapshot | `J:\My Drive\RAG\PCM_RAG\rag_storage.tgz` | `J:\My Drive\RAG\MECH_RAG\rag_storage.tgz` |

Identical in both, so nothing to change: shared venv `F:\____IL_AI\RAG\lightrag\.venv-rag`, embeddings
(Ollama `bge-m3`, dim 1024), `rag_sync.ps1` semantics, storage layout under `lightrag\data\rag_storage`.

## 2. Confirm the target's facts first

Do not skip this. Run against the target and write the answers into the substitution table above.

```powershell
docker ps -a --filter name=lightrag --format '{{.Names}}|{{.Status}}'
Select-String -Path F:\____IL_AI\MECH_RAG\lightrag\.env -Pattern '^(PORT|EMBEDDING_MODEL|EMBEDDING_DIM|EMBEDDING_BINDING)='
Get-ChildItem F:\____IL_AI\MECH_RAG\lightrag\data\rag_storage\vdb_*.json | Select-Object Name,Length
Get-ChildItem F:\____IL_AI\MECH_RAG\lightrag\*.ps1
```

A container showing `Exited (137)` means it was OOM-killed, not shut down cleanly — its JSON stores may
be mid-write. Start it, let it settle, then stop it properly before auditing.

## 3. Seed the ledger

`INGESTED_SOURCES.txt` exists because slices get ingested under renamed short filenames while the source
PDF keeps its long name in `IN\`, so a filename diff of `IN\` against `/documents` re-proposes sources
that are already done. Content hashing cannot substitute — a slice is not byte-identical to its source.

Create `F:\____IL_AI\MECH_RAG\lightrag\INGESTED_SOURCES.txt` with PCM's header comment adapted, then seed
it from what the target has ALREADY ingested — read `kv_store_doc_status.json` `file_path` values with the
container stopped, and map each back to its original source name. Never copy PCM's rows.

## 4. Rewrite points inside the two skills

Copy the skill folders, then fix every one of these. Grep for the old values afterwards to prove none survived:

```powershell
Select-String -Path F:\____IL_AI\MECH_RAG\.claude\skills\il-*\SKILL.md -Pattern 'PCM_RAG|pcm_rag|9622|ingest_resume|raganything-ingest'
```

**il-rag-ingest**
- All paths and the container name and port.
- The launcher section is the big one. PCM builds an inline `$pdfs` array in `ingest_resume.ps1`;
  MECH_RAG writes `ingest_list.txt` and calls `ingest_detached.ps1 -ListFile`. Rewrite the step, do not
  translate it literally.
- The launch guard PCM added (refuse to run on an empty `$pdfs` or a missing file) must be re-expressed
  for the target: refuse to run on an empty or missing `ingest_list.txt`, and on any line in it that does
  not resolve to a file.
- Use `-ListFile` and never bare path arguments — MECH_RAG has German filenames (`Stäben`,
  `Verzerrungszustand`) that get mangled through the ANSI codepage when passed as process args. Write the
  list file as UTF-8. Same reason the ledger must be UTF-8 and any Python touching these names needs
  `PYTHONIOENCODING=utf-8`.
- Keep: the PDF route probe (images AND vector figures — `get_images()` alone mis-routes vector-figure
  PDFs, also check `get_drawings()`), the ≤10-page slice rule for MinerU, the "EXITCODE=0 with no work
  done" case, the four verification checks, and the slice-cleanup-then-ledger-append step.

**il-check-rag-base**
- All paths, container name, port, Drive project folder.
- Step 0's two-blind-spots table is generic — keep it exactly.
- **Delete PCM's "known standing gaps" baseline.** Those numbers (199/233 entities, 439 edges, 9 chunks)
  were never a property of LightRAG; they were one broken flush in PCM's store, since repaired. Carrying
  them over would teach the target's auditors to ignore real damage. Establish the target's own baseline
  from its first clean audit instead, and record it in project memory rather than in the skill.
- Invariant F's slice check is only meaningful if the target slices. Drop it otherwise.
- Add `check_vectors.py` to invariant A as a second, complementary probe — see §5.

## 5. repair_vdb.py

Paths are the only edit for correctness. Two operational caveats:

- **Memory.** It does `json.load` on each store. MECH_RAG's `vdb_relationships.json` is 1.26 GB, which
  needs roughly 6–8 GB of RAM to load and rewrite. If that thrashes, add a `--store entities|relations|chunks`
  flag and run one store per invocation rather than reaching for a streaming parser.
- **It does not replace `check_vectors.py`.** Both projects have `check_vectors.py` now, they catch
  different failures, and both should run:
  `repair_vdb.py` finds records MISSING a vector or STALE vectors whose parent is gone;
  `check_vectors.py` finds vectors that exist but are POISONED — zero vectors from a corrupt Ollama blob
  normalize to NaN, NaN poisons the whole nano-vectordb matrix at load, and retrieval silently returns
  nothing while the ingest still exits 0.

Always dry-run first. It backs up each store before writing; delete the `.bak` files only after verifying.

## 6. CLAUDE.md rules

Create `F:\____IL_AI\MECH_RAG\CLAUDE.md` with a `## RAG Ingest Rules` section adapted from PCM's:
always launch ingests via the detached wrapper so a log exists; delete the run log only after
`EXITCODE=0`; probe every PDF for embedded images AND vector figures before routing; slice oversized
PDFs and delete slices only once every slice is confirmed processed; verify every ingest with doc-count
delta, graph-node delta, vector sanity check, and one targeted query.

Do not touch `lightrag\CLAUDE.md` — that is upstream LightRAG's own file.

## 7. Lessons that cost real time here — carry them, do not rediscover them

- **Deferred embedding is the dangerous failure mode.** `nano_vector_db_impl.py` commits graph writes
  immediately and flushes vectors later. If the flush raises, the pending buffer is kept and *nothing* is
  written — leaving a document fully present in the graph and completely invisible to vector search, with
  a clean `processed` status and exit code 0. Detection recipe: set-difference the graphml node ids
  against `vdb_entities.json` `entity_name`, and normalized `(src,tgt)` edge pairs against
  `vdb_relationships.json`, then group the misses by the graphml `d4` (`file_path`) attribute. **If the
  misses cluster onto one or two files, it is a failed flush for those docs, not a corpus-wide property.**
  Chunks fail the same way — check `kv_store_text_chunks.json` against `vdb_chunks.json` too.
- **Audit the stopped container.** `GET /documents` omits `handling` rows entirely, and the `kv_store_*.json`
  files are stale while the container is up because LightRAG flushes doc_status on shutdown.
- **Deleting a doc leaves vdb rows behind**, especially multimodal ones (`(image)`, `(chart)`, `(table)`,
  `(equation)`). Expect stale vectors after any delete-and-reingest, and sweep for them.
- **Repeated first-N-character prefixes are NOT duplicate chunks** — that is chunk overlap. A subagent
  reported a critical double-ingest on that signal here and it was wrong. Confirm with exact content hashes
  before believing any duplicate finding.
- **`chunks_count` in `kv_store_doc_status.json` drifts** and nothing reads it at query time. A mismatch
  against the real chunk count is cosmetic; do not "repair" it.
- **`EXITCODE=0` can mean no work was done.** Always confirm with a doc-count delta.
- **MinerU fails above roughly 20 pages on this hardware.** Slice to ≤10 pages.
- **A short one-chunk doc is not automatically truncated.** Compare the stored chunk length against the
  full-doc length before flagging it.
- **`J:` only exists while `GoogleDriveFS` is running.** A failed `Test-Path` means Drive is not started,
  not that the backup is gone. Take a `rag_sync.ps1 push` snapshot before any risky operation and again
  after a successful repair.

## 8. Order of operations

1. §2 — confirm the target's facts.
2. `rag_sync.ps1 push` — snapshot before touching anything.
3. Copy `repair_vdb.py` + the applicable repair scripts; fix paths; dry-run only.
4. Port both skills; apply every §4 rewrite; grep to prove no PCM strings survive.
5. Seed `INGESTED_SOURCES.txt`.
6. Create the root `CLAUDE.md`.
7. Stop the container; run the full audit; record the target's real baseline in project memory.
8. Fix only what the audit proves is broken. Re-verify with a targeted query per repaired doc —
   `local` mode exercises entity vectors, `naive` mode exercises chunk vectors.
9. `rag_sync.ps1 push` again, then commit.

## 9. Verification checklist

- `Select-String` for `PCM_RAG|pcm_rag|9622|ingest_resume` across the ported files returns nothing.
- `repair_vdb.py` dry run reports 0 to add / 0 to drop, or a gap you can explain by file.
- `check_vectors.py` exits 0.
- Audit reports every doc `processed`, no `handling`, no `dup-*`.
- One `local`-mode and one `naive`-mode query both return real content.
- Drive snapshot timestamp is newer than the repair.

## 10. Backported the other way (MECH_RAG → PCM_RAG)

Traffic went both ways. These three came from MECH_RAG into PCM_RAG and are now common to both, so a
future port in either direction should not treat them as missing on the far side:

- **`lightrag\check_vectors.py`** — copied with zero edits; it derives its storage path from its own
  location and both projects use dim 1024. It passes on the PCM store: chunks 1928, entities 19540,
  relationships 54269, every row/matrix pair aligned, 0 nonfinite, 0 zero.
- **The success-path vector check in `ingest_resume.ps1`** — from MECH's `ingest_detached.ps1`. It runs
  `check_vectors.py` after a successful ingest and folds a non-zero result into `EXITCODE`, so a silently
  poisoned store keeps its run log instead of having it deleted.
- **`$env:PYTHONINTMAXSTRDIGITS = '0'` in `ingest_resume.ps1`** — also from MECH.

Deliberately NOT backported: MECH's `-ListFile` / `ingest_list.txt` mechanism. It defends against ANSI
codepage mangling of non-ASCII filenames passed as process args; PCM's filenames are all ASCII, so that
failure cannot occur. Port it to PCM only if non-ASCII source filenames ever show up there.

## Periodic LLM cache flush (port this)

LightRAG persists `kv_store_llm_response_cache.json` only at pipeline end, so any multi-hour ingest
loses all extraction work on a crash. PCM_RAG fixes this with `periodic_cache_flush(rag, every=300)`
in `lightrag/rag_ingest.py` — an `asyncio.create_task` started before the ingest loop and cancelled
in a `finally`, calling `rag.lightrag.llm_response_cache.index_done_callback()`.

Port it to every RAG base that runs long ingests. It needs no new dependency and touches only the
two entry points (`main()` and any merged-insert equivalent). Verify with
`grep -n 'periodic_cache_flush' rag_ingest.py` and by watching for `--- llm cache flushed to disk`
in the run log.

While porting, also carry over `repairs/repair_vdb.py` — `delete_document` strands orphaned entity
vectors on every delete, not just after crashes.
