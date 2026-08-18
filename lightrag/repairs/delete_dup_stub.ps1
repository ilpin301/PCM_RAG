# Repair: delete the leftover dup-* FAILED stub from doc_status via the LightRAG API.
# Idempotent: a stub already gone is reported as "absent" and the script exits 0.
# Default is a dry run. Pass -Apply to actually delete.
param([switch]$Apply)

$ErrorActionPreference = 'Stop'
$stubs = @('dup-b85eb57c176c324b03906870300d8f34')
$key = (Get-Content F:\____IL_AI\PCM_RAG\lightrag\.env | Select-String '^LIGHTRAG_API_KEY=').Line.Split('=',2)[1].Trim()
$h = @{ 'X-API-Key' = $key; 'Content-Type' = 'application/json' }

$live = (Invoke-RestMethod http://localhost:9622/documents -Headers $h)
$present = $live.statuses.PSObject.Properties.Value | ForEach-Object { $_.id }

foreach ($s in $stubs) {
  if ($present -notcontains $s) { "absent (nothing to do): $s"; continue }
  if (-not $Apply) { "DRY RUN would DELETE doc_id=$s"; continue }
  $body = @{ doc_ids = @($s) } | ConvertTo-Json -Compress
  $r = Invoke-RestMethod http://localhost:9622/documents/delete_document -Method Delete -Headers $h -Body $body
  "DELETED $s -> $($r | ConvertTo-Json -Compress)"
}
if (-not $Apply) { "`n(dry run; re-run with -Apply to delete). Deletion is async and needs an IDLE pipeline." }
