# quake2-data-steam

Quake II data via Steam

## Building

Game data comes from Steam via steamcmd, using an account that owns the
game. Either set `STEAM_USER` (steamcmd asks for the password and Steam Guard
code), or download once with `tools/fetch-steam quake2-data-steam` and build offline from
the cache.

## Notes

The original Quake II data (baseq2, The Reckoning in xatrix, Ground Zero in
rogue, and CTF) for source ports such as yquake2. The 2023 remaster in
rerelease/ is not included.
