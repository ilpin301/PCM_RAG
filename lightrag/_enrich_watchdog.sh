#!/bin/bash
cd /x/RAG_MAIN/PCM_RAG/lightrag
LOG=_enrich_full.log
killp(){ powershell -NoProfile -Command "Get-CimInstance Win32_Process -Filter \"Name='python.exe'\" | Where-Object {\$_.CommandLine -like '*enrich_openalex*'} | ForEach-Object { Stop-Process -Id \$_.ProcessId -Force }" 2>/dev/null; }
nproc_enrich(){ powershell -NoProfile -Command "@(Get-CimInstance Win32_Process -Filter \"Name='python.exe'\" | Where-Object {\$_.CommandLine -like '*enrich_openalex*'}).Count" 2>/dev/null; }
launch(){ killp; sleep 2; NO_PROXY='*' nohup python enrich_openalex.py >> "$LOG" 2>&1 & echo "$(date +%H:%M:%S) [watchdog] launched enrich"; }

echo "$(date +%H:%M:%S) [watchdog] start"
launch
for i in $(seq 1 160); do
  sleep 30
  if grep -q "==== SUMMARY ====" "$LOG" 2>/dev/null; then
     echo "$(date +%H:%M:%S) [watchdog] SUMMARY found -> DONE"; break
  fi
  now=$(date +%s); m=$(stat -c '%Y' "$LOG" 2>/dev/null); age=$((now-m))
  p=$(nproc_enrich)
  en=$(grep -c '\[enriched\]' "$LOG" 2>/dev/null)
  echo "$(date +%H:%M:%S) [watchdog] age=${age}s proc=$p enriched=$en"
  if [ "$p" -lt 1 ]; then
     echo "$(date +%H:%M:%S) [watchdog] proc dead, no SUMMARY -> relaunch"; launch; continue
  fi
  if [ "$age" -gt 150 ]; then
     echo "$(date +%H:%M:%S) [watchdog] STALL ${age}s -> kill+relaunch"; launch; continue
  fi
done
killp
echo "$(date +%H:%M:%S) [watchdog] EXIT. final enriched=$(grep -c '\[enriched\]' "$LOG")"
grep -A12 "==== SUMMARY ====" "$LOG" 2>/dev/null | tail -14
