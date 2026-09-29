# Plan Review Log: Shape 1 — PubChem enrichment of PCM_RAG
Act 1 (grill) complete — plan locked with the user. MAX_ROUNDS=5.

## Round 1 — GLM

Plan reviewed against live code in `lightrag/lightrag/` (networkx backend). Findings:

**[HIGH] Enumeration silently truncated.** Plan step 1 uses `GET /graphs?label=*&max_nodes=5000` as a complete enumeration AND the RMW read. But `networkx_impl.py:511` does `max_nodes = min(max_nodes, self.global_config.get("max_graph_nodes", 1000))` and `config.py:510` defaults `MAX_GRAPH_NODES=1000`. Graph has 1376 nodes → top-1000-by-degree returned, 376 dropped, response flag `is_truncated` never checked. Low-degree obscure compounds (exactly your enrichment targets) are the ones cut, and the plan would report success while silently missing them.
Fix: either raise `MAX_GRAPH_NODES` (one server restart — conflicts with "server stays up" claim, so state it), add an HTTP route over `get_all_nodes()` (networkx_impl.py:665), or read the persisted `graph_chunk_entity_relation.*` storage file directly; always check `is_truncated` and hard-fail if set.

**[MED] Stale RMW read → clobber.** `aedit_entity` REPLACES `description` wholesale (it does not merge). Plan reuses the step-1 description as the base, which can sit for minutes/hours while the judge + PubChem phases run. Any WebUI/manual edit in between is overwritten and lost.
Fix: fetch a fresh per-node description immediately before each write — `/graphs?label=<name>&max_depth=1` returns the node's current `properties`. Separate "enumerate candidates" from "RMW read per node".

