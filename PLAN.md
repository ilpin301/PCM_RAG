# Plan: Portable universal RAG toolkit (`ragkit`) + ingest sound notifications
_Locked via grill — by Claude + ilpin301, 2026-08-24_

## Goal

Stop hand-porting RAG tooling between LightRAG bases. Today every base (PCM_RAG, MECH_RAG, and
any future one) keeps its own near-identical copies of `rag_ingest.py`, `check_vectors.py` and an
ingest launcher, plus its own project-scoped copies of the RAG skills with ~50 hardcoded
references to base path, port and container name. Fixes applied to one base (the
`periodic_cache_flush` crash guard, the `check_vectors` poison gate, the PDF route probe) do not
reach the others, and `PORT_RAG_TOOLING.md` exists solely to describe the manual copy.

Replace that with one shared, version-controlled toolkit at `F:\____IL_AI\RAG\ragkit\` and one
set of user-level skills at `~\.claude\skills\` that auto-derive every per-base fact at runtime.
A new RAG base should then need zero tooling setup: create it, and the skills work.

The same must hold across machines. This toolkit and the bases created with it will run on more
than one computer — same LLM models and API keys, but a different drive layout, user profile and
possibly a different GPU. So no absolute machine path may appear in the kit, the launcher or the
skills. Per-machine facts are confined to exactly two places: one environment variable and one
gitignored file. Everything else is derived.

Fold in the new requirement while the launcher is being rewritten anyway: audible completion
signals. `C:\Windows\Media\Ring10.wav` on success, `C:\Windows\Media\Windows Critical Stop.wav`
on failure — replacing the existing `[console]::beep(880,300)` ×3 in PCM's wrapper, which MECH
does not have at all.

## Execution segments (resumable)

This plan is built to be executed across several sessions. The segments below are ordered but individually shippable: **every segment ends with both bases fully working**, so a session may stop after any of them. Nothing is deleted until Segments 5 and 6, and until then both bases still run on their original launchers.

**Status:** none started. Update this line as segments complete — it is what a fresh session reads first.

| Seg | What | Covers | Depends on | Size |
|---|---|---|---|---|
| S0 | Safety net + checkpoint commits | Phase 0 | — | small |
| S1 | Build the kit (copy, no cutover) | Phase 0b, Phase 1 | S0 | large |
| S2 | Author the six skills in the kit, run bootstrap | Phase 2 | S1 | large |
| S3 | Prove the new path — scratch base + one small PCM ingest | Phase 5 scratch + PCM acceptance | S2 | medium |
| S4 | MECH wiring — ledger, CLAUDE.md, gitignore whitelist | Phase 3 MECH items | S2 | medium |
| S5 | Cut PCM over — delete PCM's old launcher, moved scripts, project skills | Phase 3 PCM items | S3 | small |
| S6 | Cut MECH over + one small MECH ingest | Phase 3 MECH deletions, Phase 5 MECH acceptance | S4, S5 | medium |
| S7 | MECH integrity audit | Phase 4 | S0 | open-ended |
| S8 | Docs, portability grep, final snapshots + commits | Phase 5 dry-check, Phase 3 runbook rewrite | S6 | small |

### Per-segment exit state

- **S0 done** — both bases have a fresh Drive snapshot and a clean `git status`. Proof: `git status --porcelain` empty on both; snapshot timestamp newer than the session start.
- **S1 done** — the kit repo exists with `requirements.txt`, `ingest.ps1`, `notify.ps1`, `bootstrap.ps1`, the four python scripts, the tiktoken seed and a README. Scripts were **copied**, not moved, so both bases still run untouched. Proof: `ingest_merged.py --self-test` passes from inside the kit; both bases' original launchers still present.
- **S2 done** — the six skills exist under `ragkit\skills\` and bootstrap has installed them to `~\.claude\skills\`. The per-base skill folders still exist and still shadow the global ones, so behaviour is unchanged. Proof: the Phase 2 grep returns nothing across both the kit source and the install target.
- **S3 done** — the scratch-base test passed and one small PCM PDF ingested end to end through the kit launcher, with the success wav heard. Proof: `EXITCODE=0`, doc-count delta +1 read from `kv_store_doc_status.json`, `check_vectors.py` exit 0, one targeted query returns the new content. PCM's original launcher is still in place and still works.
- **S4 done** — MECH has its seeded `INGESTED_SOURCES.txt`, a root `CLAUDE.md`, and a `.gitignore` whitelist that actually tracks both. Proof: `git check-ignore -v` confirms neither is ignored. No MECH behaviour has changed yet.
- **S5 done** — PCM runs only through the kit. Its old launcher, the copied-out python and its six project skill folders are gone. Proof: PCM's `.claude\skills\` holds no RAG skill; a second small PCM ingest through the kit still exits 0.
- **S6 done** — MECH runs only through the kit, proven by one small MECH ingest. Proof: same four checks as S3, run against MECH; MECH's `.claude\skills\` holds only `il-aufgabe`.
- **S7 done** — MECH's real baseline is recorded in project memory and only proven damage was repaired. Proof: the audit report plus one `local`-mode and one `naive`-mode query returning real content. **This segment is open-ended and deliberately isolated — it can be deferred indefinitely without blocking anything else.**
- **S8 done** — `PORT_RAG_TOOLING.md` is rewritten as "how to register a new base", the portability grep returns nothing, both bases and the kit are snapshotted and committed. Proof: the Phase 5 dry-check grep is empty; three clean `git status` results.

### Resuming in a fresh session

Read this file's **Status** line, then the exit-state paragraph for the last completed segment and verify its proof still holds — do not trust the marker alone. `PLAN-REVIEW-LOG.md` holds the full argument behind every decision here and does not need re-reading unless a decision is being reopened.

Two standing rules across all segments: take a `rag_sync.ps1 push` snapshot before any segment that writes to a store (S3, S5, S6, S7), and never delete a run log before `EXITCODE=0`.

## Evidence this is feasible (measured, not assumed)

- `PCM_RAG/lightrag/check_vectors.py` and `MECH_RAG/lightrag/check_vectors.py` are byte-identical
  (`diff -q` silent).
- `rag_ingest.py` differs between the two bases **only** by the `periodic_cache_flush` definition
  + its `create_task`/cancel pair, and one `WORKING_DIR` line. 44 diff lines total, 202 vs 177
  lines. The `_VLM_SEMAPHORE = asyncio.Semaphore(2)` and the three monkey-patches are already
  identical in both.
- `MECH_RAG/lightrag/ingest_detached.ps1` is already parameterized with `$root` / `$venv` / `$log`
  locals. Its real deltas from PCM's `ingest_resume.ps1` are: the root path, the `.env` key name
  (`LLM_BINDING_API_KEY` vs `ZAI_API_KEY`), the entrypoint (`rag_ingest.py` vs
  `ingest_merged.py --pages`), and PCM's extra failure branch (timestamped log, `ingest_triage.py`,
  `LAST_FAILURE.txt`, beep).
- Both bases already share one venv: `F:\____IL_AI\RAG\lightrag\.venv-rag`. `ragkit` sits beside it.
- Both wav files exist on this machine.
- Each base carries its OWN vendored `lightrag\lightrag\` package that shadows the venv install via
  `sys.path[0]`. Measured: PCM vendored vs venv `lightrag_hku` = 144 differing files; PCM vendored
  vs MECH vendored = 57 differing files. This is a fifth per-base variable and the largest one — it
  is handled by pinning `PYTHONPATH`, not by unifying it.
- `Media.SoundPlayer` was verified to resolve under this machine's PowerShell 7 (`pwsh -NoProfile`
  constructed it successfully), so `notify.ps1` needs no `Add-Type` shim.
- The plan as first drafted embedded 9 machine-bound absolute paths (kit root, venv,
  `TIKTOKEN_CACHE_DIR`, `MINERU_DEVICE_MODE=cuda`, the `C:\Windows\Media` wavs, and the `F:` drive
  assumptions in the tradeoff and risk sections). All are removed by this revision.
- `check_vectors.py:22` hardcodes `DIM = 1024`. Both current bases are `bge-m3` /
  `EMBEDDING_DIM=1024`, so the hardcode has never been exercised — but `EMBEDDING_DIM` is present
  in both `.env` files and can simply be read.
- The venv is not clonable: `pyvenv.cfg` records `home = C:\Python\Python313` and the
  console-script shims embed absolute paths. Machine 2 must build its own venv, not receive a copy.
- Version stack measured on this machine: `lightrag-hku 1.5.4`, `raganything 1.3.1`, `mineru
  3.4.2`, `torch 2.7.1+cu126`. Nothing currently pins these, and the three monkey-patches hook
  private call paths that are version-fragile.
- `repair_vdb.py:10` hardcodes its base path with FORWARD slashes (`"F:/..."`), so a portability
  grep anchored on backslashes would have missed it.

So the per-base divergence that the manual port exists to manage is five variables: root path,
port, container name, `.env` key name, and the vendored `lightrag` package. The first four are
derivable at runtime; the fifth is pinned per base via `PYTHONPATH` rather than unified.

## Approach

### Phase 0 — safety net
1. `rag_sync.ps1 push` on **both** PCM_RAG and MECH_RAG. `J:` only exists while GoogleDriveFS is
   running; a failed `Test-Path J:\` means Drive is not started, not that the backup is gone —
   start it and retry rather than proceeding without a snapshot.
2. Commit PCM_RAG's existing uncommitted work as its own commit, so the port diff is separable.
   Enumerate the files explicitly at commit time rather than `git add -A` — the working tree
   currently also holds untracked `.obsidian/`, `FOUND/no-ENG/` and a stray `IN/*.pdf` that must
   NOT be swept in. Add `.obsidian/` to `.gitignore`.
3. Commit MECH_RAG's dirty tree as-is (`chore: checkpoint before ragkit port`). This includes
   modified `lightrag/data/rag_storage/*` and deleted `FOUND/` PDFs. Deliberately **not** fixing
   the fact that MECH tracks 13 rag_storage files in git (`.git` is already 259 MB) — out of scope,
   recorded as a follow-up. Enumerate files there too — `git add -A` would sweep unrelated
   untracked paths into the repo permanently.

### Phase 0b — machine-portability contract

Everything the kit does must resolve at runtime. Exactly two per-machine facts are allowed to be
configured, and nothing else:

- **`RAGKIT_HOME`** — one environment variable per machine, pointing at the cloned kit. The skills
  need it because they run from an arbitrary working directory and have no other anchor to the
  kit. Discovery fails loudly if it is unset; it never guesses a drive letter.
- **`ragkit\machine.ps1`** — one gitignored file per machine, holding BOTH the venv path (`$VENV`)
  and the CUDA verdict (`$HasCUDA`). Generated by `ragkit\bootstrap.ps1`, which autodetects both
  and writes the file. This is a
  per-*machine* config, not a per-*base* one, so it does not reopen the "auto-derive, no config
  file" decision — that decision governs bases, of which there may be many; machines are few and
  their layout genuinely cannot be derived. `bootstrap.ps1` does not merely autodetect a venv — on
  a fresh machine there is none to detect. See Phase 1's bootstrap step: detect, else create from
  the pinned requirements.

Everything else derives:
- The launcher locates itself with `$PSScriptRoot`; it never names its own path.
- `TIKTOKEN_CACHE_DIR` = `"$env:TEMP\data-gym-cache"`.
- `MINERU_DEVICE_MODE` = `cuda` or `cpu`, read from `$HasCUDA` in `machine.ps1` — decided once by
  bootstrap via `torch.cuda.is_available()`, never re-probed at launch. `nvidia-smi` resolving on
  `PATH` is NOT the test: a driver present with a cpu-only torch in the venv would select `cuda`
  and crash at parse time. This stays inside the two-facts contract, because `machine.ps1` is the
  designated per-machine file.
- The wav paths = `"$env:WINDIR\Media\Ring10.wav"` and `"$env:WINDIR\Media\Windows Critical Stop.wav"`.
- Base root, port, container, `.env` key name, embedding dim — all discovered per base, as already
  specified.

Distribution to a second machine is `git clone` of the kit repo, then `bootstrap.ps1`. The clone
must therefore carry everything machine 2 needs: the launcher, the python, the pinned
requirements, AND the six skills — a skill written only to `~\.claude\skills\` on machine 1
reaches machine 2 by no path at all. The `.env` files carrying the API keys are gitignored and
copied by hand per machine — deliberately not automated, because they are secrets and must never
enter the kit repo.

### Phase 1 — build the kit
4. `git init` the kit as its own repo, independent of any base. On this machine it lives beside
   the shared venv; its location is not baked into anything — the skills find it through
   `RAGKIT_HOME` and the launcher finds itself through `$PSScriptRoot`.
5. Copy into it (the originals stay until S5/S6 — see Execution segments), taking the PCM variant as canonical since it is strictly newer:
   - `rag_ingest.py` — with `periodic_cache_flush`, the 3 monkey-patches, `_VLM_SEMAPHORE = 2`.
     `WORKING_DIR` now comes from `--root` / `RAGBASE_ROOT`, not a literal.
   - `ingest_merged.py` — merged-document ingest; keeps its `--self-test`.
   - `check_vectors.py` — already identical in both; derive the storage path from `--root`, and
     **read the embedding dim from `<root>\lightrag\.env` (`EMBEDDING_DIM`) instead of the
     hardcoded `DIM = 1024` at `check_vectors.py:22`**. Fail loudly if the key is absent — never
     default to 1024. A future base on a different embedding model would otherwise get a poison
     gate checking the wrong dim, and since the result is folded into `$ec`, every ingest would
     report failure and play the error wav.
   - `repair_vdb.py` and the applicable `repairs/*.ps1`.
   - `ingest_triage.py`.
   - `repairs\resync_chunks_count.py` — **not** moved. It repairs a `chunks_count` field that
     nothing reads at query time; the drift is cosmetic. Leave it in PCM_RAG with a one-line note
     in `ragkit/README.md` saying it was deliberately not adopted.
   - `skills\` — the six global skills (authored here per Phase 2), and `seed\data-gym-cache\` — a
     one-time copy of this machine's tiktoken cache, a few MB of `.tiktoken` files. Nothing else
     populates it, so if it is not copied in deliberately, bootstrap's seed step has nothing to seed
     from.
6. Write `ragkit\requirements.txt`, pinning the stack this tooling is actually proven against:
   `lightrag-hku==1.5.4`, `raganything==1.3.1`, `mineru==3.4.2`, and torch `2.7.1+cu126` (which
   needs its CUDA index URL, so record that in the file as a comment). Capture the full set with
   `pip freeze` from the current venv rather than hand-listing it. Rationale: an unpinned `pip
   install` on machine 2 fetches latest, and the three monkey-patches hook private call paths —
   `_rebuild_role_llm_funcs`, the asdict redirect, the separate_content filter — that a minor
   version bump can silently move.
7. Write `ragkit/ingest.ps1` — the one universal launcher.
   - Signature: `-Root <base> -ListFile <utf8 list> [-Merged] [-Pages N]`.
   - Run **all input guards first** (empty/missing list file, unresolvable line, missing `.env`,
     missing key, missing `EMBEDDING_DIM`, `-Merged` with multiple entries), and only once the
     invocation is committed to running do `Set-Location "$Root\lightrag"` and
     `docker compose stop`. `rag_ingest.py:4-5` states the container must be stopped before running
     — shared JSON storage, concurrent writes corrupt it. Today neither wrapper does this; the stop
     lives informally in the skill flow. Under one universal entrypoint the launcher must own it, or
     a new base's operator who only knows the launcher will corrupt their store. `docker compose
     start` still runs at the end of BOTH branches, as today. Rationale for the ordering: a guard
     that throws after the stop is in neither the success nor the failure branch, so the trailing
     `docker compose start` never runs and the base's server stays down until somebody notices.
   - **`$env:PYTHONPATH = "$Root\lightrag"`** before invoking python. Each base vendors its own
     `lightrag\lightrag\` package which currently shadows the venv because the script sits in the
     clone root; running from `ragkit\` would silently swap in the venv's `lightrag_hku` instead —
     a third library variant the three monkey-patches were never tested against. Pinning
     PYTHONPATH preserves today's exact resolution per base.
   - Define the no-vendored-clone case explicitly: if `$Root\lightrag\lightrag\` does not exist,
     the base has no vendored package and `PYTHONPATH` resolves to the venv's `lightrag_hku` —
     which is correct for such a base. The launcher logs which package path won, so the resolution
     is never silent.
   - `New-Item -ItemType Directory -Force "$Root\lightrag\LOG"` — PCM's wrapper assumes `LOG\`
     exists; a brand-new base will not have it.
   - Reject `-Merged` when the list file has more than one entry: `ingest_merged.py` takes exactly
     one source PDF. Fail with a clear message rather than silently ingesting only the first line.
   - **Always** `-ListFile`, UTF-8, never bare path args — MECH has German filenames (`Stäben`,
     `Verzerrungszustand`) that mangle through the ANSI codepage as process arguments. Using it
     unconditionally means no base can regress into the bug.
   - Guards: refuse an empty or missing list file; refuse any line that does not resolve to a file;
     refuse a `-Root` with no `lightrag\.env`.
   - Auto-detect the API key: read `$Root\lightrag\.env`, accept `ZAI_API_KEY` or
     `LLM_BINDING_API_KEY`, export as `ZAI_API_KEY` (what the python expects). Fail loudly if
     neither is present. PCM's `.env` contains BOTH keys, so precedence is fixed: `ZAI_API_KEY`
     wins; `LLM_BINDING_API_KEY` is the fallback.
   - Carries the env block both bases already need, with the machine-bound values now derived per
     Phase 0b: `NO_PROXY=*`, `PYTHONIOENCODING=utf-8`, `PYTHONINTMAXSTRDIGITS=0`,
     `MINERU_DEVICE_MODE` (read from `$HasCUDA` in `machine.ps1`, never re-probed), `TIKTOKEN_CACHE_DIR` =
     `$env:TEMP\data-gym-cache`, and the venv from `machine.ps1` prepended to `PATH`.
   - Success gate is unchanged in meaning: run the entrypoint, then run `check_vectors.py` and fold
     a non-zero result into `$ec`, so a NaN-poisoned store cannot exit 0.
   - Failure branch (from PCM, which MECH lacks): timestamped `ingest_FAILED_<stamp>.log`,
     `ingest_triage.py`, `LAST_FAILURE.txt`.
   - `EXITCODE=<n>` appended to the log in both branches. Log deleted only on `$ec -eq 0`.
   - Tolerate a `docker compose stop` failure when Docker Desktop is not running — "already down"
     is the desired state, and erroring at step one would make a healthy ingest look failed. Only
     a stop failure while the container is genuinely up is fatal.
8. Write `ragkit/notify.ps1` — `Play-RagSound -Success|-Failure`.
   - `(New-Object Media.SoundPlayer $path).PlaySync()`, once, per branch, using
     `$env:WINDIR\Media\Ring10.wav` and `$env:WINDIR\Media\Windows Critical Stop.wav` rather than
     a `C:\Windows\Media\...` literal.
   - Wrapped in `try/catch`; a sound failure is swallowed and **never** alters `$ec`. A missing
     sound card, an RDP session or a locked user session must not turn a good ingest into a
     reported failure.
   - Falls back to `[console]::beep` if the wav is missing.
   - Fired from `ingest.ps1` only, on the single `$ec` decision — not from the skills, not
     mid-run. Rationale: mid-run error scanning would trip on the benign `3/4 fields on ENTITY`
     warnings (measured 0.12% of records) and on transient retries during a 6-hour run.
9. Write `ragkit\bootstrap.ps1` — run once per machine. It:
   - Verifies the interpreter is Python 3.13.x before creating the venv, and fails loudly
     otherwise. The `requirements.txt` is a `pip freeze` taken from a 3.13 venv; on another minor
     version wheels may be absent and the dependency set re-resolves — which is precisely what the
     version-fragile monkey-patches cannot absorb.
   - Detects an existing venv; if none, **creates** one and installs `ragkit\requirements.txt`. A
     venv cannot be copied between machines — `pyvenv.cfg` and the console-script shims embed
     absolute interpreter paths — so 'autodetect' is a skip-if-present optimisation, never the
     provisioning path.
   - Writes `machine.ps1` with the venv path and the CUDA verdict (`$HasCUDA`). Refuses to overwrite
     an existing one without `-Force`.
   - **Installs the six skills** from `ragkit\skills\` into `~\.claude\skills\` (copy on a plain
     machine; a directory junction is acceptable on the machine where they are being developed, so
     edits flow both ways). Overwrites stale skill folders on re-install rather than merging into
     them.
   - Seeds `$env:TEMP\data-gym-cache` from the kit if a seed copy is present, else warns clearly.
     A cold tiktoken cache makes the first ingest download `o200k_base` from the Azure CDN, which
     the existing wrapper comment records as timing out on a SOCKS-proxied machine.
   - Verifies Docker responds, both wav files exist under `$env:WINDIR\Media`, and — via the venv
     python — `torch.cuda.is_available()`, not merely that `nvidia-smi` resolves: a driver without
     a CUDA runtime, or a cpu-only torch, would otherwise select `cuda` and crash at parse time. The
     verdict is WRITTEN to `machine.ps1` as `$HasCUDA`, not merely checked — the launcher reads it
     and never probes.
   - Prints the `RAGKIT_HOME` value to set, and states explicitly that shells and any running
     Claude sessions must be restarted before it takes effect.
10. Write `ragkit/README.md`: what each script is, the `-Root` contract, the two per-machine facts
    and the "adding a new machine" procedure, and a short "adding a new base" section.

### Phase 2 — global skills
11. Author six skills in `ragkit\skills\` (version-controlled in the kit repo); they reach
    `~\.claude\skills\` only via `bootstrap.ps1`. Authoring them in the kit repo is what makes them
    portable; `~\.claude\skills\` is an install target, never the source of truth. Each opens with
    a **discovery step** that replaces every hardcoded value:
    - root = the current project directory (must contain `lightrag\`)
    - port = `PORT=` from `<root>\lightrag\.env`
    - container = `docker compose ps --format json` run in `<root>\lightrag`
    - storage = `<root>\lightrag\data\rag_storage`
    - ledger = `<root>\lightrag\INGESTED_SOURCES.txt`
    - kit = `$env:RAGKIT_HOME` — fail loudly if unset, never guess a path
    - embedding dim = `EMBEDDING_DIM` from `<root>\lightrag\.env`
    - Discovery fails loudly and stops if `lightrag\` is absent — the skill must never guess.
   The six: `il-rag-ingest` (PCM's, merged with whatever MECH's `rag-ingest` holds that PCM's does
   not — read and salvage before deleting), `il-check-rag-base`, `raganything-ingest`,
   `lightrag-query`, `lightrag-status`, `lightrag-upload`.
12. Delete the per-base copies: PCM's six under `PCM_RAG\.claude\skills\`, MECH's four
    (`rag-ingest`, `lightrag-query`, `lightrag-status`, `lightrag-upload`). MECH's `il-aufgabe`
    **stays** — it is domain-specific to technical mechanics, not RAG tooling.
13. Grep to prove no base-specific string survives in the global skills:
    `Select-String -Path ~\.claude\skills\*,ragkit\skills\* -Pattern 'PCM_RAG|pcm_rag|MECH_RAG|mech_rag|9622|9623|ingest_resume|ingest_detached'`
    must return nothing. Grep both the install target AND `ragkit\skills\` — the kit is the source
    of truth; on the development machine a junction can make the install target look identical,
    which would hide a stale or divergent source.
14. Prove no *project-scoped* RAG skill survives to shadow a global one — project skills win over
    global. `Get-ChildItem <base>\.claude\skills` on every base must show no RAG skill folder
    (MECH's `il-aufgabe` is the only permitted survivor). The step 13 grep only scans the global
    folder and cannot catch this.
15. Strip PCM's "known standing gaps" baseline (199/233 entities, 439 edges, 9 chunks) from the
    global `il-check-rag-base`. Those numbers were one broken flush in PCM, since repaired; as a
    global default they would teach every base's auditor to ignore real damage. Per-base baselines
    live in that base's project memory instead.

**Sequencing:** `bootstrap.ps1` (Phase 1) installs the skills authored in this phase, so on machine
1 bootstrap is run *after* Phase 2 completes and *before* Phase 5 acceptance. Writing the bootstrap
earlier is fine; running it earlier installs nothing.

### Phase 3 — per-base wiring
16. PCM_RAG: delete `lightrag\ingest_resume.ps1` and the moved python. Keep `.env`,
    `docker-compose`, `data\`, `IN\`, `FOUND\`, `INGESTED_SOURCES.txt`, `keepawake.ps1`.
17. MECH_RAG: delete `lightrag\ingest_detached.ps1` and the moved python. Update MECH's
    `.gitignore`, whose whitelist currently names `!/lightrag/rag_ingest.py`,
    `!/lightrag/ingest_detached.ps1`, `!/lightrag/check_vectors.py` — all three are leaving.
    MECH's `.gitignore` is a **whitelist** (`/lightrag/*` then `!` exceptions), so the new files
    created in the following steps are untracked by default. Add `!/lightrag/INGESTED_SOURCES.txt`
    explicitly, and confirm with `git check-ignore -v` that both it and the new root `CLAUDE.md`
    are tracked. An unversioned ledger silently loses the re-ingest guard.
18. Seed `MECH_RAG\lightrag\INGESTED_SOURCES.txt` from what MECH has already ingested: read
    `kv_store_doc_status.json` `file_path` values **with the container stopped** (the JSON is stale
    while it is up) and map each back to its original source name. Never copy PCM's rows.
19. Create `MECH_RAG\CLAUDE.md` with the `## RAG Ingest Rules` section adapted from PCM's. Do
    **not** touch `MECH_RAG\lightrag\CLAUDE.md` — that file belongs to the upstream LightRAG clone.
20. Rewrite `PORT_RAG_TOOLING.md`: it stops being a copy procedure and becomes "how to register a
    new base with ragkit", which is short.

### Phase 4 — audit MECH (PORT_RAG_TOOLING §8 step 7)
21. Stop the MECH container, run the full `il-check-rag-base` audit against it, record MECH's own
    real baseline in project memory.
22. Fix only what the audit proves is broken. Re-verify each repaired doc with a targeted query —
    `local` mode exercises entity vectors, `naive` mode exercises chunk vectors.
    - Note: `repair_vdb.py` does `json.load` per store and MECH's `vdb_relationships.json` is
      ~1.26 GB, needing roughly 6–8 GB RAM to load and rewrite. If it thrashes, add a
      `--store entities|relations|chunks` flag and run one store per invocation rather than
      reaching for a streaming parser.

### Phase 5 — acceptance
23. Pick one small, text-only PDF per base from its `FOUND\` backlog. Run each end to end through
    `ragkit\ingest.ps1`. ~10–20 min each, not hours.
24. Per base, confirm: discovery resolved the right port/container; `--- llm cache flushed to disk`
    appears in the run log; `EXITCODE=0`; doc-count delta +1 read from `kv_store_doc_status.json`
    (not `GET /documents`, which hides `handling` rows); graph node delta > 0; `check_vectors.py`
    exits 0; one targeted query returns the new content; the ledger gained a row; **Ring10 played**.
25. Force one failure deliberately (point the list file at a nonexistent path) and confirm the
    critical-stop wav plays, the log is kept under `ingest_FAILED_<stamp>.log`, and
    `LAST_FAILURE.txt` is written.
26. `rag_sync.ps1 push` both bases again. Commit ragkit, PCM_RAG and MECH_RAG separately.
27. Scaffold a throwaway scratch base (a directory with only `lightrag\.env`, a compose file and
    an empty `IN\`) and run discovery plus every launcher guard against it — empty list file,
    missing list file, a list line that does not resolve, `-Merged` with two entries, missing
    `.env` key, missing `EMBEDDING_DIM`. No real ingest. This is the only step that actually tests
    the universality claim; Phases 1–4 only ever exercise the two bases the code was derived from.
    Then run `ingest_merged.py --self-test` — it imports `rag_ingest`, which reads `ZAI_API_KEY`
    at module import — the scratch invocation must export a key (any non-empty value is enough for
    the self-test) or it dies before testing anything — and run `check_vectors.py` against it
    expecting **exit 3 with all three stores reported `missing`** — measured, that is what it does
    on an absent store, and it is the correct answer for a base that has ingested nothing. No new
    code in `check_vectors.py` is needed; what the run proves is that `PYTHONPATH` resolved and the
    `EMBEDDING_DIM` read from the scratch `.env` succeeded, both of which happen before the store
    check. Delete the scratch base afterwards.
28. Portability dry-check: grep the whole kit and all six global skills for absolute machine
    paths. The pattern must catch `[A-Za-z]:[\\/]` (both slash directions — `repair_vdb.py:10`
    uses forward slashes today), UNC prefixes (`\\\\`), and the literal string `____IL_AI`, across
    `ragkit\*`, `ragkit\skills\*` and the global skills install target — a backslash-only pattern
    proves nothing, and grepping only the install target proves nothing either: the kit is the
    source of truth; on the development machine a junction can make the install target look
    identical, which would hide a stale or divergent source. Must return nothing outside
    `machine.ps1` (gitignored) and prose examples in the README.

## Key decisions & tradeoffs

- **Auto-derive, no per-base config file.** Rejected `ragbase.json` and the derive-plus-override
  hybrid. A future base then needs zero setup, and there is one code path rather than two. Cost: a
  base with an unusual layout has no escape hatch — accepted, because both current bases share a
  layout and the discovery step fails loudly rather than guessing.
- **One universal launcher, per-base wrappers deleted.** Rejected "kit holds a template, a sync
  script patches each base". Sync-from-template still allows drift, which is exactly the failure
  this plan exists to end. Cost: a base is no longer runnable if the kit is unreachable. Accepted
  — the venv already creates that dependency.
- **Kit owns all four python scripts, not just the utilities.** Justified by measurement: the
  PCM/MECH `rag_ingest.py` delta is one `WORKING_DIR` line plus the flush block. Keeping per-base
  copies "for independence" would preserve exactly the drift that lost the monkey-patches and the
  cache flush from MECH.
- **Kit gets its own git repo** rather than living inside PCM_RAG. Making PCM the canonical home
  keeps it special forever and reads wrong once a third base exists.
- **Sounds live in the launcher only, fire once on the `$ec` decision, and can never change the
  exit code.** Rejected "fire on any ERROR line in the log" as noisy against benign warnings, and
  rejected "repeat until dismissed" outright — a detached run has no interactive console, so it
  would hang forever with nobody at the machine.
- **`-ListFile` UTF-8 becomes unconditional**, even though PCM's filenames are all ASCII and
  `PORT_RAG_TOOLING.md` §10 deliberately did not backport it. Under one shared launcher the
  cheaper choice is to make the safe path the only path.
- **MECH's dirty tree is committed as-is, not cleaned.** Untracking `rag_storage` would not shrink
  the existing 259 MB of history anyway, and would demand the same treatment for PCM. Recorded as
  a follow-up, not done here.
- **Both enrichment agents (`pcm-PubChem-runner`, `pcm-OpenAlex-runner`) stay project-scoped to
  PCM_RAG.** They are chemistry/bibliography specific; MECH has no use for them. This reaffirms an
  earlier decision, not a new one.
- **`PYTHONPATH` pinning over library unification.** The three vendored `lightrag` trees differ by
  57–144 files. Merging them is a separate, much larger project with its own regression risk;
  pinning `PYTHONPATH` per base makes the kit portable without touching the library each base is
  actually proven against.
- **The launcher owns `docker compose stop`/`start`.** Moving it out of the skill flow and into the
  one entrypoint means a base cannot be corrupted by an operator who invokes the launcher directly.
- **Two per-machine facts, no more.** `RAGKIT_HOME` and a gitignored `machine.ps1`. Rejected
  deriving the kit location from the base (layouts differ between machines) and rejected a fully
  env-var-driven setup (too many variables to set in every shell). Cost: a second machine needs one
  bootstrap run before anything works — acceptable, because it is once per machine, not once per
  base.
- **Read `EMBEDDING_DIM` rather than defaulting it.** A silent default of 1024 would make the
  poison gate pass wrongly on a base with a different embedding model, which is worse than failing
  loudly — the gate exists precisely to catch silent vector corruption.
- **The kit repo carries the skills, the requirements pin and the launcher — everything machine 2
  needs.** Anything written only to a user-profile directory is invisible to a `git clone` and
  therefore does not exist on machine 2.
- **Pin the dependency stack rather than tracking latest.** The monkey-patches hook private APIs;
  a silent minor bump is exactly the failure that is hardest to attribute later. Cost: pinned
  versions go stale and must be bumped deliberately.
- **Phase 1 copies rather than moves; the deletions are deferred to S5/S6.** The reviewed plan said
  "move (not copy)", which would cut both bases over the instant the kit exists and leave them
  broken if a session stopped mid-way. Copy-then-delete-later keeps every segment independently
  shippable and revertible. Cost: the two copies coexist until S5/S6, so an edit made to a base's
  copy in that window would be lost — during it, the kit is the only place to edit. **This
  deviation was introduced after the round-4 approval and has not been through adversarial
  review.**

## Risks / open questions

- **Non-project invocation.** A global skill invoked from a directory that is not a RAG base has no
  root to derive. Discovery must stop with a clear message, not fall back to a default base.
- **Discovery cost.** `docker compose ps` per skill invocation adds a second or two and requires
  Docker to be running. A `lightrag-status` call against a stopped stack must still report
  usefully rather than failing in discovery.
- **The kit repo must not capture the venv directory.** The venv lives beside `ragkit` as a
  sibling, and `ragkit` is its own repo, so the venv should not be captured — verify this rather
  than assume it.
- **MECH audit scope is unbounded.** Phase 4 may surface real damage, and the 1.26 GB relationship
  store makes repairs slow and memory-hungry. If it grows past this session, Phases 1–3 and 5 still
  stand on their own and Phase 4 can be split out.
- **Two BSODs in 72 hours** on this machine (`APC_INDEX_MISMATCH` 2026-08-20,
  `MEMORY_MANAGEMENT` 2026-08-18) under GPU/RAM load, never diagnosed. Phase 5's acceptance ingests
  are deliberately small partly for this reason. `keepawake.ps1` before any long run.
- **Unknown:** whether MECH's `rag-ingest` skill holds MECH-specific knowledge worth salvaging. It
  is modified-uncommitted right now. Read it before merging, do not assume PCM's is a superset.
- **`PYTHONPATH` pinning is a preservation, not a fix.** Each base stays on its own vendored
  library variant, so a bug fixed upstream still reaches no base. Unifying them is deliberately
  deferred; the acceptance run in Phase 5 only proves the current variant still works from the kit.
- **Interpreter mismatch.** PCM's vendored `__pycache__` is cpython-314 while the shared venv is
  cpython-313, so PCM has been run under a different interpreter at some point. Stale 314 bytecode
  is ignored by a 313 run, but confirm the acceptance ingest actually uses the venv python.
- **Second machine is unverified.** Everything here is designed for portability but only ever run
  on this machine. The Phase 5 portability dry-check proves no absolute paths remain; it does not
  prove the kit runs elsewhere. First real run on the second machine is the actual test.
- **`rag_sync.ps1` snapshot paths stay per-base and machine-bound** (the Drive mount letter differs
  per machine). Not addressed here; the kit does not own backup.
- **Ollama and Docker must be present and serving the same models on the second machine.** The kit
  checks for their presence in `bootstrap.ps1` but cannot verify model parity.
- **The pinned stack will go stale.** Nothing here schedules a bump, and `torch 2.7.1+cu126` in
  particular ties the kit to a CUDA generation. Revisit when machine 2 has different hardware.
- **`bootstrap.ps1` becomes the single point of failure for a new machine.** It provisions the
  venv, installs the skills, seeds the cache and verifies the host. It is also the one component
  that by definition cannot be tested on the machine that already works — its first real exercise
  is machine 2.
- **`machine.ps1` now carries a cached hardware verdict.** `$HasCUDA` is decided once at bootstrap.
  Swapping a GPU, or reinstalling torch as cpu-only, silently invalidates it — re-run bootstrap
  after any such change. Deliberate tradeoff: probing per launch was the alternative, and probing
  cheaply (`nvidia-smi`) is what produced the wrong answer in the first place.
- **Segment boundaries are only as safe as the exit proofs.** Each segment claims both bases still
  work; that claim is only real if the stated proof is actually run before the session ends. A
  segment marked done without its proof is worse than one left unfinished.

## Out of scope

- Untracking `rag_storage` from either base's git, and any history rewrite to reclaim the 259 MB.
- Porting the enrichment agents to MECH.
- Ingesting the PCM `FOUND\` backlog beyond the single acceptance PDF.
- Raising `timeout=` / `max_retries=` on `openai_complete_if_cache` — a separate, untested
  hardening idea.
- The MinerU OCR-misread question (`Venkitaraj` → `Venkitarai`).
- Non-Windows portability. The PowerShell launcher and the `%WINDIR%\Media` wavs are
  Windows-specific by design. Portability *between Windows machines* is now in scope and handled
  in Phase 0b.
- Unifying the three divergent vendored `lightrag` packages (57–144 differing files).
  `PYTHONPATH` pinning sidesteps it; merging them is its own project.
