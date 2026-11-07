#!/bin/sh
# Shared install step for PKGBUILD, RPM spec and debian/rules.
#   install.sh <extracted XLiveLessNess-*-Release dir> <destdir>
set -eu
src=$1 dest=$2
# /opt, not /usr/lib: umu/Proton's pressure-vessel container replaces /usr, so
# gamelaunch's links to these files would dangle there.
lib=$dest/opt/xlln
install -Dm644 "$src/xlive.dll" "$lib/xlive.dll"
(cd "$src" && find XLiveLessNess -type d) | while read -r d; do install -d "$lib/$d"; done
(cd "$src" && find XLiveLessNess -type f) | while read -r f; do install -m644 "$src/$f" "$lib/$f"; done
install -Dm644 "$src/README.md" "$dest/usr/share/doc/xlln/README.md"
install -Dm644 "$src/XLiveLessNess/modules/README.md" "$dest/usr/share/doc/xlln/README.modules.md"
# Compatibility links for gamelaunch < 1.1.2 (plain Wine only). One link per
# file: replacing the old /usr/lib/xlln directory with a symlink breaks upgrades.
(cd "$lib" && find . -type f) | while read -r f; do
    install -d "$dest/usr/lib/xlln/$(dirname "$f")"
    ln -s "/opt/xlln/${f#./}" "$dest/usr/lib/xlln/${f#./}"
done
