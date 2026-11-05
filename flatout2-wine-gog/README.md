# flatout2-wine-gog

FlatOut 2 using Wine with data via GOG

Run it with `flatout2` or from the desktop menu.

This is a Windows game run by `gamelaunch` through umu-launcher (Proton) when
it is installed, otherwise system wine with your distribution's DXVK. Use
`GAMELAUNCH_RUNNER=wine flatout2` to force system wine. Prefixes and saves
live in `~/.local/share/gamelaunch/flatout2/`; the first start takes a while.

## Building

Place these files next to the build files or in
`${TMPDIR:-/var/tmp}/linux-packages-cache/flatout2-wine-gog/` before building:

- `setup_flatout_2_1.0_(26697).exe` - GOG (lgogdownloader: flatout_2/en1installer0)
- `setup_flatout_2_1.0_(26697)-1.bin` - GOG (lgogdownloader: flatout_2/en1installer1)
