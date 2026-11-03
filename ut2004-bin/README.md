# ut2004-bin

Native Linux binaries for Unreal Tournament 2004 from OldUnreal's community
patch (3374), installed to `/opt/ut2004`. The game data is not included:
install one of

- `ut2004-data-gog` (GOG installer you download yourself),
- `ut2004-data-steam` (Steam, via steamcmd),
- `ut2004-data-archiveorg` (the free ECE DVD image hosted by OldUnreal).

Start the game with `ut2004` or from the desktop menu. Arguments are passed
to the game, e.g. `ut2004 -log`.

Settings, saves, logs and downloaded content live in `~/.ut2004/System`; the
game creates `UT2004.ini` and `User.ini` there on its first start. For GOG
data the CD key is copied from the GOG install script into
`~/.ut2004/System/CDkey` if that file does not exist yet.

SDL3 and OpenAL come from the distribution; OldUnreal's bundled copies are
not installed. The bundled LLVM `libomp.so.5` is kept.

## Upgrading from ut2004-gog

`ut2004-gog` (binaries and GOG data in one package) is retired. This package
replaces it; install `ut2004-data-gog` alongside it for the data. Your
`~/.ut2004` directory is kept as is.

If you used earlier versions of these packages, `~/.ut2004/System` may hold
copies of `Default.ini`, `DefUser.ini`, `DefUnrealEd.ini` and
`CacheRecords.ucl` that the old launcher copied there. They are not needed
and can be deleted.
