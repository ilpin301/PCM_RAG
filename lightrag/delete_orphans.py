"""Delete orphaned nodes/edges from data/audit/orphans.json through the LightRAG API.

Only deleted_doc_only items. Nodes first (their edges go with them), then edges whose two
endpoints both survive. Sequential - every call rewrites the graphml. Resumable: an item that is
already gone counts as done. Log: data/audit/delete_orphans.log, one line per item.

  python delete_orphans.py            # dry: counts only
  python delete_orphans.py --apply [--limit N]
"""
import json
import sys
from pathlib import Path

import httpx

import enrich_pubchem as ep  # LIGHTRAG_URL, LIGHTRAG_KEY (from lightrag/.env)

AUDIT = Path(__file__).parent / "data" / "audit"
GONE = ("not found", "does not exist", "not exist")


def _gone(r):
    return r.status_code == 404 or any(g in r.text.lower() for g in GONE)


def main(argv):
    apply = "--apply" in argv
    limit = int(argv[argv.index("--limit") + 1]) if "--limit" in argv else None
    items = [x for x in json.loads((AUDIT / "orphans.json").read_text(encoding="utf-8")) if x["deleted_doc_only"]]
    nodes = sorted({x["key"] for x in items if x["kind"] == "node"})
    edges = [tuple(x["key"]) for x in items
             if x["kind"] == "edge" and x["key"][0] not in nodes and x["key"][1] not in nodes]
    print(f"nodes {len(nodes)}  edges with surviving endpoints {len(edges)}  apply={apply}", flush=True)
    if not apply:
        return 0
    h = {"X-API-Key": ep.LIGHTRAG_KEY}
    todo = [("node", n) for n in nodes] + [("edge", e) for e in edges]
    fails = 0
    with httpx.Client(trust_env=False, timeout=600) as c, \
            open(AUDIT / "delete_orphans.log", "a", encoding="utf-8") as log:
        for kind, key in todo[:limit]:
            if kind == "node":
                r = c.request("DELETE", f"{ep.LIGHTRAG_URL}/graph/entity/delete", headers=h,
                              json={"entity_name": key})
            else:
                r = c.request("DELETE", f"{ep.LIGHTRAG_URL}/graph/relation/delete", headers=h,
                              json={"source_entity": key[0], "target_entity": key[1]})
                if r.status_code != 200 and _gone(r):  # graphml direction may be reversed
                    r = c.request("DELETE", f"{ep.LIGHTRAG_URL}/graph/relation/delete", headers=h,
                                  json={"source_entity": key[1], "target_entity": key[0]})
            status = "ok" if r.status_code == 200 and not _gone(r) else "gone" if _gone(r) else "FAIL"
            fails += status == "FAIL"
            log.write(json.dumps({"kind": kind, "key": key, "status": status,
                                  "http": r.status_code, "body": r.text[:200]}, ensure_ascii=False) + "\n")
            log.flush()
    print(f"done, failures {fails}", flush=True)
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
