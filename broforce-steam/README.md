# broforce-steam

Broforce (native Linux) with data via Steam

Run it with `broforce` or from the desktop menu.

`broforce -h` lists the available modes:

- `-m`: 64-bit build (default)
- `-l`: legacy 32-bit build

## Building

Game data comes from Steam via steamcmd, using an account that owns the
game. Either set `STEAM_USER` (steamcmd asks for the password and Steam Guard
code), or download once with `tools/fetch-steam broforce-steam` and build offline from
the cache.
