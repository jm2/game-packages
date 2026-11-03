#!/bin/sh
# Shared install step for the PKGBUILD, the RPM spec and debian/rules.
#   install.sh <built Q2RTX source tree> <extracted q2rtx release dir> <destdir> <doc dir name> <license dir, absolute inside destdir>
# The engine, game module and shaders come from the source build; the
# media archives (blue_noise.pkz, q2rtx_media.pkz) and the shareware
# pak0.pak come from the release, as they are not in the git repository.
set -eu
src=$1 rel=$2 dest=$3 doc=$4 lic=$5
here=$(cd "$(dirname "$0")" && pwd)
share=$dest/usr/share/quake2rtx

# The engine hardcodes /usr/share/quake2rtx as its base and library directory.
install -d "$share/bin" "$share/baseq2/shader_vkpt"
install -m755 "$src/q2rtx" "$src/q2rtxded" "$share/bin/"
install -m755 "$src"/baseq2/game*.so "$share/baseq2/"
install -m644 "$src"/baseq2/shader_vkpt/*.spv "$share/baseq2/shader_vkpt/"
install -m644 "$src/baseq2/q2rtx.cfg" "$src/baseq2/q2rtx.menu" "$share/baseq2/"
install -m644 "$rel/baseq2/blue_noise.pkz" "$rel/baseq2/q2rtx_media.pkz" "$rel/baseq2/pak0.pak" "$share/baseq2/"

# The release's retail pak importer (the 1.8.1 tree's copy has a broken
# XDG_DATA_HOME test); point it at the directory the launcher passes in
# DEST_DIR.
sed 's|^DEST_DIR=.*|DEST_DIR="${DEST_DIR:-${XDG_DATA_HOME:-$HOME/.local/share}/quake2rtx}"|' \
    "$rel/find-retail-paks.sh" > "$share/bin/find-retail-paks.sh"
chmod 755 "$share/bin/find-retail-paks.sh"

# Commands
install -Dm755 "$here/q2rtx.sh" "$dest/usr/bin/q2rtx"
ln -sf q2rtx "$dest/usr/bin/quake2rtx"
ln -sf /usr/share/quake2rtx/bin/q2rtxded "$dest/usr/bin/q2rtxded"
ln -sf /usr/share/quake2rtx/bin/find-retail-paks.sh "$dest/usr/bin/quake2rtx-find-retail-paks"

# Desktop entry and icon
install -Dm644 "$here/q2rtx.desktop" "$dest/usr/share/applications/q2rtx.desktop"
install -Dm644 "$src/setup/q2rtx.png" "$dest/usr/share/icons/hicolor/256x256/apps/q2rtx.png"

# Documentation and licenses
install -d "$dest/usr/share/doc/$doc" "$lic"
install -m644 "$src/readme.md" "$src/changelog.md" "$dest/usr/share/doc/$doc/"
install -m644 "$src/license.txt" "$src/notice.txt" "$lic/"
