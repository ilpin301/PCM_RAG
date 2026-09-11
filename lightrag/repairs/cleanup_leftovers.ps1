<#
Fixes: deletes known-safe leftover files from prior ingest runs (stale .bak
vector dumps, orphaned mineru_output folders, already-merged Bruns slice
PDFs, and stale run logs). DRY RUN IS THE DEFAULT — pass -Apply to delete.

Usage:
  .\cleanup_leftovers.ps1                         # dry run, all sections
  .\cleanup_leftovers.ps1 -Apply                  # delete, all sections
  .\cleanup_leftovers.ps1 -BakVectors -Apply       # delete, one section only
#>
param(
    [switch]$Apply,
    [switch]$BakVectors,
    [switch]$MineruOrphans,
    [switch]$BrunsSlices,
    [switch]$Logs
)

$ErrorActionPreference = "Stop"

$LightragDir = "X:\RAG_MAIN\PCM_RAG\lightrag"
$RagStorage  = Join-Path $LightragDir "data\rag_storage"
$MineruOut   = Join-Path $LightragDir "data\mineru_output"
$ParsedDir   = Join-Path $LightragDir "data\inputs\__parsed__"
$LogDir      = Join-Path $LightragDir "LOG"
$PythonExe   = "X:\RAG_MAIN\RAG\lightrag\.venv-rag\Scripts\python.exe"
$CheckVectorsScript = Join-Path $LightragDir "check_vectors.py"

# If no section switch given, all four are in scope.
$anySection = $BakVectors -or $MineruOrphans -or $BrunsSlices -or $Logs
if (-not $anySection) {
    $BakVectors = $true
    $MineruOrphans = $true
    $BrunsSlices = $true
    $Logs = $true
}

function Get-SizeBytes($path) {
    if (Test-Path $path -PathType Leaf) {
        return (Get-Item $path).Length
    }
    if (Test-Path $path -PathType Container) {
        $items = Get-ChildItem $path -Recurse -File -ErrorAction SilentlyContinue
        if (-not $items) { return 0 }
        return ($items | Measure-Object -Property Length -Sum).Sum
    }
    return 0
}

function Format-MiB($bytes) {
    return [math]::Round($bytes / 1MB, 2)
}

$grandTotalBytes = 0
$missingCount = 0

# ---------------------------------------------------------------
# Section A: -BakVectors
# ---------------------------------------------------------------
if ($BakVectors) {
    Write-Host "=== Section A: BakVectors ==="
    $targets = @(
        (Join-Path $RagStorage "vdb_relationships.json.bak"),
        (Join-Path $RagStorage "vdb_entities.json.bak"),
        (Join-Path $RagStorage "vdb_chunks.json.bak")
    )

    $existing = @()
    foreach ($t in $targets) {
        if (Test-Path $t) { $existing += $t } else { $missingCount++ }
    }

    $sectionBytes = 0
    foreach ($t in $existing) {
        $sz = Get-SizeBytes $t
        $sectionBytes += $sz
        Write-Host ("  {0}  ({1} MiB)" -f $t, (Format-MiB $sz))
    }
    Write-Host ("  Subtotal: {0} MiB" -f (Format-MiB $sectionBytes))
    $grandTotalBytes += $sectionBytes

    if ($Apply -and $existing.Count -gt 0) {
        Write-Host "  Guard: running check_vectors.py before deleting .bak vector files..."
        $env:NO_PROXY = "*"
        & $PythonExe $CheckVectorsScript
        $exitCode = $LASTEXITCODE
        if ($exitCode -ne 0) {
            Write-Host "  ABORT Section A: check_vectors.py exited $exitCode. .bak files are the only rollback for the live vector stores; not deleting." -ForegroundColor Red
        } else {
            foreach ($t in $existing) {
                Remove-Item -LiteralPath $t -Force -Confirm:$false
                Write-Host "  Deleted: $t"
            }
        }
    }
    Write-Host ""
}

