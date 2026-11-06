# doom3-data-steam

Doom 3 data via Steam

## Building

Game data comes from Steam via steamcmd, using an account that owns the
game. Either set `STEAM_USER` (steamcmd asks for the password and Steam Guard
code), or download once with `tools/fetch-steam doom3-data-steam` and build offline from
the cache.

## Notes

base/*.pk4 for dhewm3 and other Doom 3 engines. Resurrection of Evil is
doom3xp-data-steam.
