# knockoutcity-server

Velan Studios' Private Hosted Server for Knockout City (version 10.0), run
through gamelaunch with a private per-user PostgreSQL and Valkey/Redis. Also
provides the `knockoutcity` launcher used by the knockoutcity-wine and
knockoutcity-wine-steam client packages: host a game on this PC, or pick a
server announced on the LAN.

Run it with `knockoutcity-server` or from the desktop menu.

This is a Windows game run by `gamelaunch` through umu-launcher (Proton) when
it is installed, otherwise system wine with your distribution's DXVK. Use
`GAMELAUNCH_RUNNER=wine knockoutcity-server` to force system wine. Prefixes and saves
live in `~/.local/share/gamelaunch/knockoutcity-server/`; the first start takes a while.

## Notes

The server comes from Velan's original download (KnockoutCity-Server-10.0-269701.zip),
which Velan no longer hosts; the build fetches the Internet Archive's
byte-identical capture of it and checks its sha256.

`knockoutcity-server [--name NAME] [--secret PASSWORD] [--max-players N] [--port 23600]`
runs a dedicated server in the foreground. While it runs it holds a private
PostgreSQL and Valkey/Redis on 127.0.0.1 (ports 23651/23652), with their data
in `~/.local/share/knockoutcity-server/`, and announces itself on the LAN.
Players need TCP 23600, UDP 23600-23699 and UDP 23599 (LAN announcements)
open; on firewalld: `firewall-cmd --add-service=knockoutcity --permanent`.

`knockoutcity` (from a client package) asks whether to host on this PC or
join a server found on the LAN; `--host`, `--join ADDR[:PORT]` and `--scan`
skip the question. The player name defaults to the machine's short host name;
`--name` and `--secret` are remembered in `~/.config/knockoutcity/launcher.conf`.
Every server keeps its own player database, so use the same name each time.
