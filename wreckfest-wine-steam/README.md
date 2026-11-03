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
