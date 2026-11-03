# doom3bfg-data-steam

Doom 3 BFG Edition data via Steam

## Building

Game data comes from Steam via steamcmd, using an account that owns the
game. Either set `STEAM_USER` (steamcmd asks for the password and Steam Guard
code), or download once with `tools/fetch-steam doom3bfg-data-steam` and build offline from
the cache.
