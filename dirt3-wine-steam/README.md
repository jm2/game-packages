# dirt3-wine-steam

DiRT 3 Complete Edition using Wine with data via Steam

Run it with `dirt3` or from the desktop menu.

This is a Windows game run by `gamelaunch` through umu-launcher (Proton) when
it is installed, otherwise system wine with your distribution's DXVK. Use
`GAMELAUNCH_RUNNER=wine dirt3` to force system wine. Prefixes and saves
live in `~/.local/share/gamelaunch/dirt3/`; the first start takes a while.

## Building

Game data comes from Steam via steamcmd, using an account that owns the
game. Either set `STEAM_USER` (steamcmd asks for the password and Steam Guard
code), or download once with `tools/fetch-steam dirt3-wine-steam` and build offline from
the cache.

## Notes

If DiRT 3 crashes on the first start, set your native resolution in
`Documents/My Games/DiRT3/hardwaresettings/hardware_settings_config.xml`
(under `~/.local/share/gamelaunch/dirt3/userdata/`), and if that is not
enough also `<directx forcedx9="true" />`.
