"""Jev (TypeSafe System One) second opinion for the PubChem same-substance check.

Verified 2026-11-11 by jev_smoke.py: POST https://api.typesafe.ai/v1/systemone, Authorization: Bearer
$TYPESAFE_API_KEY, model alias jev-latest (served jev-1.14.0), body['answers']['same']['noul'] float in
[0,1], body['usage']['input_tokens']; host needs trust_env=False.
Jev output is a probability, never proof; nothing here writes graph or verdicts.

Usage: python lightrag/jev_verify.py --selftest   (offline, httpx.MockTransport)
"""
import argparse
import asyncio
import json
import math
import os
import sys
import weakref

import httpx

MODEL = "jev-latest"
PROMPT_VERSION = "v1"
BASE_URL = "https://api.typesafe.ai"
TIMEOUT = 15.0
MAX_TRIES = 5
BACKOFF = 1.0  # doubles each retry; the selftest sets it to 0
CONCURRENCY = 4
USAGE = {"input_tokens": 0, "calls": 0}

_SEMS = weakref.WeakKeyDictionary()  # one Semaphore per event loop


def _sem():
    loop = asyncio.get_running_loop()
    if loop not in _SEMS:
        _SEMS[loop] = asyncio.Semaphore(CONCURRENCY)
    return _SEMS[loop]


def build_state(name, facts):
    facts = facts if isinstance(facts, dict) else {}
    return {
        "entity_name": name,
        "pubchem_iupac": facts.get("iupac") or "(none)",
        "pubchem_formula": facts.get("formula") or "(none)",
    }


QUESTION_TEXT = {
    "v1": {
        "instructions": (
            "Decide whether the PubChem record (pubchem_iupac, pubchem_formula) is the SAME substance "
            "that entity_name denotes. Form words (Nanoparticles, Powder, Nanofluid, Nanowire, Flakes) "
            "do not change the substance. A different compound, hydration state or composition is NOT "
            "the same (e.g. 'Graphene Oxide' vs methane CH4 -> not the same). If pubchem_iupac or "
            "pubchem_formula is '(none)' there is no evidence for a match."
        ),
        "true": "Same substance (form words ignored)",
        "false": "Different compound, hydration state or composition, or no usable record",
    },
    "v2": {  # experimental, probed by jev_v2_probe.py
        "instructions": (
            "Decide whether entity_name unambiguously denotes exactly the one pure substance in the "
            "PubChem record (pubchem_iupac, pubchem_formula), so that the record's properties (formula, "
            "molar mass, melting point) may be attached to a knowledge-graph node named entity_name. "
            "Form words (Nanoparticles, Powder, Nanofluid, Nanowire, Flakes) do not change the substance. "
            "Answer false when any of these holds: the name denotes a different compound, hydration state "
            "or composition; the name is a generic family or class, or does not fix the stoichiometry "
            "(for example 'Manganese Oxide', 'Metal Hydride', 'Fatty Acid'); the name is an ambiguous "
            "abbreviation, code or trade name that could stand for several substances; the name denotes "
            "a mixture, solution, alloy or composite rather than one pure substance; the name denotes a "
            "spectral line, an energy level, a single atom, an ion, a cluster, a slab or surface model, "
            "or a physical state or phase (vapor, ice, liquid, amorphous) rather than the substance "
            "itself; or the record is '(none)'."
        ),
        "true": "The name fixes exactly this one pure substance (form words ignored)",
        "false": ("A different substance, or the name is generic or ambiguous, a mixture, a spectral "
                  "line, atom, ion, cluster, slab, or a physical state rather than the substance itself, "
                  "or there is no usable record"),
    },
}


def build_question(version=PROMPT_VERSION):
    t = QUESTION_TEXT.get(version)
    if t is None:
        raise ValueError(f"unknown prompt version {version!r}")
    return {"same": {"type": "noul", "instructions": t["instructions"],
                     "criteria": {"true": t["true"], "false": t["false"]}}}


def parse_noul(body):
    try:
        v = body["answers"]["same"]["noul"]
    except (KeyError, TypeError):
        return None
    if isinstance(v, bool) or not isinstance(v, (int, float)):
        return None
    v = float(v)
    return v if math.isfinite(v) and 0.0 <= v <= 1.0 else None


def usage_tokens(body):
    u = body.get("usage") if isinstance(body, dict) else None
    n = u.get("input_tokens") if isinstance(u, dict) else None
    return n if isinstance(n, int) and not isinstance(n, bool) else 0


