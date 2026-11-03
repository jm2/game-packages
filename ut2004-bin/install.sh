#!/bin/sh
# Shared install step for the PKGBUILD, the RPM spec and debian/rules.
#
#   install.sh <extracted OldUnreal patch> <package dir> <destdir> <x86_64|aarch64>
#
# <package dir> holds ut2004.sh, ut2004.desktop, ut2004.png and README.md.
# The game data (Maps, Textures, ...) comes from a separate ut2004-data-*
# package that installs into the same /opt/ut2004 tree.
set -eu
src=$1 files=$2 dest=$3 arch=$4
root=$dest/opt/ut2004

install -d "$root"
# Everything but the per-architecture System folders: Help, Sounds,
# SystemLocalized, Textures, Web.
for d in "$src"/*/; do
    d=${d%/}
    case ${d##*/} in System|SystemARM64|SystemPPC64LE) continue ;; esac
    cp -R --no-preserve=ownership "$d" "$root/"
done

# System holds the x86_64 binaries and the shared .u/.ini files; SystemARM64
# holds only the aarch64 binaries, so lay it over System.
cp -R --no-preserve=ownership "$src/System" "$root/"
case $arch in
    x86_64) ;;
    aarch64)
        cp -R --no-preserve=ownership --remove-destination "$src/SystemARM64/." "$root/System/"
        rm -f "$root"/System/*-amd64 ;;
    *) echo "install.sh: unsupported architecture $arch" >&2; exit 1 ;;
esac

# SDL3 and OpenAL come from the distribution (the binaries use RUNPATH=$ORIGIN,
# so a bundled copy would win). libomp.so.5 stays: Arch and Fedora ship only an
# unversioned libomp.so, and GCC's libgomp is not ABI compatible.
rm -f "$root"/System/libSDL3.so* "$root"/System/libopenal.so*

find "$root" -name '.git*' -prune -exec rm -rf {} +
find "$root" -type d -exec chmod 755 {} +
find "$root" -type f -exec chmod 644 {} +
find "$root/System" -type f \( -name UT2004 -o -name UCC -o -name '*.so' -o -name '*.so.*' \) -exec chmod 755 {} +

install -Dm755 "$files/ut2004.sh" "$dest/usr/bin/ut2004"
install -Dm644 "$files/ut2004.desktop" -t "$dest/usr/share/applications/"
install -Dm644 "$files/ut2004.png" -t "$dest/usr/share/icons/hicolor/256x256/apps/"
install -Dm644 "$files/README.md" -t "$dest/usr/share/doc/ut2004-bin/"
