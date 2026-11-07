#!/bin/sh
# Shared build/install step for the PKGBUILD and the RPM spec.
#   install.sh build   <source dir>
#   install.sh install <source dir> <destdir> <doc dir name> <license dir, absolute inside destdir>
# The game library goes next to the engine, in /usr/lib/yamagi-quake2/xatrix
# (upstream's packaging layout, also used by Debian); the game data is read
# from /usr/share/games/quake2/xatrix.
set -eu
cmd=$1 src=$2
here=$(cd "$(dirname "$0")" && pwd)
mod=xatrix
lib=/usr/lib/yamagi-quake2/$mod

case $cmd in
build)
    # CFLAGS/LDFLAGS come from the environment (the Makefile appends its own).
    make -C "$src" VERBOSE=1
    ;;
install)
    dest=$3 doc=$4 lic=$5
    install -Dm755 "$src/release/game.so" "$dest$lib/game.so"

    # Fixed entity lists for buggy maps
    install -Dm644 -t "$dest$lib/maps" "$src"/stuff/mapfixes/*.ent

    # Launcher and desktop entry
    install -Dm755 "$here/yamagi-quake2-$mod.sh" "$dest/usr/bin/yamagi-quake2-$mod"
    install -Dm644 "$here/yamagi-quake2-$mod.desktop" "$dest/usr/share/applications/yamagi-quake2-$mod.desktop"

    # Documentation and license
    install -Dm644 "$here/README.md" "$dest/usr/share/doc/$doc/README.md"
    install -m644 "$src/README.md" "$dest/usr/share/doc/$doc/README.$mod.md"
    install -m644 "$src/CHANGELOG" "$dest/usr/share/doc/$doc/"
    install -Dm644 "$src/LICENSE" "$lic/LICENSE"
    ;;
*)
    echo "usage: install.sh build|install ..." >&2
    exit 2
    ;;
esac
