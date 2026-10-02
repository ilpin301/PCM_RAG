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
from decimal import Decimal
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


SUP_RE = re.compile(r"<sup>\s*([-−+]?\d+)\s*</sup>", re.I)
SPACED_RE = re.compile(r"(?<![\w.])\d(?: [\d.])+(?<=\d)(?= ?[°º˚◦∘℃^{%\\A-Za-zµμ])")  # "3 9 . 1 8 °C", "1 8 ^ {..
_SCI = r"(\d+(?:[.,]\d+)?)\s*(?:[×x·*]|\\times)\s*10\s*\^\s*\{?\s*([-+]?\d+)\s*\}?"
SCI_RE = re.compile(rf"(?<![\w.]){_SCI}|(?<![\w.])(\d+(?:\.\d+)?)[eE]([-+]?\d+)(?=\s*[A-Za-z%°])")


def _sci(m):
    a, b = (m.group(1), m.group(2)) if m.group(1) else (m.group(3), m.group(4))
    return format(Decimal(f"{a.replace(',', '.')}E{b}"), "f") if abs(int(b)) <= 30 else m.group(0)


def _prep(text):
    """Normalise OCR / markup variants so unit patterns see plain text: unicode minus and a leading en/em dash
    become '-', HTML <sup>n</sup> -> ^n, LaTeX-spaced digits are closed up, a x 10^b / aEb become decimals."""
    t = (text or "").replace("−", "-")
    t = re.sub(r"(?<![\w.])[–—](?=\d)", "-", t)
    t = SUP_RE.sub(lambda m: "^" + m.group(1).replace("−", "-"), t)
    t = SPACED_RE.sub(lambda m: m.group().replace(" ", ""), t)
    return SCI_RE.sub(_sci, t)


def _signed(s):
    """Normalised numbers of s, '-' kept for a sign (a hyphen glued to a preceding word/digit or following a
    digit is a range / label, not a minus)."""
    out = []
    for m in NUM_RE.finditer(s):
        pre, neg = s[:m.start()], False
        if pre.endswith("-"):
            p = pre[:-1]
            neg = not p or (not re.search(r"[\w/+.]$", p) and not p.rstrip()[-1:].isdigit())
        n = _norm(m.group())
        out.append("-" + n if neg and float(n) else n)
    return out


def unit_pairs(text):
    """{(unit family, normalised signed number)}; every number of a range / +- chain counts."""
    t = _prep(text)
    return {(m.lastgroup, n) for m in UNIT_NUM_RE.finditer(t) for n in _signed(m.group("n"))}


def unit_numbers(text):
    """Normalised values of numbers followed by a unit (sign dropped)."""
    return {n.lstrip("-") for _, n in unit_pairs(text)}


def all_numbers(text):
    return {_norm(x) for x in NUM_RE.findall(text or "")}


# a unit named in a table header / caption without a number: bracketed, after a comma / slash / "in", or the
# whole cell; degree and % symbols count anywhere in a header cell (not in a caption)
_HDR_RE = {f: re.compile(rf"(?:^|[(\[,/]|\bin\s)\s*(?:{rx})\s*(?:[)\]]|$)") for f, rx in UNIT_FAMILIES.items()}
_HDR_SYM = {"temp": re.compile(r"[°º˚◦∘℃]|\\circ"), "pct": re.compile(r"%")}


def _hdr_fams(s, loose=True):
    s = re.sub(r"<[^>]+>", "", s or "").strip()
    return {f for f, rx in _HDR_RE.items() if rx.search(s) or (loose and f in _HDR_SYM and _HDR_SYM[f].search(s))}


def _tables(t):
    """[(caption, rows)] for HTML <table>s and markdown pipe tables; rows = lists of tag-free cell strings."""
    out = []
    for m in re.finditer(r"<table\b.*?</table>", t, re.S | re.I):
        rows = [[re.sub(r"<[^>]+>", "", c) for c in re.findall(r"<t[hd]\b[^>]*>(.*?)</t[hd]>", r, re.S | re.I)]
                for r in re.findall(r"<tr\b.*?</tr>", m.group(), re.S | re.I)]
        cap = re.findall(r"<caption\b[^>]*>(.*?)</caption>", m.group(), re.S | re.I)
        pre = [ln for ln in t[max(0, m.start() - 300):m.start()].splitlines() if ln.strip()]
        out.append((" ".join(cap + pre[-1:]), rows))
    lines, i = t.splitlines(), 0
    while i < len(lines):
        if lines[i].count("|") < 2:
            i += 1
            continue
        j = i
        while j < len(lines) and lines[j].count("|") >= 2:
            j += 1
        rows = [[c.strip() for c in ln.strip().strip("|").split("|")] for ln in lines[i:j]]
        rows = [r for r in rows if not all(re.fullmatch(r":?-{2,}:?", c) for c in r)]
        pre = [ln for ln in lines[:i] if ln.strip()]
        out.append((pre[-1] if pre else "", rows))
        i = j
    return out