**[MED] Fuzzy-match rule unimplemented (plan's own open question).** Step 3's "require the returned CID's IUPAC/synonym set to fuzzy-match" has no concrete rule. Too loose → wrong compound poisons the graph; too strict → drops valid CIDs. PubChem `/name/` lookup is fuzzy and returns a list (you take `cid[0]`).
Fix: exact normalized-lowercase match of the query name against the resolved CID's IUPAC name OR containment in its synonym list; else drop and log "unresolved".

**[MED] Strip-regex must be DOTALL-anchored or idempotency breaks.** Block replacement assumes single-line content. pug_view melting-point strings can contain newlines; a value containing `<!--PUBCHEM_...-->` or a newline defeats a non-DOTALL strip → blocks stack on re-run and the marker skip-check then falsely reports "done".
Fix: `re.sub(r'<!--PUBCHEM_START-->.*?<!--PUBCHEM_END-->', '', desc, flags=re.DOTALL)`.

**[MED] Melting-point value selection undefined.** pug_view `Melting Point` section returns multiple values across °C/°F/K, ranges, and "decomposes". Plan says "best-effort" with no pick rule → risk of injecting a decomposition temp or Fahrenheit value as "the" melting point.
Fix: take first numeric value whose unit is °C; else write "not available"; never guess.

**[MED] PubChem volume may trip the 5-min budget.** Official limits: 5 req/s AND 400 req/5min/IP. Confidence check adds a synonyms call not counted in the "4 calls/compound"; ~96 compounds × ~5 ≈ 480 → possible 403/blocks. No User-Agent/`From` header specified.
Fix: count every call against both budgets, honor `Retry-After`, set a descriptive User-Agent + email header, back off on 503.

**[LOW] Goal mentions enthalpy; implementation fetches only melting point.** PubChem rarely carries ΔHfusion (that's OpenAlex/DIPPR territory).
Fix: drop "enthalpy" from the goal or explicitly note PubChem ≠ source.

**[LOW] name→CID 404 not handled.** Names with no CID return PUG 404; must map to "unresolved", not crash the run.
Fix: catch 404 → log unresolved → continue.

**[LOW] Judge concurrency stated two ways.** Step 2 says "batch", Risks says serial/sem≤2; z.ai 1305 is concurrency (per memory `project_zai_429_behavior`), so "batch" risks flooding.
Fix: state `asyncio.Semaphore(2)` (≤2), serial fallback; cache verdicts.

**[LOW] Resumability depends on the capped enumeration.** Skip-check reads the marker from descriptions found via step 1 — same truncation as [HIGH] makes enriched-but-cut nodes invisible on resume. Subsumed by the [HIGH] fix.

Non-blocking follow-ups remain (the MED/LOW items above). [HIGH] #1 unresolved → core goal can silently under-deliver.

VERDICT: REVISE

### Claude's response
Accepted all findings — every one verified against live code and legitimate.
- [HIGH] enumeration cap: VERIFIED (networkx_impl.py:511 caps at min(max_nodes, MAX_GRAPH_NODES=1000); graph has 1786 nodes). Fix: enumerate from graphml file directly instead of /graphs; only names/types taken so staleness is moot. (GLM's node count said 1376; actual is 1786 — flaw stands, just larger.)
- [MED] stale RMW clobber: accepted — step 5 now re-reads each node's description fresh via /graphs?label=<name> immediately before write.
- [MED] fuzzy-match rule: accepted — concrete rule = normalized-lowercase query name exact-matches IUPAC OR is in synonym list, else drop+log.
- [MED] DOTALL strip: accepted — regex now flags=re.DOTALL.
- [MED] melting-point pick: accepted — first numeric °C value / convert / range-low / else "not available".
- [MED] PubChem 400/5-min budget: accepted — throttle both limits, Retry-After, User-Agent + From header; note synonyms call adds a 5th call/compound.
- [LOW] enthalpy: accepted — dropped from goal, stated PubChem is not a ΔHfus source.
- [LOW] 404 handling: accepted — 404 → unresolved, continue.
- [LOW] judge concurrency: accepted — stated Semaphore(2), serial fallback.
- [LOW] resumability: subsumed by the [HIGH] graphml-enumeration fix.
Nothing rejected.

## Round 2 — GLM

Re-review done. Prior findings first, then new.

## Round-1 findings — status

- **[HIGH] enum truncation → RESOLVED & verified.** Reads `graph_chunk_entity_relation.graphml` directly. File exists (`lightrag/data/rag_storage/...`), is `.graphml` (networkx_impl.py:155 `graph_{namespace}.graphml`), uncapped. Verified node count **1786** and `naturalobject` **91×** — both match the plan's grounded claims. API cap bypassed.
- **[MED] stale RMW → RESOLVED.** Fresh per-node read via `/graphs?label=<name>&max_depth=1`. Verified: even degree-0 nodes are returned (BFS seeds the node unconditionally, networkx_impl.py:565), so no silent skip.
- **[MED] fuzzy-match rule → RESOLVED.** Concrete: exact normalized-IUPAC OR synonym-list membership.
- **[MED] DOTALL strip → RESOLVED.** Regex pinned with `re.DOTALL`.
- **[MED] melting-point pick → RESOLVED.** First °C numeric, convert °F/K, range→low, decomposes→"not available".
- **[MED] PubChem budget → ADDRESSED but see new [MED] below.**
- **[LOW] enthalpy → RESOLVED.** Dropped, noted as DIPPR/literature.
- **[LOW] name→CID 404 → RESOLVED.** 404→unresolved→continue.
- **[LOW] judge concurrency → RESOLVED.** `Semaphore(2)`, serial fallback.
- **[LOW] resume-vs-cap → RESOLVED** (graphml uncapped; single-node fresh read for skip-check).

No [HIGH] remains.

## New findings (introduced by revision)

**[MED] Rate-limit spec is self-contradictory (won't meet 400/5-min as written).** Plan keeps `sleep(0.25)` (=4 req/s) for the ≤5/s cap AND says "throttle to stay under 400/5-min." ~480 calls at 4/s land ~480 in the first ~120s window → exceeds 400/300s. The two limits aren't simultaneously satisfiable at sleep=0.25; needs ≤1.33/s (sleep ≥0.75s) or an explicit rolling-window gate. Self-healing (honors `Retry-After`, per-CID cache → ~0 calls on re-run), so slow not broken — hence MED not HIGH.
Fix: pick one concrete throttle — e.g. `sleep(0.75)` flat, or a sliding 5-min counter capped at 390 — and drop the "sleep(0.25)" line, or state both limits resolve to the tighter one.

**[LOW] Path prefix drift.** Plan writes `data/rag_storage/...` and `data/enrich_cache/`; actual tree is `lightrag/data/...`. If `enrich_pubchem.py` runs from repo root (its path is `lightrag/enrich_pubchem.py`), the relative paths miss.
Fix: resolve from the script's own dir (`Path(__file__).parent / "data/..."`) or the server's `working_dir` config, not cwd.

**[LOW] Personal email in outbound header.** `From: ilpin301@gmail.com` ships to PubChem request logs on every call. Standard best practice, your own address, presumably consented — but worth a conscious OK since it's published off-machine.
Fix: fine as-is, or use a non-personal alias if you'd rather not log it.

**[LOW] Confidence rule wording ambiguity.** "contained in the CID's synonym list" could read as substring. Synonym lists are large; substring match on a short/generic name over-matches.
Fix: state "exact whole-string equality against any synonym" (not substring).

**[LOW] Fresh-read empty-response not handled.** If a candidate was renamed/deleted by hand between step 1 (graphml) and step 5 (live `/graphs`), `label=<oldname>` returns empty KnowledgeGraph.
Fix: empty read → log "gone" → skip.

**[LOW] Graphml mutated by the script's own edits mid-run.** Each `aedit_entity` flushes graphml via `index_done_callback`. Harmless here (step 1 reads it once, names only), but document that the candidate list is a point-in-time snapshot.

## Verdict

Round-1 [HIGH] resolved and verified against real files/counts. Remaining items are MED (self-healing rate-limit spec) and LOW (path precision, wording, edge cases) — non-blocking.

VERDICT: APPROVED

### Non-blocking follow-ups (from Round 2 APPROVED)
- [MED] Rate-limit spec self-contradictory: sleep(0.25)=4/s vs 400/5-min not simultaneously satisfiable → FOLDED INTO PLAN (sleep 0.75s flat / sliding 390-per-5min gate).
- [LOW] Path prefix drift: paths are lightrag/data/... not data/... → FOLDED INTO PLAN (resolve from Path(__file__).parent).
- [LOW] Synonym match wording → FOLDED: exact whole-string equality against any synonym, not substring.
- [LOW] Fresh-read empty response (node renamed/deleted between step1 and step5) → FOLDED: empty → log "gone", skip.
- [LOW] From: personal email in PubChem logs → left as-is (user's own address, consented).
- [LOW] graphml mutated by own edits mid-run → documented: candidate list is a point-in-time snapshot.

## Resolution: APPROVED at Round 2 (of MAX_ROUNDS=5). One [HIGH] found + fixed; MED/LOW folded or noted.

## Round 3 — GLM (Option C scope widening)

Option C verified against the real graphml (concept=372 ✓, artifact=335 ✓, naturalobject=91 ✓, material+substance=5 ✓). Cited regex-hit nodes confirmed present, incl. the messy ones (`Al2O3 Nanoparticle-infused Ne-PCM`, `Al2O3-CuO Hybrid`, `Lauric Acid PCMs`, `Ag2O Nanoparticles`). Chemical-token regex hits only **8** node names graph-wide → regex-only additions ≈24, so "~120 total candidates" is sound and judge cost stays bounded (not the 707/803 blind-widening figure).

## Prior findings — still hold under widening
Graphml enum (uncapped), fresh RMW + empty→"gone", whole-string synonym confidence, DOTALL strip, °C melting-point pick, `sleep(0.75)`/sliding-390 rate budget — all intact and now MORE load-bearing (more candidates). No regression.

## New flaw introduced by the widening

**[MED] Provenance leakage on PCM-system / composite / infused nodes.** The regex path pulls in nodes like `Al2O3 Nanoparticle-infused Ne-PCM` and `Lauric Acid PCMs`. The plan tells the judge to extract the base compound (`Al2O3`, `lauric acid`) for these and resolve it. The CID is then correct, but pure-base thermophysics gets written onto a node that is a **composite/PCM system**, not the pure compound — e.g. Al2O3 mp 2072°C attached to a nano-PCM node, or lauric acid 44°C onto a lauric-acid *eutectic* node. RAG then retrieves the system node and may cite the wrong melting point. The plan's own Risks note only covers composites *with no single CID* (skipped) — single-base systems slip through and get pure-compound data. Silent, wrong thermophysics, exactly the graph-poisoning-adjacent outcome the gate was built to prevent. Not a HIGH (small count, CID cited/verifiable, judge-remediable, doesn't block the bulk of enrichments).
Fix: judge must **SKIP** any candidate whose name denotes a system/composite/derivative (`PCM`, `PCMs`, `Eutectic`, `Hybrid`, `infused`, `Nano-PCM`, `Doped`, `Composite`, `Mixture`, `Blend`, `Bi-`, or any `X-Y`/`X-Y-Z` multi-element token) even when a single base CID is extractable; allow base-extraction ONLY for pure-material form suffixes (`Nanoparticles`, `Powder`, `Nanofluid`, `Nanowire`) that don't change thermophysics.

## Non-blocking follow-ups (LOW)
- **[LOW] "~803" blind-widening figure is loose** — actual concept+artifact = 707 (≈6×, not 8×). Directionally fine; fix the round number to 707 for accuracy.
- **[LOW] Formula-regex noise** — `^[A-Z][a-z]?\d` (and `Na2`/`CaCl2` substrings) can tag non-compound concept/artifact labels (channel/section ids, author codes). Judge absorbs it (~1 call each, cached); just expect a few `skipped-judge` rows, not enrichment errors.
- **[LOW] Residual gap acknowledged** — compound misfiled under concept/artifact with no chemical token in its name is missed. Plan already calls this out; fine.

No [HIGH] introduced by Option C; prior [HIGH] stays resolved.

VERDICT: APPROVED

### Claude's response (Round 3)
APPROVED — no HIGH. Folding the one [MED] + one LOW:
- [MED] provenance leakage on composite/system nodes → FOLDED: judge must SKIP system/composite/derivative names (PCM/PCMs/Eutectic/Hybrid/infused/Nano-PCM/Doped/Composite/Mixture/Blend/multi-element X-Y) even if a base CID is extractable; allow base-extraction ONLY for pure-material forms (Nanoparticles/Powder/Nanofluid/Nanowire).
- [LOW] "~803" → corrected to 707 (concept 372 + artifact 335).
- [LOW] formula-regex noise (a few skipped-judge rows) → accepted, noted, judge absorbs it.
- [LOW] residual no-token gap → already documented.

## Resolution: APPROVED at Round 3 (of MAX_ROUNDS=5). Option C scope-widening validated; provenance-leakage [MED] fixed. Plan converged.

---

# Re-review 2026-09-29 (post-implementation, post-Qdrant). MAX_ROUNDS=5.

## Round 4 — GLM (session a0e6b8a9, 760 s, modelUsage glm-5.3)

Re-review done. Plan vs script vs current reality (post-Qdrant, 78 docs). All settled Round 1–3 items re-verified intact — graphml enumeration uncapped, fresh per-node read, whole-string synonym rule, DOTALL strip, °C pick rule, throttle present. Script matches plan on all eight named rule-areas. New findings:

---

**[HIGH] Enrichment writes are never persisted by the run — edit path has no flush, and Qdrant made it worse.**
Evidence: `utils_graph.py:737-748` — `aedit_entity`'s normal path calls `_edit_entity_impl` and returns with **no** `_persist_graph_updates`. Every sibling admin flow flushes (delete `utils_graph.py:517`, relation-edit `:921`, create `:1042`, merge `:1193`); edit is the only one that doesn't. Post-migration, `QdrantVectorDBStorage.upsert` only *buffers* (`qdrant_impl.py:706-742`; "NOT visible until index_done_callback / finalize", `:749-754`) — so the plan's step-5 claim "aedit_entity re-embeds into entities_vdb (operate.py:1541)" is now both line-stale and semantically wrong: embed + Qdrant write happen at flush. `NetworkXStorage` has no `finalize` (base no-op), so graceful shutdown flushes Qdrant (`qdrant_impl.py:1287`) but **not the graphml**; only the ingest pipeline's `_insert_done` (`pipeline.py:2616`) flushes both, and there is no flush API endpoint (verified: zero hits in `lightrag/api/`).
Consequences for a re-run: (a) facts invisible to entity/local retrieval until an unrelated future ingest — plan step 7's query verification fails otherwise; (b) `rag_sync.ps1 push` right after MODE=full (the standard per-run workflow here) tars the pre-enrichment graphml and snapshots pre-enrichment Qdrant — the sanctioned backup silently lacks the entire run, and restore-from-Drive (an actually-used recovery in this base) loses it with no trace; (c) a graceful restart alone split-brains: Qdrant keeps enriched vectors, graph reverts, markers gone. The 2026-08-12 run persisted only because later ingests flushed.
Fix: plan step 7 must gate completion on a flush — after MODE=full, run the next queued ingest (the only existing trigger that flushes graph+vdb), then verify markers via `/graphs` AND the retrieval query, and only then `rag_sync.ps1 push`; treat enrich-without-flush as an incomplete run.

**[MED] Graphml key-id hardcoded (`enrich_pubchem.py:76` `K_TYPE = "d1"`).**
networkx `write_graphml` assigns `dN` in first-encounter order; the graphml has been rewritten by every pipeline flush since August (and restored from a Drive tgz after the delete bug). If attribute registration order ever shifts, the script silently reads the wrong attribute as `entity_type` → garbage candidate set, no error. Unverifiable on disk from here (scope limit bars `data/`).
Fix: parse the `<key>` registry and resolve `attr.name == "entity_type"` → id instead of hardcoding.

**[MED] Judge failures masquerade as SKIPs, then freeze forever.**
`judge_one` returns `None` after 4 failed attempts; `run()` computes `skipped_judge = len(names) - len(compounds)` — a z.ai outage or 1305 storm produces "286 skipped, 0 errors" and looks healthy. `_parse_judge` (`:200-204`) reads only the first line, so a fenced/preamble reply ("```COMPOUND: x", "Sure! COMPOUND: x") silently parses as SKIP. Verdicts are cached permanently in `judge.json`, and `--refresh` bypasses only the marker check, not the judge cache — one bad or transiently-failed verdict permanently excludes that node from every future run. Also a plan deviation: plan promises "serial fallback on repeated 1305"; script stays at Semaphore(2) with backoff.
Fix: separate judge-error stat (abort if error rate high), match `COMPOUND:`/`SKIP` case-insensitively anywhere in the reply, make `--refresh` re-judge cached SKIPs.

**[MED] Plan's cost/coverage model is stale — required re-estimate before re-run.**
Plan still claims "expected ≈120 candidates / ~480 PubChem calls / Option C keeps judge cost ≈120". Observed: 455 candidates on the *smaller* 1786-node graph; the graph has since grown well past that (78 docs). A re-run fires hundreds of NEW judge calls (z.ai spend + wall time) plus a bigger PubChem set.
Fix: strike the ~120 estimate, record 455@1786 as the observed point, and make MODE=dry on the current base a mandatory plan step before MODE=full.

**[LOW] Throttle comment overclaims.** Flat 0.75s = exactly 400 calls/5-min (300/0.75) — at the cap, not under; 429/503 retries consume slots on top. Fix: 0.8s (375/5-min) or the sliding-390 gate the plan offered.

**[LOW] 404 vs retry-exhaustion conflated.** `_pubchem_get` returns `None` for both; "unresolved" may hide rate-blocked calls that would resolve on retry (some of the 40 from Aug-12 plausibly this). Fix: log/cache a distinct outcome for exhausted retries.

**[LOW] `_parse_mp` robustness/provenance nits.** `val["Number"]` assumed list — a scalar would iterate digits (PubChem always sends a list today); °F/K-derived values written as plain °C with no "converted" annotation. Fix: `isinstance` guard; append "(converted from °F/K)".

**[LOW] Disk graphml may lag server memory** if any WebUI edits happened since the last ingest flush — newest nodes missed until next flush + re-run. Snapshot semantics already documented in plan; note only.

Re-run is otherwise safe and correct on the current base: enumeration stays uncapped (file read), skip-check is live-marker-based so idempotent regardless of flush state, caches make old candidates free, and `/graph/entity/edit` behavior (wholesale description replace, busy-pipeline 409, keyed lock vs concurrent edge writes) matches every plan assumption.

VERDICT: REVISE


### Claude's response (Round 4)
- **[HIGH] persistence — REJECTED.** Verified `lightrag/lightrag/utils_graph.py`: line 517 is inside `_edit_entity_impl` (defined at 268, ends 532), not in delete; it unconditionally calls `_persist_graph_updates` → `index_done_callback` on entities_vdb/relationships_vdb/graph/chunk storages, which flushes the Qdrant buffer (qdrant_impl.py upsert only buffers) and writes the graphml. The normal edit path at 737-748 goes through `_edit_entity_impl`, so every edit is persisted before returning. Plan step 5 stale reference (operate.py:1541) replaced with this path.
- **[MED] hardcoded K_TYPE — ACCEPTED.** On-disk registry today: d1 = entity_type (correct), but plan now requires runtime resolution from `<key>` registry.
- **[MED] judge failures / parse / cache — ACCEPTED with correction.** Failed judge calls are NOT cached (`judge_one` returns None without writing the cache), so "freeze forever" applies only to mis-parsed SKIPs. Plan now: case-insensitive token match anywhere, separate judge_error stat with 10% abort, `--refresh` re-judges cached SKIPs, serial-fallback promise dropped to match code.
- **[MED] stale cost model — ACCEPTED.** ~120 estimate struck; 455@1786 recorded; MODE=dry mandatory before MODE=full.
- **[LOW] throttle — ACCEPTED** (0.8 s). **[LOW] 404 vs retry exhaustion — ACCEPTED** (fetch_failed outcome). **[LOW] _parse_mp — ACCEPTED** (list guard + conversion annotation). **[LOW] graphml lag — ACCEPTED** as a documented risk.
- Note: plan-level only. `lightrag/enrich_pubchem.py` does not yet implement the accepted MED/LOW changes; code changes wait for human sign-off.
## Round 5 — GLM (resume a0e6b8a9, 120 s, modelUsage glm-5.3)

Round 4 findings vs revised plan — status:

- **[HIGH] persistence — RETRACTED, my error.** Verified: `_edit_entity_impl` spans 268–531; line 517 `await _persist_graph_updates(...)` is its unconditional tail; the script's path (no rename, no merge) runs through it: `aedit_entity:738` → `_edit_entity_impl` → `upsert_node:390` → vdb buffer `:409` → persist `:517` → Qdrant `_flush_pending_vector_ops` (embed + write, `qdrant_impl.py:784`) + `write_nx_graph` (`networkx_impl.py:733`) before the call returns. Plan's new step-5 persistence sentence is accurate as written, including the Qdrant buffering nuance and `rag_sync.ps1 push` after run. My mis-attribution: stopped reading at line 427 mid-function, then guessed line 517 belonged to a delete flow from bare grep numbers.
- **[MED] K_TYPE hardcode — ADDRESSED.** Step 1 now mandates runtime resolution from the `<key>` registry; current `d1` hardcode noted as accepted pending code change.
- **[MED] judge failures/parse/cache — ADDRESSED.** Case-insensitive token match anywhere, separate `judge_error` (never cached, 10% pre-write abort), `--refresh` re-judges cached SKIPs, serial-fallback claim dropped. Your correction is right — failed calls were never cached (`judge_one` returns None without writing); freeze applied only to mis-parsed successful replies, which the parsing fix + re-judge cover.
- **[MED] stale cost model — ADDRESSED.** 455@1786 recorded, ~120 struck, MODE=dry mandatory before MODE=full.
- **[LOW] throttle / 404-vs-retry / _parse_mp / graphml lag — all ADDRESSED** (0.8 s, `fetch_failed`, list guard + conversion annotation, documented risk).

New in the revision — nothing blocking:

- **[LOW] Partial-failure window on the persist gather.** `_persist_graph_updates` fires all five `index_done_callback`s via bare `asyncio.gather` (`utils_graph.py:62-69`) — unlike the merge path, no `VectorStorageConsistencyError` isolation. If the Qdrant flush fails (e.g. Ollama embed hiccup — this box has embed-timeout history) while `write_nx_graph` already succeeded, the node carries the marker but keeps its stale vector, and the marker skip-check then hides it from every future run. Fix: on write error, log the node for a `--refresh` follow-up (or verify retrieval for error'd nodes in step 7).
- **[LOW] Stale figure left in step 3.** Rate-budget paragraph still says "~5 calls/compound × ~96 candidates ≈ 480 calls" — the ~96 estimate was struck everywhere else. Cosmetic; mandatory MODE=dry re-measure covers it functionally. Fix: replace with the 455-observed figure.
- **[LOW] Per-edit cost scales with graph.** Each edit now rewrites the whole graphml atomically plus one single-doc embed flush; at 78 docs and hundreds of candidates the write phase adds minutes. No change needed — just expect slower per-node writes than the Aug-12 run.

No [HIGH] remains. Plan describes target behavior correctly; code deltas are explicitly gated on sign-off, not flagged.

VERDICT: APPROVED

### Non-blocking follow-ups
- [LOW] Persist gather partial failure: log nodes whose edit call errored for a --refresh follow-up / retrieval check in step 7.
- [LOW] Step 3 still cites the stale "~96 candidates / ~480 calls" budget; MODE=dry re-measure covers it.
- [LOW] Per-edit graphml rewrite + embed flush makes the write phase slower on the bigger graph; expected.

## Resolution: APPROVED at Round 5 (2 rounds this re-review, MAX_ROUNDS=5). One [HIGH] raised and retracted by GLM after Claude rebuttal; 3 MED + 4 LOW accepted into the plan. Code changes to enrich_pubchem.py await human sign-off.
