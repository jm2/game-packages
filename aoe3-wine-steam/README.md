# aoe3-wine-steam

Age of Empires III (2007) Complete Collection using Wine with data via Steam

Run it with `aoe3` or from the desktop menu.

This is a Windows game run by `gamelaunch` through umu-launcher (Proton) when
it is installed, otherwise system wine with your distribution's DXVK. Use
`GAMELAUNCH_RUNNER=wine aoe3` to force system wine. Prefixes and saves
live in `~/.local/share/gamelaunch/aoe3/`; the first start takes a while.

`aoe3 -h` lists the available modes:

- `-o`: Age of Empires III (original game)
- `-x`: The WarChiefs
- `-y`: The Asian Dynasties (default)

## Building

Game data comes from Steam via steamcmd, using an account that owns the
game. Either set `STEAM_USER` (steamcmd asks for the password and Steam Guard
code), or download once with `tools/fetch-steam aoe3-wine-steam` and build offline from
the cache.
