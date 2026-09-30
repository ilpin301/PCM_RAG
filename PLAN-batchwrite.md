# Plan: collect-first, write-once enrichment (batch graph writer)
_Round 2: APPROVED by GLM (see PLAN-REVIEW-LOG-batchwrite.md); round-2 LOW follow-ups folded in_

## Goal
PubChem and OpenAlex enrichment currently write each node through `POST /graph/entity/edit`.
Each call makes the server rewrite the whole 125 MB `graph_chunk_entity_relation.graphml`
(~30 s per edit), so ~400 nodes take ~3.3 h. The fix is to split the run into two phases.
Phase A collects every new description without writing anything. Phase B applies them all in one
host-side LightRAG process while the `lightrag` service is stopped: one graphml write and one
batched embed flush into Qdrant. The target is minutes instead of hours, with byte-identical
store semantics to an API edit.

## Facts established from the code (not assumptions)
- An API edit with `allow_rename=false` ends in `lightrag/lightrag/utils_graph.py::_edit_entity_impl`
  (non-rename branch, lines 389-409):
  `graph.upsert_node(name, {**node_data, **updated_data, entity_id: name})`, then
  `entities_vdb.upsert({compute_mdhash_id(name, "ent-"): {content: name + "\n" + description,
  entity_name, source_id, description, entity_type}})`, then an entity_chunks backfill if missing,
  then `_persist_graph_updates(...)`. That last call runs `index_done_callback` on graph + vdbs +
  chunk KV, which is the 30 s graphml rewrite that happens on every edit.
- Container `pcm_rag-lightrag-1` runs lightrag 1.5.4 (`/app/lightrag`). The host ingest uses
  the vendored 1.5.5 at `PCM_RAG/lightrag/lightrag` (ingest.ps1 sets `PYTHONPATH`). Diffed from
  inside the container: `utils_graph.py` and `kg/networkx_impl.py` are identical, and
  `kg/qdrant_impl.py` differs only in `finalize()` closing the client. The point-ID derivation,
  the payload build in `upsert()` and the deferred embed in `_flush_pending_vector_ops` are
  identical.
- `QdrantVectorDBStorage.upsert` only buffers. Embedding and writes happen in
  `index_done_callback` in batches, so N buffered upserts become one batched embed pass.
