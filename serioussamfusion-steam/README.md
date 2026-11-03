# serioussamfusion-steam

Serious Sam Fusion 2017 (native Linux) with data via Steam

Run it with `serioussamfusion` or from the desktop menu.

## Building

Game data comes from Steam via steamcmd, using an account that owns the
game. Either set `STEAM_USER` (steamcmd asks for the password and Steam Guard
code), or download once with `tools/fetch-steam serioussamfusion-steam` and build offline from
the cache.
