# cod4-wine-steam

Call of Duty 4: Modern Warfare (1.8), run through gamelaunch (umu/Proton or
system wine). This package is only the launcher: the game data comes from
cod4-data-steam, installed to /opt/cod4.

Run it with `cod4` or from the desktop menu.

This is a Windows game run by `gamelaunch` through umu-launcher (Proton) when
it is installed, otherwise system wine with your distribution's DXVK. Use
`GAMELAUNCH_RUNNER=wine cod4` to force system wine. Prefixes and saves
live in `~/.local/share/gamelaunch/cod4/`; the first start takes a while.

`cod4 -h` lists the available modes:

- `-m`: multiplayer (default)
- `-s`: singleplayer

## Notes

The game data comes from cod4-data-steam (installed to /opt/cod4), which the
native KisakCOD engine (kisakcod-bin) uses too.
