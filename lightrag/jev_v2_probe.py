"""Probe an experimental Jev prompt version (default v2) on the gold dev set or a fresh labelled set.

Scores rows with jev_verify.jev_same(version=pv), caches per name|iupac|formula|model|pv, prints false-accept
sweep, per-label histogram and every disagreement with the 0.5 cut. Writes nothing to graph or verdicts.

Usage: python lightrag/jev_v2_probe.py --selftest | --set dev | --set fresh --file rows.json [--pv v2]
"""
import argparse
import asyncio
import json
import os
import sys
import tempfile

import httpx

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import jev_eval
import jev_verify

DIR = jev_eval.DIR
CACHE = os.path.join(DIR, "jev_v2_cache.json")
HIS = [0.5, 0.6, 0.7, 0.8, 0.85, 0.9, 0.95, 0.97, 0.99]


# ------------------------------------------------------------------ data + cache
def key(row, pv):
    return f"{row['name']}|{row['iupac']}|{row['formula']}|{jev_verify.MODEL}|{pv}"


def load_dev():
    rows = jev_eval.load_pairs()[0]
    return [r for r in rows if r["by"] == "claude-review"]


def load_fresh(path):
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, list):
        raise TypeError("fresh file must be a JSON list")
    out = []
    for d in data:
        if not (isinstance(d, dict) and isinstance(d.get("name"), str) and isinstance(d.get("same"), bool)):
            raise TypeError(f"bad fresh row: {d!r}")
        out.append({"name": d["name"], "iupac": str(d.get("iupac") or ""),
                    "formula": str(d.get("formula") or ""), "same": d["same"]})
    return out


def load_cache(path=CACHE):
    try:
        with open(path, encoding="utf-8") as f:
            d = json.load(f)
    except (OSError, ValueError):
        return {}
    return d if isinstance(d, dict) else {}


def save_cache(cache, path=CACHE):
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(cache, f, ensure_ascii=False, indent=1)
    os.replace(tmp, path)


async def score(rows, cache, pv, path, client):
    """Fill cache for rows; returns (calls_made, cached_hits, none_count). None is never cached."""
    todo = {}
    for r in rows:
        todo.setdefault(key(r, pv), r)
    hits = sum(k in cache for k in todo)
    todo = {k: r for k, r in todo.items() if k not in cache}
    done = 0

    async def one(k, r):
        nonlocal done
        p = await jev_verify.jev_same(client, r["name"], {"iupac": r["iupac"], "formula": r["formula"]},
                                      version=pv)
        if p is not None:
            cache[k] = p
        done += 1
        if done % 100 == 0:
            save_cache(cache, path)

    await asyncio.gather(*(one(k, r) for k, r in todo.items()))
    save_cache(cache, path)
    return len(todo), hits, sum(k not in cache for k in todo)


# ------------------------------------------------------------------ report
def sweep(rows, probs, his=HIS):
    """[(hi, false_accepts, upper95, distinct_fa_names, coverage)]; the upper bound uses n = negatives."""
    pos = [p for r, p in zip(rows, probs, strict=True) if r["same"]]
    neg = [(r, p) for r, p in zip(rows, probs, strict=True) if not r["same"]]
    out = []
    for h in his:
        fa = [r for r, p in neg if p is not None and p >= h]
        acc = sum(p is not None and p >= h for p in pos)
        out.append((h, len(fa), jev_eval.upper_bound(len(fa), len(neg)), len({r["name"] for r in fa}),
                    acc / len(pos) if pos else 0.0))
    return out


