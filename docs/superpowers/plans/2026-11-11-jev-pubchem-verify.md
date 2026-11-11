# Jev PubChem Same-Substance Check Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Prove, then pilot, TypeSafe's Jev model as a cheap second opinion on the PubChem same-substance check, so Claude reviews fewer new entities without ever accepting a wrong match.

**Architecture:** One new module `lightrag/jev_verify.py` asks Jev one yes/no (Noul) question per (entity name, PubChem record) and returns a probability. An offline eval script scores it against the verdicts already in `verify.json`. A default-off `--jev-shadow` flag in `enrich_pubchem.py` records Jev next to the GLM verdict on live runs without changing any decision. Routing (letting Jev skip a review) is a separate user decision after the evidence is in.

**Tech Stack:** Python (ragkit venv), httpx (already used by `enrich_pubchem.py`), TypeSafe HTTP API `POST https://api.typesafe.ai/v1/systemone`, model alias `jev-latest`.

**Spec:** Conversation of 2026-11-11 (user asked for a plan to add Jev to the RAG process and to test everything after). Existing rule it must respect: `X:\RAG_MAIN\PCM_RAG\CLAUDE.md`, "GLM verify alone is not enough for NEW entities"; the base holds only checked, verified data.

## Global Constraints

- Jev output is a probability, not proof. No code path may write a graph change or a `same:true` verdict from Jev alone.
- `--jev-shadow` is OFF by default. With it off, behaviour and outputs of `enrich_pubchem.py` are byte-identical to today.
- Data sent to TypeSafe: entity name, PubChem IUPAC name, molecular formula only. No paper text, no paths, no personal data.
- API key comes from environment variable `TYPESAFE_API_KEY`. Never write it into `lightrag\.env` (user rule: do not modify .env keys), never into git, never into logs or chat.
- Host-side Python on this box needs `NO_PROXY=*` (system SOCKS proxy); use `httpx.AsyncClient(trust_env=False)` like the existing code.
- Concurrency: at most 4 in-flight Jev requests; retry 429 and 529 with exponential backoff, max 5 tries.
- Tests are offline and mock the network (project AGENTS.md: mock-based tests for external services; report pass counts; `ruff check` clean). Existing style is a `--selftest` flag with plain asserts; follow it.
- Pricing per docs: input about $0.042 per million tokens, output free. Budget for the full eval (768 pairs, about 150 tokens each) is about $0.005.
- Labels caveat: `by: claude-review` verdicts are Claude's judgement, not chemical ground truth. The eval measures agreement with that reviewer. Every Jev/label disagreement is re-checked by hand against the PubChem record.
- Every false-accept count is reported with its 95% binomial upper bound (rule of three: 0 of n gives about 3/n).
- Jev request timeout 15 s. Circuit breaker: Jev is disabled for the rest of a run after a 401, a missing key, or 3 consecutive hard failures, logged once.
- Shadow mode never changes a verdict, exit code or graph.

## Review Focus

- `TYPESAFE_API_KEY` missing or 401: shadow mode must log once and carry on; an ingest or enrichment run must never fail because of Jev.
- 429/529/timeouts: backoff, then record `None` (unknown); never treat unknown as yes.
- Probability exactly near 0.5: treated as undecided, never as yes.
- Form words ("Graphene Nanoparticles", "ZnO Nanofluid" vs ZnO): form words must not flip the answer; hydration or composition differences must.
- Empty IUPAC or formula (`(none)`): must not produce a confident yes.
- Non-ASCII names and very long names: request builds and parses without error.
- Cost runaway: the eval caches every answer per (name, CID, model, prompt version); a rerun costs nothing.
- Key set after the Claude session started is invisible to runner shells (silent no-op).

---

### Task 1: API smoke test and shape check

**Files:**
- Create: `lightrag/jev_smoke.py`

**Interfaces:**
- Produces: confirmed response shape (`answers[<key>].noul`), confirmed auth and proxy behaviour, recorded in the module docstring of `jev_verify.py` (Task 2).

