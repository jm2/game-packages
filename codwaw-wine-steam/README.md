# codwaw-wine-steam

Call of Duty: World at War using Wine with data via Steam

Run it with `codwaw` or from the desktop menu.

This is a Windows game run by `gamelaunch` through umu-launcher (Proton) when
it is installed, otherwise system wine with your distribution's DXVK. Use
`GAMELAUNCH_RUNNER=wine codwaw` to force system wine. Prefixes and saves
live in `~/.local/share/gamelaunch/codwaw/`; the first start takes a while.

`codwaw -h` lists the available modes:

- `-z`: campaign and zombies (large-address-aware build) (default)
- `-s`: campaign and zombies (standard build)
- `-m`: multiplayer

## Building

Game data comes from Steam via steamcmd, using an account that owns the
game. Either set `STEAM_USER` (steamcmd asks for the password and Steam Guard
code), or download once with `tools/fetch-steam codwaw-wine-steam` and build offline from
the cache.

## Notes

The executables are replaced with DRM-free builds from
jm2/archlinux-package-codwaw-wine-steam.
