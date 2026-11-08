#!/bin/sh
# Shared install step for the PKGBUILD, the RPM spec and debian/rules.
#   install.sh <source dir> <cmake build dir> <destdir> <version> <doc dir name>
set -eu
src=$1 build=$2 dest=$3 ver=$4 doc=$5
here=$(cd "$(dirname "$0")" && pwd)
lib=$dest/usr/lib/mightymike

# Game binary and its data
install -Dm755 "$build/MightyMike" "$lib/MightyMike"
cp -r --no-preserve=ownership "$src/Data" "$lib/"
find "$lib/Data" -type d -exec chmod 755 {} +
find "$lib/Data" -type f -exec chmod 644 {} +

# Launcher, desktop entry and icon
install -Dm755 "$here/mightymike.sh" "$dest/usr/bin/mightymike"
install -Dm644 "$here/mightymike.desktop" "$dest/usr/share/applications/mightymike.desktop"
install -Dm644 "$src/packaging/MightyMike512.png" \
    "$dest/usr/share/icons/hicolor/512x512/apps/mightymike.png"

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