def table_pairs(text):
    """(unit family, number) for bare numbers in table cells whose column header, row header (first cell) or
    caption names that unit family, in that order of precedence."""
    res = set()
    for cap, rows in _tables(_prep(text)):
        capf, ncol = _hdr_fams(cap, loose=False), max((len(r) for r in rows), default=0)
        colf = [set().union(*(_hdr_fams(r[i]) for r in rows[:2] if i < len(r))) for i in range(ncol)]
        for r in rows:
            rowf = _hdr_fams(r[0]) if r else set()
            for i, c in enumerate(r):
                for f in colf[i] or (rowf if i else set()) or capf:
                    res.update((f, n) for n in _signed(c))
    return res


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
    """Items whose description (blocks removed) has (unit family, signed number) pairs absent from their source
    chunks. A pair is supported only by the same number WITH a same-family unit (sign preserved) or as a bare
    number in a table cell whose header / caption names that family. missing = the unsupported numbers;
    bare_only = the subset still present in the chunks as a bare number elsewhere (page / figure / reference /
    year or another unit - reviewer hint only, still missing)."""
    res = []
    for kind, key, a in graph:
        desc = BLOCK_RE.sub("", a.get("description") or "")
        pairs = unit_pairs(desc)
        if not pairs:
            continue
        ids = source_ids(a)
        text = "\n".join(chunks[c]["content"] for c in ids if c in chunks)
        missing = sorted({n for _, n in pairs - unit_pairs(text) - table_pairs(text)})
        if missing:
            bare = all_numbers(text)
            res.append({"kind": kind, "key": key, "entity_type": a.get("entity_type", ""),
                        "missing": missing, "bare_only": [n for n in missing if n.lstrip("-") in bare],
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
    # F2: a bare number elsewhere in the chunk never grounds a unit claim
    assert [(x["missing"], x["bare_only"]) for x in one("ref 273 and Smith 2015, 12.5 mm", "melts at 12.5 °C")] \
        == [(["12.5"], ["12.5"])]
    # sign is preserved (en dash / unicode minus count as minus; range hyphen is not a sign)
    assert [x["missing"] for x in one("-5 °C", "5 °C")] == [["5.0"]]
    assert [x["missing"] for x in one("5 °C", "-5 °C")] == [["-5.0"]]
    assert not one("−5 °C", "-5 °C") and not one("–5 °C", "-5 °C") and not one("20-25 °C", "25 °C")
    assert not one("from -5 to -3 °C", "-3 °C")
    # LaTeX-spaced digits, HTML <sup>, scientific notation
    assert not one("avg 3 9 . 1 8 °C", "39.18 °C") and not one("1 8 ^ { \\circ } C", "18 °C")
    assert not one("0.2 W m<sup>-1</sup> K<sup>-1</sup>", "0.2 W/(m·K)")
    assert not one("1.2 × 10^{3} kg/m3", "1200 kg/m3") and not one("1.2 × 10<sup>-3</sup> W/m K", "0.0012 W/m K")
    assert not one("k = 1.5e-1 W/mK", "0.15 W/m K")
    # table cells: column / row header or caption carries the unit; a cell under another header does not
    tb = lambda hdr, cell: f"<table><tr><td>{hdr}</td><td>Name</td></tr><tr><td>{cell}</td><td>PCM</td></tr></table>"
    assert not one(tb("T (°C)", "58.2"), "melts at 58.2 °C")
    assert not one(tb("T (K)", "58.2"), "58.2 K")
    assert [x["missing"] for x in one(tb("T (°C)", "58.2"), "58.2 kJ/kg")] == [["58.2"]]
    assert [x["bare_only"] for x in one(tb("Page", "58.2"), "58.2 °C")] == [["58.2"]]
    assert not one(tb("&Delta;H (kJ/kg)", "210"), "210 kJ/kg")
    assert not one("| Sample | T (°C) |\n|---|---|\n| A | 58.2 |", "58.2 °C")
    assert [x["missing"] for x in one("| T (°C) | Page |\n|---|---|\n| 40 | 58.2 |", "58.2 °C")] == [["58.2"]]
    assert not one("Table 2. Melting points (°C)\n\n<table><tr><td>A</td><td>B</td></tr><tr><td>58.2</td></tr></table>", "58.2 °C")
    assert not one("<table><tr><td>T (°C)</td><td>50</td><td>58.2</td></tr><tr><td>x</td><td>1</td><td>2</td></tr></table>", "58.2 °C")
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
