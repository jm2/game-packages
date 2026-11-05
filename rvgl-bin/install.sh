#!/bin/sh
# Shared install step for the PKGBUILD, the RPM spec and debian/rules.
#
#   install.sh <extracted rvgl_<ver>_linux.7z> <package dir> <destdir> <x86_64|aarch64>
#
# <package dir> holds rvgl.sh, rvgl.desktop, rvgl.xml and README.md.
#
# Layout (the one RVGL Launcher uses, with one folder per content pack):
#   /opt/rvgl/rvgl                    the engine binary for this architecture
#   /opt/rvgl/lib/libunistring.so.2   upstream's bundled copy (no distro ships .so.2)
#   /opt/rvgl/packs/rvgl_assets/      RVGL's own data (shaders, strings, fixed tracks)
# The game data packages add packs/game_files, packs/rvgl_dcpack and
# packs/soundtrack; /usr/bin/rvgl merges them through a packlist.
set -eu
src=$1 files=$2 dest=$3 arch=$4
root=$dest/opt/rvgl
pack=$root/packs/rvgl_assets
doc=$dest/usr/share/doc/rvgl-bin
lic=$dest/usr/share/licenses/rvgl-bin

case $arch in
    x86_64)  bin=rvgl.64    lib=lib64 ;;
    aarch64) bin=rvgl.arm64 lib=libarm64 ;;
    *) echo "install.sh: unsupported architecture $arch" >&2; exit 1 ;;
esac

install -Dm755 "$src/$bin" "$root/rvgl"
# SDL2, SDL2_image, OpenAL and ENet come from the distribution; libunistring.so.2
# is kept from the bundle, as upstream's own launch script does when the
# system has no libunistring.so.2.
install -d "$root/lib"
install -m755 "$src/lib/$lib/libunistring.so.2.1.0" "$root/lib/"
ln -s libunistring.so.2.1.0 "$root/lib/libunistring.so.2"

# Everything else in the archive is RVGL's asset pack, except the launch and
# setup scripts, the bundled libraries, the per-user folders (they live in
# ~/.local/share/RVGL), the icons and the license texts.
install -d "$pack"
for f in "$src"/* "$src"/.[!.]*; do
    [ -e "$f" ] || continue
    case ${f##*/} in
        rvgl|rvgl.32|rvgl.64|rvgl.arm64|rvgl.armhf|setup|fix_cases|alsoft_log) ;;
        lib|icons|licenses|cache|profiles|replays|times) ;;
        *) cp -R --no-preserve=ownership "$f" "$pack/" ;;
    esac
done
find "$pack" -type d -exec chmod 755 {} +
find "$pack" -type f -exec chmod 644 {} +

for s in 16 24 32 48 256; do
    install -Dm644 "$src/icons/${s}x${s}/apps/rvgl.png" \
        "$dest/usr/share/icons/hicolor/${s}x${s}/apps/rvgl.png"
done
install -Dm644 "$src"/licenses/*.txt -t "$lic/"

install -Dm755 "$files/rvgl.sh" "$dest/usr/bin/rvgl"
install -Dm644 "$files/rvgl.desktop" -t "$dest/usr/share/applications/"
install -Dm644 "$files/rvgl.xml" -t "$dest/usr/lib/firewalld/services/"
install -Dm644 "$files/README.md" -t "$doc/"
# Upstream writes the changelog with DOS line ends.
sed 's/\r$//' "$src/rvgl_changelog.txt" > "$doc/changelog.txt"
chmod 644 "$doc/changelog.txt"
