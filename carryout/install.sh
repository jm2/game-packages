#!/bin/sh
# Shared install step for the PKGBUILD, the RPM spec and debian/rules.
#   install.sh <built source tree> <destdir>
set -eu
src=$1 dest=$2

# What upstream's release archives hold: the binary, README.md and LICENSE.
install -Dm755 "$src/carryout" "$dest/usr/bin/carryout"
install -Dm644 "$src/README.md" "$dest/usr/share/doc/carryout/README.md"
