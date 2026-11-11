"""Build the fresh labelled set for jev_v2_probe (--set fresh): hand-constructed negatives + GLM-only positives.

Labels are fixed by construction. Run this BEFORE any scoring and never edit the written file afterwards.
Negatives pair an invented-but-plausible entity name with the real PubChem cache record of the underlying
element/compound; positives are verify.json same=True rows without a 'by' field (GLM-only).
Writes enrich_cache/jev_fresh_set.json. Nothing touches the graph or verify.json.

Usage: python lightrag/jev_fresh_build.py [--selftest]
"""
import argparse
import collections
import json
import os
import random
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import jev_eval

OUT = os.path.join(jev_eval.DIR, "jev_fresh_set.json")
XRAY_EXCL = {"O", "Fe", "Mg", "K", "Ca", "Na"}
XRAY_LINES = ["Ka1", "Kb", "La1"]
ABC_EXCL = {"Si", "Ge", "Cr"}
ABC_TEMPLATES = ["{e} Atoms", "Single {e} Atom", "{e} Ions", "{e} Nanoclusters", "{e} Slabs"]
VAPOR = {"ethanol": "Ethanol", "methanol": "Methanol", "propan-2-ol": "Isopropanol", "propan-2-one": "Acetone",
         "hexane": "Hexane", "octane": "Octane", "toluene": "Toluene", "benzene": "Benzene"}
OXIDES = {"Fe2O3", "MnO2", "V2O5", "WO3", "Co3O4", "SnO2", "PbO", "MoO3", "NiO", "CeO2"}
OXIDE_EXCL = {"Cu", "Ti"}
ABBREV = {"PA": "hexadecanoic acid", "LA": "dodecanoic acid", "MA": "tetradecanoic acid",
          "AA": "icosanoic acid", "BA": "docosanoic acid"}
LIMITS = {"A": 10, "B": 10, "C": 5, "D": 6, "E": 5}
N_POS = 100


def _elements(records):
    """symbol -> (Capitalised element name, record); bare-symbol formulas with a one-word, non-hydride iupac."""
    out = {}
    for cid in sorted(records):
        r = records[cid]
        if (re.fullmatch(r"[A-Z][a-z]?", r["formula"]) and r["iupac"].isalpha()
                and not r["iupac"].endswith("ane")):
            out.setdefault(r["formula"], (r["iupac"].capitalize(), r))
    return out


def _row(name, rec, same, note):
    return {"name": name, "iupac": rec["iupac"], "formula": rec["formula"], "same": same, "note": note}


def build(records, verify_names, pos_pool, seed=0):
    """records: cid -> {iupac, formula}; verify_names: set of verify.json names;
    pos_pool: jev_eval.load_pairs()-style rows. Returns rows (negatives then positives)."""
    rng = random.Random(seed)
    taken = {n.lower() for n in verify_names}
    rows = []

    def add(name, rec, note, cat):
        if name.lower() in taken:  # absent from verify.json AND unique within the set
            return False
        taken.add(name.lower())
        rows.append(dict(_row(name, rec, False, f"{cat}: {note}")))
        return True

    els = _elements(records)
    syms = sorted(els)

    # A: X-ray lines
    a_syms = [s for s in syms if s not in XRAY_EXCL]
    rng.shuffle(a_syms)
    used_a = set()
    for s in a_syms:
        if len(used_a) >= LIMITS["A"]:
            break
        line = XRAY_LINES[len(used_a) % len(XRAY_LINES)]
        en, rec = els[s]
        if add(f"{en} ({s} {line})", rec, f"xray_line, spectral line of {en}, not the bulk element", "xray_line"):
            used_a.add(s)

    # B: atoms / ions / clusters / slabs
    b_syms = [s for s in syms if s not in ABC_EXCL and s not in used_a]
    rng.shuffle(b_syms)
    nb = 0
    for s in b_syms:
        if nb >= LIMITS["B"]:
            break
        tpl = ABC_TEMPLATES[nb % len(ABC_TEMPLATES)]
        en, rec = els[s]
        if add(tpl.format(e=en), rec, f"{tpl.format(e='X')} is not the bulk element", "atom_ion_cluster_slab"):
            nb += 1

    # C: vapors (water excluded by construction: not in VAPOR)
    vrecs = sorted((cid for cid, r in records.items() if r["iupac"].lower() in VAPOR),
                   key=lambda c: records[c]["iupac"])
    rng.shuffle(vrecs)
    nc = 0
    for cid in vrecs:
        if nc >= LIMITS["C"]:
            break
        rec = records[cid]
        if add(f"{VAPOR[rec['iupac'].lower()]} Vapor", rec, f"vapor phase of {rec['iupac']}", "vapor"):
            nc += 1

    # D: ambiguous oxides
    drecs = sorted((cid for cid, r in records.items() if r["formula"] in OXIDES), key=lambda c: records[c]["formula"])
    rng.shuffle(drecs)
    nd = 0
    for cid in drecs:
        if nd >= LIMITS["D"]:
            break
        rec = records[cid]
        sym = [e for e in re.findall(r"[A-Z][a-z]?", rec["formula"]) if e != "O"]
        if len(sym) != 1 or sym[0] in OXIDE_EXCL or sym[0] not in els:
            continue
        en = els[sym[0]][0]
        if add(f"{en} Oxide", rec, f"{en} has several oxides; paired record is {rec['iupac']} ({rec['formula']})",
               "ambiguous_oxide"):
            nd += 1

    # E: ambiguous 2-letter abbreviations
    ne = 0
    by_iupac = {r["iupac"].lower(): r for r in records.values()}
    for code, iu in ABBREV.items():
        if ne >= LIMITS["E"] or iu not in by_iupac:
            continue
        rec = by_iupac[iu]
        if add(code, rec, f"{code} is ambiguous; paired record is {iu}", "ambiguous_abbrev"):
            ne += 1

    # positives: GLM-only trues with an iupac
    pool = sorted((r for r in pos_pool if r["same"] and not r["by"] and r["iupac"]), key=lambda r: r["name"])
    for r in rng.sample(pool, min(N_POS, len(pool))):
        rows.append(_row(r["name"], r, True, "glm_only_true"))
    return rows