def build_report(rows, probs, set_name, pv, stats):
    calls, hits, nones, tokens = stats
    pos = [p for r, p in zip(rows, probs, strict=True) if r["same"]]
    neg = [p for r, p in zip(rows, probs, strict=True) if not r["same"]]
    L = [f"Jev prompt probe: set={set_name} pv={pv} model={jev_verify.MODEL}",
         (f"rows={len(rows)} (same=True {len(pos)}, same=False {len(neg)}) calls={calls} cached hits={hits} "
          f"None={nones} tokens={tokens} cost=${tokens * jev_eval.COST_PER_M / 1e6:.4f}"), "",
         "Histogram (count per 0.1 bin)", "bin        same=True  same=False"]
    for b in range(10):
        c = [sum(p is not None and min(int(p * 10), 9) == b for p in ps) for ps in (pos, neg)]
        L.append(f"{b / 10:.1f}-{(b + 1) / 10:.1f} {c[0]:>12}{c[1]:>12}")
    L.append(f"None       {sum(p is None for p in pos):>12}{sum(p is None for p in neg):>12}")
    L += ["", ("Sweep (false accepts: same=False and p>=hi; coverage: share of same=True with p>=hi; "
               "ub95 = Clopper-Pearson one-sided upper bound, n = negatives)"),
          "hi     false_accepts  ub95   fa_names  coverage"]
    for h, fa, ub, names, cov in sweep(rows, probs):
        L.append(f"{h:.2f}   {fa:>13}  {ub:.3f}  {names:>8}  {cov:>8.3f}")
    L += ["", "All negatives with p>=0.5 (name | iupac | formula | p)"]
    L += [f"{r['name']} | {r['iupac']} | {r['formula']} | {p:.3f}" for r, p in
          sorted(((r, p) for r, p in zip(rows, probs, strict=True) if not r["same"] and p is not None and p >= 0.5),
                 key=lambda t: -t[1])] or ["(none)"]
    L += ["", "All positives with p<0.5 (name | iupac | formula | p)"]
    L += [f"{r['name']} | {r['iupac']} | {r['formula']} | {p:.3f}" for r, p in
          sorted(((r, p) for r, p in zip(rows, probs, strict=True) if r["same"] and p is not None and p < 0.5),
                 key=lambda t: t[1])] or ["(none)"]
    return chr(10).join(L) + chr(10)


async def _run(rows, pv):
    cache = load_cache()
    u0, c0 = jev_verify.USAGE["input_tokens"], jev_verify.USAGE["calls"]
    async with httpx.AsyncClient(trust_env=False) as client:
        _, hits, nones = await score(rows, cache, pv, CACHE, client)
    return [cache.get(key(r, pv)) for r in rows], (jev_verify.USAGE["calls"] - c0, hits, nones,
                                                   jev_verify.USAGE["input_tokens"] - u0)


def run(set_name, fresh_file, pv):
    if not os.environ.get("TYPESAFE_API_KEY"):
        print("TYPESAFE_API_KEY not set", file=sys.stderr)
        return 2
    if set_name == "fresh" and not fresh_file:
        print("--set fresh needs --file", file=sys.stderr)
        return 2
    rows = load_dev() if set_name == "dev" else load_fresh(fresh_file)
    sys.stdout.reconfigure(encoding="utf-8")  # formulas carry subscript digits; cp1251 console
    probs, stats = asyncio.run(_run(rows, pv))
    txt = build_report(rows, probs, set_name, pv, stats)
    out = os.path.join(DIR, f"jev_v2_{set_name}_report.txt")
    with open(out, "w", encoding="utf-8") as f:
        f.write(txt)
    print(txt, end="")
    print(f"report: {out}")
    return 3 if jev_verify.BREAKER.tripped else 0


# ------------------------------------------------------------------ selftest
_N = 0


def check(cond, msg):
    global _N
    assert cond, msg
    _N += 1


def _rows():
    def r(name, same, iupac="i", formula="F"):
        return {"name": name, "same": same, "iupac": iupac, "formula": formula}
    return [r("A", True), r("B", True), r("C", True), r("D", False), r("E", False, "ie", "FE"),
            r("E", False, "ie2", "FE2"), r("bad", True)]


PROBS = [0.95, 0.4, 0.99, 0.6, 0.95, 0.3, None]


async def _selftest_async(d):
    path = os.path.join(d, "c.json")
    seen = []

    def handler(req):
        body = json.loads(req.content)
        seen.append(body)
        n = body["state"]["entity_name"]
        if n == "bad":
            return httpx.Response(422)
        return httpx.Response(200, json={"answers": {"same": {"noul": 0.8}}, "usage": {"input_tokens": 10}})

    rows = _rows() + [dict(_rows()[0])]  # exact duplicate of A -> one call
    cache = {}
    async with httpx.AsyncClient(transport=httpx.MockTransport(handler), trust_env=False) as c:
        calls, hits, nones = await score(rows, cache, "v2", path, c)
        check((calls, hits, nones) == (7, 0, 1), "first run: 7 unique keys, 0 hits, 1 None")
        check(len(cache) == 6 and key(rows[0], "v2") in cache and key(rows[6], "v2") not in cache,
              "None is not cached")
        check(all(b["questions"] == jev_verify.build_question("v2") for b in seen), "v2 question sent")
        seen.clear()
        calls, hits, nones = await score(rows, cache, "v2", path, c)
        check((calls, hits, nones) == (1, 6, 1) and len(seen) == 1, "rerun: cache hits, only None retried")
    check(load_cache(path) == cache, "cache persisted atomically")
    check(os.listdir(d) == ["c.json"], "no temp file left")


