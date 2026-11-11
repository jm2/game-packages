#!/bin/sh
# Shared install step for the PKGBUILD, the RPM spec and debian/rules.
#   install.sh <built source tree> <destdir>
set -eu
src=$1 dest=$2

# Upstream's staging script, which its own rpm, deb and Arch packages use:
# the binary, the systemd units, sysusers.d, tmpfiles.d, the firewalld
# service and /etc/crossdock/crossdock.yaml. Nothing is enabled.
sh "$src/build-aux/linux/install-tree.sh" "$dest" "$src" /usr
install -Dm644 "$src/README.md" "$dest/usr/share/doc/crossdock/README.md"