class JevBreaker:
    """Stops calling Jev after 3 consecutive failures or one fatal error (reasons are constants)."""

    def __init__(self):
        self.fails = 0
        self.tripped = False
        self.reason = ""

    def allow(self):
        return not self.tripped

    def record(self, ok):
        self.fails = 0 if ok else self.fails + 1
        if self.fails >= 3:
            self.trip("3 consecutive failures")

    def trip(self, reason):
        if not self.tripped:
            self.tripped, self.reason = True, reason
            print(f"[jev] disabled: {reason}", file=sys.stderr)


BREAKER = JevBreaker()


async def jev_same(client, name, facts, breaker=None, version=PROMPT_VERSION):
    """P(PubChem record is the same substance as name), or None. Never raises."""
    breaker = breaker or BREAKER
    if not breaker.allow():
        return None
    key = os.environ.get("TYPESAFE_API_KEY")
    if not key:
        breaker.trip("no TYPESAFE_API_KEY")
        return None
    headers = {"Authorization": f"Bearer {key}"}
    try:
        payload = {"model": MODEL, "state": build_state(name, facts), "questions": build_question(version)}
        for attempt in range(MAX_TRIES):
            async with _sem():
                r = await client.post(f"{BASE_URL}/v1/systemone", json=payload, headers=headers,
                                      timeout=TIMEOUT)
            if r.status_code == 401:
                breaker.trip("http-401")
                return None
            if r.status_code in (429, 529):
                if attempt < MAX_TRIES - 1:
                    await asyncio.sleep(BACKOFF * 2 ** attempt)
                continue
            if r.status_code != 200:
                break
            body = r.json()
            p = parse_noul(body)
            if p is None:
                break
            USAGE["input_tokens"] += usage_tokens(body)
            USAGE["calls"] += 1
            breaker.record(True)
            return p
    except (httpx.HTTPError, ValueError, KeyError, TypeError):
        pass
    breaker.record(False)
    return None


def decide(p, lo, hi):
    if not (lo < hi and hi > 0.5):  # hi <= 0.5 would let a coin-flip p count as 'yes'
        raise ValueError(f"need lo < hi and hi > 0.5, got {lo}, {hi}")
    if p is None:
        return "review"
    return "yes" if p >= hi else "no" if p <= lo else "review"


# ------------------------------------------------------------------ selftest
_N = 0
_V1_FROZEN = {"same": {
    "type": "noul",
    "instructions": (
        "Decide whether the PubChem record (pubchem_iupac, pubchem_formula) is the SAME substance "
        "that entity_name denotes. Form words (Nanoparticles, Powder, Nanofluid, Nanowire, Flakes) "
        "do not change the substance. A different compound, hydration state or composition is NOT "
        "the same (e.g. 'Graphene Oxide' vs methane CH4 -> not the same). If pubchem_iupac or "
        "pubchem_formula is '(none)' there is no evidence for a match."
    ),
    "criteria": {
        "true": "Same substance (form words ignored)",
        "false": "Different compound, hydration state or composition, or no usable record",
    },
}}


def check(cond, msg):
    global _N
    assert cond, msg
    _N += 1


def _client(handler):
    return httpx.AsyncClient(transport=httpx.MockTransport(handler), trust_env=False)


def _ok_body(p=0.93, tokens=40):
    return {"answers": {"same": {"noul": p}}, "usage": {"input_tokens": tokens}}


