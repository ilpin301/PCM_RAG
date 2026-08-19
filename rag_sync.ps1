# rag_sync.ps1 - move the LightRAG DB snapshot between machines via a Google Drive folder.
# Lives in the repo root, next to the lightrag\ folder.
#   .\rag_sync.ps1 push     # this machine's DB -> Drive
#   .\rag_sync.ps1 pull     # Drive -> this machine's DB (full overwrite, not a merge)
# Drive root: -DriveDir, else $env:MECH_RAG_DRIVE, else "J:\My Drive\RAG" (the ilpin301 account).
# Snapshot lives in <root>\<project>\rag_storage.tgz - e.g. "...\RAG\MECH_RAG\rag_storage.tgz".
# The project subfolder is created by the first push.
# The LightRAG container is stopped for the duration and restarted only if it was running.
param(
    [Parameter(Mandatory, Position = 0)][ValidateSet('push', 'pull')][string]$Action,
    [string]$DriveDir = $(if ($env:MECH_RAG_DRIVE) { $env:MECH_RAG_DRIVE } else { 'J:\My Drive\RAG' }),
    [switch]$KeepRunning,
    [switch]$Force
)
$ErrorActionPreference = 'Stop'

$storage = Join-Path $PSScriptRoot 'lightrag\data\rag_storage'
$dataDir = Split-Path $storage
$project = Split-Path $PSScriptRoot -Leaf
$destDir = [System.IO.Path]::Combine($DriveDir, $project)
$archive = [System.IO.Path]::Combine($destDir, 'rag_storage.tgz')

if (-not [System.IO.Directory]::Exists($DriveDir)) {
    throw "Drive folder not found: $DriveDir`nStart Google Drive for Desktop, or pass -DriveDir '<path>'."
}

# A running server writes vdb_*.json continuously; a snapshot taken mid-write is a corrupt graph.
$container = $null
$wasRunning = $false
if (-not $KeepRunning) {
    $port = 9621
    $envFile = Join-Path $PSScriptRoot 'lightrag\.env'
    if (Test-Path $envFile) {
        $m = Select-String -Path $envFile -Pattern '^\s*PORT\s*=\s*(\d+)' | Select-Object -First 1
        if ($m) { $port = [int]$m.Matches[0].Groups[1].Value }
    }

    # Stopping the container mid-ingest kills that ingest and leaves the graph half-written.
    # An unreachable server just means nothing is running - that is fine, carry on.
    $irm = @{ Uri = "http://localhost:$port/health"; TimeoutSec = 10 }
    if ($PSVersionTable.PSVersion.Major -ge 6) { $irm.NoProxy = $true }
    $health = $null
    try { $health = Invoke-RestMethod @irm } catch { }
    if ($health -and ($health.pipeline_busy -or $health.pipeline_active -or $health.pipeline_scanning)) {
        if (-not $Force) {
            throw "LightRAG is mid-ingest (busy=$($health.pipeline_busy) active=$($health.pipeline_active) scanning=$($health.pipeline_scanning)).`nWait for it to finish, or pass -Force to stop it anyway."
        }
        "WARNING: pipeline busy, -Force given - the running ingest will be killed."
    }

    if (Get-Command docker -ErrorAction SilentlyContinue) {
        $container = @(docker ps -a --filter 'name=lightrag' --format '{{.Names}}')[0]
        if (-not $container) { $container = "$($project.ToLower())-lightrag-1" }
        $wasRunning = [bool](@(docker ps --filter "name=^$container$" --format '{{.Names}}')[0])
        if ($wasRunning) {
            "stopping $container ..."
            docker stop $container | Out-Null
            if ($LASTEXITCODE -ne 0) { throw "docker stop $container failed (exit $LASTEXITCODE)" }
        }
    }
    elseif (Get-NetTCPConnection -LocalPort $port -State Listen -ErrorAction SilentlyContinue) {
        # No docker CLI - refuse to touch the DB while anything still holds the server port.
        throw "docker CLI not found and port $port is still in use. Stop LightRAG manually, or pass -KeepRunning."
    }
}

try {
    if ($Action -eq 'push') {
        if (-not (Test-Path $storage)) { throw "No local DB at $storage" }
        [void][System.IO.Directory]::CreateDirectory($destDir)
        # Build outside the Drive folder. Renaming a temp file over the archive inside Drive
        # is a "swap", and on a streaming mount Drive refuses to commit one until it has
        # pulled the whole old version back down first (SWAPPED_ITEM_NOT_FULLY_DOWNLOADED in
        # drive_fs.txt) - a pointless download of the copy we are about to discard.
        $tmp = Join-Path ([System.IO.Path]::GetTempPath()) "rag_storage.$PID.tgz"
        try {
            tar -czf $tmp -C $dataDir 'rag_storage'
            if ($LASTEXITCODE -ne 0) { throw "tar failed (exit $LASTEXITCODE)" }
            # Overwrite in place. Copy-Item opens the destination with CREATE_ALWAYS, which
            # Drive records as a new revision. Deleting first does not work on a streaming
            # mount: the delete is only queued for the cloud and Drive immediately restores
            # the placeholder, so the follow-up move fails with "The file exists".
            Copy-Item $tmp $archive -Force
        }
        finally {
            if (Test-Path $tmp) { Remove-Item $tmp -Force }
        }
        "pushed {0:N0} MB -> {1}" -f ((Get-Item $archive).Length / 1MB), $archive
        'Wait for the Drive tray icon to finish uploading before pulling on the other machine.'
    }
    else {
        if (-not [System.IO.File]::Exists($archive)) {
            throw "No snapshot at $archive`nPush from the other machine first."
        }
        $bak = "$storage.bak"
        if (Test-Path $bak) { Remove-Item $bak -Recurse -Force }
        if (Test-Path $storage) { Move-Item $storage $bak }
        try {
            tar -xzf $archive -C $dataDir
            if ($LASTEXITCODE -ne 0) { throw "tar failed (exit $LASTEXITCODE)" }
        }
        catch {
            if (Test-Path $storage) { Remove-Item $storage -Recurse -Force }
            if (Test-Path $bak) { Move-Item $bak $storage }
            throw
        }
        "pulled {0} -> {1}" -f $archive, $storage
        "previous DB kept at $bak - delete it once the RAG answers correctly"
    }
}
finally {
    if ($wasRunning) {
        "starting $container ..."
        docker start $container | Out-Null
    }
}
