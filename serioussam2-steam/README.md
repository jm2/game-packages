# serioussam2-steam

Serious Sam 2 (flibit's Linux port) with data via Steam

Run it with `serioussam2` or from the desktop menu.

## Building

Game data comes from Steam via steamcmd, using an account that owns the
game. Either set `STEAM_USER` (steamcmd asks for the password and Steam Guard
code), or download once with `tools/fetch-steam serioussam2-steam` and build offline from
the cache.

## Notes

Uses flibitijibibo's Linux build of Serious Sam 2 with the game data from the
Windows Steam release. It is a 32-bit game: it needs 32-bit OpenAL and
libXxf86misc. libXxf86misc is no longer packaged by Fedora or Debian (on Arch
it is lib32-libxxf86misc in the AUR).
