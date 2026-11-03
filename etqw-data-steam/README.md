# etqw-data-steam

Enemy Territory: Quake Wars data via Steam

## Building

Game data comes from Steam via steamcmd, using an account that owns the
game. Either set `STEAM_USER` (steamcmd asks for the password and Steam Guard
code), or download once with `tools/fetch-steam etqw-data-steam` and build offline from
the cache.

## Notes

Used by the native openETQW engine (openetqw-bin) and the AUR etqw package.
