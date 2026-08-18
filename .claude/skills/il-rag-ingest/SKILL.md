---
name: il-rag-ingest
description: Run the full PCM_RAG PDF ingest loop end to end - diff IN/ against the graph, probe each PDF for images AND vector figures, slice oversized PDFs, launch detached via ingest_resume.ps1, wait silently, verify, clean up. Use when the user says "ingest new PDFs from IN", "run the ingest", "/il-rag-ingest", or a close variant.
---

# il-rag-ingest

Orchestrator for the whole ingest procedure. Reads/uses the existing skills rather than
duplicating them: `lightrag-status` (server + doc list), `lightrag-upload` (text-only path),
`raganything-ingest` (MinerU/VLM path details, env vars, failure recovery),
`lightrag-query` (final sanity query).

Hard rules also live in `F:\____IL_AI\PCM_RAG\CLAUDE.md` (`## RAG Ingest Rules`) and the global
`## Background Monitoring`. Do not violate them; this skill is their executable form.

Paths:
- source folder: `F:\____IL_AI\PCM_RAG\IN\` — **ingest ONLY from here**
- project: `F:\____IL_AI\PCM_RAG\lightrag`
- wrapper: `lightrag\ingest_resume.ps1`
- log: `lightrag\LOG\ingest_run.log`
- storage: `lightrag\data\rag_storage`
- server: http://localhost:9622, key from `lightrag\.env` (`LIGHTRAG_API_KEY`) — never hardcode

## Step 0 — preflight

```powershell
$key = (Get-Content F:\____IL_AI\PCM_RAG\lightrag\.env | Select-String '^LIGHTRAG_API_KEY=').Line.Split('=',2)[1].Trim()
curl.exe -s http://localhost:9622/health -H "X-API-Key: $key"
curl.exe -s http://localhost:11434/api/version    # Ollama MUST be up before any ingest
Get-ChildItem F:\____IL_AI\PCM_RAG\lightrag\LOG\ingest_run.log -ErrorAction SilentlyContinue
Get-Content F:\____IL_AI\PCM_RAG\lightrag\LOG\LAST_FAILURE.txt -ErrorAction SilentlyContinue
```

- `ingest_run.log` already present + a live python process => a run is IN FLIGHT. Do not start another;
  attach to it at Step 4 instead.
- `LAST_FAILURE.txt` present => previous run failed. Read it (it already contains `ingest_triage.py`
  output with a verdict + hint) and report before doing anything new.
- **Never wipe `ingest_run.log` before a run.** The wrapper deletes it itself on `EXITCODE=0`.

`GET /documents` **hides `handling` rows**, so a half-ingested doc is invisible there. Cross-check the
store's own count before trusting a clean bill:

```powershell
$fileCount = ((Get-Content F:\____IL_AI\PCM_RAG\lightrag\data
ag_storage\kv_store_doc_status.json -Raw | ConvertFrom-Json).PSObject.Properties | Measure-Object).Count
$apiCount  = (($docs.statuses.PSObject.Properties.Value) | Measure-Object).Count
"file=$fileCount api=$apiCount"   # a positive difference = a hidden 'handling' doc
```

That file is only authoritative with the container STOPPED (LightRAG flushes doc_status on shutdown);
while the server runs it can be stale in the other direction. When the two disagree, stop the
container and re-read before deciding anything.

## Step 1 — diff IN/ against the graph

Two filters, both required. A filename check alone is NOT enough: slices were often ingested under
RENAMED short names (`Electromechanical_Hysteresis_Sb2S3-01-10.pdf` for a source called
`Electromechanical_Hysteresis_in_Phase_Change_Material_Sb2S3.pdf`), so the un-sliced source still
sitting in `IN\` looks new and gets ingested a second time. Content hashing does not help — a slice
is not byte-identical to its source.

```powershell
$key = (Get-Content F:\____IL_AI\PCM_RAG\lightrag\.env | Select-String '^LIGHTRAG_API_KEY=').Line.Split('=',2)[1].Trim()
$docs = (curl.exe -s http://localhost:9622/documents -H "X-API-Key: $key" | ConvertFrom-Json)
$known = $docs.statuses.PSObject.Properties.Value | ForEach-Object { $_.file_path } | Sort-Object -Unique
# ledger of sources already ingested (possibly under renamed slice names)
$ledger = Get-Content F:\____IL_AI\PCM_RAG\lightrag\INGESTED_SOURCES.txt |
          ForEach-Object { ($_ -replace '#.*$','').Trim() } | Where-Object { $_ }
Get-ChildItem F:\____IL_AI\PCM_RAG\IN\*.pdf |
  Where-Object { $known -notcontains $_.Name -and $ledger -notcontains $_.Name }
```

`lightrag\INGESTED_SOURCES.txt` is the ledger: one original source filename per line, `#` comments
ignored. Its comment block also records PARTIAL documents (slice families with a failed or missing
range) — those are deliberately NOT listed as done, and its notes say which page ranges are missing.

Report the genuinely new list. Before ingesting anything from it, sanity-check each candidate against
the ledger comments and against `/documents` for a *renamed* slice family covering the same paper —
if you find one, it is not new; add it to the ledger instead of ingesting it.

A file already PROCESSED is not new. A file in `FAILED` or stuck `handling` is a *repair* case, not a
new ingest — say so and stop for the user's call.

## Step 2 — probe each new PDF (routing)

Full image detection: `get_images()` alone MIS-ROUTES vector-figure PDFs. Always check
`get_drawings()` too.

```powershell
$py = "F:\____IL_AI\RAG\lightrag\.venv-rag\Scripts\python.exe"
& $py -c @'
import sys, fitz
for p in sys.argv[1:]:
    d = fitz.open(p)
    imgs = sum(len(pg.get_images()) for pg in d)
    maxdraw = max((len(pg.get_drawings()) for pg in d), default=0)
    chars = sum(len(pg.get_text()) for pg in d)
    route = "MINERU" if (imgs or maxdraw > 50 or chars/max(d.page_count,1) < 100) else "TEXT"
    print(f"{route} pages={d.page_count} images={imgs} maxdraw={maxdraw} chars/pg={chars//max(d.page_count,1)} {p}")
'@ <pdf paths...>
```

- `MINERU` => this skill's detached path (below).
- `TEXT` => `lightrag-upload` skill instead; far cheaper. Do not push text-only PDFs through MinerU.

## Step 3 — slice oversized PDFs

MinerU on this box fails above roughly 20 pages (5GB VRAM / 32GB RAM). Slice anything over
**10 pages** into `<=10`-page parts, named `<stem>-01-07.pdf` style, written into `IN\`.

```powershell
& $py -c @'
import sys, fitz
src = sys.argv[1]; step = 10
d = fitz.open(src)
for a in range(0, d.page_count, step):
    b = min(a+step, d.page_count) - 1
    out = fitz.open(); out.insert_pdf(d, from_page=a, to_page=b)
    name = src[:-4] + "-%02d-%02d.pdf" % (a+1, b+1)
    out.save(name); print(name)
'@ "F:\____IL_AI\PCM_RAG\IN\big.pdf"
```

Keep the source PDF. Slices are what gets ingested.

## Step 4 — launch detached, then wait silently

Rewrite the `$pdfs = @( ... )` block in `ingest_resume.ps1` with this run's file list — it always holds
the PREVIOUS run's paths, which are usually deleted slices by now, so never launch without rewriting it
and confirming every listed path exists. (The wrapper
carries the required env vars, the `EXITCODE=` marker, the failure triage and `docker compose start`
— do not reimplement it, and do not run `rag_ingest.py` inline.)

```powershell
Set-Location F:\____IL_AI\PCM_RAG\lightrag
docker compose stop     # REQUIRED - script writes the same storage files as the container
Start-Process pwsh -ArgumentList "-NoProfile","-File","F:\____IL_AI\PCM_RAG\lightrag\ingest_resume.ps1" -WindowStyle Hidden
```

Wait with ONE silent one-shot waiter that terminates by itself. Never `tail -f | grep`, never a
poller that emits progress notifications:

```bash
cd /f/____IL_AI/PCM_RAG/lightrag
until [ -f LOG/ingest_run.log ]; do sleep 2; done
while [ -f LOG/ingest_run.log ] && ! grep -q EXITCODE LOG/ingest_run.log; do sleep 20; done
if [ -f LOG/LAST_FAILURE.txt ]; then cat LOG/LAST_FAILURE.txt; else echo "EXITCODE=0"; fi
```

Log deleted + no `LAST_FAILURE.txt` = success (the wrapper deletes the log on `EXITCODE=0`).

## Step 5 — on failure: triage once, then escalate

`LAST_FAILURE.txt` already holds the verdict from `ingest_triage.py`. Known verdicts and the single
fix to attempt before escalating to the user:

| verdict | fix to try once |
|---|---|
| `MINERU_PARSE_FAILED` / `CUDA_OOM` / `HOST_OOM` | slice smaller (5-7 pages) and re-run |
| `LLM_RATE_LIMIT` | wait, re-run as-is (resumable, caches replay); do NOT raise the VLM semaphore above 2 |
| `ENDPOINT_UNREACHABLE` | start Ollama / z.ai reachable, re-run |
| `INTERRUPTED` | re-run as-is |
| `UNKNOWN` | do NOT guess a fix — report the log tail and stop |

### The dangerous case: `EXITCODE=0` with no work done

If the doc is already registered (typically stuck `handling` from an earlier killed run),
`rag_ingest.py` writes a fresh `dup-*` FAILED stub and exits **0** in under a minute. The wrapper
deletes the log, the waiter reports success, and nothing was ingested. Signature: finished far too
fast, graph node/edge counts unchanged, `vdb_*.json` byte-identical.

Deleting the `dup-*` stub does NOT fix this — the stub is a shadow of the real doc and comes back.
Repair the underlying doc:

```powershell
# the stuck doc will NOT appear in GET /documents - get its id from the store file
$full = (Get-Content F:\____IL_AI\PCM_RAG\lightrag\data
ag_storage\kv_store_doc_status.json -Raw | ConvertFrom-Json).PSObject.Properties |
        Where-Object { $_.Value.file_path -eq '<slice>.pdf' } | ForEach-Object { $_.Name }
$body = @{ doc_ids = @($full) } | ConvertTo-Json -Compress
Invoke-RestMethod http://localhost:9622/documents/delete_document -Method Delete -Headers $h -Body $body
```

`delete_document` accepts an id that `/documents` does not list. It is async and takes ~6 minutes
(it rewrites the graph and the ~460MB relationship vdb) — wait for `/health` -> `pipeline_busy=False`
with a silent until-loop, verify the doc's chunks are gone from `kv_store_text_chunks.json` and that
the graph counts DROPPED, then re-ingest. Re-ingesting reuses the same doc id (hashed from file path),
which is expected. See [[project_lightrag_delete_endpoint]].

Also check for the rest of the wreckage a killed run leaves: other docs stuck in `handling`, and
missing `vdb_*.json`. Recovery steps are in the `raganything-ingest` skill — reuse them, don't
invent new ones.

## Step 6 — verify (non-optional, all four)

**`EXITCODE=0` is not evidence that anything was ingested** — see the no-op case in Step 5. Only the
deltas below prove work happened. Record the baseline BEFORE launching (`grep -c '<node '` /
`grep -c '<edge '` on the graphml, plus the three `vdb_*.json` sizes and mtimes).

1. **Doc count delta** — `/documents` count before vs after; every new file PROCESSED, none FAILED/handling.
2. **Graph node delta** — `graph_chunk_entity_relation.graphml` node count grew:
   `grep -c '<node ' lightrag/data/rag_storage/graph_chunk_entity_relation.graphml`
3. **Vector sanity** — all three `vdb_chunks.json`, `vdb_entities.json`, `vdb_relationships.json`
   exist, have mtimes AFTER the run start, and GREW. Byte-identical sizes = the run did nothing. Missing/stale vdb => queries
   return `[no-context]`; the run did not finish cleanly.
4. **One targeted query** per ingested doc via `lightrag-query`, asking something only that document
   answers. Answer must cite it.

Report the four numbers. Do not claim success without them.

## Step 7 — cleanup and bookkeeping

Only after `EXITCODE=0` **and** Step 6 passing:

- delete the slice PDFs (`<stem>-NN-MM.pdf`); keep the source PDF
- append the SOURCE filename (not the slices) to `lightrag\INGESTED_SOURCES.txt`; if any slice of
  it failed, add it as a commented PARTIAL entry naming the missing page range instead
- update `memory\project_ingest_state.md` with the new doc count/state — do this without asking
- `docker ps` to confirm the container came back up (wrapper runs `docker compose start`, which
  fails silently if Docker Desktop is down)

Emit ONE end-of-run summary: files ingested, the four verification numbers, anything skipped and why.

## Windows gotchas that cost time

- Any python that prints extracted PDF text needs `PYTHONIOENCODING=utf-8`; the default cp1251 console
  codec raises `UnicodeEncodeError` on the first umlaut and kills the script mid-report.
- `import fitz` warns it is deprecated — use `import pymupdf` in new snippets; both ship in the venv.
- Deleted source PDFs are usually still in git: `git show HEAD:FOUND/<name>.pdf > <scratchpad>/<name>.pdf`
  recovers one for page-count or gap classification without touching the worktree.
- **Upload from PowerShell, never from bash.** `curl.exe -s -X POST .../documents/upload -F "file=@F:\...\x.pdf"`
  run through the Bash tool returns an EMPTY response and uploads nothing — bash mangles the Windows
  path in the `-F` argument, and the server never sees a file. The same command from PowerShell returns
  `{"status":"success",...,"track_id":"upload_..."}`. An empty response body is the tell; always confirm
  the doc count actually rose before waiting on a pipeline that was never given any work.
- Foreground `sleep` is blocked by the harness. Wait with an `until`-loop in a `run_in_background`
  shell, which also satisfies the silent-monitoring rule.
