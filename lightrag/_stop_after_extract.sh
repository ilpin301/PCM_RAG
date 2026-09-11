#!/bin/bash
cd /x/RAG_MAIN/PCM_RAG/lightrag
cnt(){ python -c "import json;print(len(json.load(open('data/enrich_cache/$1.json',encoding='utf-8'))))" 2>/dev/null || echo -1; }
kill_enrich(){
  powershell -NoProfile -Command "Get-CimInstance Win32_Process -Filter \"Name='python.exe'\" | Where-Object {\$_.CommandLine -like '*enrich_openalex*'} | ForEach-Object { Stop-Process -Id \$_.ProcessId -Force; Write-Output ('killed '+\$_.ProcessId) }" 2>/dev/null
}
base_s=$(cnt search_openalex)
echo "$(date +%H:%M:%S) baseline search=$base_s"
for i in $(seq 1 150); do
  e=$(cnt extract_openalex); s=$(cnt search_openalex); jd=$(cnt judge_openalex)
  procs=$(tasklist //FI "IMAGENAME eq python.exe" 2>/dev/null | grep -c python.exe)
  echo "$(date +%H:%M:%S) extract=$e search=$s judge=$jd procs=$procs"
  if [ "$s" -gt "$base_s" ] && [ "$s" -ge 12 ]; then
     echo "EXTRACT_DONE search advanced $base_s->$s ; killing enrich"
     kill_enrich
     sleep 2
     echo "final extract=$(cnt extract_openalex) search=$(cnt search_openalex) judge=$(cnt judge_openalex)"
     echo "TRIGGER extract_phase_complete"
     break
  fi
  if [ "$procs" -lt 1 ]; then echo "TRIGGER all_python_gone"; break; fi
  sleep 20
done
echo "STOPWATCH_DONE"
