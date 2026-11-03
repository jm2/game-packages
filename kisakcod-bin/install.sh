#!/bin/sh
# Shared install step for the PKGBUILD, the RPM spec and debian/rules.
#   install.sh <extracted kisakcod-<ver>-linux-<arch> directory> <destdir> <docdir name>
set -eu
src=$1 dest=$2 doc=$3
here=$(cd "$(dirname "$0")" && pwd)
opt=$dest/opt/kisakcod

# Client, dedicated server and the bundled runtime (SDL3, OpenAL Soft,
# Bink-only FFmpeg, dxvk-native), found through RUNPATH $ORIGIN/lib.
install -d "$opt/lib"
install -m755 "$src/KisakCOD-mp" "$src/KisakCOD-dedi" "$opt/"
for so in "$src"/lib/*.so.*; do
    if [ -L "$so" ]; then
        cp -P "$so" "$opt/lib/"
    else
        install -m755 "$so" "$opt/lib/"
    fi
done

# Launcher, with the dedicated server symlinked to it
install -Dm755 "$here/kisakcod.sh" "$dest/usr/bin/kisakcod"
ln -sf kisakcod "$dest/usr/bin/kisakcod-dedi"

# Desktop entry and icon
install -Dm644 "$here/kisakcod.desktop" "$dest/usr/share/applications/kisakcod.desktop"
install -Dm644 "$src/kisakcod.svg" "$dest/usr/share/icons/hicolor/scalable/apps/kisakcod.svg"

# Documentation
install -Dm644 "$here/README.md" "$dest/usr/share/doc/$doc/README.md"
install -m644 "$src/README.txt" "$src/THIRD-PARTY-NOTICES" "$dest/usr/share/doc/$doc/"
