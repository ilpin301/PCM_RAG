"""Apply data/audit/edge_edits.json [{source, target, old, new}] via POST /graph/relation/edit.

Sequential (each call rewrites the graphml), resumable: an edge whose graph description equals "new"
counts as done ("already") only when its relation vector is also in Qdrant (COLL, content ends with
the new description); otherwise it is re-embedded ("revectored") or reported VECTOR_MISSING. One whose
current description is neither old nor new is reported as CHANGED and left alone. Current descriptions
come from GET /graphs around the source entity. --apply starts with LightRAG, Ollama and Qdrant
preflight checks (FATAL, exit 3, before any edit). A Qdrant error during the vector check/poll is logged
for that edge as QDRANT_ERROR (with the exception text), the loop continues, and the run exits 1.
--selftest runs asserts against fakes (no network).
Log: data/audit/apply_edge_edits.log.   python apply_edge_edits.py [--apply | --selftest]
"""
import json
import os
import sys
import time
from pathlib import Path

import httpx

import enrich_pubchem as ep

AUDIT = Path(__file__).parent / "data" / "audit"
QDRANT_URL = os.environ.get("QDRANT_URL", "http://127.0.0.1:6333")
COLL = "lightrag_vdb_relationships_bge_m3_1024d"


def current(c, h, s, t):
    r = c.get(f"{ep.LIGHTRAG_URL}/graphs", params={"label": s, "max_depth": 1, "max_nodes": 1000},
              headers=h)
    r.raise_for_status()
    for e in r.json().get("edges", []):
        if {e.get("source"), e.get("target")} == {s, t}:
            return (e.get("properties") or {}).get("description")
    return None


def vector_matches(points, new):
    return any((p.get("payload") or {}).get("content", "").rstrip().endswith(new.rstrip())
               for p in points)


def vector_ok(c, s, t, new):
    for a, b in ((s, t), (t, s)):
        r = c.post(f"{QDRANT_URL}/collections/{COLL}/points/scroll",
                   json={"filter": {"must": [{"key": "src_id", "match": {"value": a}},
                                             {"key": "tgt_id", "match": {"value": b}}]},
                         "limit": 10, "with_payload": True, "with_vector": False})
        r.raise_for_status()
        if vector_matches(r.json()["result"]["points"], new):
            return True
    return False


def status_for(cur, old, new, vec_ok):
    if cur == new:
        return "already" if vec_ok else "REVECTOR"
    if cur is None:
        return "GONE"
    return "EDIT" if cur == old else "CHANGED"


BAD = ("FAIL", "CHANGED", "GONE", "VECTOR_MISSING", "QDRANT_ERROR", "ERROR")


def require_qdrant(get=httpx.get):
    """Fail fast before any edit: without Qdrant the vector check/poll cannot work."""
    try:
        get(f"{QDRANT_URL}/collections", timeout=5, trust_env=False).raise_for_status()
    except Exception as e:
        ep.log(f"FATAL: Qdrant not reachable at {QDRANT_URL} ({type(e).__name__}: {e}) - "
               "start the compose stack first")
        sys.exit(3)


class QdrantError(Exception):
    pass


def process_edge(c, h, x, cur_fn=current, vec_fn=vector_ok, sleep=time.sleep):
    """One edge -> (status, error text or None). Never raises: a Qdrant failure is QDRANT_ERROR (a rerun
    re-checks it: pre-edit failure -> nothing edited; post-edit failure -> graph is new, vector unproven
    -> REVECTOR), any other exception is ERROR."""
    def vec(*a):
        try:
            return vec_fn(c, x["source"], x["target"], x["new"])
        except Exception as e:
            raise QdrantError(f"{type(e).__name__}: {e}") from e
    try:
        cur = cur_fn(c, h, x["source"], x["target"])
        status = status_for(cur, x["old"], x["new"], cur == x["new"] and vec())
        if status in ("EDIT", "REVECTOR"):
            done = "ok" if status == "EDIT" else "revectored"
            status = "FAIL"
            for s, t in ((x["source"], x["target"]), (x["target"], x["source"])):
                r = c.post(f"{ep.LIGHTRAG_URL}/graph/relation/edit", headers=h,
                           json={"source_id": s, "target_id": t,
                                 "updated_data": {"description": x["new"]}})
                if r.status_code == 200:
                    status = "VECTOR_MISSING"
                    for _ in range(5):
                        sleep(2)
                        if vec():
                            status = done
                            break
                    break
        return status, None
    except QdrantError as e:
        return "QDRANT_ERROR", str(e)
    except Exception as e:
        return "ERROR", f"{type(e).__name__}: {e}"


