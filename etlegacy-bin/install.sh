#!/bin/sh
# Shared install step for the PKGBUILD, the RPM spec and debian/rules.
#
#   install.sh <extracted etlegacy-v<ver>-<arch> dir> <destdir> <x86_64|aarch64> <package name>
#              [<licence dir, absolute inside destdir>]
#
# The launcher, desktop entry, systemd unit, firewalld service and README
# are next to this script.
set -eu
src=$1 dest=$2 arch=$3 pkg=$4 lic=${5:-}
here=$(cd "$(dirname "$0")" && pwd)

case $arch in
    x86_64|aarch64) ;;
    *) echo "install.sh: unsupported architecture $arch" >&2; exit 1 ;;
esac
opt=$dest/opt/etlegacy
data=/usr/share/enemy-territory/etmain

# Engine, dedicated server and renderer (aarch64 has the renderer built in).
# The launcher points fs_basepath here, for etmain/ and legacy/.
install -d "$opt"
install -m755 "$src/etl.$arch" "$src/etlded.$arch" "$opt/"
for f in "$src"/librenderer_*_"$arch".so; do
    [ -e "$f" ] && install -m755 "$f" "$opt/"
done

# Server configs (etl_server.cfg and the map cycles; copy one to
# ~/.etlegacy/etmain/ to change it) and the original game paks from
# enemy-territory-data, which the engine only looks for in etmain/.
install -d "$opt/etmain"
install -m644 "$src"/etmain/*.cfg "$opt/etmain/"
for p in pak0 pak1 pak2; do
    ln -s "$data/$p.pk3" "$opt/etmain/$p.pk3"
done

# The legacy mod: game modules, ETTV module, pk3, Lua libraries, WolfAdmin
# and the bundled GeoIP database.
cp -R --no-preserve=ownership "$src/legacy" "$opt/"
# Omni-Bot ships every platform's library; keep the one for this
# architecture.
ob=$opt/legacy/omni-bot
keep=omnibot_et.$arch.so
for f in "$ob"/omnibot_et*; do
    [ "${f##*/}" = "$keep" ] || rm -f "$f"
done
# Other architectures' game modules never ship, but be safe.
find "$opt/legacy" -maxdepth 1 -name '*.mp.*.so' ! -name "*.mp.$arch.so" -delete
# Upstream's omni-bot tree is drwxr--r--; the tree is read-only shared data.
find "$opt" -type d -exec chmod 755 {} +
find "$opt" -type f -exec chmod 644 {} +
find "$opt" -type f \( -name "etl.$arch" -o -name "etlded.$arch" -o -name '*.so' \) -exec chmod 755 {} +

# Launcher, with the dedicated server symlinked to it
install -d "$dest/usr/bin"
sed "s|@ARCH@|$arch|g" "$here/etl.sh" > "$dest/usr/bin/etl"
chmod 755 "$dest/usr/bin/etl"
ln -s etl "$dest/usr/bin/etlded"

# Desktop entry (handles et:// links) and upstream's scalable icon
install -Dm644 "$here/etlegacy.desktop" "$dest/usr/share/applications/etlegacy.desktop"
install -Dm644 "$src/icons/hicolor/scalable/apps/etl.svg" \
    "$dest/usr/share/icons/hicolor/scalable/apps/etlegacy.svg"

# Manual pages
install -d "$dest/usr/share/man/man6"
for m in etl etlded; do
    gzip -9nc "$src/man/man6/$m.6" > "$dest/usr/share/man/man6/$m.6.gz"
done

# Dedicated server as a systemd service (not enabled) and a firewalld service
# for the game port
install -Dm644 "$here/etlegacy-server.service" "$dest/usr/lib/systemd/system/etlegacy-server.service"
install -Dm644 "$here/etlegacy.xml" "$dest/usr/lib/firewalld/services/etlegacy.xml"

# Documentation and the GPL (Debian points to common-licenses instead)
install -Dm644 "$here/README.md" "$dest/usr/share/doc/$pkg/README.md"
if [ -n "$lic" ]; then
    install -Dm644 "$src/licenses/etlegacy/COPYING.txt" "$lic/COPYING.txt"
fi
