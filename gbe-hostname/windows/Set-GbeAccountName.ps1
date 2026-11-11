# Keep the Goldberg (gbe-fork) player name in step with this computer's name.
#
# Runs at each logon as the user (scheduled task \game-packages\gbe-hostname,
# registered by the gbe-hostname package). It sets account_name in
#   %APPDATA%\GSE Saves\settings\configs.user.ini
# (gbe's global user settings, read by every Goldberg game) to the host name in
# lower case. The name is only rewritten while it is unset, gbe's own default
# ("gse orca") or the name this script last wrote (kept in
# account_name.gbe-hostname next to the file), so a renamed computer shows its
# new name and a name the user set themselves is left alone.
$ErrorActionPreference = 'Stop'

# The DNS host name keeps its full length (the NetBIOS COMPUTERNAME is cut to
# 15 characters and upper case).
$name = [System.Net.Dns]::GetHostName()
if (-not $name) { $name = $env:COMPUTERNAME }
$name = ($name.Split('.')[0]).ToLowerInvariant() -replace '[^a-z0-9._-]', ''
if ($name.Length -gt 32) { $name = $name.Substring(0, 32) }
if (-not $name -or $name -like 'localhost*') { exit 0 }

$dir = Join-Path $env:APPDATA 'GSE Saves\settings'
$ini = Join-Path $dir 'configs.user.ini'
$state = Join-Path $dir 'account_name.gbe-hostname'
$utf8 = New-Object System.Text.UTF8Encoding $false   # gbe's ini parser wants no BOM

$lines = @()
if (Test-Path -LiteralPath $ini) { $lines = @([System.IO.File]::ReadAllLines($ini)) }
$last = ''
if (Test-Path -LiteralPath $state) { $last = ([System.IO.File]::ReadAllText($state)).Trim() }

# Current account_name in [user::general].
$cur = ''; $sec = $false
foreach ($l in $lines) {
    if ($l -match '^\s*\[') { $sec = $l -match '^\s*\[user::general\]\s*$'; continue }
    if ($sec -and $l -match '^\s*account_name\s*=\s*(.*?)\s*$') { $cur = $Matches[1] }
}
if ($cur -and $cur -ne 'gse orca' -and $cur -ne $last) { exit 0 }

if ($cur -ne $name) {
    $out = New-Object System.Collections.Generic.List[string]
    $sec = $false; $done = $false
    foreach ($l in $lines) {
        if ($l -match '^\s*\[') {
            if ($sec -and -not $done) { $out.Add("account_name=$name"); $done = $true }
            $sec = $l -match '^\s*\[user::general\]\s*$'
            $out.Add($l); continue
        }
        if ($sec -and $l -match '^\s*account_name\s*=') {
            if (-not $done) { $out.Add("account_name=$name"); $done = $true }
            continue
        }
        $out.Add($l)
    }
    if (-not $done) {
        if (-not $sec) { $out.Add('[user::general]') }
        $out.Add("account_name=$name")
    }
    New-Item -ItemType Directory -Force -Path $dir | Out-Null
    $tmp = "$ini.tmp"
    [System.IO.File]::WriteAllLines($tmp, $out, $utf8)
    Move-Item -Force -LiteralPath $tmp -Destination $ini
}
New-Item -ItemType Directory -Force -Path $dir | Out-Null
[System.IO.File]::WriteAllText($state, "$name`r`n", $utf8)