async def _selftest_async():
    facts = {"cid": 962, "formula": "H2O", "iupac": "oxidane"}

    # 429 twice then 200 -> exactly 3 requests
    reqs = []

    def h429(req):
        reqs.append(req)
        return httpx.Response(429 if len(reqs) <= 2 else 200, json=_ok_body(0.91))

    b = JevBreaker()
    async with _client(h429) as c:
        p = await jev_same(c, "Water", facts, b)
    check(p == 0.91 and len(reqs) == 3, "429x2 then 200 -> p after exactly 3 requests")
    check(not b.tripped and b.fails == 0, "retried success leaves breaker clean")

    # request shape: auth header, model, name intact (non-ASCII and 300 chars)
    seen = []

    def hseen(req):
        seen.append(req)
        return httpx.Response(200, json=_ok_body())

    names = ["Zinkoxid-Nanopartikel ZnO/Wasser 水 α-Al2O3", "N" * 300]
    async with _client(hseen) as c:
        for nm in names:
            check(await jev_same(c, nm, facts, JevBreaker()) == 0.93, "name call returns p")
    for nm, rq in zip(names, seen, strict=True):
        body = json.loads(rq.content)
        check(body["state"]["entity_name"] == nm, "entity_name intact in request")
        check(rq.headers["authorization"] == "Bearer test-key", "Bearer header")
        check(body["model"] == "jev-latest", "model alias in body")
        check(str(rq.url) == "https://api.typesafe.ai/v1/systemone", "endpoint url")

    # version selects the question text; unknown version -> None, never raises
    seen.clear()
    async with _client(hseen) as c:
        check(await jev_same(c, "X", facts, JevBreaker(), version="v2") == 0.93, "v2 call returns p")
        check(await jev_same(c, "X", facts, JevBreaker()) == 0.93, "default call returns p")
        n = len(seen)
        check(await jev_same(c, "X", facts, JevBreaker(), version="v9") is None and len(seen) == n,
              "unknown version -> None, no request")
    check(json.loads(seen[0].content)["questions"] == build_question("v2"), "v2 question sent")
    check(json.loads(seen[1].content)["questions"] == _V1_FROZEN, "default question sent is v1")

    # 401 -> None, tripped, next call makes no request
    reqs.clear()

    def h401(req):
        reqs.append(req)
        return httpx.Response(401, json={"error": "nope"})

    b = JevBreaker()
    async with _client(h401) as c:
        check(await jev_same(c, "X", facts, b) is None, "401 -> None")
        check(b.tripped and b.reason == "http-401", "401 trips breaker")
        n = len(reqs)
        check(await jev_same(c, "X", facts, b) is None and len(reqs) == n, "no request after trip")

    # missing key -> None, tripped, zero requests
    reqs.clear()
    saved = os.environ.pop("TYPESAFE_API_KEY")
    try:
        b = JevBreaker()
        async with _client(h401) as c:
            check(await jev_same(c, "X", facts, b) is None, "missing key -> None")
        check(b.tripped and b.reason == "no TYPESAFE_API_KEY" and not reqs, "missing key trips, 0 requests")
    finally:
        os.environ["TYPESAFE_API_KEY"] = saved

    # transport errors -> None, breaker trips after 3, 4th call sends nothing
    for exc in (httpx.ConnectError, httpx.ReadTimeout):
        reqs.clear()

        def herr(req, exc=exc):
            reqs.append(req)
            raise exc("boom", request=req)

        b = JevBreaker()
        async with _client(herr) as c:
            for _ in range(3):
                check(await jev_same(c, "X", facts, b) is None, f"{exc.__name__} -> None")
            check(b.tripped and b.reason == "3 consecutive failures" and len(reqs) == 3, "trips after 3")
            check(await jev_same(c, "X", facts, b) is None and len(reqs) == 3, "4th call sends nothing")

    # 422 -> None, counts as failure
    b = JevBreaker()
    async with _client(lambda req: httpx.Response(422, json={"detail": "bad"})) as c:
        check(await jev_same(c, "X", facts, b) is None and b.fails == 1, "422 -> None, one failure")

    # bad JSON and out-of-range noul -> None, failure
    b = JevBreaker()
    async with _client(lambda req: httpx.Response(200, content=b"not json")) as c:
        check(await jev_same(c, "X", facts, b) is None and b.fails == 1, "bad JSON -> None")
    async with _client(lambda req: httpx.Response(200, json=_ok_body(1.7))) as c:
        check(await jev_same(c, "X", facts, b) is None and b.fails == 2, "noul 1.7 -> None")

    # 429 forever -> exactly MAX_TRIES requests then None
    reqs.clear()

    def hforever(req):
        reqs.append(req)
        return httpx.Response(429)

    b = JevBreaker()
    async with _client(hforever) as c:
        check(await jev_same(c, "X", facts, b) is None, "429 forever -> None")
    check(len(reqs) == MAX_TRIES and b.fails == 1, "MAX_TRIES requests, one recorded failure")

    # no usage.input_tokens -> p returned, USAGE tokens unchanged
    before = USAGE["input_tokens"]
    async with _client(lambda req: httpx.Response(200, json={"answers": {"same": {"noul": 0.5}}})) as c:
        check(await jev_same(c, "X", facts, JevBreaker()) == 0.5, "no usage -> p still returned")
    check(USAGE["input_tokens"] == before, "USAGE tokens unchanged without usage")
    async with _client(lambda req: httpx.Response(200, json=_ok_body(0.9, 7))) as c:
        await jev_same(c, "X", facts, JevBreaker())
    check(USAGE["input_tokens"] == before + 7, "USAGE tokens accumulate")

    # success after 2 failures resets the consecutive counter
    state = {"n": 0}

    def hmix(req):
        state["n"] += 1
        return httpx.Response(422) if state["n"] <= 2 else httpx.Response(200, json=_ok_body())

    b = JevBreaker()
    async with _client(hmix) as c:
        for _ in range(3):
            await jev_same(c, "X", facts, b)
    check(b.fails == 0 and not b.tripped, "success resets consecutive failures")


