# codmwr-wine-steam

Call of Duty: Modern Warfare Remastered (H1-Mod) using Wine with data via Steam

Run it with `codmwr` or from the desktop menu.

This is a Windows game run by `gamelaunch` through umu-launcher (Proton) when
it is installed, otherwise system wine with your distribution's DXVK. Use
`GAMELAUNCH_RUNNER=wine codmwr` to force system wine. Prefixes and saves
live in `~/.local/share/gamelaunch/codmwr/`; the first start takes a while.

`codmwr -h` lists the available modes:

- `-m`: H1-Mod multiplayer (default)
- `-s`: H1-Mod campaign
- `-v`: stock multiplayer, LAN via Goldberg
- `-c`: stock campaign

## Building

Game data comes from Steam via steamcmd, using an account that owns the
game. Either set `STEAM_USER` (steamcmd asks for the password and Steam Guard
code), or download once with `tools/fetch-steam codmwr-wine-steam` and build offline from
the cache.

## Notes

H1-Mod (https://github.com/auroramod/h1-mod, GPL-3.0) is the community client
for Modern Warfare Remastered: dedicated servers, LAN play and mods, with its
own Steam emulation. `codmwr` starts H1-Mod multiplayer, `codmwr -s` the
H1-Mod campaign. `-v` and `-c` start the stock h1_mp64_ship.exe and
h1_sp64_ship.exe against the Goldberg emulator instead.

H1-Mod's automatic update check (which would replace h1-mod.exe and its data
from auroramod's servers) is turned off with `+set cg_auto_update 0`; the
packaged version stays as installed and works offline.

H1-Mod's client data (data/cdata from the release's source) is installed to
h1-mod/ in the game directory, which H1-Mod searches, so it doesn't have to
download it at first launch. H1-Mod refuses game builds it doesn't support
(it checks zone file hashes), so a Steam update can need a newer H1-Mod.

Steam sells multiplayer (app 393100) and the campaign (app 393080) as
separate apps of one purchase; this package downloads both.
