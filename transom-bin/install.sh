#!/bin/sh
# Install step for the PKGBUILD.
#   install.sh <unpacked upstream package> <destdir> <doc dir name>
# The unpacked tree is the payload of upstream's release .pkg.tar.zst (files
# under usr/).
set -eu
src=$1 dest=$2 doc=$3
id=io.github.jm2.Transom

install -Dm755 "$src/usr/bin/transom" "$dest/usr/bin/transom"
install -Dm644 "$src/usr/share/applications/$id.desktop" "$dest/usr/share/applications/$id.desktop"
install -Dm644 "$src/usr/share/metainfo/$id.metainfo.xml" "$dest/usr/share/metainfo/$id.metainfo.xml"
install -Dm644 "$src/usr/share/mime/packages/$id.xml" "$dest/usr/share/mime/packages/$id.xml"
for size in 16 24 32 48 64 128 256 512; do
    install -Dm644 "$src/usr/share/icons/hicolor/${size}x${size}/apps/$id.png" \
        "$dest/usr/share/icons/hicolor/${size}x${size}/apps/$id.png"
done
install -Dm644 "$src/usr/share/icons/hicolor/scalable/apps/$id.svg" \
    "$dest/usr/share/icons/hicolor/scalable/apps/$id.svg"
# Upstream's licenses: the GPL, the Apache license of the transom-view widget
# and the licenses of the bundled Rust crates.
for f in COPYING LICENSE-APACHE RUST-CRATE-LICENSES.txt; do
    install -Dm644 "$src/usr/share/licenses/transom/$f" "$dest/usr/share/licenses/$doc/$f"
done
install -Dm644 "$(dirname "$0")/README.md" "$dest/usr/share/doc/$doc/README.md"
