# codbo3-wine-steam

Call of Duty: Black Ops III (BOIII) using Wine with data via Steam

Run it with `codbo3` or from the desktop menu.

This is a Windows game run by `gamelaunch` through umu-launcher (Proton) when
it is installed, otherwise system wine with your distribution's DXVK. Use
`GAMELAUNCH_RUNNER=wine codbo3` to force system wine. Prefixes and saves
live in `~/.local/share/gamelaunch/codbo3/`; the first start takes a while.

`codbo3 -h` lists the available modes:

- `-x`: BOIII (default)
- `-v`: stock executable, LAN via Goldberg

## Building

Game data comes from Steam via steamcmd, using an account that owns the
game. Either set `STEAM_USER` (steamcmd asks for the password and Steam Guard
code), or download once with `tools/fetch-steam codbo3-wine-steam` and build offline from
the cache.

## Notes

BOIII (Ezz-lol/boiii-free, https://github.com/Ezz-lol/boiii-free, GPL-3.0) is
the community client for Black Ops III: dedicated servers, LAN play, mods and
custom maps, with its own Steam handling. `codbo3` starts BOIII with
`-launch -noupdate` (straight into the game, no self-update); `codbo3 -v`
starts the stock BlackOps3.exe against the Goldberg emulator.

BOIII's data (data/ from the release's source) is installed to boiii/ in the
game directory, which BOIII searches next to its own appdata copy, so it
doesn't have to download it. Its launcher window reads its page from the
appdata copy only, so it's skipped with -launch. DLC is downloaded when the
Steam account owns it.
