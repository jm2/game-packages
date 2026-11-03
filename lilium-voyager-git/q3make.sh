#!/bin/sh
# Shared build/install step for the PKGBUILD, the RPM spec and debian/rules.
#   q3make.sh build   <source dir>
#   q3make.sh install <source dir> <destdir> <doc dir name>
# The engine is built with DEFAULT_BASEDIR=/opt/lilium-voyager: that is where
# eliteforce-data-gog installs baseEF/, and where the binaries live.
set -eu
cmd=$1 src=$2
here=$(cd "$(dirname "$0")" && pwd)
opt=/opt/lilium-voyager

# The distro flags go in through the environment: on the command line they
# would replace the Makefile's own CFLAGS additions (-DELITEFORCE, ...).
export CFLAGS="${CFLAGS:-} ${CPPFLAGS:-}"

q3make() {
    make -C "$src" "$@" \
        BUILD_CLIENT=1 \
        BUILD_SERVER=1 \
        BUILD_BASEGAME=0 \
        BUILD_MISSIONPACK=0 \
        BUILD_GAME_SO=0 \
        BUILD_GAME_QVM=0 \
        BUILD_RENDERER_OPENGL2=1 \
        DEFAULT_BASEDIR="$opt" \
        FULLBINEXT='' \
        GENERATE_DEPENDENCIES=0 \
        OPTIMIZE='' \
        USE_OPENAL=1 \
        USE_OPENAL_DLOPEN=0 \
        USE_CURL=1 \
        USE_CURL_DLOPEN=0 \
        USE_CODEC_MP3=1 \
        USE_CODEC_VORBIS=1 \
        USE_CODEC_OPUS=1 \
        USE_FREETYPE=1 \
        USE_MUMBLE=1 \
        USE_VOIP=1 \
        USE_INTERNAL_LIBS=0 \
        STRIP_FLAG=
}

case $cmd in
build)
    q3make release
    ;;
install)
    dest=$3 doc=$4
    install -d "$dest$opt/baseEF" "$dest/usr/bin"
    q3make release copyfiles COPYDIR="$dest$opt"

    # Commands, plus the names older packages used
    for b in lilium-voyager lilium-voyager-server; do
        ln -sf "../../opt/lilium-voyager/$b" "$dest/usr/bin/$b"
    done
    ln -sf lilium-voyager "$dest/usr/bin/liliumvoyhm"
    ln -sf lilium-voyager-server "$dest/usr/bin/liliumvoyded"

    # Dedicated server unit
    install -Dm644 "$here/lilium-voyager-server.service" \
        "$dest/usr/lib/systemd/system/lilium-voyager-server.service"

    # Desktop entry and icons
    install -Dm644 "$here/lilium-voyager.desktop" "$dest/usr/share/applications/lilium-voyager.desktop"
    install -Dm644 "$src/misc/lilium.png" "$dest/usr/share/icons/hicolor/256x256/apps/lilium-voyager.png"
    install -Dm644 "$src/misc/lilium.svg" "$dest/usr/share/icons/hicolor/scalable/apps/lilium-voyager.svg"

    # Documentation
    install -Dm644 "$here/README.md" "$dest/usr/share/doc/$doc/README.md"
    install -m644 "$src/README.md" "$dest/usr/share/doc/$doc/README.lilium-voyager.md"
    install -m644 "$src/README-ioq3.md" "$src/ChangeLog" "$src/id-readme.txt" "$dest/usr/share/doc/$doc/"
    ;;
*)
    echo "usage: q3make.sh build|install ..." >&2
    exit 2
    ;;
esac
