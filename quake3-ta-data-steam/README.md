# quake3-ta-data-steam

Quake III: Team Arena data via Steam

## Building

Game data comes from Steam via steamcmd, using an account that owns the
game. Either set `STEAM_USER` (steamcmd asks for the password and Steam Guard
code), or download once with `tools/fetch-steam quake3-ta-data-steam` and build offline from
the cache.

## Notes

missionpack/pak0.pk3 for ioquake3-based engines; needs quake3-data.
