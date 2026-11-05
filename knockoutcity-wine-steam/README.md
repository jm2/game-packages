# knockoutcity-wine-steam

Knockout City Private Server Edition using Wine with data via Steam

Run it with `knockoutcity` or from the desktop menu.

This is a Windows game run by `gamelaunch` through umu-launcher (Proton) when
it is installed, otherwise system wine with your distribution's DXVK. Use
`GAMELAUNCH_RUNNER=wine knockoutcity` to force system wine. Prefixes and saves
live in `~/.local/share/gamelaunch/knockoutcity/`; the first start takes a while.

## Building

Game data comes from Steam via steamcmd, using an account that owns the
game. Either set `STEAM_USER` (steamcmd asks for the password and Steam Guard
code), or download once with `tools/fetch-steam knockoutcity-wine-steam` and build offline from
the cache.

## Notes

The free Steam release (app 2915930) ships only the client; the server comes
from knockoutcity-server.

Run `knockoutcity` to host a game on this PC or join a server announced on
the LAN (see knockoutcity-server for options, ports and settings). There is
no Debian package: two data files are each larger than a .deb can hold.
