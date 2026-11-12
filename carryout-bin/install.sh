#!/bin/sh
# Shared install step for the PKGBUILD, the RPM spec and debian/rules.
#   install.sh <unpacked release archive> <destdir> <docdir>
# Upstream's release archives hold the binary, README.md and LICENSE (the
# PKGBUILD and the spec install LICENSE themselves; Debian points to
# common-licenses).
set -eu
src=$1 dest=$2 docdir=$3

install -Dm755 "$src/carryout" "$dest/usr/bin/carryout"
install -Dm644 "$src/README.md" "$dest/$docdir/README.md"
