#!/bin/sh
# Shared build/install step for the PKGBUILD and the RPM spec.
#   install.sh build   <source dir>
#   install.sh install <source dir> <destdir> <doc dir name> <license dir, absolute inside destdir>
# The engine is built with SYSTEMWIDE, so it reads the game data from
# /usr/share/games/quake2 (quake2-data-gog and quake2-data-steam install it
# there). Following upstream's packaging guide (doc/070_packaging.md), the
# executables, renderers and game libraries live together in
# /usr/lib/yamagi-quake2, which is also the layout Debian uses: the mission
# pack packages add <mod>/game.so there.
set -eu
cmd=$1 src=$2
here=$(cd "$(dirname "$0")" && pwd)
lib=/usr/lib/yamagi-quake2

case $cmd in
build)
    # CFLAGS/LDFLAGS come from the environment (the Makefile appends its
    # own); the default SYSTEMDIR is /usr/share/games/quake2.
    make -C "$src" VERBOSE=1 WITH_RPATH=no WITH_SYSTEMWIDE=yes
    ;;
install)
    dest=$3 doc=$4 lic=$5
    r=$src/release

    # Engine, dedicated server, renderers (GL1, GL3, GLES3, software) and
    # the baseq2 game library
    install -d "$dest$lib/baseq2/maps"
    install -m755 "$r/quake2" "$r/q2ded" "$r"/ref_*.so "$dest$lib/"
    install -m755 "$r/baseq2/game.so" "$dest$lib/baseq2/"

    # Upstream's saner defaults (executed after default.cfg), the 3D
    # crosshair model and the fixed entity lists for buggy maps
    install -m644 "$src/stuff/yq2.cfg" "$dest$lib/baseq2/"
    install -Dm644 -t "$dest$lib/baseq2/models/crosshair" "$src"/stuff/models/crosshair/*
    install -m644 "$src"/stuff/mapfixes/baseq2/*.ent "$dest$lib/baseq2/maps/"

    # Commands: upstream says symlinking the executables is enough
    install -d "$dest/usr/bin"
    ln -sf ../lib/yamagi-quake2/quake2 "$dest/usr/bin/yamagi-quake2"
    ln -sf ../lib/yamagi-quake2/q2ded "$dest/usr/bin/yamagi-q2ded"

    # Dedicated server unit
    install -Dm644 "$here/yamagi-q2ded.service" "$dest/usr/lib/systemd/system/yamagi-q2ded.service"

    # Desktop entry and icons
    install -Dm644 "$here/yamagi-quake2.desktop" "$dest/usr/share/applications/yamagi-quake2.desktop"
    install -Dm644 "$src/stuff/icon/Quake2.png" "$dest/usr/share/icons/hicolor/512x512/apps/yamagi-quake2.png"
    install -Dm644 "$src/stuff/icon/Quake2.svg" "$dest/usr/share/icons/hicolor/scalable/apps/yamagi-quake2.svg"

    # Documentation and license
    install -Dm644 "$here/README.md" "$dest/usr/share/doc/$doc/README.md"
    install -m644 "$src/README.md" "$dest/usr/share/doc/$doc/README.yquake2.md"
    install -m644 "$src/CHANGELOG" "$src"/doc/*.md "$dest/usr/share/doc/$doc/"
    install -Dm644 "$src/LICENSE" "$lic/LICENSE"
    ;;
*)
    echo "usage: install.sh build|install ..." >&2
    exit 2
    ;;
esac
