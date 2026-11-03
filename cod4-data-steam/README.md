# cod4-data-steam

Call of Duty 4: Modern Warfare game data via Steam

## Building

Game data comes from Steam via steamcmd, using an account that owns the
game. Either set `STEAM_USER` (steamcmd asks for the password and Steam Guard
code), or download once with `tools/fetch-steam cod4-data-steam` and build offline from
the cache.

## Notes

Installs the Steam CoD4 tree to /opt/cod4 for cod4-wine-steam (Wine) and the
native KisakCOD engine (kisakcod-bin).
