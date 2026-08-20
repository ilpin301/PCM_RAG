#!/usr/bin/env python
"""
Fixes: docs in kv_store_doc_status.json whose chunks_list/chunks_count disagree
with the chunks that actually exist in kv_store_text_chunks.json for that doc
(multimodal chunks written to text_chunks but never appended to chunks_list).
Deleting a doc by its stale chunks_list would leave orphan chunks behind.

DRY RUN IS THE DEFAULT. Pass --apply to write changes.
"""
import argparse
import json
import shutil
import subprocess
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path

RAG_STORAGE = Path(r"F:\____IL_AI\PCM_RAG\lightrag\data\rag_storage")
DOC_STATUS = RAG_STORAGE / "kv_store_doc_status.json"
TEXT_CHUNKS = RAG_STORAGE / "kv_store_text_chunks.json"
CONTAINER_NAME = "pcm_rag-lightrag-1"


def container_running():
    try:
        out = subprocess.run(
            ["docker", "ps", "--filter", f"name={CONTAINER_NAME}", "--format", "{{.Names}}"],
            capture_output=True, text=True, check=True,
        )
    except Exception as e:
        print(f"WARNING: could not check docker status ({e}); assuming running for safety")
        return True
    return CONTAINER_NAME in out.stdout.split()


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--apply", action="store_true", help="write changes (default: dry run)")
    args = ap.parse_args()

    doc_status = json.loads(DOC_STATUS.read_text(encoding="utf-8"))
    text_chunks = json.loads(TEXT_CHUNKS.read_text(encoding="utf-8"))

    actual_by_doc = defaultdict(list)
    for chunk_id, chunk in text_chunks.items():
        full_doc_id = chunk.get("full_doc_id")
        actual_by_doc[full_doc_id].append(chunk_id)

    changed = 0
    for doc_id, doc in doc_status.items():
        declared_list = doc.get("chunks_list") or []
        declared_set = set(declared_list)
        actual_set = set(actual_by_doc.get(doc_id, []))

        if declared_set == actual_set:
            continue

        missing = sorted(actual_set - declared_set)   # in text_chunks, not in list
        stale = sorted(declared_set - actual_set)      # in list, not in text_chunks
        union = sorted(actual_set | declared_set - set(stale))  # union minus stale ids

        print(f"doc_id={doc_id}")
        print(f"  file_path={doc.get('file_path')}")
        print(f"  declared={len(declared_list)} actual={len(actual_set)} delta={len(actual_set) - len(declared_list)}")
        if missing:
            print(f"  missing_from_list ({len(missing)}): {missing[:5]}")
        if stale:
            print(f"  stale_in_list_not_in_text_chunks ({len(stale)}): {stale[:5]}")

        if args.apply:
            new_list = sorted(actual_set - set(stale))
            doc["chunks_list"] = new_list
            doc["chunks_count"] = len(new_list)

        changed += 1

    if not args.apply:
        print(f"\nDRY RUN — no files written. {changed} doc(s) would change.")
        print(f"CHANGED={changed}")
        return 0

    if changed == 0:
        print("No changes needed.")
        print("CHANGED=0")
        return 0

    if container_running():
        print(f"ABORT: container {CONTAINER_NAME} is running. Stop it before --apply.")
        sys.exit(1)

    ts = datetime.now().strftime("%Y%m%d-%H%M%S")
    backup = DOC_STATUS.with_name(DOC_STATUS.name + f".bak-{ts}")
    shutil.copy2(DOC_STATUS, backup)
    print(f"Backup written: {backup}")

    DOC_STATUS.write_text(json.dumps(doc_status, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {DOC_STATUS}")
    print(f"CHANGED={changed}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
