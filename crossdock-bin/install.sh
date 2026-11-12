#!/bin/sh
# Shared install step for the PKGBUILD, the RPM spec and debian/rules.
#   install.sh <unpacked release package> <destdir> <docdir> [<licensedir>]
# The release package is upstream's own .pkg.tar.zst, .rpm or .deb, unpacked.
# All three hold the files of upstream's build-aux/linux/install-tree.sh: the
# binary, the systemd units, sysusers.d, tmpfiles.d, the firewalld service and
# /etc/crossdock/crossdock.yaml (a config file). Nothing is enabled.
# Upstream's doc/copyright, changelog.gz and lintian overrides (.deb) are left
# out. LICENSE (the GPL-3.0 text; the .pkg.tar.zst and .rpm carry it) goes to
# <licensedir>; without one (Debian: /usr/share/common-licenses) it is dropped.
set -eu
src=$1 dest=$2 docdir=$3 licdir=${4:-}

install -Dm755 "$src/usr/bin/crossdock" "$dest/usr/bin/crossdock"
for unit in crossdock-serve.service crossdock-publish.service crossdock-publish.path crossdock-publish.timer; do
    install -Dm644 "$src/usr/lib/systemd/system/$unit" "$dest/usr/lib/systemd/system/$unit"
done
install -Dm644 "$src/usr/lib/sysusers.d/crossdock.conf" "$dest/usr/lib/sysusers.d/crossdock.conf"
install -Dm644 "$src/usr/lib/tmpfiles.d/crossdock.conf" "$dest/usr/lib/tmpfiles.d/crossdock.conf"
install -Dm644 "$src/usr/lib/firewalld/services/crossdock.xml" "$dest/usr/lib/firewalld/services/crossdock.xml"
install -Dm644 "$src/etc/crossdock/crossdock.yaml" "$dest/etc/crossdock/crossdock.yaml"
install -Dm644 "$src/usr/share/doc/crossdock/README.md" "$dest/$docdir/README.md"
if [ -n "$licdir" ] && [ -e "$src/usr/share/licenses/crossdock/LICENSE" ]; then
    install -Dm644 "$src/usr/share/licenses/crossdock/LICENSE" "$dest/$licdir/LICENSE"
fi
