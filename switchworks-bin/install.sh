#!/bin/sh
# Shared install step for the PKGBUILD, the RPM spec and debian/rules.
#   install.sh <unpacked release package> <destdir> <docdir> [<licensedir>]
# The release package is upstream's own .pkg.tar.zst, .rpm or .deb, unpacked.
# All three hold the files of upstream's build-aux/linux/install-tree.sh: swk,
# swk-tray, the systemd user units (node, coordinator), the system coordinator
# unit, its sysusers.d account, the tray's desktop entry and icons.
# Upstream's doc/copyright, changelog.gz and lintian overrides (.deb) are left
# out. The license texts (LICENSE, which the .deb lacks, and the OFL texts of
# the fonts the web UI embeds) go to <licensedir>, or without one (Debian) the
# OFL texts go to <docdir> and the GPL-3.0 text is left to common-licenses.
set -eu
src=$1 dest=$2 docdir=$3 licdir=${4:-}
app=io.github.jm2.Switchworks

install -Dm755 "$src/usr/bin/swk" "$dest/usr/bin/swk"
install -Dm755 "$src/usr/bin/swk-tray" "$dest/usr/bin/swk-tray"
for role in node coordinator; do
    install -Dm644 "$src/usr/lib/systemd/user/swk-$role.service" "$dest/usr/lib/systemd/user/swk-$role.service"
done
install -Dm644 "$src/usr/lib/systemd/system/swk-coordinator.service" "$dest/usr/lib/systemd/system/swk-coordinator.service"
install -Dm644 "$src/usr/lib/sysusers.d/switchworks.conf" "$dest/usr/lib/sysusers.d/switchworks.conf"
install -Dm644 "$src/usr/share/applications/$app.desktop" "$dest/usr/share/applications/$app.desktop"
for icon in "$src"/usr/share/icons/hicolor/*/apps/"$app".*; do
    rel=${icon#"$src/"}
    install -Dm644 "$icon" "$dest/$rel"
done
install -Dm644 "$src/usr/share/doc/switchworks/README.md" "$dest/$docdir/README.md"

# The .pkg.tar.zst and .rpm keep the license texts in licenses/, the .deb
# keeps the OFL texts in doc/.
for f in OFL-Onest.txt OFL-JetBrainsMono.txt LICENSE; do
    for d in licenses doc; do
        [ -e "$src/usr/share/$d/switchworks/$f" ] || continue
        if [ -n "$licdir" ]; then
            install -Dm644 "$src/usr/share/$d/switchworks/$f" "$dest/$licdir/$f"
        elif [ "$f" != LICENSE ]; then
            install -Dm644 "$src/usr/share/$d/switchworks/$f" "$dest/$docdir/$f"
        fi
        break
    done
done
