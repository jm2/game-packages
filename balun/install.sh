#!/bin/sh
# Shared install step for the PKGBUILD, the RPM spec and debian/rules.
#   install.sh <built source tree> <destdir>
set -eu
src=$1 dest=$2
id=io.github.jm2.Balun

install -Dm755 "$src/target/release/balun" "$dest/usr/bin/balun"
install -Dm644 "$src/data/$id.desktop" "$dest/usr/share/applications/$id.desktop"
install -Dm644 "$src/data/$id.metainfo.xml" "$dest/usr/share/metainfo/$id.metainfo.xml"
for size in 16 24 32 48 64 128 256 512; do
    install -Dm644 "$src/data/icons/hicolor/${size}x${size}/apps/$id.png" \
        "$dest/usr/share/icons/hicolor/${size}x${size}/apps/$id.png"
done
install -Dm644 "$src/data/icons/hicolor/scalable/apps/$id.svg" \
    "$dest/usr/share/icons/hicolor/scalable/apps/$id.svg"
install -Dm644 "$src/data/icons/hicolor/symbolic/apps/$id-symbolic.svg" \
    "$dest/usr/share/icons/hicolor/symbolic/apps/$id-symbolic.svg"
install -Dm644 "$src/README.md" "$dest/usr/share/doc/balun/README.md"
