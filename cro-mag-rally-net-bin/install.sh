#!/bin/sh
# Shared install step for the PKGBUILD, the RPM spec and debian/rules.
#   install.sh <unpacked upstream package> <destdir> <doc dir> <license dir>
# The unpacked tree is the payload of one of upstream's release packages (the
# .pkg.tar.zst, .rpm or .deb; all hold the same files under usr/). The doc and
# license dirs are absolute paths inside <destdir>.
set -eu
src=$1 dest=$2 doc=$3 lic=$4
here=$(cd "$(dirname "$0")" && pwd)
lib=$dest/usr/lib/cromagrally

# Game binary and its bundled SDL3, found through RUNPATH $ORIGIN. The
# unversioned libSDL3.so development link is left out.
install -Dm755 "$src/usr/lib/cromagrally/CroMagRally" "$lib/CroMagRally"
install -m755 "$src/usr/lib/cromagrally/libSDL3.so.0".*.* "$lib/"
cp -P "$src/usr/lib/cromagrally/libSDL3.so.0" "$lib/"

# Game data
install -d "$dest/usr/share/cromagrally"
cp -r --no-preserve=ownership "$src/usr/share/cromagrally/Data" "$dest/usr/share/cromagrally/"
find "$dest/usr/share/cromagrally" -type d -exec chmod 755 {} +
find "$dest/usr/share/cromagrally" -type f -exec chmod 644 {} +

# Upstream's launcher (it changes into /usr/share/cromagrally, where the game
# looks for Data/), plus the command name the source-built package used.
install -Dm755 "$src/usr/bin/cromagrally" "$dest/usr/bin/cromagrally"
ln -sf cromagrally "$dest/usr/bin/cro-mag-rally"

# Desktop entry, AppStream metadata and icon
install -Dm644 "$src/usr/share/applications/io.jor.cromagrally.desktop" \
    "$dest/usr/share/applications/io.jor.cromagrally.desktop"
install -Dm644 "$src/usr/share/metainfo/io.jor.cromagrally.metainfo.xml" \
    "$dest/usr/share/metainfo/io.jor.cromagrally.metainfo.xml"
install -Dm644 "$src/usr/share/icons/hicolor/512x512/apps/io.jor.cromagrally.png" \
    "$dest/usr/share/icons/hicolor/512x512/apps/io.jor.cromagrally.png"

# Documentation (upstream's README is renamed next to this package's) and
# licenses; upstream's Debian copyright file is left out.
install -Dm644 "$here/README.md" "$dest$doc/README.md"
install -m644 "$src/usr/share/doc/cromagrally/README.md" "$dest$doc/README.upstream.md"
install -m644 "$src/usr/share/doc/cromagrally/CHANGELOG.md" "$dest$doc/"
install -d "$dest$lic"
install -m644 "$src/usr/share/licenses/cromagrally/LICENSE.md" \
    "$src/usr/share/licenses/cromagrally/THIRD-PARTY-LICENSES.md" "$dest$lic/"
