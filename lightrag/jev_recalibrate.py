"""Post-ingest report: how Jev's shadow probabilities compare with Claude's final verdicts.

Reads enrich_cache/jev_shadow.json + verify.json, writes only its own report, history and cache files.
It never changes a threshold, prompt, label or graph; any change of the review rule needs the user's OK.

Usage: python lightrag/jev_recalibrate.py [--pv v2] [--compare PV] | --selftest
"""
import argparse
import asyncio
import contextlib
import datetime
import io
import json
import os
import sys
import tempfile

import httpx

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import jev_eval
import jev_v2_probe
import jev_verify

DIR = jev_eval.DIR
SHADOW = os.path.join(DIR, "jev_shadow.json")
VERIFY = os.path.join(DIR, "verify.json")
REPORT_NAME = "jev_recalibrate_report.txt"
HISTORY_NAME = "jev_recalibrate_history.jsonl"
CACHE_NAME = "jev_recalibrate_cache.json"
GRID = [0.70, 0.75, 0.80, 0.85, 0.90, 0.95, 0.97, 0.99]
NEED_GLM_YES = 100
EPS = 1e-9


# ------------------------------------------------------------------ data
def load_json(path):
    """(status, dict): status is ok | empty | missing | corrupt; an empty file or {} gives (empty, {})."""
    try:
        with open(path, encoding="utf-8") as f:
            txt = f.read()
        data = json.loads(txt) if txt.strip() else {}
    except FileNotFoundError:
        return "missing", {}
    except (OSError, ValueError):
        return "corrupt", {}
    if not isinstance(data, dict):
        return "corrupt", {}
    return ("ok" if data else "empty"), data


def join(shadow, verify, pv):
    """(reviewed & scored entities, counts). Reviewed = claude-review verdict in verify.json with the same cid."""
    c = {"shadow": len(shadow), "other_pv": 0, "unreviewed": 0, "unscored": 0}
    ents = []
    for name, e in shadow.items():
        if not isinstance(e, dict) or e.get("pv") != pv:
            c["other_pv"] += 1
            continue
        v = verify.get(name)
        if not (isinstance(v, dict) and v.get("by") == "claude-review" and e.get("cid") is not None
                and str(v.get("cid")) == str(e["cid"])):
            c["unreviewed"] += 1
            continue
        p = e.get("p")
        if isinstance(p, bool) or not isinstance(p, (int, float)):  # null: never accepted nor rejected
            c["unscored"] += 1
            continue
        ents.append({"name": name, "cid": e["cid"], "p": float(p), "glm": bool(e.get("glm_same")),
                     "final": bool(v.get("same"))})
    return ents, c


# ------------------------------------------------------------------ statistics
def jev_bin(p):
    """Ten 0.1 bins, lower edge inclusive: p=0.1 -> bin 1 (0.1-0.2); p=1.0 joins the last bin."""
    return min(int(p * 10 + EPS), 9)


def auc(pos, neg):
    """P(a Claude-yes outranks a Claude-no), ties count 0.5; None if either class is empty."""
    if not pos or not neg:
        return None
    return sum(1.0 if x > y else 0.5 if x == y else 0.0 for x in pos for y in neg) / (len(pos) * len(neg))


def analyze(ents):
    glm_yes = [e for e in ents if e["glm"]]
    pos = [e for e in glm_yes if e["final"]]
    neg = [e for e in glm_yes if not e["final"]]
    sweep = []
    for h in GRID:
        fa = sum(e["p"] >= h for e in neg)
        saves = sum(e["p"] >= h for e in pos)
        sweep.append({"hi": h, "fa": fa, "ub": jev_eval.upper_bound(fa, len(neg)), "saves": saves,
                      "cov": saves / len(pos) if pos else None})
    mx = max((e["p"] for e in ents if not e["final"]), default=None)  # all reviewed Claude-no, GLM yes or not
    sugg = next((r for r in sweep if mx is not None and r["fa"] == 0 and mx <= r["hi"] - 0.05 + EPS), None)
    bins = [[0, 0] for _ in range(10)]
    for e in ents:
        b = bins[jev_bin(e["p"])]
        b[0] += 1
        b[1] += e["final"]
    return {"n": len(ents), "n_yes": sum(e["final"] for e in ents), "n_no": sum(not e["final"] for e in ents),
            "glm_yes": len(glm_yes), "pos": len(pos), "neg": len(neg), "sweep": sweep, "mx": mx, "sugg": sugg,
            "bins": [tuple(b) for b in bins],
            "dis": sorted((e for e in ents if (e["p"] >= 0.5) != e["final"]), key=lambda e: -e["p"]),
            "auc": auc([e["p"] for e in ents if e["final"]], [e["p"] for e in ents if not e["final"]])}


