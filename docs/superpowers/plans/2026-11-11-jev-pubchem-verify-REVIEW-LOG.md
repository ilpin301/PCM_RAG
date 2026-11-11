# Plan Review Log: Jev PubChem same-substance check

Started 2026-11-11 (session). MAX_ROUNDS=5. Reviewer: GLM-5.3 read-only, plan file docs/superpowers/plans/2026-11-11-jev-pubchem-verify.md

## Round 1 - GLM

Read plan + code. Line refs verified: `verify_match` real at `enrich_pubchem.py:477`, selftest header at 1260, argparse block 1797-1818 with `--max-glm-tokens` at 1807 — plan's references all match. `VERIFY_SYSTEM` (449-457) wording and form-word rule match plan's `build_question` spec. Cache files are `<cid>.json` with `iupac`/`formula` keys — `load_pairs` join works. verify.json shape matches (`name -> {cid, same, by?}`). Cost math checks: 768 × 150 tok × $0.042/M ≈ $0.005.

Findings:

1. **[HIGH] Acceptance gate statistically unsound at n=33.** 0/33 false accepts → 95% upper bound on true FA rate ≈ 9.1% (rule of three). Gate declares "0 false accepts" as pass; Task 5 Step 3 then feeds that number into option (b) = auto-accept with no Claude review → up to ~9%-FA chemistry can enter graph. Worse: gold negatives are rows the GLM chain already rejected, so offline eval cannot estimate the joint GLM∧Jev FA rate option (b) actually needs (verify.json stores no `glm_same`; Claude-flipped GLM-yes rows are overwritten). Threshold sweep on same 33 rows then picking the passing `hi` = selection overfitting. Fix: report binomial upper bound next to every FA count; add ~100 synthetic hard negatives (PubChem hydrate/anhydrous, isomer, form-word-vs-wrong-compound pairs — generable for free) so 0-false gives bound ≤ ~2.5%; require max gold-negative p ≤ hi − 0.05 margin, not just count 0; state explicitly that option (b) needs Task 5 joint-FA data (shadow records `glm_same`) over enough new entities, not the offline gate alone.

2. **[MED] Circular labels: agreement-side blind spot.** Plan handles disagreement side (hand-check each, fix only with user OK — good). But Jev-says-yes ∧ Claude-said-yes ∧ both wrong is unmeasured: eval scores agreement with Claude, and hand-checks cover only disagreements. 405 gold trues never re-adjudicated. Fix: hand-check a random sample (e.g. 30) of gold trues that Jev scores ≥ hi against their PubChem record; report how many Claude labels fail.

3. **[MED] No request timeout, no circuit breaker.** `jev_same` spec has retries/backoff but no per-request timeout and no "stop after K consecutive hard failures". API down mid-collect: every entity pays 5 tries × timeout + backoff sequentially (collect loop is a serial `for`), can add hours to a live run. Fix: explicit timeout (e.g. 15 s) and disable Jev for the rest of the run after 401/missing key or 3 consecutive failures.

4. **[MED] `TYPESAFE_API_KEY` visibility in runner shells.** Task 1 Step 1 sets a user env var via console/setx; already-running Claude session and its Bash/PowerShell children do NOT inherit it until restart. pcm-PubChem-runner would run shadow with no key → silent no-op (by design) → Task 5 comparison has zero rows, live-run opportunity wasted. Fix: verify `os.environ.get` inside the same shell type the runner uses before Task 5; restart Claude session after setting, or pass key explicitly for that run.

5. **[LOW] `parse_noul` accepts out-of-range values.** Spec: None on missing/non-finite — but p = 1.7 or −0.3 passes and flows into `decide`. Fix: also reject p outside [0,1].

6. **[LOW] Coverage denominator skews easy.** Gold trues include trivial pairs ("Water"→water, "CaCO3"); live new entities are the hard tail. 50% offline coverage won't transfer. Task 5 shadow is the real transfer test — say so in the gate: option (b) judged on Task 5 coverage, not Task 3's.

7. **[LOW] pcm-PubChem-runner has no flag pass-through.** Runner inputs are MODE/LIMIT/REFRESH/EXCLUDE/VERIFY etc.; `--jev-shadow` must be spelled out as a raw flag instruction in the runner prompt or it will be dropped.

8. **[LOW] Missing selftest cases.** Task 3 selftest: no None-probability row (spec: unknown never yes — test it). Task 2: no timeout/`ConnectError` case; no non-ASCII/long-name build check despite Review Focus promising both. `usage.input_tokens` may be absent from some replies — cost line needs a default-0 guard.

9. **[LOW] Usage docstring drift.** `enrich_pubchem.py` header (lines 12-38) documents flags/exit codes; `--jev-shadow` must be added there or the doc goes stale.

