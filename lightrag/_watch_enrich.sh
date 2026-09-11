#!/bin/bash
cd /x/RAG_MAIN/PCM_RAG/lightrag
key=$(grep '^LIGHTRAG_API_KEY=' .env | cut -d= -f2 | tr -d '"'"'"' \r')
cnt(){ python -c "import json;print(len(json.load(open('data/enrich_cache/$1.json',encoding='utf-8'))))" 2>/dev/null || echo -1; }
graphenr(){ 
python - "$key" <<'PY' 2>/dev/null || echo 0
import sys,os,urllib.request,urllib.parse,json,random
key=sys.argv[1];base="http://localhost:9622"
def j(p):
 r=urllib.request.Request(base+p,headers={"X-API-Key":key});return json.load(urllib.request.urlopen(r,timeout=20))
labs=[l for l in j("/graph/label/list") if l.endswith("(ref_text)")]
random.seed(2);samp=random.sample(labs,min(30,len(labs)));e=0
for lbl in samp:
 try:
  u="/graphs?"+urllib.parse.urlencode({"label":lbl,"max_depth":1,"max_nodes":6})
  d=j(u);t=[n for n in d.get("nodes",[]) if n.get("id")==lbl or lbl in (n.get("labels") or [])]
  if t and "<!--OPENALEX_START-->" in t[0].get("properties",{}).get("description",""): e+=1
 except: pass
print(e)
PY
}
prev_e=-1; prev_j=-1; stall=0
for i in $(seq 1 90); do
  procs=$(tasklist //FI "IMAGENAME eq python.exe" 2>/dev/null | grep -c python.exe)
  e=$(cnt extract_openalex); s=$(cnt search_openalex); jd=$(cnt judge_openalex)
  ts=$(date +%H:%M:%S)
  echo "$ts extract=$e search=$s judge=$jd procs=$procs"
  # graph writes started?
  if [ "$jd" -gt 30 ]; then
     ge=$(graphenr)
     echo "$ts GRAPH_SAMPLE enriched=$ge/30"
     if [ "$ge" -gt 0 ]; then echo "TRIGGER writes_landed"; break; fi
  fi
  # stall detection: extract+judge unchanged
  if [ "$e" = "$prev_e" ] && [ "$jd" = "$prev_j" ]; then stall=$((stall+1)); else stall=0; fi
  if [ "$stall" -ge 6 ]; then echo "TRIGGER stalled_6x"; break; fi
  if [ "$procs" -lt 2 ]; then echo "TRIGGER procs_ended"; break; fi
  prev_e=$e; prev_j=$jd
  sleep 30
done
echo "WATCH_DONE"