- [ ] **Step 0:** Before writing code, read the existing Jev notes in the harvester project: `F:\____IL_AI\il-researchgate-harvester-agent\HANDOFF-JEV.md`, `PLAN-JEV-REVIEW-LOG.md` and `jev2-calibration\JEV-2-PAIRS-LABELLED.md` (a calibration of 509 labelled pairs). Note any labelling trap (e.g. preprint/journal twins mislabelled as different works), threshold findings and the API quirks (proxy bypass, error codes) that apply to this plan's Task 1-3, in 5-10 lines in the Task 1 smoke-test output or the eval report.
- [ ] **Step 1:** The key is ALREADY set as user environment variable `TYPESAFE_API_KEY` (found 2026-11-11 via the ResearchGate harvester project, F:\____IL_AI\il-researchgate-harvester-agent; its validity and credit are not yet tested - Step 3 tests it). Verify it is visible in the shell the runner uses with `python -c "import os;print(bool(os.environ.get('TYPESAFE_API_KEY')))"`, expected `True`; if `False`, restart the Claude Code session (user env vars are read at launch). Never print or copy the key.
- [ ] **Step 2:** Implement `main() -> int` in `jev_smoke.py`: one `GET /v1/models` and one `POST /v1/systemone` for 6 fixed pairs (3 true: "Aluminum"/aluminum, "Carbon Dioxide"/carbon dioxide CO2, "Graphene Oxide Nanoparticles"/graphene oxide; 3 false: "Zno/water Nanofluid" vs the water record, "Graphene Oxide" vs methane CH4, "Sodium Sulfate Decahydrate" vs anhydrous sodium sulfate). Print model id, each `noul`, `usage`. Request body: `{"model":"jev-latest","state":{"entity_name":..,"pubchem_iupac":..,"pubchem_formula":..},"questions":{"same":{"type":"noul","instructions":"..."}}}`.
- [ ] **Step 3:** Run: `$env:NO_PROXY='*'; python lightrag\jev_smoke.py` Expected: exit 0, six probabilities printed, true pairs above 0.5 and false pairs below 0.5. If the shape differs from `answers.same.noul`, fix the plan's accessor before Task 2.
- [ ] **Step 4:** Commit `jev_smoke.py` (named path only).

### Task 2: `jev_verify.py` core

**Files:**
- Create: `lightrag/jev_verify.py`

**Interfaces:**
- Produces:
  - `PROMPT_VERSION = "v1"`, `MODEL = "jev-latest"`
  - `build_state(name: str, facts: dict) -> dict` (keys `entity_name`, `pubchem_iupac`, `pubchem_formula`; missing values become the string `"(none)"`)
  - `build_question() -> dict` (Noul with `instructions` and `criteria` true/false; wording mirrors `VERIFY_SYSTEM` in `enrich_pubchem.py`: form words do not change the substance; different compound, hydration state or composition is NOT the same)
  - `parse_noul(body: dict) -> float | None` (None on any missing or non-finite value, and on values outside [0,1])
  - `async jev_same(client: httpx.AsyncClient, name: str, facts: dict) -> float | None` (15 s timeout; retry per Global Constraints; None on final failure; never raises)
  - `class JevBreaker` with `allow() -> bool` and `record(ok: bool) -> None`; trips at 3 consecutive failures or on 401/missing key; once tripped, `jev_same` makes no call and returns None
  - `decide(p: float | None, lo: float, hi: float) -> str` returning `"yes"`, `"no"`, or `"review"` (None and the middle band give `"review"`)
  - `--selftest` flag

- [ ] **Step 1:** Write the selftest first with a fake transport (`httpx.MockTransport`): asserts for `build_state` with empty IUPAC, `parse_noul` on a good body / missing key / NaN, `decide` at 0.5, `lo`, `hi` edges and None, `jev_same` retrying twice on 429 then succeeding, and returning None on 401 without raising. Also: `parse_noul` gives None for p=1.7 and p=-0.3; ConnectError/timeout gives None without raising and trips the breaker after 3; non-ASCII and 300-character names build a valid request body; a missing `usage.input_tokens` does not crash cost accounting (defaults to 0).
- [ ] **Step 2:** Run: `python lightrag\jev_verify.py --selftest` Expected: FAIL (functions not defined).
- [ ] **Step 3:** Implement the functions above in `lightrag/jev_verify.py`. Auth header `Authorization: Bearer <key>`; base URL `https://api.typesafe.ai`; one semaphore of 4 inside a module-level helper.
- [ ] **Step 4:** Run: `python lightrag\jev_verify.py --selftest; ruff check lightrag\jev_verify.py` Expected: `selftest OK`, ruff clean.
- [ ] **Step 5:** Commit.

### Task 3: Offline eval against existing verdicts

**Files:**
- Create: `lightrag/jev_eval.py`
- Output (not committed): `lightrag/data/enrich_cache/jev_eval.json`, `lightrag/data/enrich_cache/jev_eval_report.txt`

