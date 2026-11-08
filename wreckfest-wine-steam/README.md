# wreckfest-wine-steam

Wreckfest using Wine with data via Steam

Run it with `wreckfest` or from the desktop menu.

This is a Windows game run by `gamelaunch` through umu-launcher (Proton) when
it is installed, otherwise system wine with your distribution's DXVK. Use
`GAMELAUNCH_RUNNER=wine wreckfest` to force system wine. Prefixes and saves
live in `~/.local/share/gamelaunch/wreckfest/`; the first start takes a while.

`wreckfest -h` lists the available modes:

- `-m`: 64-bit Wreckfest_x64.exe (default)
- `-l`: legacy 32-bit Wreckfest.exe

## Building

Game data comes from Steam via steamcmd, using an account that owns the
game. Either set `STEAM_USER` (steamcmd asks for the password and Steam Guard
code), or download once with `tools/fetch-steam wreckfest-wine-steam` and build offline from
the cache.

## Notes

LAN play: the game's top-level steam_api64.dll is THQ Nordic's online
wrapper (the same file as in the GOG build), which loads Valve's Steam API
from wrapper/THQNOnline/steam/. Goldberg replaces only that inner Steam API,
so LAN discovery and joins go through THQ's layer exactly as in the GOG
build: this package finds and joins dedicated servers run by
wreckfest-wine-gog (`wreckfest-gog -s`).

Hosting from the game (Create Server) under Wine: THQ's wrapper binds a
dual-stack IPv6 socket and then an IPv4 socket on UDP 27016. Windows allows
that, Linux refuses the second bind, and nobody can join. gamelaunch preloads
wine-ipv6only (x86_64) for the 64-bit game (`-m`, the default), which makes the
IPv6 socket IPv6-only so the IPv4 bind succeeds. The legacy 32-bit `-l` runs
without it (expect the same hosting bug there). `GAMELAUNCH_NO_PRELOAD=1`
turns it off for one run.
