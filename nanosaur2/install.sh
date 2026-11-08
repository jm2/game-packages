#!/bin/sh
# Shared install step for the PKGBUILD, the RPM spec and debian/rules.
#   install.sh <source dir> <cmake build dir> <destdir> <version> <doc dir name>
set -eu
src=$1 build=$2 dest=$3 ver=$4 doc=$5
here=$(cd "$(dirname "$0")" && pwd)
lib=$dest/usr/lib/nanosaur2

# Game binary and its data
install -Dm755 "$build/Nanosaur2" "$lib/Nanosaur2"
cp -r --no-preserve=ownership "$src/Data" "$lib/"
find "$lib/Data" -type d -exec chmod 755 {} +
find "$lib/Data" -type f -exec chmod 644 {} +

# Launcher, desktop entry and icon
install -Dm755 "$here/nanosaur2.sh" "$dest/usr/bin/nanosaur2"
install -Dm644 "$here/nanosaur2.desktop" "$dest/usr/share/applications/nanosaur2.desktop"
install -Dm644 "$src/packaging/nanosaur2-desktopicon.png" \
    "$dest/usr/share/icons/hicolor/256x256/apps/nanosaur2.png"

# Documentation
d=$dest/usr/share/doc/$doc
install -d "$d"
for f in "$src"/*.md; do
    case ${f##*/} in LICENSE.md|BUILD.md) ;; *) install -m644 "$f" "$d/" ;; esac
done
for f in docs screenshot.webp; do
    cp -r --no-preserve=ownership "$src/$f" "$d/"
done
find "$d" -type d -exec chmod 755 {} +
find "$d" -type f -exec chmod 644 {} +
sed "s/@PROJECT_VERSION@/$ver/" "$src/packaging/ReadMe.txt.in" > "$d/README"