Shadow-mode design itself sound: flag off = no call, no file, selftest asserts it (Task 4 Step 1, Task 6 Step 5); Jev never alters a verdict, never writes graph, never changes exit code; key never touches .env/git/logs — matches env-key-protection rule. 401/429/529/missing-key paths all specified and tested. Data sent (name, IUPAC, formula) minimal and non-sensitive. `trust_env=False` + `NO_PROXY` consistent with existing code.

Not checked: full scan of all 768 verify.json entries (438/405/33 split taken from task context, arithmetic consistent), lightrag/AGENTS.md (outside allowed file list).

VERDICT: REVISE

### Claude's response (round 1)

All 9 findings accepted, none rejected. [HIGH] 1: gate rewritten - upper bounds reported, 100 synthetic hard negatives added with hi chosen on synthetic and the 33 real negatives held out, margin 0.05, option (b) now needs 100+ shadow entities with zero joint false accepts, offline gate alone never authorises it. [MED] 2: 30-row hand-check of high-scoring gold trues added. [MED] 3: 15 s timeout and circuit breaker added. [MED] 4: key visibility step added (restart session, verify in runner shell). [LOW] 5: out-of-range p rejected. [LOW] 6: coverage judged on Task 5 data. [LOW] 7: runner flag spelled out in the task prompt. [LOW] 8: missing selftest cases added. [LOW] 9: usage docstring update added.

## Round 2 - GLM

Re-read revised plan. All prior findings checked:

**Prior [HIGH] (gate power) — resolved.** Line 24 + Task 3 Step 6: every FA count reported with 95% binomial upper bound; explicit statement that 0/33 alone does not bound below ~9%; 100 synthetic hard negatives (hydrate/anhydrous, isomer, same-element, form-word-vs-wrong-compound) → bound ~3%; real 33 negatives held out, `hi` chosen on synthetics only (kills the sweep-overfitting problem); margin rule max-negative ≤ hi−0.05; option (b) requires zero joint GLM∧Jev false accepts over ≥100 live-reviewed entities with bound, offline gate alone never authorizes (b). Sound now.

**Prior [MED]s — resolved.** (2) agreement-side blind spot → gate (iv) hand-checks 30 gold trues ≥ hi. (3) timeout/breaker → 15 s timeout, `JevBreaker` trips on 401/missing key/3 consecutive failures, selftested both modules. (4) env var visibility → restart-session instruction + verify in runner shell type + Task 5 Step 1 "confirm rows exist before trusting comparison".

**Prior [LOW]s — resolved.** Out-of-range p (selftest p=1.7/−0.3), None-prob never accepted, ConnectError/timeout case, non-ASCII/300-char names, missing `usage.input_tokens` guard, runner flag pass-through spelled out as raw instruction, usage docstring update (Task 4), coverage-skew caveat (iii).

New findings in the revision:

1. **[LOW] Key-into-chat contradiction.** Task 1 Step 1 "(or pass the key explicitly)" — passing the key to the runner means pasting it into a task prompt = into chat/transcript, which line 18 forbids ("never into logs or chat"). Fix: delete that parenthetical; restart-session is the only compliant path.

2. **[LOW] Gate (iv) has no pass criterion.** "Report how many Claude labels fail" — but what count fails the gate? Unstated. Fix: define it, e.g. any failure → investigate that row before the gate can pass.

3. **[LOW] "Same case count as before plus one" unmeasurable.** Existing selftest prints only `selftest OK`, no count. Fix: define count = number of `_selftest_*` invocations, or just expect `selftest OK` + exit 0.

4. **[LOW] Mislabeled synthetic pair fails safe, but note it.** A synthetic negative that is secretly the same substance (synonymy slip in the generator) counts as a false accept → gate fails conservatively, never unsafely. Worth one assert in the generator: paired CID must differ from the CID verify.json holds for that name.

Non-blocking context, not findings: ~100 extra synthetic calls keep cost ≈ $0.006; option (b)'s ≥100 new reviewed entities will take several ingest queues at historical 1-21 new entities per run — that is the safe direction; breaker worst case before trip ≈ 4 min added to a run (3 failures × 5 tries × 15 s), acceptable.

No [HIGH] remains. Follow-ups: items 1-4 above, in order.

VERDICT: APPROVED

### Claude's response (round 2)

VERDICT APPROVED, no HIGH remains. All 4 LOW follow-ups accepted and applied: (1) key-in-chat parenthetical removed, (2) pass criterion for the 30-row hand-check, (3) selftest expectation reworded to exit 0 plus selftest OK, (4) CID-differs assert in the synthetic generator. Converged after 2 rounds of 5.

### Post-approval edit (2026-11-11, Claude, not re-reviewed by GLM)

Task 1 Step 1 reworded because TYPESAFE_API_KEY already exists as a user env var (found via the harvester project); Step 0 added to read the harvester Jev calibration notes first. No change to the gate, thresholds or design.
