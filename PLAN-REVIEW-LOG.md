# Plan Review Log: Universal RAG toolkit (ragkit) + ingest sound notifications

Act 1 (grill) complete — plan locked with the user. MAX_ROUNDS=5.

## Round 1 — GLM

Review done. Read PLAN.md, both wrappers, rag_ingest.py, ingest_merged.py, check_vectors, repair_vdb, triage, compose files, .env keys, and diffed the vendored `lightrag` packages. Findings:

## [HIGH] — blockers

**1. Moving the python out of the clone dir silently changes which `lightrag` code runs.**
`rag_ingest.py` does `from lightrag.llm.openai import ...` etc. Today the script lives in `<base>\lightrag\` (the clone root), so `sys.path[0]` makes the base's **vendored** `lightrag\lightrag\` package shadow the venv. Measured:
- PCM vendored vs MECH vendored: **61 differing .py files**
- PCM vendored vs venv site-packages (`lightrag_hku-1.5.4`): **142 differing .py files**
- PCM's `__pycache__` is cpython-**314**, venv is cpython-**313** — PCM has run on a different interpreter than the shared venv at some point.

After the move to `ragkit\`, `import lightrag` resolves to the venv install — a third code variant the three monkey-patches (`_rebuild_role_llm_funcs`, asdict redirect, separate_content filter) were never tested against. This also falsifies the plan's feasibility claim "the per-base divergence is four variables" — the runtime library is a fifth, bigger one.
Fix: `ingest.ps1` sets `$env:PYTHONPATH = "$Root\lightrag"` before invoking python (preserves today's per-base resolution), and one acceptance run per base before deleting the old copies.

**2. Nobody owns `docker compose stop`.**
`rag_ingest.py`'s own docstring: "stop the Docker LightRAG container before running (shared storage)". Both current wrappers only `docker compose start` at the end — the stop currently lives in the skill flow, off-plan. The plan sells `ingest.ps1` as *the* universal entrypoint, and its spec (step 6) plus the new skill discovery step (step 9) never mention stopping the container. Direct-storage writes while the server container is up = concurrent JSON storage writes = corruption/data loss. Worse for a *new* base whose operator only knows the launcher.
Fix: `ingest.ps1` itself runs `docker compose stop` in `$Root\lightrag` as its first act (and keeps the trailing `start` in both branches, as today).

## [MED]

**3. `-Merged` + multi-line `-ListFile` is undefined.** `ingest_merged.py` takes exactly one `<source.pdf>`. Plan makes `-ListFile` unconditional but never says what `-Merged` does with 2+ lines. Fix: launcher rejects `-Merged` when the list has >1 entry (or loops per file, explicitly).

**4. Step 11's grep scans only `~\.claude\skills\*`.** Project skills win over global; a missed deletion silently shadows the new global skill forever. The plan *knows* this (Risks section says "add an explicit check") but never adds it as a step. Fix: add step: `Get-ChildItem <each base>\.claude\skills` must show no RAG skill folders.

**5. Phase 0 commit inventories are stale and over-broad.** Plan says "12 tracked files + 3 untracked `repairs/` scripts"; current status shows 5 modified, 2 deleted, and untracked `.obsidian/`, `FOUND/no-ENG/`, `IN/*.pdf`. "Commit as-is" (`git add -A` style) sweeps `.obsidian/` and stray PDFs into the repo permanently. Fix: enumerate files in the commit step; `.gitignore` `.obsidian/`.

**6. `Media.SoundPlayer` may not resolve under PowerShell 7.** It lives in `System.Windows.Extensions`, which pwsh doesn't load by default (works in Windows PowerShell 5.1). The try/catch would swallow it and silently degrade to beep on every success — the exact "good ingest looks like failure-adjacent" confusion the plan tries to avoid. Fix: `Add-Type -AssemblyName System.Windows.Extensions` at top of `notify.ps1`, or verify once under the pwsh version that will actually run the launcher.

## [LOW] — non-blocking follow-ups

- **7.** PCM's wrapper assumes `LOG\` exists (no `New-Item`); MECH's creates it. Universal launcher must `New-Item -ItemType Directory -Force "$Root\lightrag\LOG"` — a brand-new base won't have it.
- **8.** PCM's `.env` contains **both** `ZAI_API_KEY` and `LLM_BINDING_API_KEY`. Auto-detect needs a precedence rule if both exist and diverge.
- **9.** `repairs\resync_chunks_count.py` isn't in the move list while its sibling `repair_vdb.py` is — decide explicitly, don't leave it orphaned in a base whose tooling "lives in ragkit".
- **10.** `docker compose start`/`stop` must run with cwd `$Root\lightrag` — plan implies but never states `Set-Location $Root\lightrag` in the launcher.

The plan is otherwise solid: evidence-based deltas, correct poison-gate/EXITCODE semantics, sound failure-branch retention, well-reasoned tradeoffs (list-file, sounds-on-decision-only, own-repo). Findings 1 and 2 are genuinely load-bearing and both have one-line fixes — revise and re-run.

VERDICT: REVISE

### Claude's response — Round 1

**Accepted and applied (both HIGH, independently verified before accepting):**
- [HIGH-1] vendored-library shadowing. Verified: PCM vendored `lightrag/` vs venv `lightrag_hku` = 144 differing files; PCM vendored vs MECH vendored = 57. Applied GLM's fix (`$env:PYTHONPATH = "$Root\lightrag"`), plus an Evidence bullet, a Key-decision bullet, an explicit Risk bullet noting this preserves rather than fixes the divergence, and an Out-of-scope bullet for unification.
- [HIGH-2] container stop. Verified: `rag_ingest.py:4-5` docstring requires it; neither wrapper does it. Launcher now owns `Set-Location $Root\lightrag` + `docker compose stop` first, `start` at the end of both branches.
- [MED-3] `-Merged` with a multi-line list file — launcher now rejects it.
- [MED-4] project-vs-global skill shadowing — promoted from a Risk note to Phase 2 step 12, an actual verification step.
- [MED-5] stale commit inventory — replaced with an explicit-enumeration instruction and a `.gitignore` entry for `.obsidian/`.
- [LOW-7] `LOG\` dir creation, [LOW-8] key precedence (`ZAI_API_KEY` wins), [LOW-9] `resync_chunks_count.py` decision, [LOW-10] `Set-Location` — all applied.

**Rejected, with reason:**
- [MED-6] `Media.SoundPlayer` unavailable under PowerShell 7. Tested on this machine: `pwsh -NoProfile -c 'New-Object Media.SoundPlayer "C:\Windows\Media\Ring10.wav"'` returned `SOUNDPLAYER-OK`. The `Add-Type -AssemblyName System.Windows.Extensions` shim would be dead code. The existing try/catch + beep fallback already covers the case if a future pwsh build regresses. Recorded as measured evidence in the plan rather than as a step.

**Also fixed, not from GLM:** the Evidence section's closing sentence still claimed "four variables" after the fifth was documented. Now says five, four derivable + one pinned.

## Round 2 — GLM

Re-review done. Prior findings vs revision:

| Prior finding | Status |
|---|---|
| [HIGH] vendored `lightrag` shadowing / import swap | **Fixed** — step 6 pins `$env:PYTHONPATH = "$Root\lightrag"`, evidence bullet added with measured counts, tradeoff + risk entries added. Ordering is correct: ragkit dir (sys.path[0]) contains no `lightrag` package, PYTHONPATH precedes site-packages, so per-base vendored package still wins. `ingest_merged.py`'s isolated subprocess re-invocation inherits the env, so the pin propagates. |
| [HIGH] unowned `docker compose stop` | **Fixed** — step 6: `Set-Location` first, launcher owns stop, `start` at end of both branches, plus tradeoff entry. |
| [MED] `-Merged` + multi-entry list | **Fixed** — explicit reject with clear message. |
| [MED] project-skill shadow not checked | **Fixed** — new step 12. |
| [MED] Phase 0 commit sweeps | **Fixed** — enumerate files on both bases, `.gitignore` `.obsidian/`. |
| [MED] SoundPlayer under pwsh 7 | **Dropped** — your machine test beats my hedged concern; plan documents the verification. |
| [LOW] LOG dir creation | **Fixed** — `New-Item -Force`. |
| [LOW] dual-key precedence | **Fixed** — `ZAI_API_KEY` wins. |
| [LOW] `Set-Location` for compose | **Fixed** — stated first action. |
| [LOW] `resync_chunks_count.py` | **Partially** — flagged in Risks ("decide explicitly at move time") but still no decision. |

Nothing new broken by the revision — I re-checked the PYTHONPATH interaction with `sys.path[0]`, the subprocess re-entry in `ingest_merged.py`, and the compose stop/start ordering. Sound.

Remaining non-blocking follow-ups:

- **[LOW]** `resync_chunks_count.py` still undecided. Pick at move time: into `ragkit` or explicitly deleted/left with a note.
- **[LOW]** Step 15 edits MECH's `.gitignore` whitelist to remove departing files, but steps 16–17 create `INGESTED_SOURCES.txt` and `CLAUDE.md` in a repo whose `.gitignore` is a whitelist — verify those two land inside the whitelist or they'll be silently untracked (and the ledger, the re-ingest guard, becomes unversioned).
- **[LOW]** `docker compose stop` when Docker Desktop isn't running errors noisily even though "container already down" is the desired state — have the launcher tolerate that specific failure so a healthy ingest can't look failed at step one.

VERDICT: APPROVED

### Non-blocking follow-ups (carried, all three folded into the plan)

- [LOW] resync_chunks_count.py — decided: NOT moved to ragkit. chunks_count is cosmetic, nothing reads it at query time. Noted in ragkit README.
- [LOW] MECH .gitignore is a whitelist, so the new INGESTED_SOURCES.txt and root CLAUDE.md would be silently untracked. Plan now adds the explicit whitelist entry and a git check-ignore verification.
- [LOW] docker compose stop errors when Docker Desktop is down, though "already down" is the wanted state. Launcher now tolerates that specific failure.

### Resolution

APPROVED at round 2 of 5. Awaiting user sign-off before any code.

## Round 3 — GLM

(Plan was substantially revised before this round: the user added a cross-machine portability requirement, and I closed three future-base gaps found in my own audit.)

Re-review done. Prior findings: all still addressed (PYTHONPATH pin + no-vendored case, launcher-owned `docker compose stop` + daemon-down tolerance, `-Merged` reject, project-skill shadow check, enumerated Phase 0 commits, LOG dir, key precedence, MECH gitignore whitelist with `git check-ignore`, `resync_chunks_count.py` decided). `EMBEDDING_DIM` fix is correct — hardcode at `check_vectors.py:22` confirmed, fail-loud is the right call given the gate folds into `$ec`.

Now the portability design. It has two structural holes:

## [HIGH]

**1. Nothing provisions the venv on the second machine.**
`bootstrap.ps1` "autodetects the venv" — on machine 2 there is no venv to autodetect. A venv is not clonable: `pyvenv.cfg` and the console-script shims embed absolute paths to the base interpreter; a copied venv breaks. So machine 2 needs `python -m venv` + full dependency install — and the kit pins nothing. No requirements file, no versions. A fresh `pip install lightrag-hku raganything` grabs *latest*, not the 1.5.4 / 1.3.1 the three monkey-patches target (patch #1 hooks a private asdict call path, patch #2 a private method — both version-fragile). The bases' vendored `lightrag` trees travel with the base repos, but raganything, mineru, torch+cuda do not exist outside this machine's venv. Without this, nothing runs on machine 2 — the new core goal is blocked, not just unverified.
Fix: bootstrap.ps1 creates the venv from a pinned `ragkit\requirements.txt` (`lightrag-hku==1.5.4`, `raganything==1.3.1`, mineru, torch) — detect-then-create, autodetect only as skip-if-present.

**2. The global skills have no distribution path.**
Phase 2 writes six skills to `~\.claude\skills\` — on this machine only. They live in neither the kit repo nor any base repo. Distribution to machine 2 is specified as "git clone the kit, run bootstrap" — which delivers the launcher but zero skills. Half the deliverable (the thing with the ~50 rewritten references) simply doesn't arrive. "A new base needs zero setup" fails on machine 2 at the first skill invocation.
Fix: keep the six skills in the kit repo under `ragkit\skills\`; bootstrap installs them (copy or junction) into `~\.claude\skills\`.

## [MED]

**3. Guard ordering leaves the container stopped.** Step 6 fixes the order as `Set-Location` → `docker compose stop` → everything else, with `docker compose start` "at the end of both branches". A guard throw (empty list, missing key, missing `EMBEDDING_DIM`) is neither branch — script dies after the stop, base's server sits down until someone notices. Fix: run all input guards *before* the stop; stop only once the invocation is committed to running.

**4. Step 27's grep misses forward-slash absolutes.** Pattern `[A-Z]:\\` only catches `F:\...`. `repair_vdb.py` *today* uses `BASE = "F:/____IL_AI/..."` — forward slashes sail through the dry-check. UNC paths too. Fix: broaden to `[A-Za-z]:[\\/]` plus literal `____IL_AI` and `\\\\` UNC, or the check proves nothing.

**5. Cold tiktoken cache on machine 2.** `TIKTOKEN_CACHE_DIR = $env:TEMP\data-gym-cache` removes the path hardcode but machine 2 starts with an empty cache — and the existing wrapper's own comment says the download "times out on the SOCKS proxy machine". First ingest on a similarly-proxied machine dies on a known issue. Fix: bootstrap seeds the cache dir (copy from machine 1) or at minimum warns.

## [LOW]

**6.** `nvidia-smi` present ≠ working CUDA (driver without CUDA runtime, cpu-only torch in venv). Selection of `cuda` then crashes parse — visible, so acceptable, but bootstrap verifying `torch.cuda.is_available()` via the venv python is one line stronger.

**7.** `RAGKIT_HOME` set user-level won't reach already-running Claude sessions or detached wrappers until restart — bootstrap's printout should say "restart shells".

**8.** Scratch-base step overclaims slightly: it exercises guards and discovery, never the venv-fallback python path (no real ingest). Cheap completion: run `ingest_merged.py --self-test` and a `check_vectors.py` dry parse against the scratch base — both are ingest-free and would exercise PYTHONPATH resolution end to end.

Prior round's leftover LOWs (MECH whitelist — now fixed; docker-stop tolerance — now fixed) are closed. The two HIGHs are both one-design-step fixes inside `bootstrap.ps1`; everything else is sound.

VERDICT: REVISE

### Claude's response — Round 3

**Accepted and applied — all 8 findings. Both HIGHs verified independently first:**
- [HIGH-1] no venv provisioning on machine 2. Verified: `pyvenv.cfg` records `home = C:\Python\Python313`, so the venv is not clonable; installed stack measured as `lightrag-hku 1.5.4`, `raganything 1.3.1`, `mineru 3.4.2`, `torch 2.7.1+cu126`; no pin file exists in the kit's future home. Applied: new `ragkit\requirements.txt` step, and `bootstrap.ps1` rewritten to CREATE the venv from the pin rather than merely detect one.
- [HIGH-2] skills have no distribution path. Verified by reading the plan's own Phase 2 — the six skills were written only to `~\.claude\skills\`, a user-profile directory no `git clone` reaches. Applied: skills are now authored in `ragkit\skills\` (in the kit repo) and installed by bootstrap; `~\.claude\skills\` is an install target, never the source of truth.
- [MED-3] guard ordering. Correct and important: guards threw AFTER `docker compose stop`, and a throw is in neither branch, so the trailing `start` never ran and the base's server stayed down. Guards now run before the stop.
- [MED-4] portability grep too narrow. Verified: `repair_vdb.py:10` is `BASE = "F:/____IL_AI/PCM_RAG/lightrag/data/rag_storage"` — forward slashes, which a `[A-Z]:\` pattern misses entirely. Pattern broadened to both slash directions, UNC, and the literal `____IL_AI`.
- [MED-5] cold tiktoken cache on machine 2 — bootstrap now seeds or warns.
- [LOW-6] `torch.cuda.is_available()` rather than `nvidia-smi` presence — applied.
- [LOW-7] restart-shells note in bootstrap output — applied.
- [LOW-8] scratch-base step overclaimed — now also runs `ingest_merged.py --self-test` and a `check_vectors.py` dry parse, so it exercises PYTHONPATH resolution and the EMBEDDING_DIM read rather than only argument guards.

**Rejected:** none this round.

**Note on provenance:** both HIGHs were created by the cross-machine requirement that arrived after round 2, not missed in earlier rounds.

## Round 4 — GLM

All eight round-3 findings verified fixed:

| # | Status |
|---|---|
| venv provisioning | Fixed — requirements.txt from `pip freeze` with measured version-stack evidence, bootstrap creates-then-installs, "autodetect = skip-if-present" stated |
| skills distribution | Fixed — authored in `ragkit\skills\`, `~\.claude\skills\` is install target only, tradeoff entry added |
| guard ordering | Fixed — "all input guards first", with the leaves-server-down rationale spelled out |
| portability grep | Fixed — both slashes, UNC, literal `____IL_AI`, with the `repair_vdb.py:10` forward-slash evidence |
| tiktoken seed | Fixed — seed-or-warn in bootstrap |
| CUDA check | Fixed in bootstrap — `torch.cuda.is_available()` |
| restart note | Fixed |
| scratch test | Fixed — `--self-test` + check_vectors dry parse added |

Prior rounds' fixes all still intact — I re-checked PYTHONPATH pin, stop/start ownership, `-Merged` reject, project-skill shadow check, MECH gitignore whitelist, docker-stop tolerance, enumerated commits.

The edits introduced two inconsistencies and left one spec hole, none blocking:

- **[MED] CUDA derivation is now split-brained.** Bootstrap verifies via `torch.cuda.is_available()`, but Phase 0b (line 102) and the launcher env block (line 176) still derive `MINERU_DEVICE_MODE` from *nvidia-smi presence*. On the exact machine that motivated your fix — driver present, cpu-only torch — bootstrap warns, the operator proceeds, and the launcher still selects `cuda` and crashes at parse. Fix: bootstrap writes `$HasCUDA` into `machine.ps1` at verification time; the launcher reads it instead of probing (stays inside the two-facts contract — machine.ps1 *is* the designated file).
- **[MED] Bootstrap doesn't pin the interpreter.** Machine 2's default `python` could be 3.12/3.14; a `pip freeze` taken from a 3.13 venv may not resolve identically on another minor (wheels absent, deps re-resolve — and the stack is exactly what the monkey-patches are fragile against). Fix: bootstrap verifies Python 3.13.x and fails loudly otherwise.
- **[MED] "check_vectors.py dry parse" against the scratch base is undefined behavior.** The scratch base has no `data\rag_storage` at all — the script may crash on missing files rather than "dry parse". Fix: spec the expected outcome (exit 0 with "0 records" on empty/absent store) and accept that this may be a few lines of new code in check_vectors, not just an invocation.

Non-blocking [LOW] follow-ups:

- `ingest_merged.py --self-test` still imports `rag_ingest`, which reads `ZAI_API_KEY` at module import — the scratch-base self-test invocation must export the key or it dies before testing anything. One line in step 27.
- Steps 13 and 28 grep the *install target* (`~\.claude\skills\`). On this machine a junction makes that identical to the source, but grep `ragkit\skills\` too — that's the truth — and have bootstrap overwrite stale skill folders on re-install.
- Nobody is tasked with putting the tiktoken seed *into* the kit. Add to Phase 1/2: copy machine 1's `data-gym-cache` into the kit once (it's a few MB of `.tiktoken` files).
- Sequencing: bootstrap (step 9) installs skills authored in step 11 — state explicitly that machine 1's bootstrap run happens after Phase 2 and before Phase 5 acceptance.

Design is now internally consistent on the two-per-machine-facts rule, and the risk section honestly bounds what the acceptance does and doesn't prove.

VERDICT: APPROVED

### Claude's response — Round 4

APPROVED at round 4 of 5. All three [MED] and all four [LOW] follow-ups were folded in anyway rather than deferred — they were cheap and two of them were inconsistencies my own round-3 edits introduced.

- [MED] CUDA split-brain. Correct and self-inflicted: my edits left bootstrap verifying via `torch.cuda.is_available()` while Phase 0b and the launcher still derived the mode from `nvidia-smi` presence. Resolved GLM's way — bootstrap decides once and writes `$HasCUDA` into `machine.ps1`; the launcher reads it and never probes. Stays inside the two-facts contract because `machine.ps1` is the designated per-machine file.
- [MED] interpreter not pinned. Bootstrap now verifies Python 3.13.x before creating the venv.
- [MED] `check_vectors.py` "dry parse" undefined on a scratch base. Measured directly: against an absent store it prints all three stores `missing` and exits **3**, not 0. That is the correct answer for a base that has ingested nothing, so the fix is a spec line stating the expected outcome — no new code in `check_vectors.py`. The run still proves what it was added to prove, because `PYTHONPATH` resolution and the `EMBEDDING_DIM` read both happen before the store check.
- [LOW] `--self-test` imports `rag_ingest`, which reads `ZAI_API_KEY` at import — the scratch invocation must export one.
- [LOW] both greps hit the install target only; they now also grep `ragkit\skills\`, and bootstrap overwrites stale skill folders rather than merging.
- [LOW] nobody owned putting the tiktoken seed INTO the kit — now an explicit item in the move list.
- [LOW] sequencing: bootstrap installs skills authored in Phase 2, so on machine 1 it runs after Phase 2 and before Phase 5.

**Rejected:** none.

## Resolution

APPROVED at round 4 of MAX_ROUNDS=5. Four rounds, 25 findings total (4 HIGH, 10 MED, 11 LOW) — 10 in round 1, 0 new in round 2, 8 in round 3, 7 in round 4 — one rejected with measured evidence (`Media.SoundPlayer` under pwsh 7), the rest applied. Awaiting user sign-off before any code.
