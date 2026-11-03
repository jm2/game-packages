#!/bin/sh
# Shared install step for the PKGBUILD, the RPM spec and debian/rules.
#   install.sh <dir with the jar and packaging files> <jar file name> <destdir> <package name>
set -eu
src=$1 jar=$2 dest=$3 name=$4

install -Dm644 "$src/$jar" "$dest/usr/share/geysermc/Geyser.jar"
install -Dm644 "$src/config.yml" "$dest/etc/geysermc/config.yml"
install -Dm644 "$src/geysermc.service" "$dest/usr/lib/systemd/system/geysermc.service"
install -Dm644 "$src/geysermc.sysusers" "$dest/usr/lib/sysusers.d/geysermc.conf"
install -Dm644 "$src/geysermc.tmpfiles" "$dest/usr/lib/tmpfiles.d/geysermc.conf"
install -Dm644 "$src/README.md" "$dest/usr/share/doc/$name/README.md"