# ------------------------------------------------------------------ report
def fmt(x, spec):
    return "n/a" if x is None else format(x, spec)


def build_report(a, c, pv):
    L = ["Jev recalibration report", "========================",
         f"read-only: changes no threshold, prompt, label or graph. shadow prompt version pv={pv}", "",
         "Counts",
         f"  shadow entries: {c['shadow']}",
         f"  other prompt version (pv != {pv}): {c['other_pv']}",
         f"  unreviewed: {c['unreviewed']} (no claude-review verdict with the same cid; left out)",
         f"  unscored: {c['unscored']} (reviewed, p null, pending backfill; never accepted or rejected)",
         f"  reviewed & scored: {a['n']}  (Claude-yes {a['n_yes']}, Claude-no {a['n_no']})",
         f"  of those with GLM yes: {a['glm_yes']} (Claude-yes {a['pos']}, Claude-no {a['neg']})", "",
         ("Sweep: joint false accept = reviewed, GLM yes, p>=hi, Claude no. ub95 = one-sided 95% "
          f"Clopper-Pearson bound, n = reviewed Claude-no entities with GLM yes = {a['neg']}. "
          f"saves / coverage = reviewed GLM-yes Claude-yes entities (n={a['pos']}) with p>=hi."),
         "hi     joint_FA  ub95   saves  coverage"]
    L += [f"{r['hi']:.2f}   {r['fa']:>8}  {r['ub']:.3f}  {r['saves']:>5}  {fmt(r['cov'], '.3f'):>8}"
          for r in a["sweep"]]
    L += ["", "Calibration (all reviewed & scored; bins are lower-edge inclusive, p=0.1 is in 0.1-0.2)",
          "p bin      n  share Claude-yes"]
    L += [f"{b / 10:.1f}-{(b + 1) / 10:.1f} {n:>6}  {fmt(y / n if n else None, '.3f')}"
          for b, (n, y) in enumerate(a["bins"])]
    L += ["", "Disagreements with the 0.5 cut (name | cid | p | glm_same | final)"]
    L += [f"{e['name']} | {e['cid']} | {e['p']:.3f} | {e['glm']} | {e['final']}" for e in a["dis"]] or ["(none)"]
    s = a["sugg"]
    L += ["", (f"Suggested hi: {s['hi']:.2f} (smallest grid hi with 0 joint false accepts and highest Claude-no p "
               f"{a['mx']:.3f} <= hi-0.05)" if s else
               "Suggested hi: none (no grid hi has 0 joint false accepts with highest Claude-no p <= hi-0.05, "
               "or no Claude-no entities)")]
    if a["glm_yes"] >= NEED_GLM_YES and s:
        L.append(f"STATUS: option (b) numbers met at hi={s['hi']:.2f} (joint FA 0 of {a['neg']}, ub95 {s['ub']:.3f}) "
                 "- needs the user's explicit OK, and an edit of the CLAUDE.md rule")
    else:
        L.append("STATUS: option (a) only (Jev may reorder the review queue, never skip it); "
                 f"reviewed glm_yes={a['glm_yes']} of {NEED_GLM_YES} needed")
    return "\n".join(L) + "\n"


def write_atomic(path, txt):
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8", newline="\n") as f:
        f.write(txt)
    os.replace(tmp, path)


