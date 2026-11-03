# serioussam3-steam

Serious Sam 3: BFE (native Linux) with data via Steam

Run it with `serioussam3` or from the desktop menu.

## Building

Game data comes from Steam via steamcmd, using an account that owns the
game. Either set `STEAM_USER` (steamcmd asks for the password and Steam Guard
code), or download once with `tools/fetch-steam serioussam3-steam` and build offline from
the cache.
