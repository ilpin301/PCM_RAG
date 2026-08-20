<#
Fixes: refreshes the stale Google Drive backup of rag_storage (last snapshot
2026-08-19 12:13, predates the merged Bruns re-ingest). DRY RUN IS THE
DEFAULT — pass -Apply to actually sync/tar and copy.

Usage:
  .\refresh_drive_snapshot.ps1          # dry run
  .\refresh_drive_snapshot.ps1 -Apply   # do it
#>
param(
    [switch]$Apply
)

$ErrorActionPreference = "Stop"

$LightragDir  = "F:\____IL_AI\PCM_RAG\lightrag"
$RagStorage   = Join-Path $LightragDir "data\rag_storage"
$DriveDir     = "J:\My Drive\RAG\PCM_RAG"
$SnapshotPath = Join-Path $DriveDir "rag_storage.tgz"
$PrevPath     = Join-Path $DriveDir "rag_storage.tgz.prev"
$ContainerName = "pcm_rag-lightrag-1"

function Format-MiB($bytes) {
    return [math]::Round($bytes / 1MB, 2)
}

# --- Check J: mounted ---
if (-not (Test-Path "J:\")) {
    Write-Host "ABORT: J: is not mounted."
    exit 1
}
Write-Host "J: is mounted."

# --- Existing snapshot info ---
if (Test-Path $SnapshotPath) {
    $item = Get-Item $SnapshotPath
    Write-Host ("Existing snapshot: {0}  size={1} MiB  mtime={2}" -f $SnapshotPath, (Format-MiB $item.Length), $item.LastWriteTime)
} else {
    Write-Host "No existing snapshot found at $SnapshotPath"
}

# --- Source size ---
if (-not (Test-Path $RagStorage)) {
    Write-Host "ABORT: source dir not found: $RagStorage"
    exit 1
}
$sourceBytes = (Get-ChildItem $RagStorage -Recurse -File -ErrorAction SilentlyContinue | Measure-Object -Property Length -Sum).Sum
Write-Host ("Source to snapshot: {0}  size={1} MiB" -f $RagStorage, (Format-MiB $sourceBytes))

# --- Look for an existing sync script to reuse ---
$syncScript = $null
$candidate = Join-Path $LightragDir "rag_sync.ps1"
if (Test-Path $candidate) {
    $syncScript = $candidate
} else {
    $found = Get-ChildItem "F:\____IL_AI\PCM_RAG" -Recurse -Filter "rag_sync.ps1" -ErrorAction SilentlyContinue | Select-Object -First 1
    if ($found) { $syncScript = $found.FullName }
}

# --- Guards for -Apply ---
if ($Apply) {
    $running = $null
    try {
        $running = docker ps --filter "name=$ContainerName" --format "{{.Names}}"
    } catch {
        Write-Host "WARNING: could not check docker status ($_); assuming running for safety."
        $running = $ContainerName
    }
    if ($running -and $running.Trim().Length -gt 0) {
        Write-Host "ABORT: container $ContainerName is running. Stop it before -Apply."
        exit 1
    }

    $cutoff = (Get-Date).AddMinutes(-5)
    $recentlyModified = Get-ChildItem $RagStorage -Filter "*.json" -ErrorAction SilentlyContinue |
        Where-Object { $_.LastWriteTime -gt $cutoff }
    if ($recentlyModified) {
        Write-Host "ABORT: these *.json files were modified in the last 5 minutes (mid-write?):"
        $recentlyModified | ForEach-Object { Write-Host "  $($_.FullName)  ($($_.LastWriteTime))" }
        exit 1
    }
}

# --- Do the thing (or say what would be done) ---
if ($syncScript) {
    Write-Host "Found existing sync script: $syncScript"
    if ($Apply) {
        Write-Host "Invoking: $syncScript push"
        & $syncScript push
    } else {
        Write-Host "DRY RUN — would invoke: $syncScript push"
    }
} else {
    Write-Host "No rag_sync.ps1 found anywhere under F:\____IL_AI\PCM_RAG — falling back to manual tar."
    $tempTgz = Join-Path $env:TEMP ("rag_storage_{0}.tgz" -f (Get-Date -Format "yyyyMMdd-HHmmss"))

    if ($Apply) {
        Write-Host "Creating temp archive: $tempTgz"
        tar -czf $tempTgz -C (Split-Path $RagStorage -Parent) (Split-Path $RagStorage -Leaf)
        if ($LASTEXITCODE -ne 0) {
            Write-Host "ABORT: tar failed with exit code $LASTEXITCODE"
            exit 1
        }

        if (Test-Path $SnapshotPath) {
            Write-Host "Preserving previous snapshot: $PrevPath"
            Copy-Item -LiteralPath $SnapshotPath -Destination $PrevPath -Force
        }

        Write-Host "Copying new archive to: $SnapshotPath"
        Copy-Item -LiteralPath $tempTgz -Destination $SnapshotPath -Force
        Remove-Item -LiteralPath $tempTgz -Force
        Write-Host "Done."
    } else {
        Write-Host "DRY RUN — would tar $RagStorage to a temp .tgz, keep previous snapshot as $PrevPath, and copy the new archive to $SnapshotPath"
    }
}

if (-not $Apply) {
    Write-Host ""
    Write-Host "DRY RUN complete — nothing changed. Re-run with -Apply to refresh the snapshot."
}
