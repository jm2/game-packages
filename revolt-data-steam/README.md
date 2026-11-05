# revolt-data-steam

The game files of Re-Volt (1999) from your Steam copy (app 287310), downloaded
with steamcmd, converted to lower-case names and installed as RVGL's
game_files pack in /opt/rvgl/packs/game_files. Play it with rvgl-bin.

## Building

Game data comes from Steam via steamcmd, using an account that owns the
game. Either set `STEAM_USER` (steamcmd asks for the password and Steam Guard
code), or download once with `tools/fetch-steam revolt-data-steam` and build offline from
the cache.

## Notes

Only the folders RVGL reads are kept: cars, edit, gallery, gfx, levels,
models and wavs (the same folders as Re-Volt I/O's game_files pack), plus the
Steam music. Steam ships the music as music/*.ogg; it is installed as
redbook/, where RVGL looks for the CD soundtrack. Steam's Windows programs,
its own settings and the Digital Extras are left out. If rvgl-soundtrack is
installed too, its music replaces Steam's (it is loaded later).

RVGL's own fixes to the original tracks and cars are in rvgl-bin's
rvgl_assets pack, which is loaded after this one.

Tested with RVGL 23.1030a1 and no other data package: RVGL loads the
frontend. Compared with revolt-data-revoltio, the Steam files lack the
reversed track variants (levels/*/reversed) and the intro's introc-j
textures.
