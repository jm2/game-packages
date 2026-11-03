# codghosts-wine-steam

Call of Duty: Ghosts using Wine with data via Steam

Run it with `codghosts` or from the desktop menu.

This is a Windows game run by `gamelaunch` through umu-launcher (Proton) when
it is installed, otherwise system wine with your distribution's DXVK. Use
`GAMELAUNCH_RUNNER=wine codghosts` to force system wine. Prefixes and saves
live in `~/.local/share/gamelaunch/codghosts/`; the first start takes a while.

`codghosts -h` lists the available modes:

- `-s`: campaign (default)
- `-m`: multiplayer / extinction (LAN via Goldberg)

## Building

Game data comes from Steam via steamcmd, using an account that owns the
game. Either set `STEAM_USER` (steamcmd asks for the password and Steam Guard
code), or download once with `tools/fetch-steam codghosts-wine-steam` and build offline from
the cache.

## Notes

The XLabs iw6x client this package used is no longer available, so the stock
executables are used against the Goldberg emulator (LAN only).
