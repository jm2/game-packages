# doom2016-wine-gog

DOOM (2016) using Wine with data via GOG

Run it with `doom2016` or from the desktop menu.

This is a Windows game run by `gamelaunch` through umu-launcher (Proton) when
it is installed, otherwise system wine with your distribution's DXVK. Use
`GAMELAUNCH_RUNNER=wine doom2016` to force system wine. Prefixes and saves
live in `~/.local/share/gamelaunch/doom2016/`; the first start takes a while.

`doom2016 -h` lists the available modes:

- `-v`: Vulkan renderer (default)
- `-o`: OpenGL renderer

## Building

Place these files next to the build files or in
`${TMPDIR:-/var/tmp}/linux-packages-cache/doom2016-wine-gog/` before building:

- `setup_doom_(2016)_20240321-110145-gentle-wolf_(80244).exe` - GOG (lgogdownloader: doom_2016/en1installer0)
- `setup_doom_(2016)_20240321-110145-gentle-wolf_(80244)-1.bin` - GOG (lgogdownloader: doom_2016/en1installer1)
- `setup_doom_(2016)_20240321-110145-gentle-wolf_(80244)-2.bin` - GOG (lgogdownloader: doom_2016/en1installer2)
- `setup_doom_(2016)_20240321-110145-gentle-wolf_(80244)-3.bin` - GOG (lgogdownloader: doom_2016/en1installer3)
- `setup_doom_(2016)_20240321-110145-gentle-wolf_(80244)-4.bin` - GOG (lgogdownloader: doom_2016/en1installer4)
- `setup_doom_(2016)_20240321-110145-gentle-wolf_(80244)-5.bin` - GOG (lgogdownloader: doom_2016/en1installer5)
- `setup_doom_(2016)_20240321-110145-gentle-wolf_(80244)-6.bin` - GOG (lgogdownloader: doom_2016/en1installer6)
- `setup_doom_(2016)_20240321-110145-gentle-wolf_(80244)-7.bin` - GOG (lgogdownloader: doom_2016/en1installer7)
- `setup_doom_(2016)_20240321-110145-gentle-wolf_(80244)-8.bin` - GOG (lgogdownloader: doom_2016/en1installer8)
- `setup_doom_(2016)_20240321-110145-gentle-wolf_(80244)-9.bin` - GOG (lgogdownloader: doom_2016/en1installer9)
- `setup_doom_(2016)_20240321-110145-gentle-wolf_(80244)-10.bin` - GOG (lgogdownloader: doom_2016/en1installer10)
- `setup_doom_(2016)_20240321-110145-gentle-wolf_(80244)-11.bin` - GOG (lgogdownloader: doom_2016/en1installer11)
- `setup_doom_(2016)_20240321-110145-gentle-wolf_(80244)-12.bin` - GOG (lgogdownloader: doom_2016/en1installer12)
- `setup_doom_(2016)_20240321-110145-gentle-wolf_(80244)-13.bin` - GOG (lgogdownloader: doom_2016/en1installer13)
- `setup_doom_(2016)_20240321-110145-gentle-wolf_(80244)-14.bin` - GOG (lgogdownloader: doom_2016/en1installer14)
- `setup_doom_(2016)_20240321-110145-gentle-wolf_(80244)-15.bin` - GOG (lgogdownloader: doom_2016/en1installer15)
- `setup_doom_(2016)_20240321-110145-gentle-wolf_(80244)-16.bin` - GOG (lgogdownloader: doom_2016/en1installer16)

## Notes

The GOG build is DRM-free (campaign only; GOG does not include multiplayer or
SnapMap). `doom2016 -o` starts the OpenGL renderer; the default is Vulkan.
