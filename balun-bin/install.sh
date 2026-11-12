#!/bin/sh
# Shared install step for the PKGBUILD and debian/rules.
#   install.sh <unpacked upstream package> <destdir> <doc dir name>
# The unpacked tree is the payload of one of upstream's release packages (the
# .pkg.tar.zst, .rpm or .deb; all hold the same files under usr/).
set -eu
src=$1 dest=$2 doc=$3
id=io.github.jm2.Balun

install -Dm755 "$src/usr/bin/balun" "$dest/usr/bin/balun"
install -Dm644 "$src/usr/share/applications/$id.desktop" "$dest/usr/share/applications/$id.desktop"
install -Dm644 "$src/usr/share/metainfo/$id.metainfo.xml" "$dest/usr/share/metainfo/$id.metainfo.xml"
for size in 16 24 32 48 64 128 256 512; do
    install -Dm644 "$src/usr/share/icons/hicolor/${size}x${size}/apps/$id.png" \
        "$dest/usr/share/icons/hicolor/${size}x${size}/apps/$id.png"
done
install -Dm644 "$src/usr/share/icons/hicolor/scalable/apps/$id.svg" \
    "$dest/usr/share/icons/hicolor/scalable/apps/$id.svg"
install -Dm644 "$src/usr/share/icons/hicolor/symbolic/apps/$id-symbolic.svg" \
    "$dest/usr/share/icons/hicolor/symbolic/apps/$id-symbolic.svg"
# Upstream's usr/share/doc/balun/copyright and usr/share/licenses/balun are left
# out: each format installs the license its own way.
install -Dm644 "$(dirname "$0")/README.md" "$dest/usr/share/doc/$doc/README.md"
