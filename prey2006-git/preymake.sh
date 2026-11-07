#!/bin/sh
# Shared build/install step for the PKGBUILD, the RPM spec and debian/rules.
#   preymake.sh build   <Prey2006 source dir> <build dir>
#   preymake.sh install <Prey2006 source dir> <build dir> <destdir> <doc dir name>
# The engine's base path (normally /usr/share/games/prey06) is changed to
# /opt/prey, where prey-data-steam installs base/pak00[0-4].pk4. The game
# library (game<cpu>.so) and the port's own base/ assets go there too.
set -eu
cmd=$1 src=$2 build=$3
here=$(cd "$(dirname "$0")" && pwd)
opt=/opt/prey

case $cmd in
build)
    pat='set(datadir	"${CMAKE_INSTALL_FULL_DATADIR}/games/prey06")'
    grep -qF "$pat" "$src/neo/CMakeLists.txt"
    sed -i "s|\"\${CMAKE_INSTALL_FULL_DATADIR}/games/prey06\"|\"$opt\"|" "$src/neo/CMakeLists.txt"
    # A translated vote string used as a format string (-Werror=format-security).
    vote='sprintf(assembledVoteString, common->GetLanguageDict()->GetString(strings[0]));'
    grep -qF "$vote" "$src/neo/game/MultiplayerGame.cpp"
    sed -i 's|sprintf(assembledVoteString, common->GetLanguageDict()->GetString(strings\[0\]));|idStr::Copynz(assembledVoteString, common->GetLanguageDict()->GetString(strings[0]), sizeof(assembledVoteString));|' \
        "$src/neo/game/MultiplayerGame.cpp"
    # hhProfilerGraph is declared with an inline destructor but its virtual
    # methods are never defined; without LTO the destructor's vtable reference
    # fails to link. Nothing uses the class, so drop it.
    grep -q '^class hhProfilerGraph : public idCinematic {' "$src/neo/renderer/Cinematic.h"
    if grep -rq 'hhProfilerGraph' "$src/neo" --include='*.cpp'; then exit 1; fi
    sed -i '/^class hhProfilerGraph : public idCinematic {/,/^};/d' "$src/neo/renderer/Cinematic.h"
    # The distro flags come in through CFLAGS/CXXFLAGS/LDFLAGS.
    cmake -S "$src/neo" -B "$build" \
        -DCMAKE_BUILD_TYPE=None \
        -DCMAKE_INSTALL_PREFIX=/usr \
        -DCMAKE_SKIP_RPATH=ON \
        -DREPRODUCIBLE_BUILD=ON \
        -DSDL3=OFF \
        -DDEDICATED=ON \
        -Wno-dev
    cmake --build "$build" --verbose --parallel "$(nproc)"
    ;;
install)
    dest=$4 doc=$5
    # prey06, prey06ded, base/game<cpu>.so, desktop entry, icons, AppStream
    DESTDIR="$dest" cmake --install "$build"

    # The port's replacement assets (GUIs, materials, defs, scripts, the SDK's
    # tutorial maps); loose files override the retail .pk4s.
    install -d "$dest$opt/base"
    cp -R --no-preserve=mode,ownership "$src/base/." "$dest$opt/base/"
    find "$dest$opt/base" -type d -exec chmod 755 {} + -o -type f ! -name '*.so' -exec chmod 644 {} +

    # Documentation
    install -Dm644 "$here/README.md" "$dest/usr/share/doc/$doc/README.md"
    install -m644 "$src/.github/README.md" "$dest/usr/share/doc/$doc/README.Prey2006.md"
    install -m644 "$src/.github/Changelog.md" "$src/.github/Configuration.md" "$dest/usr/share/doc/$doc/"
    ;;
*)
    echo "usage: preymake.sh build|install ..." >&2
    exit 2
    ;;
esac
