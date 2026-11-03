#!/bin/sh
# Shared install step for the PKGBUILD, the RPM spec and debian/rules, run
# after "make install DESTDIR=<destdir>".
#   install.sh <package dir> <destdir> <package name>
set -eu
pkg=$1 dest=$2 name=$3

# make install creates empty /var/{log,run,cache/owntone}; tmpfiles.d owns them.
find "$dest/var" -depth -type d -empty -delete
[ ! -e "$dest/var" ] || { echo "install.sh: unexpected files under /var" >&2; exit 1; }
find "$dest" -name '*.la' -delete

install -Dm644 "$pkg/override.conf" "$dest/usr/lib/systemd/system/owntone.service.d/override.conf"
install -Dm644 "$pkg/owntone.sysusers" "$dest/usr/lib/sysusers.d/owntone.conf"
install -Dm644 "$pkg/owntone.tmpfiles" "$dest/usr/lib/tmpfiles.d/owntone.conf"
install -Dm644 "$pkg/README.md" "$dest/usr/share/doc/$name/README.md"