def append_history(path, rec):
    """Append one JSON line unless the last line is identical apart from the date."""
    last = None
    try:
        with open(path, encoding="utf-8") as f:
            lines = [x for x in f.read().splitlines() if x.strip()]
        last = json.loads(lines[-1]) if lines else None
    except (FileNotFoundError, ValueError):
        pass
    if isinstance(last, dict) and {k: v for k, v in last.items() if k != "date"} == {
            k: v for k, v in rec.items() if k != "date"}:
        return False
    with open(path, "a", encoding="utf-8", newline="\n") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    return True


# ------------------------------------------------------------------ --compare
def compare(ents, pv, new_pv, outdir, records=None):
    """Re-score the reviewed & scored entities with new_pv; (text, {"shadow": m, "new": m})."""
    records = jev_eval.load_records() if records is None else records
    os.makedirs(outdir, exist_ok=True)
    path = os.path.join(outdir, CACHE_NAME)
    cache = jev_v2_probe.load_cache(path)
    rows = []
    for e in ents:
        rec = records.get(int(e["cid"]), {}) if str(e["cid"]).isdigit() else {}
        rows.append({"name": e["name"], "iupac": rec.get("iupac", ""), "formula": rec.get("formula", "")})

    async def go():
        async with httpx.AsyncClient(trust_env=False) as client:  # score() calls jev_verify.jev_same(version=)
            await jev_v2_probe.score(rows, cache, new_pv, path, client)

    asyncio.run(go())
    both = [(e, cache[jev_v2_probe.key(r, new_pv)]) for e, r in zip(ents, rows, strict=True)
            if jev_v2_probe.key(r, new_pv) in cache]
    sets = {"shadow": [e for e, _ in both], "new": [dict(e, p=p) for e, p in both]}
    m = {}
    for k, es in sets.items():
        a = analyze(es)
        s = a["sugg"]
        m[k] = {"n": a["n"], "auc": a["auc"], "suggested": s["hi"] if s else None,
                "fa": s["fa"] if s else None, "coverage": s["cov"] if s else None}
    L = ["", (f"Compare: {len(both)} reviewed & scored entities scored under both prompt versions "
              f"({len(ents) - len(both)} without a PV score left out)"),
         "pv        AUC    suggested_hi  joint_FA  coverage"]
    for k, label in (("shadow", pv), ("new", new_pv)):
        r = m[k]
        L.append(f"{label:<8} {fmt(r['auc'], '.3f'):>6}  {fmt(r['suggested'], '.2f'):>12}  "
                 f"{fmt(r['fa'], 'd'):>8}  {fmt(r['coverage'], '.3f'):>8}")
    return "\n".join(L) + "\n", m


# ------------------------------------------------------------------ commands
def run(shadow_path, verify_path, outdir, pv, compare_pv=None):
    if compare_pv is not None:
        if compare_pv not in jev_verify.QUESTION_TEXT:
            print(f"--compare {compare_pv!r}: unknown prompt version, known: {sorted(jev_verify.QUESTION_TEXT)}",
                  file=sys.stderr)
            return 2
        if not os.environ.get("TYPESAFE_API_KEY"):
            print("--compare needs TYPESAFE_API_KEY", file=sys.stderr)
            return 2
    st, shadow = load_json(shadow_path)
    if st == "corrupt":
        print(f"corrupt JSON in {shadow_path}; fix or delete it", file=sys.stderr)
        return 2
    if st != "ok":
        print(f"no shadow data yet ({shadow_path} missing/empty); run an ingest's PubChem collect "
              "with --jev-shadow first")
        return 0
    st, verify = load_json(verify_path)
    if st in ("missing", "corrupt"):
        print(f"{st} verify file {verify_path}", file=sys.stderr)
        return 2
    ents, c = join(shadow, verify, pv)
    a = analyze(ents)
    txt = build_report(a, c, pv)
    os.makedirs(outdir, exist_ok=True)
    write_atomic(os.path.join(outdir, REPORT_NAME), txt)
    print(txt, end="")
    s = a["sugg"]
    append_history(os.path.join(outdir, HISTORY_NAME), {
        "date": datetime.date.today().isoformat(), "pv": pv, "reviewed": a["n"],
        "joint_fa_at_suggested": s["fa"] if s else None, "suggested_hi": s["hi"] if s else None,
        "coverage_at_suggested": s["cov"] if s else None, "glm_yes_reviewed": a["glm_yes"]})
    if compare_pv is not None:
        print(compare(ents, pv, compare_pv, outdir)[0], end="")
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--shadow", default=SHADOW)
    ap.add_argument("--verify", default=VERIFY)
    ap.add_argument("--outdir", default=DIR)
    ap.add_argument("--pv", default="v2", help="shadow prompt version to use (default v2)")
    ap.add_argument("--compare", metavar="PV", help="re-score reviewed entities with PV (live API)")
    a = ap.parse_args(argv)
    if a.selftest:
        _selftest()
        return 0
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")  # cp1251 console vs subscript digits
    return run(a.shadow, a.verify, a.outdir, a.pv, a.compare)


