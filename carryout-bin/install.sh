#!/bin/sh
# Shared install step for the PKGBUILD and debian/rules.
#   install.sh <unpacked release package> <destdir> <docdir>
# The unpacked tree is upstream's .pkg.tar.zst or .deb payload: usr/bin/carryout
# and usr/share/doc/carryout/README.md. The PKGBUILD installs LICENSE itself;
# Debian points to common-licenses.
set -eu
src=$1 dest=$2 docdir=$3

install -Dm755 "$src/usr/bin/carryout" "$dest/usr/bin/carryout"
install -Dm644 "$src/usr/share/doc/carryout/README.md" "$dest/$docdir/README.md"
