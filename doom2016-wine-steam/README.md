# doom2016-wine-steam

DOOM (2016) using Wine with data via Steam

Run it with `doom2016` or from the desktop menu.

This is a Windows game run by `gamelaunch` through umu-launcher (Proton) when
it is installed, otherwise system wine with your distribution's DXVK. Use
`GAMELAUNCH_RUNNER=wine doom2016` to force system wine. Prefixes and saves
live in `~/.local/share/gamelaunch/doom2016/`; the first start takes a while.

`doom2016 -h` lists the available modes:

- `-v`: Vulkan renderer (default)
- `-o`: OpenGL renderer

## Building

Game data comes from Steam via steamcmd, using an account that owns the
game. Either set `STEAM_USER` (steamcmd asks for the password and Steam Guard
code), or download once with `tools/fetch-steam doom2016-wine-steam` and build offline from
the cache.

## Notes

The Steam executables are DRM-protected; supply DRM-free `DOOMx64.exe` and
`DOOMx64vk.exe` next to the build files. `doom2016 -o` starts the OpenGL
renderer, the default is Vulkan.
