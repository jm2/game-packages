#!/bin/sh
# Shared build/install step for the PKGBUILD and the RPM spec.
#   d3make.sh build   <dhewm3 source dir> <build dir> [libdir name, default lib]
#   d3make.sh install <dhewm3 source dir> <build dir> <destdir> <doc dir name>
# The engine's base path (normally <datadir>/dhewm3) is changed to /opt/doom3,
# where doom3-data-* and doom3xp-data-steam install base/ and d3xp/. The base
# and d3xp game libraries go to /usr/<libdir>/dhewm3.
set -eu
cmd=$1 src=$2 build=$3
here=$(cd "$(dirname "$0")" && pwd)
opt=/opt/doom3

case $cmd in
build)
    libdir=${4:-lib}
    grep -q '^#define BUILD_DATADIR[[:space:]]*"@datadir@"' "$src/neo/config.h.in"
    sed -i "s|^#define BUILD_DATADIR[[:space:]]*\"@datadir@\"|#define BUILD_DATADIR \"$opt\"|" "$src/neo/config.h.in"
    # The distro flags come in through CFLAGS/CXXFLAGS/LDFLAGS.
    cmake -S "$src/neo" -B "$build" \
        -DCMAKE_BUILD_TYPE=None \
        -DCMAKE_INSTALL_PREFIX=/usr \
        -DCMAKE_INSTALL_LIBDIR="$libdir" \
        -DCMAKE_SKIP_RPATH=ON \
        -DREPRODUCIBLE_BUILD=ON \
        -DSDL2=OFF -DSDL3=ON \
        -DBASE=ON -DD3XP=ON \
        -DDEDICATED=ON \
        -Wno-dev
    cmake --build "$build" --verbose --parallel "$(nproc)"
    ;;
install)
    dest=$4 doc=$5
    DESTDIR="$dest" cmake --install "$build"

    # Gamepad bindings that the engine execs from the game directories; the
    # retail .pk4 files come from the data packages.
    install -Dm644 "$src/base/gamepad.cfg" -t "$dest$opt/base/"
    install -Dm644 "$src/base/gamepad-d3xp.cfg" -t "$dest$opt/d3xp/"

    # Desktop entries (Doom 3 and Resurrection of Evil), icons, AppStream
    install -Dm644 "$here/org.dhewm3.Dhewm3.desktop" "$here/org.dhewm3.Dhewm3.d3xp.desktop" \
        -t "$dest/usr/share/applications/"
    share=$src/dist/linux/share
    for s in 128x128 256x256; do
        install -Dm644 "$share/icons/hicolor/$s/apps/org.dhewm3.Dhewm3.png" \
            -t "$dest/usr/share/icons/hicolor/$s/apps/"
    done
    install -Dm644 "$share/icons/hicolor/scalable/apps/org.dhewm3.Dhewm3.svg" \
        -t "$dest/usr/share/icons/hicolor/scalable/apps/"
    install -Dm644 "$share/metainfo/org.dhewm3.Dhewm3.metainfo.xml" -t "$dest/usr/share/metainfo/"

    # Documentation
    install -Dm644 "$here/README.md" "$dest/usr/share/doc/$doc/README.md"
    install -m644 "$src/README.md" "$dest/usr/share/doc/$doc/README.dhewm3.md"
    install -m644 "$src/Changelog.md" "$src/Configuration.md" "$dest/usr/share/doc/$doc/"
    ;;
*)
    echo "usage: d3make.sh build|install ..." >&2
    exit 2
    ;;
esac