def counts(rows):
    c = collections.Counter(r["note"].split(":")[0] for r in rows)
    return dict(c)


# ------------------------------------------------------------------ selftest
_N = 0


def check(cond, msg):
    global _N
    assert cond, msg
    _N += 1


def _selftest():
    forms = {"copper": "Cu", "iron": "Fe", "zinc": "Zn", "silver": "Ag", "gold": "Au", "nickel": "Ni",
             "cerium": "Ce", "silicon": "Si", "sodium": "Na", "methane": "C", "tin": "Sn"}
    recs = {i: {"iupac": n, "formula": f} for i, (n, f) in enumerate(forms.items(), 1)}
    recs.update({100: {"iupac": "ethanol", "formula": "C2H6O"}, 101: {"iupac": "oxidane", "formula": "H2O"},
                 102: {"iupac": "toluene", "formula": "C7H8"}, 103: {"iupac": "nickel(2+);oxygen(2-)", "formula": "NiO"},
                 104: {"iupac": "dioxocerium", "formula": "CeO2"}, 105: {"iupac": "oxocopper", "formula": "CuO"},
                 106: {"iupac": "hexadecanoic acid", "formula": "C16H32O2"},
                 107: {"iupac": "dodecanoic acid", "formula": "C12H24O2"}})
    pool = [{"name": f"P{i}", "same": True, "by": None, "iupac": f"i{i}", "formula": "X"} for i in range(150)]
    pool += [{"name": "G", "same": True, "by": "claude-review", "iupac": "i", "formula": "X"},
             {"name": "N", "same": True, "by": None, "iupac": "", "formula": "X"},
             {"name": "F", "same": False, "by": None, "iupac": "i", "formula": "X"}]
    vn = {"Zinc Oxide", "Copper Atoms"} | {p["name"] for p in pool}
    rows = build(recs, vn, pool, 0)
    rows2 = build(recs, vn, pool, 0)
    check(rows == rows2, "deterministic for a fixed seed")
    cnt = counts(rows)
    check(cnt["xray_line"] == 8, "xray: 8 eligible elements (no Fe/Na, no methane)")
    check(cnt["glm_only_true"] == 100, "100 positives")
    check(cnt["vapor"] == 2 and not any("Water" in r["name"] for r in rows), "vapor: no water")
    check(cnt["ambiguous_oxide"] == 2 and cnt.get("atom_ion_cluster_slab", 0) <= 10, "oxide count (Cu excluded)")
    check(not any(r["name"] == "Copper Oxide" for r in rows), "copper oxide excluded")
    check(cnt["ambiguous_abbrev"] == 2, "abbrev only with records present (PA, LA)")
    names = [r["name"].lower() for r in rows]
    check(len(set(names)) == len(names), "names unique")
    negs = [r for r in rows if not r["same"]]
    check(all(r["name"].lower() not in {n.lower() for n in vn} for r in negs), "negatives absent from verify")
    check(all(r["note"].split(":")[0] in LIMITS_CATS for r in negs), "every negative note names its category")
    check(all(r["same"] is False for r in negs) and all(r["same"] is True for r in rows[len(negs):]), "labels")
    xr = [r["name"] for r in rows if r["note"].startswith("xray_line")]
    check(any("Ka1" in n for n in xr) and any("Kb" in n for n in xr) and any("La1" in n for n in xr), "line rotation")
    check(not any(" (Fe " in n or " (Na " in n for n in xr), "excluded symbols absent")
    used_x = {re.search(r"\((\w+) ", n).group(1) for n in xr}
    b = [r["name"] for r in rows if r["note"].startswith("atom_ion")]
    check(not any(s in " ".join(b) for s in ("Silicon", "Germanium", "Chromium")), "B excludes Si/Ge/Cr")
    check(len(used_x) == len(xr), "A elements distinct")
    check(any("NiO" in r["note"] or "nickel" in r["note"] for r in rows if r["note"].startswith("ambiguous_oxide")),
          "oxide note names paired record")
    check(not any(r["name"] in ("N", "G", "F") for r in rows), "positives exclude by-field/no-iupac/False rows")
    check(_elements(recs).get("C") is None, "hydride-named element records skipped")
    print(f"selftest OK ({_N} asserts)")


LIMITS_CATS = {"xray_line", "atom_ion_cluster_slab", "vapor", "ambiguous_oxide", "ambiguous_abbrev"}


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        _selftest()
        return 0
    pairs, _ = jev_eval.load_pairs()
    with open(os.path.join(jev_eval.DIR, "verify.json"), encoding="utf-8") as f:
        verify = json.load(f)
    rows = build(jev_eval.load_records(), set(verify), pairs, 0)
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(rows, f, ensure_ascii=False, indent=1)
    c = counts(rows)
    for k, v in sorted(c.items()):
        print(f"{k}: {v}")
    print(f"total: {len(rows)} (negatives {sum(not r['same'] for r in rows)}, positives {sum(r['same'] for r in rows)})")
    print(f"written: {OUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
