"""Apply data/audit/edge_edits.json [{source, target, old, new}] via POST /graph/relation/edit.

Sequential (each call rewrites the graphml), resumable: an edge whose current description already
equals "new" is skipped; one whose current description is neither old nor new is reported as
CHANGED and left alone. Current descriptions come from GET /graphs around the source entity.
Log: data/audit/apply_edge_edits.log.   python apply_edge_edits.py [--apply]
"""
import json
import sys
from pathlib import Path

import httpx

import enrich_pubchem as ep

AUDIT = Path(__file__).parent / "data" / "audit"


def current(c, h, s, t):
    r = c.get(f"{ep.LIGHTRAG_URL}/graphs", params={"label": s, "max_depth": 1, "max_nodes": 1000},
              headers=h)
    r.raise_for_status()
    for e in r.json().get("edges", []):
        if {e.get("source"), e.get("target")} == {s, t}:
            return (e.get("properties") or {}).get("description")
    return None


def main(argv):
    edits = json.loads((AUDIT / "edge_edits.json").read_text(encoding="utf-8"))
    print(f"edges {len(edits)} apply={'--apply' in argv}", flush=True)
    if "--apply" not in argv:
        return 0
    h = {"X-API-Key": ep.LIGHTRAG_KEY}
    bad = 0
    with httpx.Client(trust_env=False, timeout=600) as c, \
            open(AUDIT / "apply_edge_edits.log", "a", encoding="utf-8") as log:
        for x in edits:
            cur = current(c, h, x["source"], x["target"])
            if cur == x["new"]:
                status = "already"
            elif cur != x["old"]:
                status = "CHANGED" if cur is not None else "GONE"
            else:
                status = "FAIL"
                for s, t in ((x["source"], x["target"]), (x["target"], x["source"])):
                    r = c.post(f"{ep.LIGHTRAG_URL}/graph/relation/edit", headers=h,
                               json={"source_id": s, "target_id": t,
                                     "updated_data": {"description": x["new"]}})
                    if r.status_code == 200:
                        status = "ok"
                        break
            bad += status in ("FAIL", "CHANGED", "GONE")
            log.write(json.dumps({"source": x["source"], "target": x["target"], "status": status},
                                 ensure_ascii=False) + "\n")
            log.flush()
    print(f"done, problems {bad}", flush=True)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
