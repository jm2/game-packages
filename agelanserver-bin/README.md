# agelanserver-bin

luskaner's Age Server, formerly ageLANServer
(https://github.com/luskaner/ageServer, AGPL-3.0): a LAN replacement for the online services of Age of Empires II/III: DE and
Age of Mythology: Retold, shared by the aoe2-de-wine-steam,
aoe3-de-wine-steam and aom-retold-wine-steam packages.

## Playing

Every player runs the game's "(LAN)" menu entry, or `agelan <game>`
(`agelan --list` shows the installed games). The launcher looks for a server
on the LAN; if there is none it offers to start one, then starts the game
through `gamelaunch`. The server runs its own embedded Battle Server, so no
Windows BattleServer.exe (and no Wine for it) is needed to host. Joining needs no root: the game's
companion DLLs (agelanserver-companion-bin) redirect the official hosts and
trust the server's certificate inside the game process, so `/etc/hosts` and
the system certificate store are never touched.

Start the game normally once before the first LAN game: creating its Wine
prefix can take longer than the minute the launcher waits for the game.

## Hosting

Recommended for a machine that hosts regularly: the system service, which
binds port 443 without running as root and keeps its certificates, user data
and uploaded replays in `/var/lib/agelanserver/<game>/`:

    sudo systemctl enable --now agelanserver@age2.service   # age2, age3, athens

Its settings are in `/etc/agelanserver/config.toml`. Open TCP 443, UDP 31978
(LAN announcement) and the Battle Server ports in your firewall. This package
sets `[Internet] Enabled = false` there (upstream's default is true): the
server then makes no connectivity check and no public IP lookup
(api.ipify.org), which a LAN server doesn't need.

Without the service, the launcher starts a per-user server from
`~/.local/share/agelanserver/server/`, which holds its certificates, user data
and replays. A normal user can only listen on
port 443 if unprivileged ports start at 443 or lower:

    echo net.ipv4.ip_unprivileged_port_start=443 | sudo tee /etc/sysctl.d/50-agelanserver.conf
    sudo sysctl --system

## Upgrading from agelanserver-bin 1.x

Age Server 2.0 wants fresh user data. `agelan` moves an existing per-user
`~/.local/share/agelanserver/server/resources/userData` to
`userData.ageLANServer-1.x` the first time it runs; delete that once you no
longer need it. The system service now keeps its files in subdirectories of
`/var/lib/agelanserver/<game>/` and makes new certificates there; players get
the new CA from the launcher when they join.

## Configuration

`agelan` renders the launcher configs for every run from
`/usr/share/agelanserver/templates/`. To change them, copy a template to
`~/.config/agelanserver/` and edit it; the placeholders `@GAME@`,
`@GAMELAUNCH_ID@`, `@GAME_PATH@`, `@SERVER@` and `@LIB@` are filled in the
same way. The launcher template sets `CanUseInternet = false` (the launcher
then uses only its built-in list of the official domains) and leaves the
Battle Server manager off, as upstream does. Upstream's options are documented in
`/usr/share/doc/agelanserver-bin/launcher/` (and `server/`,
`battle-server-manager/`). `/usr/lib/agelanserver/launcher/bin/revert -a -e <game>`
undoes everything the launcher may have changed after a crash.

## Not verified

These packages were built and checked without the games: loading of the
companion DLLs through Goldberg's `load_dlls`, their behaviour under
Wine/Proton, and the embedded Battle Server (experimental upstream) still
need a real LAN test.
