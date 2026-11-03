#!/bin/sh
# Shared install step for PKGBUILD, RPM spec and debian/rules.
#   install.sh <extracted ageLANServer_full tarball dir> <destdir>
set -eu
src=$1 dest=$2
lib=$dest/usr/lib/agelanserver
share=$dest/usr/share/agelanserver

# Upstream tree as shipped (launcher, server, battle-server-manager), minus
# the interactive helper scripts that assume a writable install.
install -d "$lib"
for d in launcher server battle-server-manager; do
    cp -r --no-preserve=ownership "$src/$d" "$lib/"
done
rm -f "$lib"/*/start_*.sh "$lib"/server/bin/genCert.sh \
      "$lib"/battle-server-manager/clean.sh "$lib"/battle-server-manager/remove-all.sh
# Mount point for the service's writable certificate directory.
install -d "$lib/server/resources/certificates"
find "$lib" -type d -exec chmod 755 {} +
find "$lib" -type f -exec chmod 644 {} +
for b in launcher/launcher launcher/bin/agent launcher/bin/config launcher/bin/config-admin \
         launcher/bin/config-admin-agent server/server server/bin/genCert \
         battle-server-manager/battle-server-manager; do
    chmod 755 "$lib/$b"
done

install -Dm755 client "$lib/libexec/client"
install -Dm755 wine-shim "$lib/libexec/shim/wine"
install -Dm755 agelan "$dest/usr/bin/agelan"
install -d "$share/games"

# Config templates rendered by agelan for every run (@PLACEHOLDERS@).
t=$share/templates
install -d "$t"
sed -e "/^\[Server\]$/,/^\[/s|^Executable = 'auto'|Executable = '@SERVER@'|" \
    -e "/^\[Server.BattleServerManager\]$/,/^\[/{
s|^Executable = 'auto'|Executable = '@LIB@/battle-server-manager/battle-server-manager'|
s|^ExecutableArgs = \['-e', '{Game}', '-r'\]|ExecutableArgs = ['-e', '{Game}', '-r', '--gameConfig', '@BSM_CONFIG@']|
}" "$src/launcher/resources/config.toml" > "$t/launcher.toml"
sed -e "/^\[Client\]$/,/^\[/{
s|^Executable = 'auto'|Executable = '@LIB@/libexec/client'|
s|^ExecutableArgs = \[\]|ExecutableArgs = ['@GAMELAUNCH_ID@', '--overrideHosts={HostFilePath}', '--overrideCerts={CertFilePath}']|
s|^Path = 'auto'|Path = '@GAME_PATH@'|
}" -e "/^\[Client.Isolation\]$/,/^\[/s|^Path = 'auto'|Path = '@GAME_PATH@'|" \
    "$src/launcher/resources/config.age2.toml" > "$t/launcher.game.toml"
sed -e "/^\[Executable\]$/,/^\[/s|^Path = 'auto'|Path = '@BATTLESERVER@'|" \
    "$src/battle-server-manager/resources/config.age2.toml" > "$t/battle-server-manager.toml"
# Fail the build if upstream changed the layout these edits rely on.
check() { grep -q -- "$2" "$t/$1" || { echo "install.sh: upstream config layout changed ($1: $2)" >&2; exit 1; }; }
check launcher.toml "^Executable = '@SERVER@'"
check launcher.toml "battle-server-manager/battle-server-manager'"
check launcher.toml "'--gameConfig', '@BSM_CONFIG@'"
check launcher.game.toml "^Executable = '@LIB@/libexec/client'"
check launcher.game.toml "--overrideCerts={CertFilePath}"
[ "$(grep -c "^Path = '@GAME_PATH@'" "$t/launcher.game.toml")" -eq 2 ] ||
    { echo "install.sh: upstream config layout changed (Client paths)" >&2; exit 1; }
check battle-server-manager.toml "^Path = '@BATTLESERVER@'"
chmod 644 "$t"/*.toml

# Server config for the system service (a conffile).
install -Dm644 "$src/server/resources/config/config.toml" "$dest/etc/agelanserver/config.toml"
install -Dm644 agelanserver@.service "$dest/usr/lib/systemd/system/agelanserver@.service"

doc=$dest/usr/share/doc/agelanserver-bin
install -Dm644 README.md "$doc/README.md"
install -Dm644 "$src/docs/README" "$doc/README.upstream"
for d in launcher server battle-server-manager; do
    install -Dm644 "$src/$d/docs/README" "$doc/$d/README"
done
install -Dm644 "$src/launcher/docs/README-config" "$doc/launcher/README-config"
install -Dm644 "$src/server/docs/BattleServers" "$doc/server/BattleServers"
