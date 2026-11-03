#!/bin/sh
# Shared install step for PKGBUILD, RPM spec and debian/rules.
#   install.sh <extracted companion zip dir> <destdir>
# Installs the DLLs under stable names (no version):
#   ageServerLauncherCompanion_Age2FakeOnline_release_1.4.0.0.dll -> Age2FakeOnline.dll
set -eu
src=$1 dest=$2
lib=$dest/usr/lib/agelanserver-companion
install -d "$lib"
n=0
for f in "$src"/ageServerLauncherCompanion_*_release_*.dll; do
    b=${f##*/ageServerLauncherCompanion_}
    install -m644 "$f" "$lib/${b%%_release_*}.dll"
    n=$((n + 1))
done
for d in Age2FakeOnline Age3FakeOnline AgeFakeHostsCerts; do
    [ -f "$lib/$d.dll" ] || { echo "install.sh: $d.dll missing from the companion release" >&2; exit 1; }
done
install -Dm644 README.md "$dest/usr/share/doc/agelanserver-companion-bin/README.md"
