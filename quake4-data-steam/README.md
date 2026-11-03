# quake4-data-steam

Quake 4 data via Steam

## Building

Game data comes from Steam via steamcmd, using an account that owns the
game. Either set `STEAM_USER` (steamcmd asks for the password and Steam Guard
code), or download once with `tools/fetch-steam quake4-data-steam` and build offline from
the cache.
