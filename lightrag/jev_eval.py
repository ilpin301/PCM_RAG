"""Evaluate Jev (jev_verify) against the PubChem same-substance gold labels.

Reads enrich_cache/verify.json + <cid>.json, scores (entity, record) pairs with jev_verify.jev_same,
adds synthetic wrong-record negatives, writes enrich_cache/jev_eval_report.txt with the gate (i)-(iii).
Nothing here writes graph or verdicts. Gate (iv) is a manual hand-check.

Usage: python lightrag/jev_eval.py --selftest | --build-synthetic | --run | --report [--lo L] [--hi H]
"""
import argparse
import asyncio
import collections
import io
import itertools
import json
import math
import os
import random
import re
import sys
import tempfile
import time

import httpx

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import jev_verify

DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "enrich_cache")
STORE = os.path.join(DIR, "jev_eval.json")
REPORT = os.path.join(DIR, "jev_eval_report.txt")
GRID = [0.60, 0.65, 0.70, 0.75, 0.80, 0.85, 0.90, 0.95, 0.97, 0.99]
COST_PER_M = 0.042  # USD per 1M input tokens

FORM_RE = re.compile("Nanoparticle|Powder|Nanofluid|Nanowire|Flakes|Nanotube|Nanosheet|Nanocomposite", re.IGNORECASE)
_HO = {"H", "O"}


# ------------------------------------------------------------------ data
def load_records():
    """cid -> {"iupac", "formula"} from the digit-stem cache files (others are ignored)."""
    out = {}
    for fn in sorted(os.listdir(DIR)):
        stem, ext = os.path.splitext(fn)
        if ext != ".json" or not stem.isdigit():
            continue
        try:
            with open(os.path.join(DIR, fn), encoding="utf-8") as f:
                d = json.load(f)
        except (OSError, ValueError):
            continue
        if isinstance(d, dict):
            out[int(stem)] = {"iupac": str(d.get("iupac") or ""), "formula": str(d.get("formula") or "")}
    return out


def load_pairs():
    """(rows, skipped): verify.json entries that have a cache file; skipped = those without."""
    with open(os.path.join(DIR, "verify.json"), encoding="utf-8") as f:
        verify = json.load(f)
    records = load_records()
    rows, skipped = [], 0
    for name, e in verify.items():
        try:
            cid = int(e["cid"])
            rec = records[cid]
        except (KeyError, TypeError, ValueError):
            skipped += 1
            continue
        rows.append({"name": name, "cid": cid, "same": bool(e.get("same")), "by": e.get("by"),
                     "iupac": rec["iupac"], "formula": rec["formula"]})
    return rows, skipped


def make_key(name, cid):
    return f"{name}|{cid}|{jev_verify.MODEL}|{jev_verify.PROMPT_VERSION}"


def _empty_store():
    return {"synthetic": [], "cache": {}, "meta": {}}


def load_store(path=STORE):
    try:
        with open(path, encoding="utf-8") as f:
            d = json.load(f)
    except (OSError, ValueError):
        return _empty_store()
    if not isinstance(d, dict):
        return _empty_store()
    for k, v in _empty_store().items():
        if not isinstance(d.get(k), type(v)):
            d[k] = v
    return d


def save_store(store, path=STORE):
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(store, f, ensure_ascii=False, indent=1)
    os.replace(tmp, path)


# ------------------------------------------------------------------ statistics
def upper_bound(k, n):
    """Exact one-sided 95% Clopper-Pearson upper bound for k events in n trials."""
    if n <= 0 or k >= n:
        return 1.0
    if k == 0:
        return 1 - 0.05 ** (1 / n)
    lo, hi = 0.0, 1.0
    for _ in range(100):  # shortcut: float comb() overflows for n above ~1000, not reached here
        p = (lo + hi) / 2
        cdf = sum(math.comb(n, i) * p**i * (1 - p) ** (n - i) for i in range(k + 1))
        lo, hi = (p, hi) if cdf > 0.05 else (lo, p)
    return (lo + hi) / 2


