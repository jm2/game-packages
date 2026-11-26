#!/bin/sh
# Shared install step for the PKGBUILD, the RPM spec and debian/rules.
#
#   install.sh <extracted OldUnreal patch for this arch> <package dir> <destdir> <x86_64|aarch64>
#
# <package dir> holds unreal-tournament.sh, unreal-tournament.desktop,
# unreal-tournament.png and README.md. The game data (Maps, Textures, ...)
# comes from a separate unreal-tournament-data-* package that installs into
# the same /opt/unreal-tournament tree.
set -eu
src=$1 files=$2 dest=$3 arch=$4
root=$dest/opt/unreal-tournament

# 469f's per-architecture tarballs keep the native binaries in System; 469e
# kept them in System64/SystemARM64 next to the shared .u files in System.
case $arch in
    x86_64)  sys=System64 ;;
    aarch64) sys=SystemARM64 ;;
    *) echo "install.sh: unsupported architecture $arch" >&2; exit 1 ;;
esac

install -d "$root"
for d in "$src"/*/; do
    d=${d%/}
    case ${d##*/} in System64|SystemARM64) continue ;; esac
    cp -R --no-preserve=ownership "$d" "$root/"
done
# A 469e-style tarball: merge System64/SystemARM64 into System, as
# OldUnreal's own installer does.
if [ -d "$src/$sys" ]; then
    cp -R --no-preserve=ownership "$src/$sys/." "$root/System/"
fi
[ -f "$root/System/ut-bin" ] || { echo "install.sh: System/ut-bin not found in $src (wrong patch tarball for $arch?)" >&2; exit 1; }

find "$root" -name '.git*' -prune -exec rm -rf {} +
find "$root" -type d -exec chmod 755 {} +
find "$root" -type f -exec chmod 644 {} +
find "$root/System" -type f \( -name 'ut-bin-*' -o -name 'ucc-bin-*' -o -name '*.so' -o -name '*.so.*' \) -exec chmod 755 {} +

install -Dm755 "$files/unreal-tournament.sh" "$dest/usr/bin/unreal-tournament"
install -Dm644 "$files/unreal-tournament.desktop" -t "$dest/usr/share/applications/"
install -Dm644 "$files/unreal-tournament.png" -t "$dest/usr/share/icons/hicolor/256x256/apps/"
install -Dm644 "$files/README.md" "$src/ReleaseNotes.md" -t "$dest/usr/share/doc/unreal-tournament-bin/"
