Set-Location F:\____IL_AI\PCM_RAG\lightrag
$env:Path = "F:\____IL_AI\RAG\lightrag\.venv-rag\Scripts;$env:Path"
$env:NO_PROXY='*'
$env:PYTHONIOENCODING='utf-8'
$env:PYTHONINTMAXSTRDIGITS = '0'
$env:MINERU_DEVICE_MODE='cuda'
$env:TIKTOKEN_CACHE_DIR='C:\Users\il720506\AppData\Local\Temp\data-gym-cache'
$env:ZAI_API_KEY = (Get-Content F:\____IL_AI\PCM_RAG\lightrag\.env | Select-String '^ZAI_API_KEY=').Line.Split('=',2)[1].Trim()
$pdfs = @(
  # filled in per run by the il-rag-ingest skill; must be non-empty before launching
)
if ($pdfs.Count -eq 0) { throw "ingest_resume.ps1: `$pdfs is empty - populate it before running" }
$missing = @($pdfs | Where-Object { -not (Test-Path $_) })
if ($missing) { throw "ingest_resume.ps1: missing PDF(s): $($missing -join ', ')" }
& F:\____IL_AI\RAG\lightrag\.venv-rag\Scripts\python.exe rag_ingest.py @pdfs `
  *>> F:\____IL_AI\PCM_RAG\lightrag\LOG\ingest_run.log
$ec = $LASTEXITCODE
# an ingest can exit 0 while writing NaN / all-zero vectors (corrupt embedding model);
# check_vectors.py turns that silent failure into a non-zero EXITCODE so the log is kept
# and the failure branch runs
if ($ec -eq 0) {
  & F:\____IL_AI\RAG\lightrag\.venv-rag\Scripts\python.exe F:\____IL_AI\PCM_RAG\lightrag\check_vectors.py `
    *>> F:\____IL_AI\PCM_RAG\lightrag\LOG\ingest_run.log
  if ($LASTEXITCODE -ne 0) { $ec = $LASTEXITCODE }
}
"EXITCODE=$ec" | Add-Content F:\____IL_AI\PCM_RAG\lightrag\LOG\ingest_run.log
if ($ec -eq 0) {
  Remove-Item F:\____IL_AI\PCM_RAG\lightrag\LOG\ingest_run.log -Force
  Remove-Item F:\____IL_AI\PCM_RAG\lightrag\LOG\LAST_FAILURE.txt -Force -ErrorAction SilentlyContinue
} else {
  # ingest failed: keep the log under a timestamped name and leave a marker the caller can poll
  $stamp = Get-Date -Format 'yyyyMMdd_HHmmss'
  $failLog = "F:\____IL_AI\PCM_RAG\lightrag\LOG\ingest_FAILED_$stamp.log"
  Move-Item F:\____IL_AI\PCM_RAG\lightrag\LOG\ingest_run.log $failLog -Force
  $triage = & F:\____IL_AI\RAG\lightrag\.venv-rag\Scripts\python.exe F:\____IL_AI\PCM_RAG\lightrag\ingest_triage.py $failLog $pdfs 2>&1 | Out-String
  "EXITCODE=$ec`nWHEN=$stamp`nLOG=$failLog`n$triage" |
    Set-Content F:\____IL_AI\PCM_RAG\lightrag\LOG\LAST_FAILURE.txt
  1..3 | ForEach-Object { [console]::beep(880, 300); Start-Sleep -Milliseconds 120 }
}
docker compose start
