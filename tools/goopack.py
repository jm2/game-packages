#!/usr/bin/env python3
"""Build a GooGet package (.goo) from a staged tree and a goo.toml manifest.

    tools/goopack.py <goo.toml> <stage dir> <out dir>

A .goo is a gzip tarball holding <name>.pkgspec (JSON, googet's PkgSpec),
the payload and optional install/uninstall scripts. googet extracts it,
copies each `Files` entry (a directory in the package) to its destination,
then runs Install.Path from the extracted package. Files it copied are
removed again on uninstall; the scripts only handle what googet doesn't
track (shortcuts, firewall rules, ACLs).

goo.toml:

    name = "quake3e"
    version = "2026.10.14"       # any upstream version; see goo_version()
    release = 1                   # becomes googet's @N
    arch = "x86_64"               # noarch, x86_64, x86_32, arm, arm64
    description = "..."
    license = "GPL-2.0-or-later"
    url = "https://..."
    provides = ["quake3-engine"]
    replaces = []
    conflicts = []
    release_notes = ["..."]

    [files]                       # stage subdirectory -> install directory
    "quake3" = "<ProgramFiles>/Games/quake3"

    [deps]                        # name -> minimum version ("" = any)
    quake3-data = ""

    [[shortcut]]                  # Start Menu entries (all users)
    name = "Quake3e"
    target = "quake3/quake3e.x64.exe"   # stage-relative; resolved via [files]
    args = ""
    description = "Quake III Arena (Quake3e)"

    [[firewall]]                  # inbound allow rules, local subnet only
    name = "Quake3e"
    program = "quake3/quake3e.x64.exe"  # program rule; or protocol/ports:
    # protocol = "UDP"; ports = "27960"

    [writable]                    # let Users modify these install dirs
    dirs = ["quake3/baseq3"]      # stage-relative, under a [files] directory

    [[prereq]]                    # run once at install (redistributables)
    name = "openal"
    path = "game/redist/oalinst.exe"    # stage-relative
    args = "/s"

Installs go under Program Files, where only administrators can write (not
C:\\Games: C:\\'s ACL lets every authenticated user modify new dirs there,
and per-dir fixes after googet's copy can be raced or squatted). A
writable dir lets every user modify its files, except the executables
already there (.exe, .dll, ...), so a standard user can't swap a program
that others run; new files can still be added. Only mark the dirs a game
really writes to.

A <stage dir>/.version file (written by the stage script, e.g. a Steam
build's version) overrides `version`.
"""
import gzip, io, json, os, re, sys, tarfile, tomllib
from pathlib import Path

VALID_ARCH = {"noarch", "x86_64", "x86_32", "arm", "arm64"}
MENU = "Games (linux-packages)"
EXEC = "*.exe,*.dll,*.asi,*.sys,*.ocx,*.cpl,*.scr,*.com,*.bat,*.cmd,*.ps1,*.vbs,*.msi"


def goo_version(version: str, release: int) -> str:
    """Map an upstream version to googet's "<semver>@<release>".

    googet needs three numeric components (it pads short versions from the
    left, "1" -> "0.0.1"). Numbers are taken in order; a trailing letter run
    counts as a number (a=1 ... z=26, so 1.0o -> 1.0.15 and 1.32b -> 1.32.2);
    letters followed by digits are dropped (1.27.b16986367 -> 1.27.16986367).
    Components past the third are joined into it.
    """
    nums: list[int] = []
    for part in re.split(r"[^0-9A-Za-z]+", version):
        if not part:
            continue
        for tok in re.findall(r"\d+|[A-Za-z]+", part):
            if tok.isdigit():
                nums.append(int(tok))
            elif not re.search(r"\d", part[part.index(tok) + len(tok):]):
                # A trailing letter (1.0o, 1.32b) orders like a patch level.
                n = 0
                for ch in tok.lower():
                    n = n * 26 + (ord(ch) - 96)
                nums.append(n)
    if not nums:
        sys.exit(f"goopack: can't turn version {version!r} into numbers")
    if len(nums) > 3:
        nums = nums[:2] + [int("".join(str(n) for n in nums[2:]))]
    while len(nums) < 3:
        nums.append(0)
    return f"{nums[0]}.{nums[1]}.{nums[2]}@{release}"


