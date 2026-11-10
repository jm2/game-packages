# quake3-data-steam

Quake III Arena and Team Arena data via Steam

## Building

Game data comes from Steam via steamcmd, using an account that owns the
game. Either set `STEAM_USER` (steamcmd asks for the password and Steam Guard
code), or download once with `tools/fetch-steam quake3-data-steam` and build offline from
the cache.

## Notes

baseq3/pak0.pk3 and Team Arena's missionpack/pak0.pk3 for ioquake3-based
engines such as quake3e. The 1.32 point release paks (baseq3/pak1-8.pk3,
missionpack/pak1-3.pk3) come from quake3-pointrelease-data, which this
package depends on.

Steam sells Quake III Arena with the Team Arena expansion included (store
app 2200; Team Arena's own store page, app 2350, is gone), so one purchase
owns both apps, and this package downloads both: app 2200 and depot 2351 of
app 2350. It replaces the former quake3-ta-data-steam package. An account
that got Quake III Arena some other way without Team Arena fails the
download at depot 2351.
