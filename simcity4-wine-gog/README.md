# simcity4-wine-gog

SimCity 4 Deluxe Edition using Wine with data via GOG

Run it with `simcity4` or from the desktop menu.

This is a Windows game run by `gamelaunch` through umu-launcher (Proton) when
it is installed, otherwise system wine with your distribution's DXVK. Use
`GAMELAUNCH_RUNNER=wine simcity4` to force system wine. Prefixes and saves
live in `~/.local/share/gamelaunch/simcity4/`; the first start takes a while.

## Building

Place these files next to the build files or in
`${TMPDIR:-/var/tmp}/linux-packages-cache/simcity4-wine-gog/` before building:

- `setup_simcity_4_deluxe_edition_1.1.641_hotfix_(25621).exe` - GOG (lgogdownloader: simcity_4_deluxe_edition/en1installer0)

## Notes

The launcher passes `-CustomResolution:enabled -r1920x1080x32`; to use another
resolution run `simcity4 -r<width>x<height>x32` (later arguments win).
