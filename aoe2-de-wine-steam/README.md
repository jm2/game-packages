# aoe2-de-wine-steam

Age of Empires II: Definitive Edition (with the Enhanced Graphics Pack), run
through gamelaunch (umu/Proton or system wine) with the game data downloaded
from Steam and the Goldberg Steam emulator (gbe-fork-bin). ageLANServer and
its launcher companion DLLs restore LAN multiplayer lobbies without the
official servers.

Run it with `aoe2-de` or from the desktop menu.

This is a Windows game run by `gamelaunch` through umu-launcher (Proton) when
it is installed, otherwise system wine with your distribution's DXVK. Use
`GAMELAUNCH_RUNNER=wine aoe2-de` to force system wine. Prefixes and saves
live in `~/.local/share/gamelaunch/aoe2-de/`; the first start takes a while.

## Building

Game data comes from Steam via steamcmd, using an account that owns the
game. Either set `STEAM_USER` (steamcmd asks for the password and Steam Guard
code), or download once with `tools/fetch-steam aoe2-de-wine-steam` and build offline from
the cache.

## Notes

`aoe2-de` starts the game directly. `aoe2-de-lan` (menu entry "Age of Empires II: DE (LAN)")
runs the ageLANServer launcher from agelanserver-bin: it finds a server on the
LAN or offers to start one, then starts the game through gamelaunch with the
companion DLLs (agelanserver-companion-bin, linked into
`steam_settings/load_dlls/` and loaded by gbe-fork-bin's experimental
steam_api64.dll) pointed at the server. Joining needs no root. For hosting,
see /usr/share/doc/agelanserver-bin/README.md (the agelanserver@age2.service
system service is the easy way). 

Start `aoe2-de` once before the first LAN game: creating the Wine prefix can take
longer than the minute the launcher waits for the game to appear.
