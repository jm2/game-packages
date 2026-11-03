#!/bin/sh
# Shared install step for PKGBUILD, RPM spec and debian/rules.
#   install.sh <extracted XLiveLessNess-*-Release dir> <destdir>
set -eu
src=$1 dest=$2
lib=$dest/usr/lib/xlln
install -Dm644 "$src/xlive.dll" "$lib/xlive.dll"
(cd "$src" && find XLiveLessNess -type d) | while read -r d; do install -d "$lib/$d"; done
(cd "$src" && find XLiveLessNess -type f) | while read -r f; do install -m644 "$src/$f" "$lib/$f"; done
install -Dm644 "$src/README.md" "$dest/usr/share/doc/xlln/README.md"
install -Dm644 "$src/XLiveLessNess/modules/README.md" "$dest/usr/share/doc/xlln/README.modules.md"
