#!/bin/sh
# Shared install step for the PKGBUILD, the RPM spec and debian/rules.
#   install.sh <source dir> <cmake build dir> <destdir> <version> <doc dir name>
set -eu
src=$1 build=$2 dest=$3 ver=$4 doc=$5
here=$(cd "$(dirname "$0")" && pwd)
lib=$dest/usr/lib/bugdom

# Game binary and its data
install -Dm755 "$build/Bugdom" "$lib/Bugdom"
cp -r --no-preserve=ownership "$src/Data" "$lib/"
find "$lib/Data" -type d -exec chmod 755 {} +
find "$lib/Data" -type f -exec chmod 644 {} +

# Launcher, desktop entry and icon
install -Dm755 "$here/bugdom.sh" "$dest/usr/bin/bugdom"
install -Dm644 "$here/bugdom.desktop" "$dest/usr/share/applications/bugdom.desktop"
install -Dm644 "$src/packaging/Bugdom512.png" \
    "$dest/usr/share/icons/hicolor/512x512/apps/bugdom.png"

# Documentation
d=$dest/usr/share/doc/$doc
install -d "$d"
for f in "$src"/*.md; do
    case ${f##*/} in LICENSE.md|BUILD.md) ;; *) install -m644 "$f" "$d/" ;; esac
done
for f in docs; do
    cp -r --no-preserve=ownership "$src/$f" "$d/"
done
find "$d" -type d -exec chmod 755 {} +
find "$d" -type f -exec chmod 644 {} +
sed "s/@PROJECT_VERSION@/$ver/" "$src/packaging/ReadMe.txt.in" > "$d/README"
