# codaw-wine-steam

Call of Duty: Advanced Warfare using Wine with data via Steam

Run it with `codaw` or from the desktop menu.

This is a Windows game run by `gamelaunch` through umu-launcher (Proton) when
it is installed, otherwise system wine with your distribution's DXVK. Use
`GAMELAUNCH_RUNNER=wine codaw` to force system wine. Prefixes and saves
live in `~/.local/share/gamelaunch/codaw/`; the first start takes a while.

`codaw -h` lists the available modes:

- `-s`: campaign (default)
- `-m`: multiplayer / exo survival (LAN via Goldberg)

## Building

Game data comes from Steam via steamcmd, using an account that owns the
game. Either set `STEAM_USER` (steamcmd asks for the password and Steam Guard
code), or download once with `tools/fetch-steam codaw-wine-steam` and build offline from
the cache.

## Notes

The XLabs s1x client this package used is no longer available, so the stock
executables are used. Multiplayer is the stock client against the Goldberg
emulator (LAN only); AlterWare's s1-mod has no public source release to
package.
