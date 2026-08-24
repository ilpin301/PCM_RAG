# Checking formula-recognition quality in PCM_RAG ingests

How to verify that math (and chemistry) in a PDF was recognized correctly and actually
landed in the LightRAG base. Written 2026-08-24 against the
`Optimization_of_Phase_Change_Material_Integration_for_Active_Cooling_Control.pdf` ingest.

## Background: what the pipeline already does

Both ingest entry points enable equation and table processing explicitly:

- `lightrag/rag_ingest.py:174-176` — `enable_image_processing`, `enable_table_processing`,
  `enable_equation_processing` all `True`
- `lightrag/ingest_merged.py:205-207` and `:331-333` — same three flags

MinerU splits each page into typed blocks (`text`, `image`, `table`, `equation`) and every
non-text block gets its own LLM pass. Only `page_number` / `header` / `footer` are filtered
out as noise (`rag_ingest.py:44-60`).

Result: an equation is stored as LaTeX **plus** an LLM-written explanation, then goes through
normal entity/relation extraction. It is queryable by meaning, not just as a picture caption.

Measured on the base as of 2026-08-24 (2539 chunks): 197 chunks with equation content,
164 with LaTeX markup, 95 with table content. Example stored chunk:

```
Mathematical Equation Analysis:
Equation: $$
\rho \frac{\partial u}{\partial t} + \rho u \frac{\partial u}{\partial x} + ... \tag{1}
$$
Format: latex
Mathematical Analysis: This equation represents the x-component of the two-dimensional
Navier-Stokes momentum conservation equation, specifically applied to the molten PCM...
```

Chemistry, split answer:

- Inline chemical formulas in running text (Na2SO4-10H2O, paraffin C20H42) ride the text
  path and are kept verbatim.
- Reaction schemes / drawn structures have no dedicated MinerU type. They land as `image`
  and the VLM describes them in words — described, not machine-readable SMILES.
- Chemical entities get factual backfill separately from the PubChem enrichment run.

**Known gap:** no verification pass on OCR'd math exists. Nothing checks that a `\partial`
did not become a `\delta`. Quality has not been measured on this base. That is what the
checks below are for.

## The four checks, cheapest first

### 0. Ground truth — what is actually in the PDF

Open it and count the numbered equations by hand. That number is the denominator for
everything below. No tool substitutes for this on a one-off doc.

### 1. Recall — did MinerU *see* every equation

MinerU's own parse output is the truth about what was extracted, before any LLM touched it:

```
lightrag/data/mineru_output/<stem>__pNNNN-NNNN_<hash>/<stem>__pNNNN-NNNN/hybrid_auto/<stem>__pNNNN-NNNN_content_list.json
```

Note the layout: one directory per SLICE, named `<stem>__p0001-0007_<hash>`, and the parse
output lives under `hybrid_auto/`, not `auto/`. Verified 2026-08-24. Equation items carry
the keys `type`, `text`, `text_format`, `bbox`, `page_idx`.

Count items with `"type": "equation"`, grouped by `page_idx`. Compare against the hand count.

Missing equations do not vanish — they get absorbed into the neighbouring `text` block as
garbled inline characters. So also grep the `text` items for orphan math debris (bare
partial-derivative symbols, lone `=` lines, `(1)` tags with nothing attached). That is the
signature of a missed equation, and it is the failure mode that silently degrades the base.

**Slice-seam caveat.** `ingest_resume.ps1` runs `ingest_merged.py --pages 7`, so an 8-page
PDF becomes two slices (7 + 1) and MinerU parses each independently. An equation straddling
a slice boundary can be split or double-counted. Check every seam explicitly.

### 2. Fidelity — is the LaTeX *right*

Recall says it found 12 equations. Fidelity says whether equation 7 is the equation that is
on the page. Two levels:

**Automatic (cheap, catches gross breakage).** For each extracted equation string, check it
is well-formed: balanced `{}`, balanced `$$`, non-empty body, no stray trailing backslash.
Broken LaTeX means a broken extraction, guaranteed. Clean LaTeX means nothing — but the
failures are free to find.

**Manual (the only thing that catches wrong symbols).** Render each extracted LaTeX to a
small PNG (matplotlib mathtext — no TeX install needed) and place it beside the PDF page
crop in one HTML sheet. Eyeball the pairs in two minutes. This is where a `\delta` that
should be `\partial`, a lost subscript, or a dropped minus sign gets caught. No automated
check finds those — there is no reference to diff against.

The crop step CAN be fully automated: equation items carry a `bbox`. Verified 2026-08-24 on
the Optimization/Active-Cooling ingest. No manual screenshotting needed.

Even lazier for step 0/1: MinerU also writes `<stem>_layout.pdf` next to the content list —
the source pages with every detected region drawn and labelled by type. Flip through it and
check each equation has a box around it. Beats hand-counting.

### 3. Landing — did it reach the base

Equation parsed correctly is not the same as equation in the graph. Two hops can drop it:
the multimodal LLM pass, and chunk insertion.

- In `lightrag/data/rag_storage/kv_store_text_chunks.json`, filter chunks by this doc's id
  and count those starting `Mathematical Equation Analysis:`. Must equal the count from
  step 1. A shortfall means the multimodal pass failed on those items — plausible on any
  run that hit the serial-fallback path.
- Read two or three of the LLM's `Mathematical Analysis:` prose blocks and check they
  describe the actual equation, not a hallucinated neighbour. A confidently-wrong analysis
  is worse than a missing one, because it becomes an entity and pollutes retrieval.

### 4. Retrieval — is it findable

Query the base for something only an equation in this paper answers (the governing energy
equation, a specific correlation). The answer must cite the doc and reproduce the formula.
Passing steps 1-3 with a failing step 4 means the equation is stored but not usefully
indexed.

## What is worth automating

Keep steps 1 and 3 as one script: count equations in the MinerU parse output, count
equation chunks in the store, flag any mismatch. Runs in seconds, catches the silent-drop
case on every future ingest.

Steps 2-manual and 4 stay one-off, per document you actually care about.

**Ordering matters.** Run this checkup BEFORE the Step 7 cache cleanup that deletes
`kv_store_llm_response_cache.json`. If the checkup finds dropped equations, the fix is a
re-ingest, and a re-ingest is cheap only while that cache still exists. Delete the cache
first and a shortfall costs full LLM re-extraction. Order: verify ingest -> formula checkup
-> slice cleanup -> cache deletion.

**Deliberately skipped:** any per-equation ground-truth corpus or accuracy metric across the
whole base. Add that only after sampling a few docs shows the mismatch rate is actually bad.
No point building measurement infrastructure for a problem not yet shown to exist.

## Reference numbers: Optimization_of_Phase_Change_Material_Integration_for_Active_Cooling_Control.pdf

8-page PDF, ingested 2026-08-24 via `ingest_merged.py --pages 7` (two slices). MinerU block
counts from the parse output:

| slice | equation | chart | table | image | text |
|---|---|---|---|---|---|
| p0001-0007 | 21 | 12 | 2 | 2 | 73 |
| p0008-0008 | 0 | 0 | 0 | 0 | 0 (references only) |

First equation as parsed, `text_format: latex`, `page_idx` 1:

```
$$ C_{d} \dot{T}_{d} = Q_{in} - Q_{out} - P_{d} \tag{1} $$
```

Expect 21 equation chunks in the store for this doc.
