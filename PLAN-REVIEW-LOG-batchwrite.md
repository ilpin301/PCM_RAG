# Plan Review Log: collect-first, write-once enrichment (batch graph writer)
Started 2026-09-30. MAX_ROUNDS=5. Reviewer glm-5.3 via https://api.z.ai/api/anthropic.

## Round 1 — GLM
Reviewed plan against vendored 1.5.5 sources, launcher, enrichers, kit scripts. Facts section checks out almost everywhere — verified: `qdrant_impl.upsert` buffers only (qdrant_impl.py:705-742), flush batches embed (794-956), `get_by_id` read-your-writes + payload carries `content` (meta_fields lightrag.py:1169), `_edit_entity_impl` module-global lookup makes the patch effective, `initialize_share_data` auto-runs (lightrag.py:1000), base `finalize` no-op so one graph write holds, KV callback dirty-only. Core design sound. Findings:

**[HIGH] Half-persisted recovery left as open question — re-run heals graph but not vectors, silently.** Persist runs graph write + Qdrant flush in one `asyncio.gather` (utils_graph.py:64); graph can commit while embed fails (Ollama down — see next item). Re-run then reports `[already]`, and step 9 self-verify checks only *applied* names — every gate green, stale vectors forever. Same silent-divergence class as the 2026-09-10 wiring bug. Fix: resolve the open question to YES in the plan — on `[already]` still run `_edit_entity_impl` (idempotent re-embed), and make self-verify cover them.

**[MED] No Ollama/Qdrant preflight in phase B.** Enrichers `require_ollama()` before write runs (enrich_pubchem.py:123); `apply_descriptions.py` is the write run and steps 11–14 list none. Ollama down = failure surfaces only at flush time, after the graph write — manufactures the HIGH above. Fix: require_ollama-style check + `collection_exists` ping before `initialize_storages()`.

**[MED] Self-verify reads through the storage's own client — cannot catch wrong endpoint.** `QdrantClient(url=os.environ.get("QDRANT_URL", config...))` with config.ini absent (qdrant_impl.py:43-44, 656-664): missing QDRANT_URL in the process env → silent in-memory local mode → vectors written to a throwaway collection; step 9 passes (reads own client), check_vectors passes (real collections healthy, counts unchanged). Correct only because launcher sets CWD=lightrag and `.env` loads. Fix: self-verify with an independent `QdrantClient` on the check_vectors URL, or assert the storage client's URL is remote before editing.

**[MED] `--collect` fresh-start overwrites FILE — cross-enricher clobber.** Step 2: "A resumed collect run starts FILE fresh". Point OpenAlex collect at the pending_pubchem path by mistake → PubChem batch silently destroyed. Fix: refuse an existing FILE unless `--force`.

**[MED] No second-writer detection inside the phase B window.** Phase B holds the whole graph in memory from construction (networkx_impl.py:164) and its single persist overwrites the file wholesale; any writer touching graphml between load and persist (stray host ingest, someone `docker compose start`ing the server mid-run) is silently reverted — per-node `[changed]` guard can't see nodes outside FILE. Fix: stat graphml (mtime+size) at load, re-stat immediately before the final persist, abort on change.

**[LOW]** Guard must use `node.get("description")` — graphml nodes can lack the attr; `node["description"]` (step 7) would KeyError.
**[LOW]** `[changed]`/`[gone]` names only counted, not listed — next collect re-picks them up, but log the names for the operator.
**[LOW]** Empty collect file: launcher still stops the container for a no-op run — exit early before `docker compose stop`.
**[LOW]** `import rag_ingest` needs `ZAI_API_KEY`/`RAGBASE_ROOT` at import time (rag_ingest.py:113, ragbase.py:21) — bare `--selftest` outside the launcher KeyErrors; lazy-import or say selftest runs under launcher.
**[LOW]** Exit-4 claim slightly off: PubChem quota stop fires in the judge phase *before* the collect loop (enrich_pubchem.py:664-665), so the "partial file" from a quota stop is ~empty, not partial — only mid-loop kills give a real partial. Harmless given fresh-start semantics.
**[LOW]** ingest.ps1 branches on `-DescFile` must neutralize every `$pdfs` use (header log, triage call), not just the two named skips.
**[LOW]** `created_at` on flushed points is batch time, not per-edit time (qdrant_impl.py:718) — semantic no-op, worth one line in the plan so nobody chases it comparing payloads with Gallium.
**[LOW]** Step 5 validation: also require `old` to be a non-empty string; "names unique" is vacuous for a JSON object (dupes collapse silently at parse).

