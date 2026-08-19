# Repository Guidelines

## Project Overview

LightRAG is a Retrieval-Augmented Generation (RAG) framework that uses graph-based knowledge representation for enhanced information retrieval. The system extracts entities and relationships from documents, builds a knowledge graph, and uses multiple retrieval modes (`local`, `global`, `hybrid`, `mix`, `naive`) for queries.

## Core Architecture

### Pipeline concurrency contract

The document ingestion pipeline coordinates concurrent writers through `pipeline_status` (a per-workspace shared dict in `lightrag.kg.shared_storage`). These fields are mutated under `get_namespace_lock("pipeline_status", workspace=...)`:

- **`busy`**: any pipeline-busy state. Set by both the processing loop AND destructive jobs (clear / per-doc delete). On its own, `busy=True` does NOT block enqueue — see `destructive_busy` for the exclusive subset.
- **`destructive_busy`**: the busy job is `/documents/clear` or `/documents/{doc_id}` (delete). These DROP storages and remove input files; a concurrent enqueue accepted in this window would write to storage being torn down and silently lose the document. Reservation and the enqueue last-line guard reject when this is True.
- **`scanning`**: a `/documents/scan` task is running (whole lifecycle: classification + processing). Used by the `/scan` endpoint to refuse overlapping scans. Does NOT on its own block uploads/inserts.
- **`scanning_exclusive`**: True only during the scan task's classification phase, when `run_scanning_process` is reading `doc_status` to classify files (PROCESSED → archive, FAILED-without-`full_docs` → retry-as-new, etc.) and possibly deleting stale stubs. Reservation and the enqueue last-line guard reject when this is set. Cleared before the scan transitions to its processing phase, allowing concurrent uploads to land while scan-driven processing finishes.
- **`pending_enqueues`**: count of `/upload`, `/text`, `/texts` endpoints that have reserved a slot (via `_reserve_enqueue_slot`) but whose bg task has not yet completed. Only the scan endpoint reads this — to refuse starting while uploads are mid-flight.
- **`request_pending`**: a nudge to the running processing loop. Set by either (a) `apipeline_process_enqueue_documents` when called while `busy=True` or (b) `apipeline_enqueue_documents` after writing to `doc_status` while `busy=True`. The loop checks it after each batch and re-queries `doc_status` if set.

Mutual-exclusion rules (all checked atomically inside the lock):

| Operation | Refuses if | Writes |
|---|---|---|
| `_reserve_enqueue_slot` | `scanning_exclusive` or `destructive_busy` | `pending_enqueues++` |
| `apipeline_enqueue_documents` (last-line guard) | (`scanning_exclusive` and not `from_scan`) or `destructive_busy` | — |
| Scan endpoint reservation | `busy or scanning or pending_enqueues > 0` | `scanning = True` |
| `apipeline_process_enqueue_documents` entry | (already busy → set `request_pending`, return) | `busy = True` (NOT `destructive_busy`) |
| `clear_documents` / `delete_document` (synchronous reservation) | `busy or scanning or pending_enqueues > 0` | `busy = True`, `destructive_busy = True` |

The contract permits **concurrent enqueue + processing**: a freshly-uploaded doc lands in `doc_status` while the loop is mid-batch, the loop sees `request_pending` after the current batch, re-queries `doc_status`, and picks up the new PENDING row.

For the rest — write ordering of `full_docs` vs `doc_status`, the workspace-scoped `enqueue_serialize` lock around dedup-and-upsert, and the `from_scan=True` bypass — see the docstrings on `apipeline_enqueue_documents` and `apipeline_process_enqueue_documents` in `lightrag/pipeline.py`.

## Development Commands

### Testing

- Use mock-based tests for external services (Redis, httpx, etc.) — do not depend on live services in unit tests.
- Add regression tests for every bug fix.
- Run the full test suite (or relevant subset) and report pass counts before declaring done.
- Backend tests use pytest; frontend unit tests use Bun's built-in runner.

```bash
# Preferred for fresh shells and automation; resolves PYTHON, venv, uv, .venv, venv, python, python3
./scripts/test.sh tests

# Run specific test file
./scripts/test.sh tests/kg/test_graph_storage.py

# Run with custom workers
./scripts/test.sh tests --test-workers 4
```

```bash
# Frontend testing (from lightrag_webui/) — Bun built-in runner (NOT Vitest/Jest)
bun test                           # All tests
bun test --watch                   # Watch mode
bun test --coverage                # With coverage report
bun test src/api/lightrag.test.ts  # Single test file
```

