#!/bin/sh
# Shared install step for the PKGBUILD, the RPM spec and debian/rules.
#   install.sh <source dir> <cmake build dir> <destdir> <version> <doc dir name>
set -eu
src=$1 build=$2 dest=$3 ver=$4 doc=$5
here=$(cd "$(dirname "$0")" && pwd)
lib=$dest/usr/lib/cro-mag-rally

# Game binary and its data
install -Dm755 "$build/CroMagRally" "$lib/CroMagRally"
cp -r --no-preserve=ownership "$src/Data" "$lib/"
find "$lib/Data" -type d -exec chmod 755 {} +
find "$lib/Data" -type f -exec chmod 644 {} +

# Launcher, desktop entry and icons
install -Dm755 "$here/cro-mag-rally.sh" "$dest/usr/bin/cro-mag-rally"
install -Dm644 "$here/cro-mag-rally.desktop" "$dest/usr/share/applications/cro-mag-rally.desktop"
install -Dm644 "$src/packaging/io.jor.cromagrally.png" \
    "$dest/usr/share/icons/hicolor/256x256/apps/cro-mag-rally.png"
install -Dm644 "$src/packaging/io.jor.cromagrally-alternateicon.png" \
    "$dest/usr/share/icons/hicolor/512x512/apps/cro-mag-rally.png"

# Documentation
d=$dest/usr/share/doc/$doc
install -d "$d"
for f in "$src"/*.md; do
    [ "${f##*/}" = LICENSE.md ] || install -m644 "$f" "$d/"
done
cp -r --no-preserve=ownership "$src/docs" "$d/"
sed -e "s/@GAME_FULL_NAME@/Cro-Mag Rally/" -e "s/@GAME_VERSION@/$ver/" \
    -e "s/@GAME_COPYRIGHT@/© 2000 Pangea Software, Inc., © 2025 Iliyas Jorio./" \
    -e "s/@GAME_NAME@/CroMagRally/" "$src/packaging/ReadMe.txt.in" > "$d/README"
