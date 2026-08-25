# Registering a LightRAG base with ragkit

Superseded 2026-08-25. This file used to be a manual copy procedure for hand-porting the PCM_RAG
tooling into another base. There is no tooling to copy any more: it all lives in the ragkit repo at
`$env:RAGKIT_HOME`, and both PCM_RAG and MECH_RAG now run only through it. The full reference is
`$env:RAGKIT_HOME\README.md` — "Adding a machine" and "Adding a base". This page is the short version.

## A base is a directory with five things

| Path | Purpose |
|---|---|
| `lightrag\.env` | `PORT`, `EMBEDDING_DIM`, `COMPOSE_PROJECT_NAME`, and `ZAI_API_KEY` or `LLM_BINDING_API_KEY`. Never committed, copied by hand per machine. |
| `lightrag\docker-compose*.yml` | the server |
| `IN\` | incoming PDFs; ingests read from here only |
| `lightrag\INGESTED_SOURCES.txt` | the ledger — one ORIGINAL source filename per line |
| `CLAUDE.md` | the base's `## RAG Ingest Rules`, adapted from an existing base |

`COMPOSE_PROJECT_NAME` is not optional. Without it docker compose derives the project from the
compose file's parent folder — `lightrag` for every base — and commands land on whichever base was
started last. `ingest.ps1` refuses to run without it; `rag_sync.ps1` reads it to pick which container
to stop.

## Registering it

Nothing to register in the kit. Run one ingest:

```powershell
& $env:RAGKIT_HOME\ingest.ps1 -Root <base> -ListFile <utf8 list file>
```

Discovery resolves the port, the container and the venv at runtime. If `$env:RAGKIT_HOME` is empty,
the session started before `bootstrap.ps1` set it — restart the shell and the Claude session.

## What stays in the base, not in the kit

- `rag_sync.ps1` — the Drive snapshot script, one copy per base
- `keepawake.ps1` — blocks system sleep during long runs
- one-off incident scripts (`delete_doc.ps1`, `repairs\`) that were written for a specific repair
- the store itself (`lightrag\data\rag_storage\`) — never in git, backed up to Drive

## Per-base facts that are NOT portable

Ports, container names, ledger rows, ingest-state baselines and the audit's expected counts are all
per base. Record them in that base's project memory under
`~\.claude\projects\<slug>\memory\`, never in a skill and never in the kit.

## History

The original 207-line hand-port runbook, the substitution tables and the lessons it collected are in
git history: `git show 56a72bd:PORT_RAG_TOOLING.md`. The port it described was executed as the
ragkit plan (`PLAN.md`, segments S0-S8) and does not need repeating.