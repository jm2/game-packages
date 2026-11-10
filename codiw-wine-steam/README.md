# codiw-wine-steam

Call of Duty: Infinite Warfare (IW7-Mod) using Wine with data via Steam

Run it with `codiw` or from the desktop menu.

This is a Windows game run by `gamelaunch` through umu-launcher (Proton) when
it is installed, otherwise system wine with your distribution's DXVK. Use
`GAMELAUNCH_RUNNER=wine codiw` to force system wine. Prefixes and saves
live in `~/.local/share/gamelaunch/codiw/`; the first start takes a while.

`codiw -h` lists the available modes:

- `-x`: IW7-Mod (default)
- `-v`: stock executable, LAN via Goldberg

## Building

Game data comes from Steam via steamcmd, using an account that owns the
game. Either set `STEAM_USER` (steamcmd asks for the password and Steam Guard
code), or download once with `tools/fetch-steam codiw-wine-steam` and build offline from
the cache.

## Notes

IW7-Mod (https://github.com/auroramod/iw7-mod, GPL-3.0) is the community
client for Infinite Warfare: dedicated servers, LAN play and mods, with its
own Steam emulation (it skips the Steam client under Wine). `codiw` starts
IW7-Mod (campaign, multiplayer and zombies from its menu) with -noupdate;
`codiw -v` starts the stock iw7_ship.exe against the Goldberg emulator.

IW7-Mod's client data (data/cdata from the release's source) is installed to
iw7-mod/ in the game directory, which IW7-Mod searches, so it doesn't have to
download it. IW7-Mod refuses game builds it doesn't support (it checks zone
file hashes), so a Steam update can need a newer IW7-Mod. DLC is downloaded
when the Steam account owns it.