**Interfaces:**
- Consumes: `jev_verify.jev_same`, `jev_verify.PROMPT_VERSION`, `jev_verify.MODEL`.
- Produces: `load_pairs() -> list[dict]` (rows `{name, cid, same, by, iupac, formula}` from `verify.json` joined to `data/enrich_cache/<cid>.json`; skip rows with no cache file and report how many), `evaluate(rows, probs, lo, hi) -> dict` (confusion counts, coverage), and the cache file keyed `name|cid|model|prompt_version`.
- Produces: `make_synthetic_negatives(n: int = 100) -> list[dict]` (pairs an entity name with the PubChem cache record of a DIFFERENT compound: hydrate vs anhydrous, isomer, same-element different compound, form-word name with the wrong compound; labelled `same=false` by construction; assert that the paired CID differs from the CID `verify.json` holds for that entity name, so a synonym slip cannot create a mislabelled negative; seeded, reproducible; stored in `jev_eval.json` under key `synthetic`) and `upper_bound(k: int, n: int) -> float` (95% binomial upper bound on a false-accept rate).

- [ ] **Step 1:** Selftest (`--selftest`, no network): fixture of 6 rows with fixed probabilities; assert that `evaluate` counts a `same:false` row with `p >= hi` as a **false accept** and a `same:true` row with `p <= lo` as a **false reject**, and computes auto-accept coverage = share of `same:true` rows with `p >= hi`. Also: a `None`-probability row is never counted as accepted; `upper_bound(0, 33)` is about 0.091 and `upper_bound(0, 100)` about 0.030; `make_synthetic_negatives` is reproducible for a fixed seed and every row has `same=false`.
- [ ] **Step 2:** Run selftest, expect FAIL. Implement. Run, expect `selftest OK`.
- [ ] **Step 3:** Build the synthetic hard-negative set (`make_synthetic_negatives(100)`) and store it in `jev_eval.json` under `synthetic`. Selection protocol: choose `hi` on the synthetic set only; the 33 real gold negatives are held out and only reported.
- [ ] **Step 4:** Run the eval live: `$env:NO_PROXY='*'; python lightrag\jev_eval.py --run` Expected: 768 pairs scored (minus reported skips), cost line from `usage.input_tokens`, cache written. A second run makes zero API calls.
- [ ] **Step 5:** Report in `jev_eval_report.txt`: score histogram, a threshold sweep (`hi` 0.6 to 0.99), and three tables: gold = 438 `claude-review` rows (405 true, 33 false); secondary = 330 GLM-only rows (agreement only, not gold); every disagreement listed with name, IUPAC, formula, label, p.
- [ ] **Step 6:** Acceptance gate (all must hold, else stop and report; Jev stays shadow-only or is dropped):
  - (i) 0 false accepts on the held-out 33 real gold negatives AND on the 100 synthetic negatives at the chosen `hi`, each reported with its 95% upper bound (about 9% for n=33, about 3% for n=100). State plainly in the report: 0 of 33 alone does NOT bound the true false-accept rate below about 9%.
  - (ii) the highest score among all negatives (real and synthetic) is at most `hi` minus 0.05
  - (iii) auto-accept coverage on the 405 gold `same:true` rows at that `hi`: **at least 50%** (only an offline estimate; trivial pairs like Water skew it high)
  - (iv) hand-check a random sample of 30 gold trues that Jev scores at or above `hi` against their PubChem records; report how many Claude labels fail. Pass criterion: every label that fails the check must be investigated and resolved by hand with the cause noted before the gate can pass; two or more wrong labels in the 30 means stop and re-audit the labels before any other conclusion
  - every disagreement hand-checked against its PubChem record and the outcome noted in the report (a label that proves wrong is fixed in `verify.json` only with the user's OK)
- [ ] **Step 7:** Commit the two scripts (not the cache or report).

### Task 4: Shadow mode in `enrich_pubchem.py`

**Files:**
- Modify: `lightrag/enrich_pubchem.py` (argparse block near the `--max-glm-tokens` flag; `verify_match` at line ~477; selftest section from line ~1260)
- Output: `lightrag/data/enrich_cache/jev_shadow.json`

**Interfaces:**
- Consumes: `jev_verify.jev_same`, `jev_verify.decide`, `jev_verify.JevBreaker`.
- Produces: flag `--jev-shadow` (store_true, default False), also added to the usage docstring at the top of `enrich_pubchem.py` (flags/exit codes list, near lines 12-38); after each `verify_match` that returns a verdict, if the flag is set and the breaker allows, call `jev_same` and write `{name: {"cid": cid, "p": p, "glm_same": bool, "model": MODEL, "pv": PROMPT_VERSION}}` to `jev_shadow.json`. `glm_same` is the GLM verdict.

- [ ] **Step 1:** Add a selftest case `_selftest_jev_shadow`: with the flag off, `verify_match` makes no Jev call and `jev_shadow.json` is untouched; with the flag on and a stubbed `jev_same` returning 0.91 then None, the file records `p=0.91` and `p=null`, and the returned GLM verdict is identical in both runs. Also: a tripped breaker makes no further `jev_same` calls and the verdicts still match.
- [ ] **Step 2:** Run `python lightrag\enrich_pubchem.py --selftest` Expected: FAIL on the new case.
- [ ] **Step 3:** Implement. Jev errors are caught and logged once per run; the verdict returned to callers is never altered.
- [ ] **Step 4:** Run `python lightrag\enrich_pubchem.py --selftest; ruff check lightrag\enrich_pubchem.py` Expected: all earlier cases still pass, new case passes, ruff no new findings.
- [ ] **Step 5:** Commit.

### Task 5: Live shadow run and decision gate

**Files:**
- Read: `lightrag/data/enrich_cache/jev_shadow.json`, `verify.json`

- [ ] **Step 1:** On the next ingest queue, run the PubChem collect with `--jev-shadow` (pcm-PubChem-runner, MODE=collect). The runner has no flag pass-through, so the task prompt must spell out the raw instruction: "append `--jev-shadow` to the enrich_pubchem.py collect command". Confirm in `jev_shadow.json` that rows exist before trusting the comparison. Keep the normal GLM verify and Claude review exactly as today.
- [ ] **Step 2:** After Claude's review of the new entities, compare: for every newly reviewed entity, Jev `decide(p, lo, hi)` vs the final `same`. Report counts: would-auto-accept and correct, would-auto-accept and WRONG, would-review.
- [ ] **Step 3:** Decision gate for the user (no code change before this). Option (a): Jev only reorders the review queue (zero risk); available once the Task 3 gate passes. Option (b): Jev may skip Claude review when GLM and Jev both say yes with `p >= hi`; requires, from shadow data, zero joint false accepts (GLM yes AND Jev at or above `hi` AND final Claude verdict no) over at least 100 newly reviewed entities accumulated across queues, reported with the upper bound (about 3% at 100). Until then only option (a). The offline Task 3 gate alone never authorises (b). Coverage for (b) is judged on Task 5 data, not Task 3. Option (b) changes the CLAUDE.md rule "GLM verify alone is not enough for NEW entities" and needs the user's explicit OK to edit it. Routing code is a follow-up plan, not part of this one.

### Task 6: Test everything

- [ ] **Step 1:** `python lightrag\jev_verify.py --selftest` Expected `selftest OK` (includes out-of-range p, timeout/breaker, non-ASCII/300-char names, missing `usage.input_tokens`); report the pass count.
- [ ] **Step 2:** `python lightrag\jev_eval.py --selftest` Expected `selftest OK` (includes None-probability never accepted, `upper_bound` values, synthetic-set reproducibility); report the pass count.
- [ ] **Step 3:** `python lightrag\enrich_pubchem.py --selftest` Expected exit 0 and the line `selftest OK`; report the pass count.
- [ ] **Step 4:** `ruff check lightrag\jev_verify.py lightrag\jev_eval.py lightrag\enrich_pubchem.py` Expected no findings.
- [ ] **Step 5:** Regression: run `enrich_pubchem.py --dry-run --limit 5` without `--jev-shadow`; `jev_shadow.json` must not be created or changed (compare mtime and size before and after).
- [ ] **Step 6:** Failure path: unset `TYPESAFE_API_KEY`, run a 5-entity collect with `--jev-shadow`; run must exit 0 with one logged Jev warning and unchanged verdicts.
- [ ] **Step 7:** `python lightrag\enrich_pubchem.py --scan-leaks` Expected exit 0 (this work touches no graph data).
- [ ] **Step 8:** Report pass counts, the eval report path, the eval cost, and the Task 5 comparison to the user.

## Out of scope (YAGNI, separate plans if wanted)

OpenAlex citation matching, the 4500-number unit audit, query-time reranking, and any Jev write path into the graph.