def evaluate(rows, probs, lo, hi):
    n_true = sum(1 for r in rows if r["same"])
    fa = fr = acc = nn = rev = 0
    for r, p in zip(rows, probs, strict=True):
        if p is None:
            nn += 1
            rev += 1
            continue
        if p >= hi:
            acc += r["same"]
            fa += not r["same"]
        elif p <= lo:
            fr += r["same"]
        else:
            rev += 1
    return {"n": len(rows), "n_true": n_true, "n_false": len(rows) - n_true, "n_none": nn,
            "false_accept": fa, "false_reject": fr, "accept_true": acc,
            "coverage": acc / n_true if n_true else 0.0, "review": rev}


def choose_hi(neg_probs):
    """Smallest grid hi with no synthetic false accept and max negative p <= hi-0.05; else (0.99, False)."""
    ps = [p for p in neg_probs if p is not None]
    if not ps:
        return 0.99, False
    mx = max(ps)
    for h in GRID:
        if mx < h and mx <= h - 0.05 + 1e-9:
            return h, True
    return 0.99, False


# ------------------------------------------------------------------ synthetic negatives
def elements(formula):
    return set(re.findall(r"[A-Z][a-z]?", formula or ""))


def _nf(formula):
    return (formula or "").replace(" ", "")


def pair_ok(row, own_formula, wrong_cid, wrong_formula, name_cids):
    """Hard requirements for a synthetic negative: really a different record with a different formula."""
    return (bool(_nf(wrong_formula)) and _nf(wrong_formula) != _nf(own_formula)
            and wrong_cid != row["cid"] and wrong_cid not in name_cids)


MAX_WRONG_USES = 5


