[CmdletBinding(SupportsShouldProcess)]
param(
    [Parameter(Mandatory)]
    [ValidatePattern('^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$')]
    [string]$Repo
)

$ErrorActionPreference = 'Stop'
$labelSpecs = @(Get-Content -Raw -LiteralPath (Join-Path $PSScriptRoot 'labels.json') | ConvertFrom-Json)
$seen = @{}
foreach ($spec in $labelSpecs) {
    if (-not $spec.name -or $seen.ContainsKey($spec.name) -or $spec.color -notmatch '^[0-9A-Fa-f]{6}$' -or -not $spec.description) {
        throw 'Invalid or duplicate label definition.'
    }
    $seen[$spec.name] = $true
}

if (-not $WhatIfPreference) {
    Get-Command gh -ErrorAction Stop | Out-Null
    & gh repo view $Repo --json nameWithOwner --jq '.nameWithOwner'
    if ($LASTEXITCODE -ne 0) { throw "Cannot access repository $Repo." }
}

foreach ($spec in $labelSpecs) {
    if ($PSCmdlet.ShouldProcess($Repo, "Create/update label '$($spec.name)' (#$($spec.color))")) {
        & gh label create $spec.name --repo $Repo --color $spec.color --description $spec.description --force
        if ($LASTEXITCODE -ne 0) { throw "Failed to configure label '$($spec.name)'." }
    }
}

Write-Output 'Label definitions processed. This helper does not change issue labels or Project fields, and does not delete existing labels.'
