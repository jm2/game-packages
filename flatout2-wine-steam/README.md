# flatout2-wine-steam

FlatOut 2 using Wine with data via Steam

Run it with `flatout2` or from the desktop menu.

This is a Windows game run by `gamelaunch` through umu-launcher (Proton) when
it is installed, otherwise system wine with your distribution's DXVK. Use
`GAMELAUNCH_RUNNER=wine flatout2` to force system wine. Prefixes and saves
live in `~/.local/share/gamelaunch/flatout2/`; the first start takes a while.

## Building

Game data comes from Steam via steamcmd, using an account that owns the
game. Either set `STEAM_USER` (steamcmd asks for the password and Steam Guard
code), or download once with `tools/fetch-steam flatout2-wine-steam` and build offline from
the cache.

## Notes

Steam's current FlatOut 2 (the re-release with fo2_launcher.exe, dxwrapper and
SDL3); its steam_api.dll is replaced by gbe-fork's. FlatOut2.exe has no version
resource, so the version is the Steam build ID. LAN play between this and the
older GOG build has not been tested.