- The host ingest already writes to this exact store and Qdrant collection through
  `ragkit/rag_ingest.py::embedding_func` (model_name = EMBEDDING_MODEL, so the collection suffix
  matches the server's) and `vector_storage=LIGHTRAG_VECTOR_STORAGE` from `.env`.
- `created_at` on flushed points is the batch flush time, not a per-edit time
  (qdrant_impl.py:718). This is the same as an API edit (flush time) and is expected to differ
  when payloads are compared.

## Approach

### Phase A: `--collect FILE` in both enrichers (no graph writes)
1. `enrich_pubchem.py` and `enrich_openalex.py` get a `--collect FILE` flag. It runs exactly
   like a full run: the same enumerate, judge, fetch and hard rules, and the same
   `fresh_description` read through `/graphs` right before the would-be write. The one change is
   that `await write_entity(...)` becomes `collected[name] = {"old": desc, "new": new_desc}`,
   logged as `[collected]`. `enrich_pubchem.py --fix-blocks --collect FILE` does the same in
   `fix_blocks`.
2. **Refuse an existing FILE** (exit 1 with a message) unless `--force` is given. This prevents
   cross-enricher clobbering. FILE is written atomically (tmp + `os.replace`) in a `finally`, so
   a mid-loop kill leaves a usable partial file. A PubChem GLM quota stop fires before the collect
   loop, so it leaves an empty or absent FILE, and a resumed run simply collects again from the
   caches.
3. `--collect` implies no graph writes, so `require_ollama()` is skipped. The server must be up,
   because `/graphs` is how phase A reads.

### Phase B: `ragkit/apply_descriptions.py FILE` (base-agnostic, run only through the launcher)
4. Parse FILE with `object_pairs_hook` that rejects duplicate names. Validate every entry: `new`
   is a non-empty string and `old` is a string (it may be "": a node that had an empty
   description). If anything is invalid, exit 2 before touching anything.
5. **Preflight, before any storage is built:**
   (a) `QDRANT_URL` is taken from `ragbase.env_value("QDRANT_URL")`, exported into
   `os.environ`, and must start with `http://127.0.0.1:`; anything else, including missing, is
   exit 3 (no silent in-memory Qdrant).
   (b) Ollama `GET 127.0.0.1:11434/api/version` must be OK, else exit 3.
   (c) An independent `QdrantClient(url=QDRANT_URL)` must see the entities collection whose name comes from `migrate_nano_to_qdrant.collection_name(ns, model, dim)` (ragkit helper, the same one check_vectors.py uses)
   (`collection_exists`), else exit 3.
   `rag_ingest` is imported lazily (inside the main path, not at module top), so `--selftest`
   runs without ZAI_API_KEY/RAGBASE_ROOT.
6. Build a plain `LightRAG(working_dir=ragbase.STORAGE, embedding_func=rag_ingest.embedding_func,
   llm_model_func=rag_ingest.llm_model_func, vector_storage=<.env LIGHTRAG_VECTOR_STORAGE>)`,
   then `await rag.initialize_storages()`. Record the graphml `(mtime_ns, size)` immediately
   after the load.
7. Write the rollback file `FILE.rollback.<stamp>.json` BEFORE any mutation. For every entry
   that will be applied or re-embedded (`[already]` included; its inverse is a harmless new->new re-embed), it holds `{name: {"old": new, "new": current}}`, i.e. the inverse.
   Applying it with the same tool restores both graph and vectors.
8. Monkey-patch `lightrag.utils_graph._persist_graph_updates` to an async no-op. Then, for each
   entry, `node = await graph.get_node(name)`; `cur = (node or {}).get("description")`:
   - node missing → `[gone] <name>`, skip
   - `cur == new` → `[already] <name>`, **still call `_edit_entity_impl`** (graph no-op,
     re-upserts the vector). A re-run therefore heals a run whose graph committed but whose
     vector flush failed. Counted as `already`, and included in verify.
   - `cur != old` → `[changed] <name>`, skip (stale-clobber guard)
   - otherwise call `_edit_entity_impl(graph, rag.entities_vdb, rag.relationships_vdb, name,
     {"description": new}, entity_chunks_storage=rag.entity_chunks,
     relation_chunks_storage=rag.relation_chunks)` → `[applied] <name>`.
   Every skipped name is logged by name, not only counted.
9. **Second-writer guard:** re-stat the graphml; if `(mtime_ns, size)` differs from step 6,
   abort with exit 6 BEFORE persisting (nothing written; the rollback file is unused).
   Otherwise restore the real `_persist_graph_updates` and call it once with all five storages:
   one graphml write plus one batched embed/upsert of every applied + already entity vector.
   Then `await rag.finalize_storages()`.
10. **Self-verify with independent readers:** for every applied + already name, (a) an
    independent `QdrantClient` retrieves the point (`compute_mdhash_id_for_qdrant(ent_id, prefix=<effective workspace, default "_">)`, as qdrant_impl.py derives it) and
    requires payload `content == name + "\n" + new` and a vector of length EMBEDDING_DIM;
    (b) a fresh `NetworkXStorage`-independent parse of the graphml (`networkx.read_graphml`)
    requires `description == new`. Any mismatch → exit 5 with the rollback path printed.
    Summary: applied / already / gone / changed.

### Launcher: `ragkit/ingest.ps1 -DescFile FILE`
11. `-ListFile` becomes optional. Exactly one of `-ListFile` / `-DescFile` is required. With
    `-DescFile`:
    - guards: FILE exists, parses as JSON and has ≥ 1 entry. An empty file exits 0 with "nothing
      to apply" BEFORE `docker compose stop` (no pointless server stop).
    - runs `apply_descriptions.py FILE` in place of `rag_ingest.py`.
    - every `$pdfs` use (header log line, 429-loss grep, `ingest_triage.py`) is branched: the
      header logs `desc=<FILE> entries=<n>`, and the grep and triage are skipped.
    - everything else is reused unchanged: env export, vendored PYTHONPATH, `Set-Location` to
      lightrag (so LightRAG's `load_dotenv(".env")` also sees the base .env), stop + still-running
      guard, `patch_flush_safety.py`, `check_vectors.py` after exit 0, `EXITCODE=` line, log
      archive, `docker compose start lightrag`.

### Operating sequence (for the remaining ~323 PubChem compounds)
12. Phase A: `NO_PROXY='*' python enrich_pubchem.py --collect data/enrich_cache/pending_pubchem.json`
    (server up). Review the `[collected]` count.
13. Start Google Drive at the start. `rag_sync.ps1 push` as the pre-write restore point (the tgz
    includes Qdrant snapshots). Also keep a local copy of the graphml.
14. Phase B: launch detached `ingest.ps1 -Root X:\RAG_MAIN\PCM_RAG -DescFile <json>` and wait
    silently for `EXITCODE=`.
15. Verify: EXITCODE=0 (includes self-verify + check_vectors). `/graphs?label=<one applied
    node>` shows the block. Compare one batch-applied node's Qdrant payload against a node
    API-edited in an earlier run (e.g. `Gallium`): same payload key set, content format
    `name\n<description>` (created_at is expected to differ). Run one `/query` that should
    retrieve a PubChem fact. Then `rag_sync.ps1 push`.
16. First real use is a proving run of `--limit 10`, followed by the full set.

### Tests (one runnable check)
17. `apply_descriptions.py --selftest`: a temp working dir with NetworkX graph + NanoVectorDB and
    a deterministic fake embedding func (no Qdrant, no Ollama, no rag_ingest import). It seeds 4
    nodes and applies a file with one good, one gone, one changed and one already entry. It
    asserts the graph descriptions, the vdb content for applied + already, the counts, and that
    the graph file was written once. It then applies the rollback file and asserts the originals
    are back. The duplicate-key rejection and the mtime guard (touching the graph between load
    and persist → abort, nothing written) are also asserted. The preflight and independent-reader
    verify are Qdrant-specific, so they are exercised by the `--limit 10` proving run, not the
    selftest.

## Key decisions & tradeoffs
- **Reuse `_edit_entity_impl` with persist deferred**, rather than hand-writing Qdrant points.
  IDs, payload, content format and chunk-tracking backfill are LightRAG's own by construction.
  The cost is coupling to a private function name and signature. A signature change raises at
  the first entry, before persist, so nothing is written.
- **Monkey-patching `_persist_graph_updates`**, not calling `graph.upsert_node` +
  `entities_vdb.upsert` directly. Patching keeps the full edit semantics. `_edit_entity_impl`
  looks the name up in its module globals at call time (GLM verified).
- **old/new pair in the collect file** (not marker regexes). This makes phase B
  enricher-agnostic and gives the stale guard for free.
- **`[already]` still re-embeds.** It costs one embed per already-applied node, and in exchange a
  re-run is the recovery path for any half-persisted run.
- **Launcher reuse** (ingest.ps1 mode) instead of a new wrapper.
- **Rollback = inverse collect file.** No new restore code, and it is exercised by the selftest.

## Risks / open questions
- Server downtime for phase B: graph load (~1 min) + edits (seconds) + one graphml write (~30 s)
  + embed ~400 texts (< 1 min) + independent graphml re-parse (~1 min). Expected < 5 min.
- Persist failure after the graph commit (e.g. Ollama dies mid-flush): exit non-zero. Recovery is
  to re-run the same FILE; `[already]` re-embeds. If the graph did NOT commit, the re-run applies
  normally.
- The mtime guard catches another writer between load and persist. A writer that races the
  persist itself is not caught. The procedure (one run at a time, launcher stops the server)
  covers that; accepted.

## Out of scope
- Changing the pcm-PubChem-runner / pcm-OpenAlex-runner agent definitions to drive the new mode
  (follow-up once proven).
- MECH/CHEM bases (the tool is base-agnostic, but only PCM is exercised).
- Relationship vectors (enrichment edits entity descriptions only; no renames).
