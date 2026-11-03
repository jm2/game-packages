# grid-wine-gog

Race Driver GRID (2008) using Wine with data via GOG

Run it with `grid` or from the desktop menu.

This is a Windows game run by `gamelaunch` through umu-launcher (Proton) when
it is installed, otherwise system wine with your distribution's DXVK. Use
`GAMELAUNCH_RUNNER=wine grid` to force system wine. Prefixes and saves
live in `~/.local/share/gamelaunch/grid/`; the first start takes a while.

## Building

Place these files next to the build files or in
`${TMPDIR:-/var/tmp}/linux-packages-cache/grid-wine-gog/` before building:

- `setup_race_driver_grid_1.0_(18584).exe` - GOG (lgogdownloader: race_driver_grid/en1installer0)
- `setup_race_driver_grid_1.0_(18584)-1.bin` - GOG (lgogdownloader: race_driver_grid/en1installer1)
- `setup_race_driver_grid_1.0_(18584)-2.bin` - GOG (lgogdownloader: race_driver_grid/en1installer2)

## Notes

For better visuals set `<postprocess enabled="false" blur="false" />` in
`Documents/Codemasters/GRID/hardwaresettings/hardware_settings_config.xml`
(under `~/.local/share/gamelaunch/grid/userdata/`).
