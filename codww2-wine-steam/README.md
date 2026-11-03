# codww2-wine-steam

Call of Duty: WWII using Wine with data via Steam

Run it with `codww2` or from the desktop menu.

This is a Windows game run by `gamelaunch` through umu-launcher (Proton) when
it is installed, otherwise system wine with your distribution's DXVK. Use
`GAMELAUNCH_RUNNER=wine codww2` to force system wine. Prefixes and saves
live in `~/.local/share/gamelaunch/codww2/`; the first start takes a while.

`codww2 -h` lists the available modes:

- `-s`: campaign (default)
- `-m`: multiplayer / nazi zombies (LAN via Goldberg)

## Building

Game data comes from Steam via steamcmd, using an account that owns the
game. Either set `STEAM_USER` (steamcmd asks for the password and Steam Guard
code), or download once with `tools/fetch-steam codww2-wine-steam` and build offline from
the cache.