def _selftest():
    global BACKOFF
    old_backoff, old_key = BACKOFF, os.environ.get("TYPESAFE_API_KEY")
    BACKOFF = 0
    os.environ["TYPESAFE_API_KEY"] = "test-key"
    try:
        s = build_state("Water", {"iupac": "", "cid": 1})
        check(s == {"entity_name": "Water", "pubchem_iupac": "(none)", "pubchem_formula": "(none)"},
              "empty iupac / missing formula -> (none)")
        s = build_state("Water", {"iupac": "oxidane", "formula": "H2O"})
        check(s["pubchem_iupac"] == "oxidane" and s["pubchem_formula"] == "H2O", "facts pass through")
        q = build_question()["same"]
        check(q["type"] == "noul" and set(q["criteria"]) == {"true", "false"}, "question shape")
        check(PROMPT_VERSION == "v1" and build_question() == build_question("v1") == _V1_FROZEN,
              "v1 question byte-identical to frozen copy")
        q2 = build_question("v2")["same"]
        check(q2["type"] == "noul" and set(q2["criteria"]) == {"true", "false"}, "v2 question shape")
        check(q2["instructions"].startswith("Decide whether entity_name unambiguously denotes exactly")
              and q2["instructions"].endswith("or the record is '(none)'."), "v2 instructions")
        check(q2["criteria"]["true"].startswith("The name fixes exactly this one pure substance"),
              "v2 criteria true")
        try:
            build_question("v9")
        except ValueError:
            check(True, "unknown version raises")
        else:
            check(False, "unknown version must raise")

        good = {"answers": {"same": {"noul": 0.9}}}
        check(parse_noul(good) == 0.9, "parse good")
        check(parse_noul({"answers": {}}) is None, "parse missing key")
        for bad in (float("nan"), float("inf"), 1.7, -0.3, True, "0.9", None):
            check(parse_noul({"answers": {"same": {"noul": bad}}}) is None, f"parse rejects {bad!r}")
        check(parse_noul(None) is None and parse_noul([1]) is None, "parse non-dict")
        check(usage_tokens({"usage": {"input_tokens": 12}}) == 12, "usage tokens")
        check(usage_tokens({"usage": 5}) == 0 and usage_tokens("x") == 0 and usage_tokens({}) == 0,
              "usage robust")

        check(decide(0.5, 0.2, 0.8) == "review", "decide 0.5 review")
        check(decide(0.2, 0.2, 0.8) == "no", "decide exactly lo -> no")
        check(decide(0.8, 0.2, 0.8) == "yes", "decide exactly hi -> yes")
        check(decide(None, 0.2, 0.8) == "review", "decide None -> review")
        for lo, hi in ((0.8, 0.2), (0.5, 0.5), (0.2, 0.5), (0.1, 0.3)):  # hi must exceed 0.5
            try:
                decide(0.5, lo, hi)
            except ValueError:
                check(True, "decide lo>=hi raises")
            else:
                check(False, "decide lo>=hi must raise")

        b = JevBreaker()
        b.record(False)
        b.record(False)
        b.record(True)
        b.record(False)
        check(not b.tripped and b.fails == 1, "breaker counts consecutive only")
        asyncio.run(_selftest_async())
    finally:
        BACKOFF = old_backoff
        if old_key is None:
            os.environ.pop("TYPESAFE_API_KEY", None)
        else:
            os.environ["TYPESAFE_API_KEY"] = old_key
    print(f"selftest OK ({_N} asserts)")


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--selftest", action="store_true", help="offline self-check")
    if not ap.parse_args().selftest:
        ap.print_usage()
        return 2
    _selftest()
    return 0


if __name__ == "__main__":
    sys.exit(main())
