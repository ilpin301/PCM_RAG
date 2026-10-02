"""Delete orphaned nodes/edges from data/audit/orphans.json through the LightRAG API.

Only deleted_doc_only items. Nodes first (their edges go with them), then edges whose two
endpoints both survive. Sequential - every call rewrites the graphml. Resumable: an item that is
already gone counts as done. Log: data/audit/delete_orphans.log, one line per item.

  python delete_orphans.py            # dry: counts only
  python delete_orphans.py --apply [--limit N]
  python delete_orphans.py --selftest
"""
import json
import sys
from pathlib import Path

import httpx

import audit_integrity
import enrich_pubchem as ep  # LIGHTRAG_URL, LIGHTRAG_KEY (from lightrag/.env)

AUDIT = Path(__file__).parent / "data" / "audit"
GONE = ("not found", "does not exist", "not exist")


def _gone(r):
    return r.status_code == 404 or any(g in r.text.lower() for g in GONE)


def _k(kind, key):
    return (kind, key if kind == "node" else frozenset(key))


def safe_plan(items, graph, chunks, doc_files):
    """Re-check orphans.json against the live store: delete only still-fresh orphans, and a node only
    if every incident edge is itself a fresh orphan (node delete cascades to its edges)."""
    fresh = {_k(x["kind"], x["key"]) for x in audit_integrity.orphans(graph, chunks, doc_files) if x["deleted_doc_only"]}
    items = [x for x in items if x["deleted_doc_only"]]
    ok = [x for x in items if _k(x["kind"], x["key"]) in fresh]
    cand = {x["key"] for x in ok if x["kind"] == "node"}
    blocked = {}
    for kind, key, _ in graph:
        if kind == "edge":
            for n in set(key) & cand:
                if _k("edge", key) not in fresh:
                    blocked.setdefault(n, []).append(key)
    nodes = sorted(cand - set(blocked))
    edges = [tuple(x["key"]) for x in ok
             if x["kind"] == "edge" and x["key"][0] not in nodes and x["key"][1] not in nodes]
    return {"nodes": nodes, "edges": edges, "blocked": blocked, "stale": len(items) - len(ok)}


def _selftest():
    chunks = {"c1": {"content": "x"}}
    g = [("node", "Old", {"source_id": "gone1", "file_path": "s.pdf"}),
         ("node", "Live", {"source_id": "c1", "file_path": "a.pdf"}),
         ("node", "Hub", {"source_id": "gone2", "file_path": "s.pdf"}),
         ("edge", ("Old", "Live"), {"source_id": "gone1", "file_path": "s.pdf"}),
         ("edge", ("Hub", "Live"), {"source_id": "c1", "file_path": "a.pdf"})]
    items = audit_integrity.orphans(g, chunks, {"a.pdf"}) + [
        {"kind": "node", "key": "Ghost", "deleted_doc_only": True}]
    p = safe_plan(items, g, chunks, {"a.pdf"})
    assert p["nodes"] == ["Old"], p
    assert list(p["blocked"]) == ["Hub"] and p["blocked"]["Hub"] == [("Hub", "Live")], p
    assert p["stale"] >= 1, p
    assert ("Old", "Live") not in p["edges"] and p["edges"] == [], p
    print("selftest OK")


def main(argv):
    if "--selftest" in argv:
        return _selftest()
    apply = "--apply" in argv
    limit = int(argv[argv.index("--limit") + 1]) if "--limit" in argv else None
    store = audit_integrity.STORE
    rd = lambda n: json.loads((store / n).read_text(encoding="utf-8"))
    docs = {v.get("file_path") for v in rd("kv_store_doc_status.json").values()}
    p = safe_plan(json.loads((AUDIT / "orphans.json").read_text(encoding="utf-8")),
                  audit_integrity.load_graph(), rd("kv_store_text_chunks.json"), docs)
    nodes, edges, blocked = p["nodes"], p["edges"], p["blocked"]
    print(f"nodes {len(nodes)}  edges with surviving endpoints {len(edges)}  apply={apply}"
          f"  stale {p['stale']}, blocked {len(blocked)}", flush=True)
    for n in list(blocked)[:20]:
        print(f"  BLOCKED {n}: {blocked[n]}", flush=True)
    if not apply:
        return 1 if blocked else 0
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
    return 1 if fails or blocked else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
