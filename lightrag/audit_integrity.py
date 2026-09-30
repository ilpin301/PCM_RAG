"""Read-only integrity audits of the PCM_RAG store (data-integrity plan 2026-09-30).

  python audit_integrity.py orphans     -> data/audit/orphans.json
  python audit_integrity.py grounding   -> data/audit/grounding.json
  python audit_integrity.py --selftest
Reads graphml, kv_store_text_chunks.json, kv_store_doc_status.json; writes only under data/audit/.
"""
import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
STORE = SCRIPT_DIR / "data" / "rag_storage"
GRAPHML = STORE / "graph_chunk_entity_relation.graphml"
OUT = SCRIPT_DIR / "data" / "audit"
NS = "{http://graphml.graphdrawing.org/xmlns}"
SEP = "<SEP>"
BLOCK_RE = re.compile(r"<!--(PUBCHEM|OPENALEX)_START-->.*?<!--\1_END-->", re.DOTALL)
UNIT_NUM_RE = re.compile(r"(?<![\w.])(-?\d+(?:[.,]\d+)?)\s*(?:°\s*C|K\b|kJ/kg|J/g|W/\(?m|g/cm|kg/m|%|"
                         r"MPa|GPa|nm|µm|μm|mm|kJ/mol)")
NUM_RE = re.compile(r"\d+(?:[.,]\d+)?")


def _norm(x):
    return str(float(x.replace(",", ".")))


def unit_numbers(text):
    """Normalised values of numbers followed by a unit (sign dropped)."""
    t = (text or "").replace("−", "-")
    return {_norm(m.group(1).lstrip("-")) for m in UNIT_NUM_RE.finditer(t)}


def all_numbers(text):
    return {_norm(x) for x in NUM_RE.findall(text or "")}


def load_graph(path=GRAPHML):
    """[(kind, key, attrs)] for every node and edge; key = node id or (source, target)."""
    root = ET.parse(path).getroot()
    keys = {k.get("id"): k.get("attr.name") for k in root.iter(NS + "key")}
    attrs = lambda el: {keys[d.get("key")]: d.text or "" for d in el.findall(NS + "data")}
    return ([("node", el.get("id"), attrs(el)) for el in root.iter(NS + "node")]
            + [("edge", (el.get("source"), el.get("target")), attrs(el)) for el in root.iter(NS + "edge")])


def source_ids(a):
    return [s for s in (a.get("source_id") or "").split(SEP) if s]


def files(a):
    return [f for f in (a.get("file_path") or "").split(SEP) if f]


def orphans(graph, chunks, doc_files):
    """Items whose every source chunk is gone; deleted_doc_only = none of their files is a live
    document (only those are safe to delete - anything else is a store bug to report)."""
    res = []
    for kind, key, a in graph:
        s = source_ids(a)
        if s and all(c not in chunks for c in s):
            res.append({"kind": kind, "key": key, "entity_type": a.get("entity_type", ""),
                        "files": files(a), "deleted_doc_only": all(f not in doc_files for f in files(a))})
    return res


def grounding(graph, chunks):
    """Items whose description (blocks removed) has unit-numbers absent from their source chunks."""
    res = []
    for kind, key, a in graph:
        desc = BLOCK_RE.sub("", a.get("description") or "")
        nums = unit_numbers(desc)
        if not nums:
            continue
        ids = source_ids(a)
        missing = sorted(nums - all_numbers("\n".join(chunks[c]["content"] for c in ids if c in chunks)))
        if missing:
            res.append({"kind": kind, "key": key, "entity_type": a.get("entity_type", ""),
                        "missing": missing, "description": desc, "files": files(a),
                        "chunk_ids": ids, "dangling_chunks": [c for c in ids if c not in chunks]})
    return res


def _selftest():
    chunks = {"c1": {"content": "Paraffin melts at 58.2 °C with 200 kJ/kg."}}
    g = [("node", "Paraffin", {"description": "Melts at 58.2 °C; latent heat 210 kJ/kg.",
                               "source_id": "c1", "file_path": "a.pdf"}),
         ("node", "Old", {"description": "x", "source_id": "gone1<SEP>gone2", "file_path": "s-001-010.pdf"}),
         ("node", "Mixed", {"description": "y", "source_id": "c1<SEP>gone1", "file_path": "a.pdf"}),
         ("node", "Live", {"description": "z", "source_id": "gone3", "file_path": "a.pdf"}),
         ("edge", ("A", "B"), {"description": "Tm 58.2 °C", "source_id": "c1", "file_path": "a.pdf"})]
    gr = grounding(g, chunks)
    assert [(x["key"], x["missing"]) for x in gr] == [("Paraffin", ["210.0"])], gr
    orph = orphans(g, chunks, {"a.pdf"})
    assert [(x["key"], x["deleted_doc_only"]) for x in orph] == [("Old", True), ("Live", False)], orph
    assert unit_numbers("−5 °C, 1,5 %, 3 K and 12 cycles") == {"5.0", "1.5", "3.0"}
    assert unit_numbers(BLOCK_RE.sub("", "W. <!--PUBCHEM_START-->mp 0 °C<!--PUBCHEM_END-->")) == set()
    print("selftest OK")


def main(argv):
    if argv[1:] == ["--selftest"]:
        return _selftest()
    if argv[1:] not in (["orphans"], ["grounding"]):
        sys.exit(__doc__)
    chunks = json.loads((STORE / "kv_store_text_chunks.json").read_text(encoding="utf-8"))
    graph = load_graph()
    OUT.mkdir(parents=True, exist_ok=True)
    if argv[1] == "orphans":
        docs = json.loads((STORE / "kv_store_doc_status.json").read_text(encoding="utf-8"))
        res = orphans(graph, chunks, {v.get("file_path") for v in docs.values()})
    else:
        res = grounding(graph, chunks)
    (OUT / f"{argv[1]}.json").write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
    kinds = {k: sum(1 for x in res if x["kind"] == k) for k in ("node", "edge")}
    print(f"{argv[1]}: {kinds} -> {OUT / (argv[1] + '.json')}")
    if argv[1] == "orphans":
        print("NOT deleted_doc_only (report, never delete):", sum(1 for x in res if not x["deleted_doc_only"]))


if __name__ == "__main__":
    main(sys.argv)