Simpler alternatives checked: none better — `rebuild_vdb.py` re-embeds everything; hand-rolled Qdrant points lose the chunk-tracking backfill; the monkey-patch + one persist is the right laziness level.

VERDICT: REVISE
### Claude's response (round 1)
Accepted:
- HIGH half-persist: `[already]` now still runs `_edit_entity_impl` (re-embeds), and verify covers applied + already. A re-run is the recovery path.
- MED preflight: QDRANT_URL from .env, forced to http://127.0.0.1:, plus an Ollama ping and `collection_exists` via an independent client, all before the storages are built.
- MED wrong endpoint: self-verify now uses an independent QdrantClient and `networkx.read_graphml`, not the storage's own client.
- MED collect clobber: an existing FILE is refused unless `--force`.
- MED second writer: graphml (mtime_ns, size) is stat'ed at load and re-stat'ed before persist; exit 6 on change.
- LOWs: `.get("description")`; skipped names are logged; an empty FILE exits before the container stop; lazy rag_ingest import; the exit-4 wording is fixed; every `$pdfs` use is branched; a created_at note is added; duplicate-key rejection via object_pairs_hook.
Partially rejected:
- "old must be non-empty": a node may legitimately have an empty description, so `old` only has to be a str. `new` must be non-empty.

## Round 2 — GLM

Re-reviewed revised plan + response log against same sources.

**Round-1 disposition check — all addressed:**

- **[HIGH] half-persisted** → step 8: `[already]` still runs `_edit_entity_impl` (re-embed), verify covers applied+already (step 10), recovery documented (Risks). Resolved. Guard order also correct: `cur == new` fires before the `cur != old` stale check, so a node already at `new` heals instead of being skipped.
- **[MED] preflight** → step 5(a-c) before any storage is built; `http://127.0.0.1:` prefix requirement kills the in-memory local-mode class fail-loud. Resolved.
- **[MED] wrong endpoint verify** → step 10 independent `QdrantClient` + bare `networkx.read_graphml`. Resolved.
- **[MED] collect clobber** → step 2 refuse existing FILE unless `--force`. Resolved.
- **[MED] second writer** → steps 6/9 `(mtime_ns, size)` stat + re-stat, exit 6 before persist (edits in-memory only at that point, so "nothing written" claim is accurate). Persist-race residual accepted explicitly in Risks — acceptable, server stopped.
- **[LOW]s** — `.get("description")`, names logged, empty-file pre-stop exit, lazy `rag_ingest` import (selftest now needs no env), exit-4 wording, `$pdfs` branching, `created_at` note, dup-key rejection via `object_pairs_hook`: all in.
- **Rejected "old must be non-empty"** — rejection is correct: `fresh_description` returns `""` for empty/missing desc (enrich_pubchem.py:621), and a legitimately empty old produces `new = block` (line 715). `old` as bare str is the right rule.

**New findings in the revision** (nothing HIGH/MED):

- **[LOW]** Step 10(a): `compute_mdhash_id_for_qdrant(ent-id)` needs the workspace prefix — storage derives point ids as `compute_mdhash_id_for_qdrant(doc_id, prefix=effective_workspace)` with default workspace `"_"` (qdrant_impl.py:874-876). Pass the raw ent-id with no prefix → retrieve misses → false exit 5 on a healthy run. Fix: state `prefix="_"` (the effective workspace) explicitly in the plan.
- **[LOW]** Step 5(c): "collection by the name the storage will use" invites re-deriving `_generate_collection_suffix`. Reuse `migrate_nano_to_qdrant.collection_name(ns, model, dim)` — same helper check_vectors.py:96 already uses — so the preflight can't drift from reality.
- **[LOW]** Step 7 wording: "every entry that will be applied" is now ambiguous — `[already]` entries also mutate (re-embed). Either include them (rollback inverse becomes a harmless no-op `new→new` + re-embed) or exclude them; one clarifying sentence so the implementer doesn't guess.

Non-blocking follow-ups only. Plan's load-bearing claims all still check out against the sources; nothing new at MED or above.

VERDICT: APPROVED

### Non-blocking follow-ups (folded into the plan by Claude)
- Step 10(a): the Qdrant point id is `compute_mdhash_id_for_qdrant(ent_id, prefix=<effective workspace, default "_">)`.
- Step 5(c): the collection name comes from `migrate_nano_to_qdrant.collection_name(ns, model, dim)`, the same helper check_vectors.py uses.
- Step 7: the rollback file includes `[already]` entries too (harmless new->new re-embed).

Converged: APPROVED in round 2.