def make_synthetic_negatives(n=100, seed=0, rows=None, records=None):
    if rows is None:
        rows = load_pairs()[0]
    if records is None:
        records = load_records()
    name_cids = {}
    for r in rows:
        name_cids.setdefault(r["name"], set()).add(r["cid"])
    ents = sorted((r for r in rows if r.get("by") == "claude-review" and r["same"]
                   and _nf(records.get(r["cid"], {}).get("formula"))), key=lambda r: (r["name"], r["cid"]))
    wrongs = sorted(c for c, v in records.items() if _nf(v.get("formula")))
    rng = random.Random(seed)
    out, used_ents, used_pairs = [], set(), set()
    uses = collections.Counter()  # per wrong CID, capped so H2O/H2 cannot dominate

    def pred(cat, name, own_el, wrong_el):
        if cat == "subset":
            # non-strict on purpose: equal element sets (hydrate vs anhydrous, homologs) are the hard negatives
            w = wrong_el - _HO
            return bool(w) and w <= own_el - _HO
        if cat == "sibling":
            return bool((wrong_el & own_el) - _HO - {"C"})
        if cat == "formword":
            return FORM_RE.search(name) is not None
        return True

    def fill(cat, quota, reuse):
        order = list(ents)
        rng.shuffle(order)
        got = 0
        for e in order:
            if got >= quota:
                break
            if not reuse and e["name"] in used_ents:
                continue
            own_f = records[e["cid"]]["formula"]
            own_el = elements(own_f)
            cands = [c for c in wrongs if (e["name"], c) not in used_pairs and uses[c] < MAX_WRONG_USES
                     and pair_ok(e, own_f, c, records[c]["formula"], name_cids[e["name"]])
                     and pred(cat, e["name"], own_el, elements(records[c]["formula"]))]
            if not cands:
                continue
            c = rng.choice(cands)
            used_ents.add(e["name"])
            used_pairs.add((e["name"], c))
            uses[c] += 1
            out.append({"name": e["name"], "cid": c, "same": False, "by": "synthetic",
                        "iupac": records[c]["iupac"], "formula": records[c]["formula"],
                        "category": cat, "true_cid": e["cid"]})
            got += 1
        return got

    for cat in ("subset", "sibling", "formword"):
        fill(cat, n // 4, False)
    if len(out) < n:
        fill("random", n - len(out), False)
    if len(out) < n:
        fill("random", n - len(out), True)
    for s in out:  # hard requirements, re-checked on the result
        own = _nf(records[s["true_cid"]]["formula"])
        if _nf(s["formula"]) == own or s["cid"] in name_cids[s["name"]]:
            raise ValueError(f"invalid synthetic negative {s['name']} -> {s['cid']}")
    return out


# ------------------------------------------------------------------ report
def _bin(p):
    return min(int(p * 10), 9)


def _cut(p, lo, hi):
    return "none" if p is None else jev_verify.decide(p, lo, hi)


def _cut5(p):
    return "none" if p is None else "yes" if p >= 0.5 else "no"


def _conf(rows, probs, fn):
    c = {"yes": 0, "review": 0, "no": 0, "none": 0}
    for p in probs:
        c[fn(p)] += 1
    return f"yes={c['yes']} review={c['review']} no={c['no']} none={c['none']}"


def _fmtp(p):
    return "None" if p is None else f"{p:.3f}"


def build_report(rows, synthetic, cache, skipped, lo, hi_arg):
    def P(r):
        return cache.get(make_key(r["name"], r["cid"]))

    gold = [r for r in rows if r["by"] == "claude-review"]
    sec = [r for r in rows if r["by"] != "claude-review"]
    groups = {
        "gold_true": [P(r) for r in gold if r["same"]], "gold_false": [P(r) for r in gold if not r["same"]],
        "sec_true": [P(r) for r in sec if r["same"]], "sec_false": [P(r) for r in sec if not r["same"]],
        "synthetic": [P(r) for r in synthetic]}
    gp, sp, yp = [P(r) for r in gold], [P(r) for r in sec], groups["synthetic"]
    hi, hi_ok = (choose_hi(yp) if hi_arg is None else (hi_arg, True))
    n_none = sum(p is None for p in gp + sp + yp)
    L = ["Jev evaluation report", "=====================",
         (f"model={jev_verify.MODEL} prompt_version={jev_verify.PROMPT_VERSION} lo={lo} "
          f"chosen hi = {hi:.2f} ({'auto, synthetic only' if hi_arg is None else 'manual'})"),
         (f"real rows: {len(rows)} (gold {len(gold)}, secondary {len(sec)}); synthetic: {len(synthetic)}; "
          f"skipped for no cache file: {skipped}; unscored (None): {n_none}"), "",
         "Score histogram (count per 0.1 bin)", "bin       " + "".join(f"{g:>12}" for g in groups)]
    for b in range(10):
        L.append(f"{b / 10:.1f}-{(b + 1) / 10:.1f} " + "".join(
            f"{sum(1 for p in ps if p is not None and _bin(p) == b):>12}" for ps in groups.values()))
    L.append("None      " + "".join(f"{sum(p is None for p in ps):>12}" for ps in groups.values()))
    L += ["", ("Threshold sweep (secondary disagreement = secondary accepted-but-labelled-false or "
               "rejected-but-labelled-true; secondary is NOT gold)"),
          "hi     synthetic FA  real-gold FA  real-gold coverage  secondary disagreements"]
    for h in GRID:
        eg, es = evaluate(gold, gp, lo, h), evaluate(sec, sp, lo, h)
        L.append(f"{h:.2f}   {sum(p is not None and p >= h for p in yp):>12}  {eg['false_accept']:>12}  "
                 f"{eg['coverage']:>18.3f}  {es['false_accept'] + es['false_reject']:>23}")

    def table(title, rs, ps):
        L.extend(["", title])
        for lab in (True, False):
            sub = [p for r, p in zip(rs, ps, strict=True) if r["same"] is lab]
            L.append(f"  label same={lab}: n={len(sub)}")
            L.append(f"    at lo={lo} hi={hi:.2f}: {_conf(sub, sub, lambda p: _cut(p, lo, hi))}")
            L.append(f"    at 0.5:           {_conf(sub, sub, _cut5)}")

    table("GOLD (by=claude-review)", gold, gp)
    table("SECONDARY (GLM-only labels, NOT gold; agreement judged with the 0.5 cut only)", sec, sp)
    table("SYNTHETIC (all label same=False)", synthetic, yp)
    L.append("  synthetic by category (n / false accepts at hi / max p):")
    for cat in sorted({s["category"] for s in synthetic}):
        cp = [P(s) for s in synthetic if s["category"] == cat]
        ok = [p for p in cp if p is not None]
        L.append(f"    {cat}: {len(cp)} / {sum(p >= hi for p in ok)} / {max(ok, default=0.0):.3f}")

    L += ["", "Disagreements with the 0.5 cut (gold and secondary): name | iupac | formula | label | p"]
    dis = [(r, p) for grp, rs in (("gold", gold), ("secondary", sec)) for r in rs for p in [P(r)]
           if p is not None and ((r["same"] and p < 0.5) or (not r["same"] and p >= 0.5))]
    for r, p in dis:
        L.append(f"  {r['name']} | {r['iupac']} | {r['formula']} | "
                 f"{'gold' if r['by'] == 'claude-review' else 'secondary'} same={r['same']} | {_fmtp(p)}")
    if not dis:
        L.append("  (none)")

    neg_gold = [P(r) for r in gold if not r["same"]]
    fa_g = sum(p is not None and p >= hi for p in neg_gold)
    fa_s = sum(p is not None and p >= hi for p in yp)
    ub_g, ub_s = upper_bound(fa_g, len(neg_gold)), upper_bound(fa_s, len(yp))
    unscored = sum(p is None for p in neg_gold + yp)
    allneg = [p for p in neg_gold + yp if p is not None]
    mx = max(allneg, default=0.0)
    eg = evaluate(gold, gp, lo, hi)
    i_ok = bool(neg_gold) and bool(yp) and unscored == 0 and fa_g == 0 and fa_s == 0
    ii_ok = bool(allneg) and unscored == 0 and mx <= hi - 0.05 + 1e-9
    iii_ok = eg["n_true"] > 0 and eg["coverage"] >= 0.5
    pf = lambda ok: "PASS" if ok else "FAIL"
    L += ["", f"GATE at lo={lo} hi={hi:.2f}",
          f"hi selection: {'PASS' if hi_ok else 'FAIL - no hi satisfies the rule on synthetic, using 0.99'}",
          (f"(i) {pf(i_ok)} false accepts: real gold negatives {fa_g}/{len(neg_gold)} "
           f"(95% upper bound {ub_g:.3f}), synthetic {fa_s}/{len(yp)} (95% upper bound {ub_s:.3f}); "
           f"unscored negatives {unscored}")]
    if fa_g == 0 and neg_gold:
        L.append(f"    0 of {len(neg_gold)} real negatives alone does NOT bound the true false-accept rate "
                 f"below about {ub_g:.3f}")
    L += [f"(ii) {pf(ii_ok)} highest p among all negatives = {mx:.3f}, needs <= hi-0.05 = {hi - 0.05:.3f}",
          (f"(iii) {pf(iii_ok)} coverage on gold trues at hi = {eg['accept_true']}/{eg['n_true']} = "
           f"{eg['coverage']:.3f}, needs >= 0.500"),
          f"overall (i)-(iii): {pf(i_ok and ii_ok and iii_ok and hi_ok)}", ""]
    sample = sorted((r for r in gold if r["same"] and P(r) is not None and P(r) >= hi),
                    key=lambda r: (r["name"], r["cid"]))
    sample = random.Random(0).sample(sample, min(30, len(sample)))
    L.append(f"(iv) hand-check sample, MANUAL step not scored here: {len(sample)} gold same:true rows with "
             f"p >= hi; confirm each record is the named substance (name | iupac | formula | p)")
    L += [f"  [hc] {r['name']} | {r['iupac']} | {r['formula']} | {_fmtp(P(r))}" for r in sample]
    return "\n".join(L) + "\n"


# ------------------------------------------------------------------ commands
def cmd_build_synthetic():
    rows, skipped = load_pairs()
    syn = make_synthetic_negatives(100, 0, rows)
    store = load_store()
    store["synthetic"] = syn
    save_store(store)
    cats = {}
    for s in syn:
        cats[s["category"]] = cats.get(s["category"], 0) + 1
    print(f"synthetic negatives: {len(syn)} " + " ".join(f"{k}={v}" for k, v in sorted(cats.items())))
    print(f"skipped (verify.json rows without cache file): {skipped}")
    return 0


def _write_report(rows, store, skipped, lo, hi):
    txt = build_report(rows, store["synthetic"], store["cache"], skipped, lo, hi)
    with open(REPORT, "w", encoding="utf-8") as f:
        f.write(txt)
    print(f"report: {REPORT}")
    print("\n".join(txt.split("GATE", 1)[1].splitlines()[:7]))


def cmd_report(lo, hi):
    rows, skipped = load_pairs()
    _write_report(rows, load_store(), skipped, lo, hi)
    return 0


async def _score(todo, cache, store):
    done = 0
    async with httpx.AsyncClient(trust_env=False) as client:
        async def one(key, name, facts):
            nonlocal done
            p = await jev_verify.jev_same(client, name, facts)
            if p is not None:  # None is never cached so a rerun retries it
                cache[key] = p
            done += 1
            if done % 100 == 0:
                save_store(store)

        await asyncio.gather(*(one(k, n, f) for k, (n, f) in todo.items()))
    save_store(store)


def cmd_run(lo, hi):
    if not os.environ.get("TYPESAFE_API_KEY"):
        print("TYPESAFE_API_KEY not set", file=sys.stderr)
        return 2
    rows, skipped = load_pairs()
    store = load_store()
    if not store["synthetic"]:
        print("no synthetic negatives stored; run --build-synthetic first", file=sys.stderr)
        return 2
    cache, todo, hits = store["cache"], {}, 0
    for r in rows + store["synthetic"]:
        k = make_key(r["name"], r["cid"])
        if k in cache:
            hits += 1
        else:
            todo[k] = (r["name"], {"iupac": r["iupac"], "formula": r["formula"]})
    store["meta"] = {"model": jev_verify.MODEL, "prompt_version": jev_verify.PROMPT_VERSION,
                     "updated": time.strftime("%Y-%m-%d %H:%M:%S")}
    asyncio.run(_score(todo, cache, store))
    tokens = jev_verify.USAGE["input_tokens"]
    nones = sum(k not in cache for k in todo)
    print(f"api calls: {jev_verify.USAGE['calls']}  cached hits: {hits}  None: {nones}  "
          f"input_tokens: {tokens}  cost: ${tokens * COST_PER_M / 1e6:.4f}")
    _write_report(rows, store, skipped, lo, hi)
    return 3 if jev_verify.BREAKER.tripped else 0

# ------------------------------------------------------------------ selftest
_N = 0


def check(cond, msg):
    global _N
    assert cond, msg
    _N += 1


def _fixture():
    forms = {1: "Al2O3", 2: "Al", 3: "CuH10O9S", 4: "CuO4S", 5: "Cu", 6: "ZnO", 7: "Zn", 8: "TiO2",
             9: "Ti", 10: "Fe2O3", 11: "Fe", 12: "NaCl", 13: "Na", 14: "Cl2", 15: "CH4", 16: "C",
             17: "H2O", 18: "SiO2", 19: "Si", 20: "Ag"}
    records = {c: {"iupac": f"iupac{c}", "formula": f} for c, f in forms.items()}
    names = [("Alumina Nanoparticles", 1), ("Aluminum Powder", 2), ("Copper Sulfate Pentahydrate", 3),
             ("Zinc Oxide Nanoparticles", 6), ("Titanium Dioxide Nanofluid", 8), ("Iron Oxide", 10),
             ("Sodium Chloride", 12), ("Silicon Dioxide Nanowire", 18), ("Copper", 5), ("Zinc", 7),
             ("Titanium", 9), ("Iron Flakes", 11), ("Silver Nanoparticles", 20)]
    rows = [{"name": n, "cid": c, "same": True, "by": "claude-review", **records[c]} for n, c in names]
    rows.append({"name": "Glm Only", "cid": 4, "same": True, "by": None, **records[4]})
    rows.append({"name": "Gold False", "cid": 15, "same": False, "by": "claude-review", **records[15]})
    return rows, records


def _fixture_report(gold_false_p=0.1):
    rows, cache = [], {}
    for i in range(40):
        r = {"name": f"T{i}", "cid": 100 + i, "same": True, "by": "claude-review",
             "iupac": f"i{i}", "formula": "X"}
        rows.append(r)
        cache[make_key(r["name"], r["cid"])] = 0.95
    for i in range(5):
        r = {"name": f"F{i}", "cid": 200 + i, "same": False, "by": "claude-review", "iupac": "", "formula": "Y"}
        rows.append(r)
        cache[make_key(r["name"], r["cid"])] = gold_false_p if i == 0 else 0.1
    r = {"name": "S0", "cid": 300, "same": True, "by": None, "iupac": "", "formula": "Z"}
    rows.append(r)
    cache[make_key("S0", 300)] = 0.4  # secondary disagreement
    syn = []
    for i in range(10):
        s = {"name": f"T{i}", "cid": 400 + i, "same": False, "by": "synthetic", "iupac": "", "formula": "W",
             "category": "random", "true_cid": 100 + i}
        syn.append(s)
        cache[make_key(s["name"], s["cid"])] = 0.05
    return rows, syn, cache


def _selftest():
    # evaluate
    rows = [{"same": s} for s in (True, True, True, False, False, True)]
    probs = [0.95, 0.1, 0.5, 0.9, 0.3, None]
    e = evaluate(rows, probs, 0.2, 0.9)
    check(e["n"] == 6 and e["n_true"] == 4 and e["n_false"] == 2 and e["n_none"] == 1, "evaluate counts")
    check(e["false_accept"] == 1, "false accept at p>=hi (exactly hi counts)")
    check(e["false_reject"] == 1, "false reject at p<=lo")
    check(e["accept_true"] == 1 and e["coverage"] == 0.25, "coverage = accept_true / n_true, None not accepted")
    check(e["review"] == 3, "review = neither accepted nor rejected (incl None)")
    e = evaluate([{"same": False}], [None], 0.2, 0.9)
    check(e["false_accept"] == 0 and e["false_reject"] == 0 and e["n_none"] == 1, "None never counted")
    check(evaluate([{"same": False}], [0.1], 0.2, 0.9)["coverage"] == 0.0, "coverage 0.0 without trues")

    # main rejects cut-offs decide() would refuse (exit 2, nothing runs)
    for argv in (["--report", "--hi", "0.5"], ["--run", "--lo", "0.6", "--hi", "0.55"],
                 ["--report", "--lo", "0.1", "--hi", "0.3"]):
        sys.argv, saved, sys.stderr = ["jev_eval.py", *argv], sys.argv, io.StringIO()
        try:
            rc, msg = main(), sys.stderr.getvalue()
        finally:
            sys.argv, sys.stderr = saved, sys.__stderr__
        check(rc == 2 and "--hi" in msg, f"main rejects {argv}")

    # upper_bound
    check(abs(upper_bound(0, 33) - 0.091) < 0.01 and abs(upper_bound(0, 33) - 0.087) < 0.001, "ub 0/33")
    check(abs(upper_bound(0, 100) - 0.030) < 0.01, "ub 0/100")
    check(upper_bound(0, 0) == 1.0, "ub n=0")
    check(0.3 < upper_bound(3, 10) < 0.8, "ub 3/10 range")
    ubs = [upper_bound(k, 20) for k in range(21)]
    check(all(a < b for a, b in itertools.pairwise(ubs)), "ub monotone in k")
    check(abs(upper_bound(1, 100) - 0.0466) < 0.001, "ub 1/100 known value")

    # synthetic negatives
    rows, records = _fixture()
    a = make_synthetic_negatives(8, 0, rows, records)
    b = make_synthetic_negatives(8, 0, rows, records)
    c = make_synthetic_negatives(8, 1, rows, records)
    check(a == b, "seed 0 reproducible")
    check(a != c, "seed 1 differs")
    check(len(a) == 8, "8 negatives produced")
    own = {r["name"]: r for r in rows}
    for s in a:
        o = own[s["name"]]
        check(s["same"] is False and s["by"] == "synthetic", "synthetic flags")
        check(s["formula"].replace(" ", "") != o["formula"].replace(" ", ""), "wrong formula differs")
        check(s["cid"] != o["cid"] and s["true_cid"] == o["cid"], "wrong cid differs, true_cid kept")
        check(s["formula"] == records[s["cid"]]["formula"], "wrong record described")
    check(len({(s["name"], s["cid"]) for s in a}) == 8, "no duplicate pairs")
    cats = sorted(s["category"] for s in a)
    check(cats == ["formword"] * 2 + ["random"] * 2 + ["sibling"] * 2 + ["subset"] * 2, "n//4 per category")
    for s in a:
        if s["category"] == "formword":
            check(FORM_RE.search(s["name"]) is not None, "formword name")
        if s["category"] == "subset":
            w, o = elements(s["formula"]) - {"H", "O"}, elements(own[s["name"]]["formula"]) - {"H", "O"}
            check(bool(w) and w <= o, "subset: non-empty, subset or equal")
        if s["category"] == "sibling":
            check(bool((elements(s["formula"]) & elements(own[s["name"]]["formula"])) - {"H", "O", "C"}),
                  "sibling shares element")
    hyd = [{"name": "Cu Sulfate", "cid": 1, "same": True, "by": "claude-review", "iupac": "", "formula": "CuH10O9S"}]
    hrec = {1: {"iupac": "", "formula": "CuH10O9S"}, 2: {"iupac": "", "formula": "CuO4S"}}
    check([(s["category"], s["cid"]) for s in make_synthetic_negatives(4, 0, hyd, hrec)][:1] == [("subset", 2)],
          "subset admits equal element set (hydrate vs anhydrous)")
    capr = [{"name": f"E{i}", "cid": 100 + i, "same": True, "by": "claude-review", "iupac": "", "formula": "Fe"}
            for i in range(12)]
    caprec = {r["cid"]: {"iupac": "", "formula": "Fe"} for r in capr}
    caprec.update({1: {"iupac": "", "formula": "Zn"}, 2: {"iupac": "", "formula": "Cu"}})
    capout = make_synthetic_negatives(12, 0, capr, caprec)
    uses = collections.Counter(s["cid"] for s in capout)
    check(len(capout) == 10 and max(uses.values()) == 5, "wrong cid used at most 5 times (cap binds)")
    one = [{"name": "A", "cid": 1, "same": True, "by": "claude-review", "iupac": "", "formula": "Al2O3"}]
    only_same = {1: {"iupac": "", "formula": "Al2O3"}, 2: {"iupac": "", "formula": "Al2 O3"}}
    check(make_synthetic_negatives(4, 0, one, only_same) == [], "same-formula record yields no pair")
    dup = one + [{"name": "A", "cid": 2, "same": True, "by": None, "iupac": "", "formula": "Al"}]
    recs3 = {1: {"iupac": "", "formula": "Al2O3"}, 2: {"iupac": "", "formula": "Al"},
             3: {"iupac": "", "formula": "Zn"}}
    out = make_synthetic_negatives(4, 0, dup, recs3)
    check(out and all(s["cid"] == 3 for s in out), "cid of any row with that name excluded")
    check(not pair_ok(one[0], "Al2O3", 2, "Al2 O3", {1}), "pair_ok rejects same formula")
    check(not pair_ok(one[0], "Al2O3", 1, "Al", {1}), "pair_ok rejects same cid")
    check(pair_ok(one[0], "Al2O3", 3, "Zn", {1}), "pair_ok accepts a real negative")

    # cache key + store
    check(make_key("Water", 962) == "Water|962|jev-latest|v1", "cache key format")
    with tempfile.TemporaryDirectory() as d:
        p = os.path.join(d, "jev_eval.json")
        check(load_store(p) == {"synthetic": [], "cache": {}, "meta": {}}, "missing store tolerated")
        st = {"synthetic": a, "cache": {"x|1|jev-latest|v1": 0.5}, "meta": {"k": "v"}}
        save_store(st, p)
        check(load_store(p) == st, "store roundtrip")
        check(os.listdir(d) == ["jev_eval.json"], "no temp file left")
        with open(p, "w", encoding="utf-8") as f:
            f.write("{not json")
        check(load_store(p) == {"synthetic": [], "cache": {}, "meta": {}}, "corrupt store tolerated")

    # choose_hi
    check(choose_hi([0.1, 0.62, 0.3]) == (0.70, True), "max 0.62 -> 0.70")
    check(choose_hi([0.0, 0.5, None]) == (0.60, True), "max 0.5 -> 0.60")
    check(choose_hi([0.99]) == (0.99, False), "max 0.99 -> no hi satisfies")
    check(choose_hi([]) == (0.99, False) and choose_hi([None]) == (0.99, False), "no scores -> FAIL")

    # report
    rows, syn, cache = _fixture_report()
    txt = build_report(rows, syn, cache, 3, 0.2, None)
    check("chosen hi = 0.60" in txt, "report chosen hi")
    check("(i) " in txt and "(ii) " in txt and "(iii) " in txt and "(iv) " in txt, "gate blocks present")
    check("FAIL" not in txt.split("GATE")[1], "gate passes on clean fixture")
    check(txt.count("\n  [hc] ") == 30, "hand-check sample of 30")
    check("S0 |" in txt, "secondary disagreement listed")
    check("does NOT bound the true false-accept rate below about" in txt, "upper-bound sentence")
    rows, syn, cache = _fixture_report(gold_false_p=0.95)
    gate = build_report(rows, syn, cache, 0, 0.2, None).split("GATE")[1]
    check("(i) FAIL" in gate, "gold false accept fails gate (i)")
    print(f"selftest OK ({_N} asserts)")


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--build-synthetic", action="store_true")
    ap.add_argument("--run", action="store_true")
    ap.add_argument("--report", action="store_true")
    ap.add_argument("--lo", type=float, default=0.2)
    ap.add_argument("--hi", type=float, default=None)
    a = ap.parse_args()
    if a.hi is not None and not (a.lo < a.hi and a.hi > 0.5):
        print(f"--hi must satisfy --lo < --hi and --hi > 0.5, got lo={a.lo} hi={a.hi}", file=sys.stderr)
        return 2
    if a.selftest:
        _selftest()
        return 0
    if a.build_synthetic:
        return cmd_build_synthetic()
    if a.run:
        return cmd_run(a.lo, a.hi)
    if a.report:
        return cmd_report(a.lo, a.hi)
    ap.print_usage()
    return 2


if __name__ == "__main__":
    sys.exit(main())
