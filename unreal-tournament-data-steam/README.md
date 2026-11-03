# unreal-tournament-data-steam

Game data for Unreal Tournament: Game of the Year Edition, downloaded from
Steam with steamcmd and installed to /opt/unreal-tournament. Play it with
the native OldUnreal binaries from unreal-tournament-bin.

## Building

Game data comes from Steam via steamcmd, using an account that owns the
game. Either set `STEAM_USER` (steamcmd asks for the password and Steam Guard
code), or download once with `tools/fetch-steam unreal-tournament-data-steam` and build offline from
the cache.