# ------------------------------------------------------------------ selftest
_N = 0


def check(cond, msg):
    global _N
    assert cond, msg
    _N += 1


def _put(sh, vf, name, cid, p, glm, final, pv="v2", by="claude-review", vcid=None, inverify=True):
    sh[name] = {"cid": cid, "p": p, "glm_same": glm, "model": "jev-latest", "pv": pv}
    if inverify:
        vf[name] = {"cid": cid if vcid is None else vcid, "same": final}
        if by:
            vf[name]["by"] = by


def _fixture():
    sh, vf = {}, {}
    for i, p in enumerate((0.99, 0.96, 0.92, 0.88, 0.82, 0.72, 0.4)):
        _put(sh, vf, f"Y{i + 1}", 100 + i, p, True, True)  # Claude yes, GLM yes
    for i, p in enumerate((0.93, 0.5, 0.2)):
        _put(sh, vf, f"N{i + 1}", 200 + i, p, True, False)  # Claude no, GLM yes
    _put(sh, vf, "G1-α", 300, 0.6, False, True)  # GLM no, Claude yes
    _put(sh, vf, "G2", 301, 0.1, False, False)  # GLM no, Claude no
    _put(sh, vf, "U1", 400, 0.9, True, False, inverify=False)  # not in verify.json
    _put(sh, vf, "U2", 401, 0.9, True, False, vcid=999)  # cid mismatch
    _put(sh, vf, "U3", 402, 0.9, True, False, by="glm")  # not claude-review
    _put(sh, vf, "U4", 403, 0.9, True, False, by=None)  # by missing
    _put(sh, vf, "R0", 500, None, True, True)  # reviewed, p null
    _put(sh, vf, "O1", 600, 0.99, True, False, pv="v1")  # other prompt version
    return sh, vf


def _ents(*rows):
    return [{"name": f"e{i}", "cid": i, "p": p, "glm": g, "final": f} for i, (p, g, f) in enumerate(rows)]


def _status_fixture(n_glm_yes, neg_p):
    sh, vf = {}, {}
    for i in range(n_glm_yes - 1):
        _put(sh, vf, f"Y{i}", i, 0.99, True, True)
    _put(sh, vf, "NEG", 9999, neg_p, True, False)
    return sh, vf


def _call(sp, vp, outdir, pv="v2"):
    out, err = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
        rc = run(sp, vp, outdir, pv)
    return rc, out.getvalue(), err.getvalue()


def _dump(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)


def _run(sh, vf, d, pv="v2"):
    sp, vp = os.path.join(d, "shadow.json"), os.path.join(d, "verify.json")
    _dump(sp, sh)
    _dump(vp, vf)
    return _call(sp, vp, os.path.join(d, "out"), pv)


def _history(d):
    with open(os.path.join(d, "out", "jev_recalibrate_history.jsonl"), encoding="utf-8") as f:
        return [json.loads(x) for x in f.read().splitlines()]


