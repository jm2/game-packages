# unreal-tournament-data-gog

Game data for Unreal Tournament: Game of the Year Edition, extracted from the
GOG installer you download yourself and installed to /opt/unreal-tournament.
Play it with the native OldUnreal binaries from unreal-tournament-bin.

## Building

Place these files next to the build files or in
`${TMPDIR:-/var/tmp}/linux-packages-cache/unreal-tournament-data-gog/` before building:

- `setup_ut_goty_2.0.0.5.exe` - GOG (lgogdownloader: unreal_tournament_goty/en1installer0)

## Notes

GOG no longer sells Unreal Tournament; use the installer from your GOG
library (GOG names it setup_ut_goty_2.0.0.5.exe; older copies of this
package called it setup_unreal_tournament_goty_2.0.0.5.exe, so rename it if
you kept that one).
