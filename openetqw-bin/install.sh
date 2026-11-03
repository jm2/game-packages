#!/bin/sh
# Shared install step for the PKGBUILD, the RPM spec and debian/rules.
#   install.sh <extracted openetqw-<ver>-linux-<arch> dir> <extracted ET:QW 1.5 patch data/ dir>
#              <destdir> <arch tag: x64|arm64> <doc dir name> <license dir, absolute inside destdir>
set -eu
src=$1 patch=$2 dest=$3 arch=$4 doc=$5 lic=$6
here=$(cd "$(dirname "$0")" && pwd)
opt=$dest/opt/openetqw

# Engine, dedicated server, game module, shader compiler and bundled SDL3
# (found through RUNPATH $ORIGIN), plus the engine's own loose content.
install -d "$opt"
install -m755 "$src/openETQW-client_$arch" "$src/openETQW-ded_$arch" "$src/game_$arch.so" \
    "$src/glslangValidator" "$src/libSDL3.so.0" "$opt/"
# The 0.1.0 client's RUNPATH also names the CI runner's SDL3 build directory
# (/home/runner/work/_temp/sdl3/lib); keep only $ORIGIN.
patchelf --set-rpath '$ORIGIN' "$opt/openETQW-client_$arch"
for d in base assets; do
    (cd "$src" && find "$d" -type d) | while read -r dir; do install -d "$opt/$dir"; done
    (cd "$src" && find "$d" -type f) | while read -r f; do install -m644 "$src/$f" "$opt/$f"; done
done

# ET:QW 1.5 patch paks from id's Linux client patch; openETQW requires
# pak005-pak008, the English zpaks are optional.
install -m644 "$patch"/base/pak00[5-8].pk4 "$patch"/base/zpak_english00[1-3].pk4 "$opt/base/"

# Launcher, with the dedicated server symlinked to it
install -d "$dest/usr/bin"
sed "s/@ARCH@/$arch/g" "$here/openetqw.sh" > "$dest/usr/bin/openetqw"
chmod 755 "$dest/usr/bin/openetqw"
ln -sf openetqw "$dest/usr/bin/openetqw-dedicated"

# Desktop entry and icon (upstream's tools/build/linux/openetqw.desktop and
# assets/icons/etqw_icon.png, the retail ET:QW icon)
install -Dm644 "$here/openetqw.desktop" "$dest/usr/share/applications/openetqw.desktop"
install -Dm644 "$here/etqw_icon.png" "$dest/usr/share/icons/hicolor/256x256/apps/openetqw.png"

# Documentation and licences (engine GPL, ET:QW SDK EULA, third parties,
# id's EULA for the patch paks)
install -Dm644 "$here/README.md" "$dest/usr/share/doc/$doc/README.md"
install -m644 "$src/README.txt" "$dest/usr/share/doc/$doc/"
install -d "$lic"
cp -r --no-preserve=ownership,mode "$src/licenses/." "$lic/"
find "$lic" -type d -exec chmod 755 {} +
find "$lic" -type f -exec chmod 644 {} +
install -m644 "$patch/EULA.txt" "$lic/ETQW-EULA.txt"
