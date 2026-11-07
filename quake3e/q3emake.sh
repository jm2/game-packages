#!/bin/sh
# Shared build/install step for the PKGBUILD, the RPM spec and debian/rules.
#   q3emake.sh build   <source dir>
#   q3emake.sh install <source dir> <destdir> <doc dir name>
# Quake3e uses the directory of its (symlink-resolved) executable as both
# fs_basepath and the place it loads its renderer libraries from, so the
# binaries go to /opt/quake3, where the quake3-data-* packages install
# baseq3/ and missionpack/. /usr/bin only has symlinks; no wrapper needed.
set -eu
cmd=$1 src=$2
here=$(cd "$(dirname "$0")" && pwd)
opt=/opt/quake3

# The distro flags go in through the environment: the Makefile appends its
# own (-O2 -fvisibility=hidden, -fPIC for the renderers) to them.
export CFLAGS="${CFLAGS:-} ${CPPFLAGS:-}"

q3emake() {
    make -C "$src" "$@" \
        BUILD_CLIENT=1 \
        BUILD_SERVER=1 \
        USE_SDL=1 \
        USE_RENDERER_DLOPEN=1 \
        USE_OPENGL=1 \
        USE_VULKAN=1 \
        USE_OPENGL2=0 \
        RENDERER_DEFAULT=opengl \
        USE_CURL=1 \
        USE_CURL_DLOPEN=0 \
        USE_SYSTEM_JPEG=1 \
        USE_OGG_VORBIS=1 \
        USE_SYSTEM_OGG=1 \
        USE_SYSTEM_VORBIS=1 \
        USE_LOCAL_HEADERS=0 \
        GENERATE_DEPENDENCIES=0 \
        V=1
}

case $cmd in
build)
    q3emake release
    ;;
install)
    dest=$3 doc=$4
    arch=$(uname -m)
    # The Makefile's suffix: .x64 on x86_64, .aarch64 on aarch64.
    case $arch in
        x86_64) ext=x64 ;;
        *)      ext=$arch ;;
    esac
    out=$src/build/release-linux-$arch
    install -d "$dest$opt" "$dest/usr/bin"
    install -m755 "$out/quake3e.$ext" "$dest$opt/quake3e"
    install -m755 "$out/quake3e.ded.$ext" "$dest$opt/quake3e.ded"
    # Renderers (cl_renderer opengl|vulkan); the engine looks for
    # quake3e_<renderer>_<arch>.so next to the executable.
    install -m755 "$out"/quake3e_opengl_*.so "$out"/quake3e_vulkan_*.so "$dest$opt/"

    # Commands: quake3e.ded is the name the AUR quake3e-git package used.
    ln -sf ../../opt/quake3/quake3e "$dest/usr/bin/quake3e"
    ln -sf ../../opt/quake3/quake3e.ded "$dest/usr/bin/quake3e-server"
    ln -sf quake3e-server "$dest/usr/bin/quake3e.ded"

    # Dedicated server unit
    install -Dm644 "$here/quake3e-server.service" \
        "$dest/usr/lib/systemd/system/quake3e-server.service"

    # Desktop entries and icons
    install -Dm644 "$here/quake3e.desktop" "$dest/usr/share/applications/quake3e.desktop"
    install -Dm644 "$here/quake3e-teamarena.desktop" "$dest/usr/share/applications/quake3e-teamarena.desktop"
    install -Dm644 "$src/code/unix/quake3.svg" "$dest/usr/share/icons/hicolor/scalable/apps/quake3e.svg"
    install -Dm644 "$src/code/unix/quake3.png" "$dest/usr/share/icons/hicolor/32x32/apps/quake3e.png"

    # Documentation
    install -Dm644 "$here/README.md" "$dest/usr/share/doc/$doc/README.md"
    install -m644 "$src/README.md" "$dest/usr/share/doc/$doc/README.quake3e.md"
    install -m644 "$src/id-readme.txt" "$src/docs/quake3e.md" "$dest/usr/share/doc/$doc/"
    # These have DOS line endings.
    for f in quake3e-changes.txt quake3e-FAQ.txt filter.txt; do
        tr -d '\r' < "$src/docs/$f" > "$dest/usr/share/doc/$doc/$f"
        chmod 644 "$dest/usr/share/doc/$doc/$f"
    done
    ;;
*)
    echo "usage: q3emake.sh build|install ..." >&2
    exit 2
    ;;
esac