def run_all(c, h, edits, write, **kw):
    """Every edge gets exactly one log record; returns the number of problem edges."""
    bad = 0
    for x in edits:
        status, err = process_edge(c, h, x, **kw)
        bad += status in BAD
        rec = {"source": x["source"], "target": x["target"], "status": status}
        write(dict(rec, error=err) if err else rec)
    return bad


def selftest():
    p = [{"payload": {"content": "k\tA\nB\nnew text"}}]
    assert vector_matches(p, "new text") is True
    assert vector_matches(p, "old text") is False
    assert status_for("new", "old", "new", True) == "already"
    assert status_for("new", "old", "new", False) == "REVECTOR"
    assert status_for(None, "o", "n", True) == "GONE"
    assert status_for("x", "o", "n", True) == "CHANGED"
    assert status_for("o", "o", "n", False) == "EDIT"
    loop_selftest()
    print("selftest OK")
    return 0


def loop_selftest():
    """edit+poll loop and Qdrant preflight against fakes: no network, no sleeping."""
    class R:
        def __init__(self, code=200):
            self.status_code = code

        def raise_for_status(self):
            if self.status_code >= 400:
                raise RuntimeError(f"HTTP {self.status_code}")

    class C:  # fake httpx client: records edit posts
        def __init__(self):
            self.posts = []

        def post(self, url, **kw):
            self.posts.append(kw["json"])
            return R()

    x = {"source": "A", "target": "B", "old": "o", "new": "n"}

    def run(cur, vec):
        c = C()
        out = process_edge(c, {}, x, cur_fn=lambda *a: cur, vec_fn=vec, sleep=lambda s: None)
        return out, c

    def vec_err(*a):
        raise ConnectionError("qdrant down")

    seen = iter([False, True])  # pre-edit check n/a for cur == old; poll: missing once, then there
    (st, err), c = run("o", lambda *a: next(seen))
    assert (st, err) == ("ok", None) and len(c.posts) == 1, (st, err)
    (st, err), c = run("o", lambda *a: False)  # vector never appears
    assert (st, err) == ("VECTOR_MISSING", None) and len(c.posts) == 1, (st, err)
    (st, err), c = run("o", vec_err)  # poll raises after a successful edit
    assert st == "QDRANT_ERROR" and "qdrant down" in err and len(c.posts) == 1, (st, err)
    (st, err), c = run("n", vec_err)  # pre-edit check raises: nothing was edited
    assert st == "QDRANT_ERROR" and "qdrant down" in err and c.posts == [], (st, err)
    (st, err), c = run("n", lambda *a: True)  # rerun semantics: already done
    assert (st, err) == ("already", None) and c.posts == []
    seen = iter([False, True])
    (st, err), c = run("n", lambda *a: next(seen))  # graph ok, vector missing -> revectored
    assert (st, err) == ("revectored", None) and len(c.posts) == 1, (st, err)
    (st, err), c = run("zzz", lambda *a: True)
    assert st == "CHANGED" and c.posts == []
    # each edge gets a log line and the loop continues; problems are counted
    lines, c = [], C()
    vecs = {"A": vec_err, "B": lambda *a: True}
    edits = [dict(x, source="A"), dict(x, source="B", old="n"), dict(x, source="C", old="o")]
    curs = {"A": "o", "B": "n", "C": "o"}
    n = run_all(c, {}, edits, lines.append,
                cur_fn=lambda cc, h, s, t: curs[s],
                vec_fn=lambda cc, s, t, new: vecs.get(s, lambda *a: False)(),
                sleep=lambda s: None)
    got = [(l["source"], l["status"]) for l in lines]
    assert got == [("A", "QDRANT_ERROR"), ("B", "already"), ("C", "VECTOR_MISSING")], got
    assert "qdrant down" in lines[0]["error"] and n == 2, n

    class Up:
        def get(self, url, **kw):
            assert url.endswith("/collections"), url
            return R()

    class Down:
        def get(self, url, **kw):
            raise ConnectionError("refused")

    require_qdrant(Up().get)
    try:
        require_qdrant(Down().get)
        raise AssertionError("must exit")
    except SystemExit as e:
        assert e.code == 3, e.code


def main(argv):
    if "--selftest" in argv:
        return selftest()
    edits =json.loads((AUDIT / "edge_edits.json").read_text(encoding="utf-8"))
    print(f"edges {len(edits)} apply={'--apply' in argv}", flush=True)
    if "--apply" not in argv:
        return 0
    ep.require_lightrag()
    ep.require_ollama()
    require_qdrant()
    h = {"X-API-Key": ep.LIGHTRAG_KEY}
    with httpx.Client(trust_env=False, timeout=600) as c, \
            open(AUDIT / "apply_edge_edits.log", "a", encoding="utf-8") as log:
        def write(rec):
            log.write(json.dumps(rec, ensure_ascii=False) + "\n")
            log.flush()
        bad = run_all(c, h, edits, write)
    print(f"done, problems {bad}", flush=True)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
