# wreckfest2-wine-steam

Wreckfest 2 using Wine with data via Steam

Run it with `wreckfest2` or from the desktop menu.

This is a Windows game run by `gamelaunch` through umu-launcher (Proton) when
it is installed, otherwise system wine with your distribution's DXVK. Use
`GAMELAUNCH_RUNNER=wine wreckfest2` to force system wine. Prefixes and saves
live in `~/.local/share/gamelaunch/wreckfest2/`; the first start takes a while.

## Building

Game data comes from Steam via steamcmd, using an account that owns the
game. Either set `STEAM_USER` (steamcmd asks for the password and Steam Guard
code), or download once with `tools/fetch-steam wreckfest2-wine-steam` and build offline from
the cache.
