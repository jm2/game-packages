# quake3-data-steam

Quake III Arena data via Steam

## Building

Game data comes from Steam via steamcmd, using an account that owns the
game. Either set `STEAM_USER` (steamcmd asks for the password and Steam Guard
code), or download once with `tools/fetch-steam quake3-data-steam` and build offline from
the cache.

## Notes

baseq3/pak0.pk3 for ioquake3-based engines such as quake3e. The 1.32 point
release paks (baseq3/pak1-8.pk3) come from quake3-pointrelease-data, which
this package depends on. Team Arena is quake3-ta-data-steam.
