"""Apply data/audit/edge_edits.json [{source, target, old, new}] via POST /graph/relation/edit.

Sequential (each call rewrites the graphml), resumable: an edge whose graph description equals "new"
counts as done ("already") only when its relation vector is also in Qdrant (COLL, content ends with
the new description); otherwise it is re-embedded ("revectored") or reported VECTOR_MISSING. One whose
current description is neither old nor new is reported as CHANGED and left alone. Current descriptions
come from GET /graphs around the source entity. --apply starts with LightRAG and Ollama preflight
checks; --selftest runs pure-function asserts.
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


def selftest():
    p = [{"payload": {"content": "k\tA\nB\nnew text"}}]
    assert vector_matches(p, "new text") is True
    assert vector_matches(p, "old text") is False
    assert status_for("new", "old", "new", True) == "already"
    assert status_for("new", "old", "new", False) == "REVECTOR"
    assert status_for(None, "o", "n", True) == "GONE"
    assert status_for("x", "o", "n", True) == "CHANGED"
    assert status_for("o", "o", "n", False) == "EDIT"
    print("selftest OK")
    return 0


def main(argv):
    if "--selftest" in argv:
        return selftest()
    edits =json.loads((AUDIT / "edge_edits.json").read_text(encoding="utf-8"))
    print(f"edges {len(edits)} apply={'--apply' in argv}", flush=True)
    if "--apply" not in argv:
        return 0
    ep.require_lightrag()
    ep.require_ollama()
    h = {"X-API-Key": ep.LIGHTRAG_KEY}
    bad = 0
    with httpx.Client(trust_env=False, timeout=600) as c, \
            open(AUDIT / "apply_edge_edits.log", "a", encoding="utf-8") as log:
        for x in edits:
            cur = current(c, h, x["source"], x["target"])
            vec = cur == x["new"] and vector_ok(c, x["source"], x["target"], x["new"])
            status = status_for(cur, x["old"], x["new"], vec)
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
                            time.sleep(2)
                            if vector_ok(c, x["source"], x["target"], x["new"]):
                                status = done
                                break
                        break
            bad += status in ("FAIL", "CHANGED", "GONE", "VECTOR_MISSING")
            log.write(json.dumps({"source": x["source"], "target": x["target"], "status": status},
                                 ensure_ascii=False) + "\n")
            log.flush()
    print(f"done, problems {bad}", flush=True)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
