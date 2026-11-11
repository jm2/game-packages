#!/bin/sh
# Shared install step for the PKGBUILD, the RPM spec and debian/rules.
#   install.sh <built source tree> <destdir>
# Upstream's install-tree.sh installs what its own rpm, deb and Arch packages
# ship: swk, swk-tray, the systemd user units (node, coordinator), the system
# coordinator unit, its sysusers.d account, the tray's desktop entry and icons.
set -eu
src=$1 dest=$2

sh "$src/build-aux/linux/install-tree.sh" "$dest" "$src" /usr
install -Dm644 "$src/README.md" "$dest/usr/share/doc/switchworks/README.md"
