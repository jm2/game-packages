# aom-retold-wine-steam

Age of Mythology: Retold, run through gamelaunch
(umu/Proton or system wine) with the game data downloaded from Steam and the
Goldberg Steam emulator (gbe-fork-bin). ageLANServer and its launcher
companion DLLs restore LAN multiplayer lobbies without the official servers.

Run it with `aom-retold` or from the desktop menu.

This is a Windows game run by `gamelaunch` through umu-launcher (Proton) when
it is installed, otherwise system wine with your distribution's DXVK. Use
`GAMELAUNCH_RUNNER=wine aom-retold` to force system wine. Prefixes and saves
live in `~/.local/share/gamelaunch/aom-retold/`; the first start takes a while.

## Building

Game data comes from Steam via steamcmd, using an account that owns the
game. Either set `STEAM_USER` (steamcmd asks for the password and Steam Guard
code), or download once with `tools/fetch-steam aom-retold-wine-steam` and build offline from
the cache.

## Notes

`aom-retold` starts the game directly. `aom-retold-lan` (menu entry "Age of Mythology: Retold (LAN)")
runs the ageLANServer launcher from agelanserver-bin: it finds a server on the
LAN or offers to start one, then starts the game through gamelaunch with the
companion DLLs (agelanserver-companion-bin, linked into
`steam_settings/load_dlls/` and loaded by gbe-fork-bin's experimental
steam_api64.dll) pointed at the server. Joining needs no root. For hosting,
see /usr/share/doc/agelanserver-bin/README.md (the agelanserver@athens.service
system service is the easy way). Hosting Age of Mythology: Retold needs the Battle Server from aoe2-de-wine-steam (upstream only
supports AoE II's for it).

Start `aom-retold` once before the first LAN game: creating the Wine prefix can take
longer than the minute the launcher waits for the game to appear.
