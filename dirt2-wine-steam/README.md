# dirt2-wine-steam

Colin McRae: DiRT 2, run through gamelaunch (umu/Proton or system wine) with
the game data downloaded from Steam. Games for Windows - LIVE is replaced by
XLiveLessNess, which restores LAN multiplayer.

Run it with `dirt2` or from the desktop menu.

This is a Windows game run by `gamelaunch` through umu-launcher (Proton) when
it is installed, otherwise system wine with your distribution's DXVK. Use
`GAMELAUNCH_RUNNER=wine dirt2` to force system wine. Prefixes and saves
live in `~/.local/share/gamelaunch/dirt2/`; the first start takes a while.

## Building

Game data comes from Steam via steamcmd, using an account that owns the
game. Either set `STEAM_USER` (steamcmd asks for the password and Steam Guard
code), or download once with `tools/fetch-steam dirt2-wine-steam` and build offline from
the cache.

## Notes

If DiRT 2 crashes on the first start, set `<directx forcedx9="true" />` in
`hardware_settings_config.xml` under `Documents/My Games/DiRT2/hardwaresettings/`
in `~/.local/share/gamelaunch/dirt2/userdata/` (or `~/Documents` for prefixes
created by the old package).

LAN play uses XLiveLessNess. XLLN's DiRT 2 quick-patch allows several
instances on one machine. (dirt2_game.exe refuses to start without the
dirt2.exe launcher, so there is no "skip the launcher" mode.)
