#!/bin/sh
# Shared install step for the PKGBUILD, the RPM spec and debian/rules.
#   install.sh <built source tree> <cmake build dir> <destdir> <doc dir name> <license dir, absolute inside destdir> <icon>
# The engine finds the retail BFG data (doom3bfg-data) in
# /usr/share/games/doom3bfg/base. Its own files go into the same base
# directory, as in upstream's release archive: the SPIR-V shaders compiled
# by the build (base/renderprogs2/spirv, which the renderer can't run
# without), the configs, entity definitions and extra map entities that
# upstream packs into _rbdoom_core.pk4, and the materials and textures the
# release ships loose. None of these names exist in the retail data.
set -eu
src=$1 build=$2 dest=$3 doc=$4 lic=$5 icon=$6
here=$(cd "$(dirname "$0")" && pwd)
lib=$dest/usr/lib/rbdoom-3-bfg
base=$dest/usr/share/games/doom3bfg/base

install -Dm755 "$build/RBDoom3BFG" -t "$lib/"
install -Dm755 "$build/tools/compilers/rbdmap" -t "$lib/"

spv=$(find "$src/base/renderprogs2/spirv" -name '*.bin' | wc -l)
[ "$spv" -gt 100 ] || { echo "install.sh: only $spv compiled shaders in $src/base/renderprogs2/spirv" >&2; exit 1; }
install -d "$base"
(cd "$src/base" && find renderprogs2/spirv -name '*.bin' -exec install -Dm644 {} "$base/{}" \;)
install -m644 "$src"/base/*.cfg "$base/"
install -Dm644 "$src"/base/def/_rbdoom_*.def "$src"/base/def/_tb_*.def "$src/base/def/misc.def" -t "$base/def/"
install -Dm644 "$src"/base/maps/game/*_extra_ents.map -t "$base/maps/game/"
install -Dm644 "$src"/base/materials/*.mtr -t "$base/materials/"
install -Dm644 "$src"/base/textures/common/* -t "$base/textures/common/"
install -Dm644 "$src"/base/textures/editor/* -t "$base/textures/editor/"
install -Dm644 "$src/base/guis/assets/loadscreens/default.jpg" -t "$base/guis/assets/loadscreens/"
install -Dm644 "$src"/base/_tb/fgd/*.fgd -t "$base/_tb/fgd/"

# Commands: the launcher pins the base path; RBDoom3BFG is the AUR name.
install -Dm755 "$here/rbdoom-3-bfg.sh" "$dest/usr/bin/rbdoom-3-bfg"
ln -sf rbdoom-3-bfg "$dest/usr/bin/RBDoom3BFG"
ln -sf /usr/lib/rbdoom-3-bfg/rbdmap "$dest/usr/bin/rbdmap"

# Desktop entry and icon
install -Dm644 "$here/rbdoom-3-bfg.desktop" -t "$dest/usr/share/applications/"
install -Dm644 "$icon" "$dest/usr/share/icons/hicolor/256x256/apps/rbdoom-3-bfg.png"

# Documentation and licenses
install -Dm644 "$here/README.md" "$dest/usr/share/doc/$doc/README.md"
install -Dm644 "$src/README.md" "$dest/usr/share/doc/$doc/README.upstream.md"
install -Dm644 "$src/RELEASE-NOTES.md" -t "$dest/usr/share/doc/$doc/"
install -d "$lic"
install -m644 "$src/LICENSE.md" "$src/LICENSE_EXCEPTIONS.md" "$lic/"
install -m644 "$src/neo/extern/nvrhi/LICENSE.txt" "$lic/LICENSE.nvrhi.txt"
install -m644 "$src/neo/extern/ShaderMake/LICENSE.txt" "$lic/LICENSE.ShaderMake.txt"
