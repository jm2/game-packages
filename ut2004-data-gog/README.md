# ut2004-data-gog

Game data for Unreal Tournament 2004: Editor's Choice Edition, extracted from
the GOG installer you download yourself and installed to /opt/ut2004. Play it
with the native OldUnreal binaries from ut2004-bin.

## Building

Place these files next to the build files or in
`${TMPDIR:-/var/tmp}/linux-packages-cache/ut2004-data-gog/` before building:

- `setup_unreal_tournament_2004_1.0_(18947).exe` - GOG (lgogdownloader: unreal_tournament_2004_ece/en1installer0)
- `setup_unreal_tournament_2004_1.0_(18947)-1.bin` - GOG (lgogdownloader: unreal_tournament_2004_ece/en1installer1)

## Notes

GOG no longer sells Unreal Tournament 2004; use the installer from your GOG
library. The CD key from the GOG install script is kept in /opt/ut2004/GOG,
and the ut2004 launcher copies it to ~/.ut2004/System/CDkey on first start.
