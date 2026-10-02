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
NUM_RE = re.compile(r"\d+(?:[.,]\d+)?")
_S, _M1, _M3 = r"[\s·.]?", r"(?:\^?-1|⁻¹)", r"(?:\^?-3|⁻³)"
# family -> unit regex; order = priority (cp before latent, cond before flux), first match wins
UNIT_FAMILIES = {
    "cp": rf"k?J/\(?k?g{_S}K\)?|k?J{_S}k?g{_M1}{_S}K{_M1}",
    "cond": rf"W/\(?m{_S}K\)?|W{_S}m{_M1}{_S}K{_M1}",
    "latent": rf"kJ/kg|J/g|kJ{_S}kg{_M1}|J{_S}g{_M1}",
    "molar": r"kJ/mol",
    "dens": rf"g/cm[3³]?|kg/m[3³]?|g{_S}cm{_M3}|kg{_S}m{_M3}",
    "flux": r"W/m[2²]",
    "press": r"[kMG]Pa",
    "length": r"nm|[µμ]m|mm|cm",
    "time": r"hours?|hrs?|h|minutes?|min|seconds?|sec",
    "pct": r"(?:(?:wt|vol|mass|mol)\.?\s?)?%",
    # degree sign variants (º ˚ ◦ ∘, U+F0B0 symbol font), LaTeX ^{\circ}C, "degrees C"
    "temp": r"[°º˚◦∘]\s?[CF]|(?:\{\s*\}\s*)?\^?\s*\{?\s*\\circ\s*\}?\s*[CF]|deg(?:rees?)?\s?C|℃|K",
}
_NUM = r"\d+(?:[.,]\d+)?"
# one number, or a range / +- chain of numbers, then a unit; pct may abut text ("5 wt%Al"), others may not
UNIT_NUM_RE = re.compile(
    rf"(?<![\w.])(?P<n>-?{_NUM}(?:(?:\s*(?:[-–—±]|\+/?-)\s*|\s+to\s+)-?{_NUM})*)\s*(?:"
    + "|".join(f"(?P<{f}>(?:{rx})" + ("" if f == "pct" else "(?![A-Za-z])") + ")"
               for f, rx in UNIT_FAMILIES.items()) + ")")


def _norm(x):
    return str(float(x.replace(",", ".")))


def unit_pairs(text):
    """{(unit family, normalised unsigned number)}; every number of a range / +- chain counts."""
    t = (text or "").replace("−", "-")
    return {(m.lastgroup, _norm(n)) for m in UNIT_NUM_RE.finditer(t) for n in NUM_RE.findall(m.group("n"))}


def unit_numbers(text):
    """Normalised values of numbers followed by a unit (sign dropped)."""
    return {n for _, n in unit_pairs(text)}


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
    """Items whose description (blocks removed) has (unit family, number) pairs absent from their source
    chunks. missing = those numbers; bare_only = the subset still present in the chunks as a bare number
    (page/figure number or another unit - reviewer hint)."""
    res = []
    for kind, key, a in graph:
        desc = BLOCK_RE.sub("", a.get("description") or "")
        pairs = unit_pairs(desc)
        if not pairs:
            continue
        ids = source_ids(a)
        text = "\n".join(chunks[c]["content"] for c in ids if c in chunks)
        # sign is ignored (unit_pairs drops it); a pair counts as supported only with the same family
        missing = sorted({n for _, n in pairs - unit_pairs(text)})
        if missing:
            bare = all_numbers(text)
            res.append({"kind": kind, "key": key, "entity_type": a.get("entity_type", ""),
                        "missing": missing, "bare_only": [n for n in missing if n in bare],
                        "description": desc, "files": files(a),
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
    for t, want in {"5 wt%": {"5.0"}, "12 vol %": {"12.0"}, "3.5 mass%": {"3.5"}, "2 mol%": {"2.0"},
                    "4 wt.%": {"4.0"}, "20-25 °C": {"20.0", "25.0"}, "20–25 °C": {"20.0", "25.0"},
                    "20 to 25 °C": {"20.0", "25.0"}, "20 °C to 25 °C": {"20.0", "25.0"},
                    "5.2 ± 0.3 %": {"5.2", "0.3"}, "5 +- 1 K": {"5.0", "1.0"}, "5 +/- 1 K": {"5.0", "1.0"},
                    "180 kJ kg-1": {"180.0"}, "180 kJ kg^-1": {"180.0"}, "180 kJ kg⁻¹": {"180.0"},
                    "180 kJ·kg⁻¹": {"180.0"}, "200 J g-1": {"200.0"}, "0.2 W m-1 K-1": {"0.2"},
                    "0.2 W m⁻¹ K⁻¹": {"0.2"}, "58 ℃": {"58.0"}, "2.1 J/(g·K)": {"2.1"},
                    "2.1 J/(g.K)": {"2.1"}, "100 °F": {"100.0"}, "5 cm": {"5.0"}, "101 kPa": {"101.0"},
                    "2 h": {"2.0"}, "30 min": {"30.0"}, "12 cycles": set(), "Fig. 3": set(),
                    "page 210": set()}.items():
        assert unit_numbers(t) == want, (t, unit_numbers(t))
    for t, want in {"43 C": {"43.0"}, "25 ◦C": {"25.0"}, "25 ∘C": {"25.0"}, "25 º C": {"25.0"},
                    "25 ˚F": {"25.0"}, "9^{\\circ}C": {"9.0"}, "9 ^ { \\circ } C": {"9.0"},
                    "9 { }^{\\circ}C": {"9.0"}, "20 degrees C": {"20.0"}, "20 degree C": {"20.0"},
                    "20 deg C": {"20.0"}, "35 minutes and 2 hours": {"35.0", "2.0"},
                    "1 hr, 2 hrs, 3 hour, 4 sec, 5 seconds, 6 second": {"1.0", "2.0", "3.0", "4.0", "5.0", "6.0"},
                    "5 s": set(), "5 items": set(), "12 cycles": set()}.items():
        assert unit_numbers(t) == want, (t, unit_numbers(t))
    assert unit_pairs("200 J g-1 and 58 ℃") == {("latent", "200.0"), ("temp", "58.0")}
    assert unit_pairs("180 kJ kg-1 K-1; 0.2 W/(m·K); 1.5 g/cm3") == {("cp", "180.0"), ("cond", "0.2"),
                                                                    ("dens", "1.5")}
    one = lambda chunk, desc: grounding([("node", "N", {"description": desc, "source_id": "c", "file_path": "a"})],
                                        {"c": {"content": chunk}})
    r = one("See page 210 and Fig. 3.", "latent heat 210 kJ/kg")
    assert [(x["missing"], x["bare_only"]) for x in r] == [(["210.0"], ["210.0"])], r
    assert not one("latent heat 210 kJ/kg", "latent heat 210 kJ/kg")
    assert not one("melts at 58.2 K", "melts at 58.2 °C")
    assert [x["missing"] for x in one("58.2 %", "58.2 °C")] == [["58.2"]]
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