def _selftest():
    check(key(_rows()[4], "v2") == "E|ie|FE|jev-latest|v2", "key format")
    check(key(_rows()[4], "v2") != key(_rows()[5], "v2"), "iupac/formula are in the key")
    with tempfile.TemporaryDirectory() as d:
        p = os.path.join(d, "c.json")
        check(load_cache(p) == {}, "missing cache tolerated")
        with open(p, "w", encoding="utf-8") as f:
            f.write("{nope")
        check(load_cache(p) == {}, "corrupt cache tolerated")
        old = os.environ.get("TYPESAFE_API_KEY")
        os.environ["TYPESAFE_API_KEY"] = "test-key"
        try:
            asyncio.run(_selftest_async(d))
        finally:
            if old is None:
                os.environ.pop("TYPESAFE_API_KEY", None)
            else:
                os.environ["TYPESAFE_API_KEY"] = old
        fp = os.path.join(d, "fresh.json")
        with open(fp, "w", encoding="utf-8") as f:
            json.dump([{"name": "X", "iupac": "i", "formula": "F", "same": False, "note": "n"}], f)
        fr = load_fresh(fp)
        check(len(fr) == 1 and fr[0]["same"] is False and fr[0]["name"] == "X", "load_fresh")
        with open(fp, "w", encoding="utf-8") as f:
            json.dump([{"name": "X", "same": "no"}], f)
        try:
            load_fresh(fp)
        except TypeError:
            check(True, "load_fresh rejects bad row")
        else:
            check(False, "load_fresh must reject bad row")

    rows = _rows()
    sw = {h: rest for h, *rest in sweep(rows, PROBS, [0.5, 0.9, 0.99])}
    # negatives: D 0.6, E 0.95, E 0.3 (n=3); positives: A .95 B .4 C .99 bad None (n=4)
    check(sw[0.5][0] == 2 and sw[0.5][2] == 2 and sw[0.5][3] == 2 / 4, "sweep hi=0.5")
    check(sw[0.9][0] == 1 and sw[0.9][2] == 1 and sw[0.9][3] == 2 / 4, "sweep hi=0.9")
    check(sw[0.99][0] == 0 and sw[0.99][3] == 1 / 4, "sweep hi=0.99 (exactly hi counts)")
    check(abs(sw[0.99][1] - jev_eval.upper_bound(0, 3)) < 1e-12, "upper bound from jev_eval, n=negatives")

    txt = build_report(rows, PROBS, "dev", "v2", (6, 0, 1, 60))
    check("calls=6" in txt and "cached hits=0" in txt and "None=1" in txt and "tokens=60" in txt
          and "cost=$0.0000" in txt, "stats line")
    check("0.9-1.0" in txt and "same=True" in txt and "same=False" in txt, "histogram present")
    neg_part = txt.split("negatives with p>=0.5")[1].split("positives with p<0.5")[0]
    pos_part = txt.split("positives with p<0.5")[1]
    check("E | ie | FE | 0.950" in neg_part and "D | i | F | 0.600" in neg_part and "FE2" not in neg_part,
          "negatives >= 0.5 listed")
    check("B | i | F | 0.400" in pos_part and "bad" not in pos_part, "positives < 0.5 listed, None excluded")
    print(f"selftest OK ({_N} asserts)")


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--set", choices=["dev", "fresh"])
    ap.add_argument("--file")
    ap.add_argument("--pv", default="v2")
    a = ap.parse_args()
    if a.selftest:
        _selftest()
        return 0
    if a.set:
        return run(a.set, a.file, a.pv)
    ap.print_usage()
    return 2


if __name__ == "__main__":
    sys.exit(main())