def ps_quote(s: str) -> str:
    return "'" + s.replace("'", "''") + "'"


def win_dest(dest: str) -> str:
    """googet destination ("<ProgramFiles>/Games/x") as a PowerShell expression."""
    m = re.match(r"^<([^>]+)>(.*)$", dest)
    rest = (m.group(2) if m else dest).replace("/", "\\")
    return f'(Join-Path $env:{m.group(1)} {ps_quote(rest)})' if m else ps_quote(rest)


def resolve(files: dict[str, str], rel: str) -> str:
    """Stage-relative path -> PowerShell expression of its installed path."""
    top, _, rest = rel.partition("/")
    if top not in files:
        sys.exit(f"goopack: {rel} is not under a [files] directory")
    base = win_dest(files[top])
    return f"(Join-Path {base} {ps_quote(rest.replace('/', chr(92)))})" if rest else base


def scripts(m: dict) -> tuple[str, str] | None:
    files, sc, fw = m.get("files", {}), m.get("shortcut", []), m.get("firewall", [])
    wr = m.get("writable", {}).get("dirs", [])
    pre = m.get("prereq", [])
    if not (sc or fw or wr or pre):
        return None
    tag = f"linux-packages:{m['name']}"
    ins = ["$ErrorActionPreference = 'Stop'",
           f"$menu = Join-Path $env:ProgramData {ps_quote('Microsoft/Windows/Start Menu/Programs/' + MENU)}"]
    un = ["$ErrorActionPreference = 'Continue'",
          f"$menu = Join-Path $env:ProgramData {ps_quote('Microsoft/Windows/Start Menu/Programs/' + MENU)}"]
    for d in wr:
        # S-1-5-32-545 = BUILTIN\\Users, whatever the system language. Programs
        # already there stay read-only for them (inheritance cut, read+run back).
        path = resolve(files, d)
        ins += [f"$d = {path}",
                "New-Item -ItemType Directory -Force -Path $d | Out-Null",
                "icacls $d /grant '*S-1-5-32-545:(OI)(CI)M' /C /Q | Out-Null",
                f"Get-ChildItem -LiteralPath $d -Recurse -File -Include {EXEC} | ForEach-Object {{",
                "    icacls $_.FullName /inheritance:d /C /Q | Out-Null",
                "    icacls $_.FullName /remove:g '*S-1-5-32-545' /C /Q | Out-Null",
                "    icacls $_.FullName /grant '*S-1-5-32-545:RX' /C /Q | Out-Null",
                "}"]
        # Left-over user files keep the dir; take the grant back with it.
        un.append(f"if (Test-Path -LiteralPath {path}) {{ icacls {path} /remove:g '*S-1-5-32-545' /C /Q | Out-Null }}")
    for r in pre:
        # 3010: success, reboot needed; 1638: a newer version is installed.
        ins += [f"$p = Start-Process -FilePath {resolve(files, r['path'])} -ArgumentList {ps_quote(r.get('args', '') or ' ')} -Wait -PassThru",
                f"if ($p.ExitCode -notin 0, 3010, 1638) {{ Write-Warning {ps_quote(r['name'] + ' installer exited with ')}$($p.ExitCode) }}"]
    if sc:
        ins += ["New-Item -ItemType Directory -Force -Path $menu | Out-Null",
                "$sh = New-Object -ComObject WScript.Shell"]
        for s in sc:
            lnk = f"(Join-Path $menu {ps_quote(s['name'] + '.lnk')})"
            target = resolve(files, s["target"])
            ins += [f"$l = $sh.CreateShortcut({lnk})",
                    f"$l.TargetPath = {target}",
                    f"$l.WorkingDirectory = {resolve(files, s['workdir'])}" if s.get("workdir")
                    else f"$l.WorkingDirectory = Split-Path -Parent {target}",
                    f"$l.Arguments = {ps_quote(s.get('args', ''))}",
                    f"$l.Description = {ps_quote(s.get('description', s['name']))}",
                    "$l.Save()"]
            un.append(f"Remove-Item -Force -ErrorAction SilentlyContinue {lnk}")
        un.append("if ((Test-Path $menu) -and -not (Get-ChildItem $menu)) { Remove-Item $menu }")
    for f in fw:
        # LAN play only: home networks are often classed as Public, so any
        # profile, but only from the local subnet.
        common = (f"-DisplayName {ps_quote(f['name'])} -Group {ps_quote(tag)} -Direction Inbound -Action Allow"
                  " -Profile Any -RemoteAddress LocalSubnet")
        if f.get("program"):
            ins.append(f"New-NetFirewallRule {common} -Program {resolve(files, f['program'])} | Out-Null")
        else:
            ins.append(f"New-NetFirewallRule {common} -Protocol {f['protocol']} -LocalPort {f['ports']} | Out-Null")
    if fw:
        # Rules are grouped per package; drop stale ones before adding.
        ins.insert(1, f"Get-NetFirewallRule -Group {ps_quote(tag)} -ErrorAction SilentlyContinue | Remove-NetFirewallRule")
        un.append(f"Get-NetFirewallRule -Group {ps_quote(tag)} -ErrorAction SilentlyContinue | Remove-NetFirewallRule")
    return "\r\n".join(ins) + "\r\n", "\r\n".join(un) + "\r\n"


