# quake3-data-steam

Quake III Arena data via Steam

## Building

Game data comes from Steam via steamcmd, using an account that owns the
game. Either set `STEAM_USER` (steamcmd asks for the password and Steam Guard
code), or download once with `tools/fetch-steam quake3-data-steam` and build offline from
the cache.

## Notes

baseq3/pak0.pk3 for ioquake3-based engines (the patch paks pak1-8 come with
the engine package, e.g. the AUR quake3). Team Arena is quake3-ta-data-steam.