def _selftest_compare(d):
    ents = _ents((0.9, True, True), (0.5, True, False), (0.5, False, True), (0.1, True, False))
    for e, n in zip(ents, "ABCD", strict=True):
        e["name"] = n
        e["cid"] = ord(n) - 64
    records = {i: {"iupac": f"i{i}", "formula": f"F{i}"} for i in range(1, 5)}
    scores = {"A": 0.95, "B": 0.2, "C": 0.8, "D": None}
    calls = []

    async def stub(client, name, facts, breaker=None, version=jev_verify.PROMPT_VERSION):
        calls.append((name, version, facts))
        return scores[name]

    saved = jev_verify.jev_same
    jev_verify.jev_same = stub
    try:
        txt, m = compare(ents, "v2", "v1", d, records)
        check(len(calls) == 4 and {c[1] for c in calls} == {"v1"}, "compare scores every reviewed entity with PV")
        check(next(c[2] for c in calls if c[0] == "A") == {"iupac": "i1", "formula": "F1"}, "facts from records")
        cache = jev_v2_probe.load_cache(os.path.join(d, "jev_recalibrate_cache.json"))
        check(cache == {"A|i1|F1|jev-latest|v1": 0.95, "B|i2|F2|jev-latest|v1": 0.2,
                        "C|i3|F3|jev-latest|v1": 0.8}, "cache keyed name|iupac|formula|model|pv, None not cached")
        check(m["shadow"]["n"] == 3 and m["new"]["n"] == 3, "compared on entities scored under both")
        check(m["shadow"]["auc"] == 0.75 and m["new"]["auc"] == 1.0, "AUC per prompt version")
        check(m["new"]["suggested"] == 0.7 and m["new"]["coverage"] == 1.0 and m["new"]["fa"] == 0,
              "suggested/coverage/FA for PV")
        check("1 without a PV score left out" in txt and "0.750" in txt and "1.000" in txt, "compare text")
        calls.clear()
        compare(ents, "v2", "v1", d, records)
        check([c[0] for c in calls] == ["D"], "rerun: cache hits, only the None is retried")
    finally:
        jev_verify.jev_same = saved