def main() -> int:
    if len(sys.argv) != 4:
        print(__doc__.strip()); return 2
    manifest, stage, out = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
    m = tomllib.loads(manifest.read_text())
    if m["arch"] not in VALID_ARCH:
        sys.exit(f"goopack: arch must be one of {sorted(VALID_ARCH)}")
    for top in m.get("files", {}):
        if not (stage / top).is_dir():
            sys.exit(f"goopack: [files] directory {top} is missing from {stage}")
    vfile = stage / ".version"
    upstream = vfile.read_text().strip() if vfile.is_file() else str(m["version"])
    version = goo_version(upstream, m.get("release", 1))
    spec = {
        "Name": m["name"], "Version": version, "Arch": m["arch"],
        "ReleaseNotes": m.get("release_notes", []),
        "Description": m.get("description", "").strip(),
        "License": m.get("license", ""), "Owners": "jm2/linux-packages",
        "Source": m.get("url", ""),
        # "" means any version to googet; crossdock wants a parseable one.
        "PkgDependencies": {k: v or "0.0.0" for k, v in m.get("deps", {}).items()},
        "Replaces": m.get("replaces", []), "Conflicts": m.get("conflicts", []),
        "Provides": m.get("provides", []),
        "Install": {}, "Uninstall": {},
        "Files": m.get("files", {}),
    }
    sc = scripts(m)
    if sc:
        spec["Install"] = {"Path": "install.ps1"}
        spec["Uninstall"] = {"Path": "uninstall.ps1"}
    spec = {k: v for k, v in spec.items() if v not in ("", [], {}) or k in ("Replaces", "Conflicts", "Provides", "Install", "Uninstall")}

    out.mkdir(parents=True, exist_ok=True)
    dest = out / f"{m['name']}.{m['arch']}.{version}.goo"
    tmp = out / f".{dest.name}.part"
    level = int(os.environ.get("GOO_GZIP_LEVEL", "6"))

    def add_bytes(tf: tarfile.TarFile, name: str, data: bytes) -> None:
        ti = tarfile.TarInfo(name)
        ti.size, ti.mode, ti.mtime = len(data), 0o644, 0
        tf.addfile(ti, io.BytesIO(data))

    def norm(ti: tarfile.TarInfo) -> tarfile.TarInfo | None:
        if ti.issym() or ti.islnk():
            sys.exit(f"goopack: {ti.name} is a link; Windows packages need real files (resolve it in staging)")
        ti.uid = ti.gid = 0
        ti.uname = ti.gname = ""
        return ti

    with open(tmp, "wb") as raw, gzip.GzipFile(fileobj=raw, mode="wb", compresslevel=level, mtime=0) as gz, \
            tarfile.open(fileobj=gz, mode="w|", format=tarfile.PAX_FORMAT) as tf:
        add_bytes(tf, f"{m['name']}.pkgspec", json.dumps(spec, indent=2).encode())
        if sc:
            add_bytes(tf, "install.ps1", sc[0].encode("utf-8-sig"))
            add_bytes(tf, "uninstall.ps1", sc[1].encode("utf-8-sig"))
        for top in sorted(m.get("files", {})):
            tf.add(stage / top, arcname=top, filter=norm)
    tmp.rename(dest)
    print(dest)
    return 0


if __name__ == "__main__":
    sys.exit(main())