# ---------------------------------------------------------------
# Section B: -MineruOrphans
# ---------------------------------------------------------------
if ($MineruOrphans) {
    Write-Host "=== Section B: MineruOrphans ==="
    $matched = @()

    if (Test-Path $MineruOut) {
        # Exact name
        $exact = Join-Path $MineruOut "Clinoptilolite_PCM_Enthalpy-01-05_3fd1e36c"
        if (Test-Path $exact) { $matched += Get-Item $exact } else { $missingCount++ }

        # Pattern: Cooling_Techniques_for_Photovoltaic_Systems* AND 0 bytes
        $coolingCandidates = Get-ChildItem $MineruOut -Directory -Filter "Cooling_Techniques_for_Photovoltaic_Systems*" -ErrorAction SilentlyContinue
        foreach ($c in $coolingCandidates) {
            $sz = Get-SizeBytes $c.FullName
            if ($sz -eq 0) {
                $matched += $c
                Write-Host "  matched (0 bytes): $($c.Name)"
            }
        }

        # Explicit Bruns page-range folders
        $brunsRanges = @(
            "DoctorArbeit_GunnarBruns_PCMs-003-006",
            "DoctorArbeit_GunnarBruns_PCMs-013-023",
            "DoctorArbeit_GunnarBruns_PCMs-025-034",
            "DoctorArbeit_GunnarBruns_PCMs-035-051",
            "DoctorArbeit_GunnarBruns_PCMs-053-069",
            "DoctorArbeit_GunnarBruns_PCMs-071-086",
            "DoctorArbeit_GunnarBruns_PCMs-087-095"
        )
        foreach ($name in $brunsRanges) {
            # on-disk names carry an 8-hex hash suffix; "__p*" merge folders cannot match
            $hits = Get-ChildItem $MineruOut -Directory -Filter "$name*" -ErrorAction SilentlyContinue
            if ($hits) {
                foreach ($c in $hits) {
                    $matched += $c
                    Write-Host "  matched (pattern $name*): $($c.Name)"
                }
            } else { $missingCount++ }
        }

        # Pattern: DoctorArbeit_GunnarBruns_PCMs__p* (12 folders)
        $brunsP = Get-ChildItem $MineruOut -Directory -Filter "DoctorArbeit_GunnarBruns_PCMs__p*" -ErrorAction SilentlyContinue
        foreach ($c in $brunsP) {
            $matched += $c
            Write-Host "  matched (pattern DoctorArbeit_GunnarBruns_PCMs__p*): $($c.Name)"
        }

        # Pattern: Enhancement_of_the_Phase_Transition_Enth__p*
        $enhP = Get-ChildItem $MineruOut -Directory -Filter "Enhancement_of_the_Phase_Transition_Enth__p*" -ErrorAction SilentlyContinue
        foreach ($c in $enhP) {
            $matched += $c
            Write-Host "  matched (pattern Enhancement_of_the_Phase_Transition_Enth__p*): $($c.Name)"
        }
    } else {
        Write-Host "  mineru_output dir not found: $MineruOut"
    }

    $matched = $matched | Sort-Object FullName -Unique

    $sectionBytes = 0
    foreach ($m in $matched) {
        $sz = Get-SizeBytes $m.FullName
        $sectionBytes += $sz
        Write-Host ("  {0}  ({1} MiB)" -f $m.FullName, (Format-MiB $sz))
    }
    Write-Host ("  Subtotal: {0} MiB" -f (Format-MiB $sectionBytes))
    $grandTotalBytes += $sectionBytes

    if ($Apply) {
        foreach ($m in $matched) {
            Remove-Item -LiteralPath $m.FullName -Recurse -Force -Confirm:$false
            Write-Host "  Deleted: $($m.FullName)"
        }
    }
    Write-Host ""
}

# ---------------------------------------------------------------
# Section C: -BrunsSlices
# ---------------------------------------------------------------
if ($BrunsSlices) {
    Write-Host "=== Section C: BrunsSlices ==="
    $names = @(
        "DoctorArbeit_GunnarBruns_PCMs-001-002.pdf",
        "DoctorArbeit_GunnarBruns_PCMs-007-012.pdf",
        "DoctorArbeit_GunnarBruns_PCMs-087-095.pdf",
        "DoctorArbeit_GunnarBruns_PCMs-097-099.pdf",
        "DoctorArbeit_GunnarBruns_PCMs-101-113.pdf",
        "DoctorArbeit_GunnarBruns_PCMs-114-116.pdf"
    )

    $existing = @()
    foreach ($n in $names) {
        $p = Join-Path $ParsedDir $n
        if (Test-Path $p) { $existing += $p } else { $missingCount++ }
    }

    $sectionBytes = 0
    foreach ($p in $existing) {
        $sz = Get-SizeBytes $p
        $sectionBytes += $sz
        Write-Host ("  {0}  ({1} MiB)" -f $p, (Format-MiB $sz))
    }
    Write-Host ("  Subtotal: {0} MiB" -f (Format-MiB $sectionBytes))
    $grandTotalBytes += $sectionBytes

    if ($Apply) {
        foreach ($p in $existing) {
            Remove-Item -LiteralPath $p -Force -Confirm:$false
            Write-Host "  Deleted: $p"
        }
    }
    Write-Host ""
}

# ---------------------------------------------------------------
# Section D: -Logs
# ---------------------------------------------------------------
if ($Logs) {
    Write-Host "=== Section D: Logs ==="
    $names = @(
        "LAST_FAILURE.txt",
        "ingest_FAILED_20260819_181127.log",
        "ingest_CRASHED_20260818_173708.log",
        "bruns_insert.log",
        "bruns_parse.log",
        "bruns_insert.prepatch.log",
        "bruns_insert.netdrop.log",
        "bruns_insert.dead.log",
        "merged_insert.log",
        "merged_insert.err",
        "merged_parse.log",
        "merged_parse.err",
        "keepawake.pid"
    )
    # explicitly never touch enrich_pubchem.log

    $existing = @()
    foreach ($n in $names) {
        $p = Join-Path $LogDir $n
        if (Test-Path $p) { $existing += $p } else { $missingCount++ }
    }

    $sectionBytes = 0
    foreach ($p in $existing) {
        $sz = Get-SizeBytes $p
        $sectionBytes += $sz
        Write-Host ("  {0}  ({1} MiB)" -f $p, (Format-MiB $sz))
    }
    Write-Host ("  Subtotal: {0} MiB" -f (Format-MiB $sectionBytes))
    $grandTotalBytes += $sectionBytes

    if ($Apply) {
        foreach ($p in $existing) {
            Remove-Item -LiteralPath $p -Force -Confirm:$false
            Write-Host "  Deleted: $p"
        }
    }
    Write-Host ""
}

Write-Host "=== Summary ==="
Write-Host ("Grand total: {0} MiB  (skipped {1} missing path(s))" -f (Format-MiB $grandTotalBytes), $missingCount)
if (-not $Apply) {
    Write-Host "DRY RUN — nothing deleted. Re-run with -Apply to delete."
} elseif ($grandTotalBytes -eq 0) {
    Write-Host "Nothing found to delete."
}
