#!/bin/sh
# Shared install step for PKGBUILD, RPM spec and debian/rules.
#   install.sh <extracted ageServer_full tarball dir> <destdir>
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
# Mount points for the service's writable directories: certificates, user
# data (profiles, matchmaking database) and each game's uploaded replays
# (<resources>/responses/cloud/<game>/replays, a fixed path next to the
# read-only builtin/ assets). agelan's per-user server copy makes them real
# directories too.
install -d "$lib/server/resources/certificates" "$lib/server/resources/userData"
for g in age1 age2 age3 age4 athens; do
    install -d "$lib/server/resources/responses/cloud/$g/replays"
done
find "$lib" -type d -exec chmod 755 {} +
find "$lib" -type f -exec chmod 644 {} +
for b in launcher/launcher launcher/bin/agent launcher/bin/config launcher/bin/config-admin \
         launcher/bin/config-admin-agent server/server server/bin/genCert \
         battle-server-manager/battle-server-manager; do
    chmod 755 "$lib/$b"
done

install -Dm755 client "$lib/libexec/client"
install -Dm755 agelan "$dest/usr/bin/agelan"
install -d "$share/games"

# Config templates rendered by agelan for every run (@PLACEHOLDERS@).
t=$share/templates
install -d "$t"
# The server starts its own embedded Battle Server when none is running, so
# the Battle Server manager (which needs the game's Windows BattleServer.exe)
# stays off, as upstream's default has it. The launcher looks up the official
# domains on the internet only to extend its built-in list; keep it offline.
sed -e "/^\[Config\]$/,/^\[/s|^CanUseInternet = true|CanUseInternet = false|" \
    -e "/^\[Server\]$/,/^\[/s|^Executable = 'auto'|Executable = '@SERVER@'|" \
    "$src/launcher/resources/config.toml" > "$t/launcher.toml"
sed -e "/^\[Client\]$/,/^\[/{
s|^Executable = 'auto'|Executable = '@LIB@/libexec/client'|
s|^ExecutableArgs = \[\]|ExecutableArgs = ['@GAMELAUNCH_ID@', '--overrideHosts={HostFilePath}', '--overrideCerts={CertFilePath}']|
s|^Path = 'auto'|Path = '@GAME_PATH@'|
}" -e "/^\[Client.Isolation\]$/,/^\[/s|^Path = 'auto'|Path = '@GAME_PATH@'|" \
    "$src/launcher/resources/config.age2.toml" > "$t/launcher.game.toml"
# Fail the build if upstream changed the layout these edits rely on.
check() { grep -q -- "$2" "$t/$1" || { echo "install.sh: upstream config layout changed ($1: $2)" >&2; exit 1; }; }
check launcher.toml "^Executable = '@SERVER@'"
check launcher.toml "^CanUseInternet = false"
check launcher.toml "^Run = 'false'"
check launcher.game.toml "^Executable = '@LIB@/libexec/client'"
check launcher.game.toml "--overrideCerts={CertFilePath}"
[ "$(grep -c "^Path = '@GAME_PATH@'" "$t/launcher.game.toml")" -eq 2 ] ||
    { echo "install.sh: upstream config layout changed (Client paths)" >&2; exit 1; }
chmod 644 "$t"/*.toml

# Server config for the system service (a conffile). A LAN server needs no
# internet: no connectivity check, no public IP lookup (api.ipify.org).
install -d "$dest/etc/agelanserver"
sed -e "/^\[Internet\]$/,/^\[/s|^Enabled = true|Enabled = false|" \
    "$src/server/resources/config/config.toml" > "$dest/etc/agelanserver/config.toml"
[ "$(sed -n '/^\[Internet\]$/,/^\[/p' "$dest/etc/agelanserver/config.toml" | grep -c '^Enabled = false')" -eq 1 ] ||
    { echo "install.sh: upstream config layout changed (server [Internet])" >&2; exit 1; }
chmod 644 "$dest/etc/agelanserver/config.toml"
install -Dm644 agelanserver@.service "$dest/usr/lib/systemd/system/agelanserver@.service"

doc=$dest/usr/share/doc/agelanserver-bin
install -Dm644 README.md "$doc/README.md"
install -Dm644 "$src/docs/README" "$doc/README.upstream"
for d in launcher server battle-server-manager; do
    install -Dm644 "$src/$d/docs/README" "$doc/$d/README"
done
install -Dm644 "$src/launcher/docs/README-config" "$doc/launcher/README-config"
install -Dm644 "$src/server/docs/BattleServers" "$doc/server/BattleServers"
