# codmw2-wine-steam

Call of Duty: Modern Warfare 2 multiplayer (IW4x) using Wine with data via Steam

Run it with `codmw2` or from the desktop menu.

This is a Windows game run by `gamelaunch` through umu-launcher (Proton) when
it is installed, otherwise system wine with your distribution's DXVK. Use
`GAMELAUNCH_RUNNER=wine codmw2` to force system wine. Prefixes and saves
live in `~/.local/share/gamelaunch/codmw2/`; the first start takes a while.

`codmw2 -h` lists the available modes:

- `-x`: IW4x multiplayer (default)
- `-v`: stock multiplayer executable

## Building

Game data comes from Steam via steamcmd, using an account that owns the
game. Either set `STEAM_USER` (steamcmd asks for the password and Steam Guard
code), or download once with `tools/fetch-steam codmw2-wine-steam` and build offline from
the cache.

## Notes

IW4x is the community multiplayer client for MW2
(https://github.com/iw4x/iw4x-client, GPL-3.0). `codmw2 -v` starts the stock
iw4mp.exe instead.
