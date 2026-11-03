# ut2004-data-steam

Game data for Unreal Tournament 2004: Editor's Choice Edition, downloaded from
Steam with steamcmd and installed to /opt/ut2004. Play it with the native
OldUnreal binaries from ut2004-bin.

## Building

Game data comes from Steam via steamcmd, using an account that owns the
game. Either set `STEAM_USER` (steamcmd asks for the password and Steam Guard
code), or download once with `tools/fetch-steam ut2004-data-steam` and build offline from
the cache.