def _selftest():
    # join logic
    sh, vf = _fixture()
    ents, c = join(sh, vf, "v2")
    check(c == {"shadow": 18, "other_pv": 1, "unreviewed": 4, "unscored": 1}, "join counts")
    names = {e["name"] for e in ents}
    check(len(ents) == 12 and not names & {"U1", "U2", "U3", "U4", "R0", "O1"}, "join keeps reviewed and scored only")
    check(next(e for e in ents if e["name"] == "N1") == {"name": "N1", "cid": 200, "p": 0.93, "glm": True,
                                                         "final": False}, "entity shape")
    e1, c1 = join(sh, vf, "v1")
    check([e["name"] for e in e1] == ["O1"] and c1["other_pv"] == 17, "pv filter")

    # sweep numbers by hand; p null never accepted; other pv and unreviewed never counted
    a = analyze(ents)
    check([r["hi"] for r in a["sweep"]] == [0.70, 0.75, 0.80, 0.85, 0.90, 0.95, 0.97, 0.99], "grid")
    check([r["fa"] for r in a["sweep"]] == [1, 1, 1, 1, 1, 0, 0, 0], "joint false accepts")
    check([r["saves"] for r in a["sweep"]] == [6, 5, 5, 4, 3, 2, 1, 1], "saves")
    check(a["sweep"][0]["cov"] == 6 / 7 and a["sweep"][7]["cov"] == 1 / 7, "coverage over 7 scored GLM-yes Claude-yes")
    check(a["neg"] == 3 and a["pos"] == 7 and a["glm_yes"] == 10 and a["n"] == 12, "split counts")
    check((a["n_yes"], a["n_no"]) == (8, 4), "Claude yes/no split")
    check(abs(a["sweep"][5]["ub"] - jev_eval.upper_bound(0, 3)) < 1e-12 and a["sweep"][0]["ub"] > 0.3, "ub with n=3")

    # calibration bins: lower edge inclusive, upper exclusive, 1.0 in the last bin
    check(all(jev_bin(k / 10) == k for k in range(10)), "p=k/10 goes to bin k (p=0.1 -> 0.1-0.2)")
    check(jev_bin(0.0999) == 0 and jev_bin(1.0) == 9 and jev_bin(0.0) == 0, "bin edges")
    check(a["bins"] == [(0, 0), (1, 0), (1, 0), (0, 0), (1, 1), (1, 0), (1, 1), (1, 1), (2, 2), (4, 3)],
          "calibration bins")

    # disagreements (p>=0.5 inclusive and Claude no; p<0.5 and Claude yes), sorted by p descending
    check([e["name"] for e in a["dis"]] == ["N1", "N2", "Y7"], "disagreement list")

    # AUC
    check(auc([0.9, 0.5], [0.5, 0.1]) == 0.875, "AUC with one tie")
    check(auc([], [0.1]) is None and auc([0.1], []) is None, "AUC undefined without both classes")
    check(a["auc"] == 25 / 32, "AUC on the fixture")

    # suggested-hi rule
    check(a["sugg"]["hi"] == 0.99 and a["mx"] == 0.93, "highest negative 0.93 <= hi-0.05 -> 0.99, not 0.95")
    check(analyze(_ents((0.6, True, False), (0.9, True, True)))["sugg"]["hi"] == 0.70, "max neg 0.6 -> 0.70")
    check(analyze(_ents((0.65, True, False)))["sugg"]["hi"] == 0.70, "highest negative exactly hi-0.05 ok")
    check(analyze(_ents((0.66, True, False)))["sugg"]["hi"] == 0.75, "highest negative 0.66 -> 0.75")
    check(analyze(_ents((0.97, False, False), (0.9, True, True)))["sugg"] is None,
          "GLM-no negative with p 0.97 still blocks every hi")
    check(analyze(_ents((0.99, True, False)))["sugg"] is None, "joint FA at every hi -> none")
    check(analyze(_ents((0.9, True, True)))["sugg"] is None, "no negatives -> none")

    with tempfile.TemporaryDirectory() as d:
        # full run on the fixture: stdout == report file, utf-8, history
        rc, out, err = _run(sh, vf, d)
        rp = os.path.join(d, "out", "jev_recalibrate_report.txt")
        with open(rp, encoding="utf-8") as f:
            check(rc == 0 and err == "" and f.read() == out, "stdout equals report file")
        for s in ("shadow entries: 18", "other prompt version (pv != v2): 1", "unreviewed: 4", "unscored",
                  "reviewed & scored: 12", "Claude-yes 8, Claude-no 4", "with GLM yes = 3",
                  f"{jev_eval.upper_bound(0, 3):.3f}", "0.7-0.8", "n/a", "N1 | 200 | 0.930 | True | False",
                  "Y7 | 106 | 0.400 | True | True", "Suggested hi: 0.99"):
            check(s in out, f"report contains {s!r}")
        check("G1-α" not in out.split("Disagreements")[1], "agreeing entity not listed as disagreement")
        check("STATUS: option (a) only (Jev may reorder the review queue, never skip it); "
              "reviewed glm_yes=10 of 100 needed" in out, "status (a) on the fixture")
        h = _history(d)
        check(len(h) == 1 and set(h[0]) == {"date", "pv", "reviewed", "joint_fa_at_suggested", "suggested_hi",
                                            "coverage_at_suggested", "glm_yes_reviewed"}, "history shape")
        check((h[0]["pv"], h[0]["reviewed"], h[0]["joint_fa_at_suggested"], h[0]["suggested_hi"],
               h[0]["coverage_at_suggested"], h[0]["glm_yes_reviewed"]) == ("v2", 12, 0, 0.99, 1 / 7, 10),
              "history values")
        datetime.date.fromisoformat(h[0]["date"])

        # history dedupe: identical apart from date -> no new line; changed numbers -> new line
        hp = os.path.join(d, "out", "jev_recalibrate_history.jsonl")
        h[0]["date"] = "2000-01-01"
        with open(hp, "w", encoding="utf-8") as f:
            f.write(json.dumps(h[0]) + "\n")
        _run(sh, vf, d)
        h = _history(d)
        check(len(h) == 1 and h[0]["date"] == "2000-01-01", "history dedupe ignores the date")
        _put(sh, vf, "Y8", 108, 0.99, True, True)
        _run(sh, vf, d)
        h = _history(d)
        check(len(h) == 2 and h[1]["reviewed"] == 13, "history appends when numbers change")
        check(os.listdir(os.path.join(d, "out")).count("jev_recalibrate_report.txt.tmp") == 0, "no temp file left")

    # STATUS branches, exactly 99 vs 100 reviewed glm_yes
    with tempfile.TemporaryDirectory() as d:
        rc, out, _ = _run(*_status_fixture(100, 0.2), d)
        st = next(x for x in out.splitlines() if x.startswith("STATUS:"))
        check(st == "STATUS: option (b) numbers met at hi=0.70 (joint FA 0 of 1, ub95 0.950) - needs the "
                    "user's explicit OK, and an edit of the CLAUDE.md rule", "status (b) at exactly 100")
    with tempfile.TemporaryDirectory() as d:
        rc, out, _ = _run(*_status_fixture(99, 0.2), d)
        st = next(x for x in out.splitlines() if x.startswith("STATUS:"))
        check(st == "STATUS: option (a) only (Jev may reorder the review queue, never skip it); "
                    "reviewed glm_yes=99 of 100 needed", "status (a) at 99")
    with tempfile.TemporaryDirectory() as d:
        rc, out, _ = _run(*_status_fixture(100, 0.99), d)
        st = next(x for x in out.splitlines() if x.startswith("STATUS:"))
        check(st.startswith("STATUS: option (a) only") and "glm_yes=100 of 100" in st and "Suggested hi: none" in out,
              "status (a) at 100 without a suggested hi")

    # missing / empty / corrupt shadow file; verify.json problems
    with tempfile.TemporaryDirectory() as d:
        sp, vp, od = (os.path.join(d, "shadow.json"), os.path.join(d, "verify.json"), os.path.join(d, "out"))
        _dump(vp, {})
        rc, out, err = _call(sp, vp, od)
        check(rc == 0 and out == f"no shadow data yet ({sp} missing/empty); run an ingest's PubChem collect "
                                 "with --jev-shadow first\n" and err == "", "missing shadow -> clean message, exit 0")
        check(not os.path.exists(od), "nothing written without shadow data")
        for body in ("", "  \n", "{}"):
            with open(sp, "w", encoding="utf-8") as f:
                f.write(body)
            rc, out, _ = _call(sp, vp, od)
            check(rc == 0 and out.startswith("no shadow data yet (") and not os.path.exists(od), f"empty {body!r}")
        for body in ("{nope", "[1, 2]"):
            with open(sp, "w", encoding="utf-8") as f:
                f.write(body)
            rc, out, err = _call(sp, vp, od)
            check(rc == 2 and out == "" and "corrupt" in err and sp in err, f"corrupt shadow {body!r} -> exit 2")
        _dump(sp, sh)
        os.remove(vp)
        rc, out, err = _call(sp, vp, od)
        check(rc == 2 and "verify" in err and "missing" in err, "missing verify.json -> exit 2")
        with open(vp, "w", encoding="utf-8") as f:
            f.write("{nope")
        rc, out, err = _call(sp, vp, od)
        check(rc == 2 and "corrupt" in err, "corrupt verify.json -> exit 2")
        _dump(vp, {})
        rc, out, err = _call(sp, vp, od)
        check(rc == 0 and "reviewed & scored: 0" in out and "Suggested hi: none" in out, "empty verify -> nothing reviewed")

    # --compare (stubbed jev_same, no network)
    with tempfile.TemporaryDirectory() as d:
        _selftest_compare(d)
    old = os.environ.pop("TYPESAFE_API_KEY", None)
    try:
        err = io.StringIO()
        with contextlib.redirect_stderr(err):
            rc9 = main(["--compare", "v9"])
            rck = main(["--compare", "v1"])
        check(rc9 == 2 and "v9" in err.getvalue(), "unknown PV -> exit 2")
        check(rck == 2 and "TYPESAFE_API_KEY" in err.getvalue(), "missing key -> exit 2")
    finally:
        if old is not None:
            os.environ["TYPESAFE_API_KEY"] = old
    print(f"selftest OK ({_N} asserts)")


if __name__ == "__main__":
    sys.exit(main())
