# etlegacy-bin

ET: Legacy (<https://www.etlegacy.com/>) is an open-source engine for
Wolfenstein: Enemy Territory 2.60b, with its own Legacy mod. This package is
upstream's prebuilt Linux release (x86_64 or aarch64) in `/opt/etlegacy`:
the client (`etl`), the dedicated server (`etlded`), the Legacy mod with
Omni-Bot, WolfAdmin and ETTV, and the server configs.

## Game data

The original game's `pak0.pk3`, `pak1.pk3` and `pak2.pk3` (ET is freeware)
come from `enemy-territory-data-etlegacy`, which installs them to
`/usr/share/enemy-territory/etmain`; `/opt/etlegacy/etmain/pak*.pk3` link
there. The AUR's `enemy-territory-data` uses the same location and works as
well.

## Running

- `etl`: the client. `etl et://host:port` (or an `et://` link in a browser)
  connects to a server.
- `etlded`: the dedicated server, e.g.

      etlded +map oasis                    # quick LAN server
      etlded +exec etl_server.cfg          # upstream's sample config (map voting)

  Add `+set omnibot_enable 1 +set omnibot_path /opt/etlegacy/legacy/omni-bot`
  for bots (x86_64 only; upstream has no aarch64 Omni-Bot support), and
  `+set dedicated 1` to keep a LAN server off the internet master server
  (`etl_server.cfg` sets `dedicated 2` and advertises the server).

Settings, downloaded mods, server configs and logs live in `~/.etlegacy`
(`fs_homepath`); files there override `/opt/etlegacy`, so copy
`/opt/etlegacy/etmain/etl_server.cfg` to `~/.etlegacy/etmain/` to change it.

The 64-bit engine can only join servers whose mod has a 64-bit build (ETrun,
ETJump, N!tmod, Legacy, ...); servers running 32-bit-only mods (Jaymod, ETPub,
NoQuarter, silEnT, ...) need upstream's 32-bit build, which this package does
not include. ETPro and PunkBuster servers are not supported by ET: Legacy.

## Server

- `etlegacy-server.service` runs `etlded +exec etl_server.cfg` as a dynamic
  user with `fs_homepath` `/var/lib/etlegacy-server`; it is not enabled.
  Put your configs in `/var/lib/etlegacy-server/etmain/` (or `legacy/`) or
  change the command with `systemctl edit etlegacy-server`.
- The firewalld service `etlegacy` opens UDP 27960-27963
  (`firewall-cmd --add-service=etlegacy`).

The client's update check only reports new releases; update the package.