- `tests/`: main test suite, mirrors feature folders. Place new tests under the subdirectory matching the module under test:
  - `tests/api/{auth,config,routes}/` for FastAPI server tests (auth/token, config loading, route handlers); top-level `tests/api/` for app-wide concerns (path prefixes, Ollama-compatible endpoint).
  - `tests/chunker/`, `tests/evaluation/`, `tests/extraction/` for the like-named modules.
  - `tests/kg/<backend>_impl/` for backend-specific storage tests, mirroring the `lightrag/kg/<backend>_impl.py` file naming. The `_impl` suffix on every subdirectory keeps the layout uniform and avoids `sys.path` shadowing on names that overlap with top-level PyPI/stdlib packages (`faiss`, `json`, `neo4j`, `networkx`, `redis`) when a test is launched directly via `python tests/kg/...`. `tests/kg/` root holds cross-backend tests (`test_graph_storage`, `test_batch_graph_operations`, `test_unified_lock_safety`, `test_file_atomic`).
  - `tests/llm/<provider>_impl/` for provider-specific behavior, same `_impl` convention. `tests/llm/` root holds cross-provider concerns (embedding, VLM, cache, role).
  - `tests/parser/`, `tests/parser/docx/`, `tests/parser/external/{mineru,docling}/` for parser implementations.
  - `tests/pipeline/` for ingestion pipeline and doc-status behavior (including `test_pipeline_*`, `test_doc_status_*`, `test_multimodal_*`, `test_graph_keyed_locks`).
  - `tests/sidecar/`, `tests/setup/`, `tests/workspace/` for the like-named cross-cutting concerns.
  - When adding a new backend or LLM provider, create a new subdirectory plus an empty `__init__.py` rather than dropping the file in the parent directory root.
- Markers (see `tests/pytest.ini`): `offline`, `integration`, `requires_db`, `requires_api`. Integration tests are skipped by default via `-m "not integration"`.
- Integration env vars: `LIGHTRAG_RUN_INTEGRATION=true`, `LIGHTRAG_KEEP_ARTIFACTS=true`, `LIGHTRAG_TEST_WORKERS=4`, plus storage-specific connection strings.

### Linting
```bash
ruff check .
```

## Key Implementation Patterns

### LightRAG Initialization (Critical)

The most common error is forgetting to initialize storages (manifests as `AttributeError: __aenter__` or `KeyError: 'history_messages'`):

```python
import asyncio
from lightrag import LightRAG
from lightrag.llm.openai import gpt_4o_mini_complete, openai_embed

async def main():
    rag = LightRAG(
        working_dir="./rag_storage",
        llm_model_func=gpt_4o_mini_complete,
        embedding_func=openai_embed
    )

    # REQUIRED: Initialize storage backends
    await rag.initialize_storages()

    # Now safe to use
    await rag.ainsert("Your text here")
    result = await rag.aquery("Your question", param=QueryParam(mode="hybrid"))

    # Cleanup
    await rag.finalize_storages()

asyncio.run(main())
```

### Custom Embedding Functions

Use `@wrap_embedding_func_with_attrs` decorator and call `.func` when wrapping (already-decorated functions cannot be wrapped again — access the underlying via `.func`):

```python
from lightrag.utils import wrap_embedding_func_with_attrs

@wrap_embedding_func_with_attrs(embedding_dim=1536, max_token_size=8192)
async def custom_embed(texts: list[str]) -> np.ndarray:
    # Call underlying function, not wrapped version
    return await openai_embed.func(texts, model="text-embedding-3-large")

# Wrong: EmbeddingFunc(func=openai_embed)
# Right: EmbeddingFunc(func=openai_embed.func)
```

> **Pitfall — switching embedding models**: when changing the embedding model you MUST clear the data directory (optionally keeping `kv_store_llm_response_cache.json` for LLM cache). Existing vectors will not match the new model's space.

## Frontend Debugging via Playwright

For WebUI bugs whose symptoms only surface in the rendered DOM — layout/overflow/scrollbar issues, transient flashes, third-party libraries attaching helpers to `<body>` outside React's tree, or end-to-end verification of a fix — drive the running dev server (`http://localhost:5173`) with the `document-skills:webapp-testing` skill instead of reasoning from source alone. Seed state directly via `localStorage` (persist key `settings-storage`, schema in `lightrag_webui/src/stores/settings.ts`) to skip live LLM calls. Use `wait_until="domcontentloaded"` plus a selector wait — Vite dev's long-lived polling makes `networkidle` time out.

## Configuration

### Setup Wizard Outputs
- Keep `.env` host-usable. Container-only hostnames and staged SSL paths belong in the wizard-managed compose layer, not persisted back into `.env`.
- Treat `docker-compose.final.yml` as generated output assembled from `scripts/setup/templates/*.yml`.
- For setup workflow changes, prefer `make env-*` targets over direct `scripts/setup/setup.sh` calls.

## Code Style

### Language
Comments, backend code, and log messages in English. Frontend uses i18next for multi-language support.

### Python
- Follow PEP 8 with 4-space indentation
- Use type annotations
- Prefer dataclasses for state management
- Use `lightrag.utils.logger` instead of print
- Async/await patterns throughout

### TypeScript / React (incl. WebUI ESLint)
- Functional components with hooks; PascalCase for components
- 2-space indentation, single quotes (enforced by `@stylistic` rules)
- Tailwind utility-first styling
- ESLint stack: TypeScript-ESLint + React Hooks plugin + Prettier; `@typescript-eslint/no-explicit-any` is disabled (allowed)

## Commit and Pull Request Guidance

- If this repo is a fork of `HKUDS/LightRAG`. Target to `HKUDS/LightRAG` when creating PRs, not the fork's own repo.
- PR descriptions should include: summary, motivation, linked issues if applyed, what's changed, what's broken and how it works.
