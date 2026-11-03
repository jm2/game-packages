# dirtshowdown-wine-steam

DiRT Showdown using Wine with data via Steam

Run it with `dirtshowdown` or from the desktop menu.

This is a Windows game run by `gamelaunch` through umu-launcher (Proton) when
it is installed, otherwise system wine with your distribution's DXVK. Use
`GAMELAUNCH_RUNNER=wine dirtshowdown` to force system wine. Prefixes and saves
live in `~/.local/share/gamelaunch/dirtshowdown/`; the first start takes a while.

`dirtshowdown -h` lists the available modes:

- `-a`: AVX build (default)
- `-n`: non-AVX build for older CPUs

## Building

Game data comes from Steam via steamcmd, using an account that owns the
game. Either set `STEAM_USER` (steamcmd asks for the password and Steam Guard
code), or download once with `tools/fetch-steam dirtshowdown-wine-steam` and build offline from
the cache.
