# wreckfest-wine-gog

Wreckfest using Wine with data via GOG

Run it with `wreckfest-gog` or from the desktop menu.

This is a Windows game run by `gamelaunch` through umu-launcher (Proton) when
it is installed, otherwise system wine with your distribution's DXVK. Use
`GAMELAUNCH_RUNNER=wine wreckfest-gog` to force system wine. Prefixes and saves
live in `~/.local/share/gamelaunch/wreckfest-gog/`; the first start takes a while.

`wreckfest-gog -h` lists the available modes:

- `-m`: 64-bit Wreckfest_x64.exe (default)
- `-l`: legacy 32-bit Wreckfest.exe
- `-s`: dedicated LAN server (server_config.cfg)

## Building

Place these files next to the build files or in
`${TMPDIR:-/var/tmp}/linux-packages-cache/wreckfest-wine-gog/` before building:

- `setup_wreckfest_1.0o_(79627).exe` - GOG (lgogdownloader: wreckfest/en1installer0)
- `setup_wreckfest_1.0o_(79627)-1.bin` - GOG (lgogdownloader: wreckfest/en1installer1)
- `setup_wreckfest_1.0o_(79627)-2.bin` - GOG (lgogdownloader: wreckfest/en1installer2)
- `setup_wreckfest_1.0o_(79627)-3.bin` - GOG (lgogdownloader: wreckfest/en1installer3)
- `setup_wreckfest_1.0o_(79627)-4.bin` - GOG (lgogdownloader: wreckfest/en1installer4)
- `setup_wreckfest_1.0o_(79627)-5.bin` - GOG (lgogdownloader: wreckfest/en1installer5)
- `setup_wreckfest_1.0o_(79627)-6.bin` - GOG (lgogdownloader: wreckfest/en1installer6)
- `setup_wreckfest_1.0o_(79627)-7.bin` - GOG (lgogdownloader: wreckfest/en1installer7)
- `setup_wreckfest_1.0o_(79627)-8.bin` - GOG (lgogdownloader: wreckfest/en1installer8)

## Notes

Season Pass DLC: install wreckfest-gog-dlc1 / wreckfest-gog-dlc2, which add
their files to /opt/wreckfest-gog.

LAN play (from jm2/lan-ipxe wreckfest-lan): GOG's 2024+ build derives each
player's SteamID from a hash of the Windows username, so machines with the
same username kick each other ("Already Logged In"). The launcher runs the
game as a Windows user named after the machine's short host name, which needs
the system wine backend: Proton always reports "steamuser", so with only
umu-launcher installed every machine collides. Give each LAN machine its own
host name, or set `GAMELAUNCH_USER=<name>` for a run. Generic host names
(localhost*, archiso) get a random `player-<hex>` name instead.

`wreckfest-gog -s` starts a dedicated LAN server with
`~/.local/share/gamelaunch/wreckfest-gog/game/server_config.cfg` (copied from
the game's initial_server_config.cfg on first start). The server still signs
in to THQ Nordic's online service, so the host needs internet; clients do
not.

Hosting from the game (Create Server) under Wine: THQ's wrapper binds a
dual-stack IPv6 socket and then an IPv4 socket on UDP 27016. Windows allows
that, Linux refuses the second bind, and nobody can join. gamelaunch preloads
wine-ipv6only (x86_64) for the 64-bit game (`-m`, the default), which makes the
IPv6 socket IPv6-only so the IPv4 bind succeeds. The legacy 32-bit `-l` runs
without it (expect the same hosting bug there). `GAMELAUNCH_NO_PRELOAD=1`
turns it off for one run. The dedicated server (`-s`) never loads it: its single
dual-stack socket would stop accepting IPv4 clients.
