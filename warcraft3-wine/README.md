# warcraft3-wine

Warcraft III Classic (1.27) using Wine

Run it with `warcraft3` or from the desktop menu.

This is a Windows game run by `gamelaunch` through umu-launcher (Proton) when
it is installed, otherwise system wine with your distribution's DXVK. Use
`GAMELAUNCH_RUNNER=wine warcraft3` to force system wine. Prefixes and saves
live in `~/.local/share/gamelaunch/warcraft3/`; the first start takes a while.

`warcraft3 -h` lists the available modes:

- `-x`: The Frozen Throne (default)
- `-o`: Reign of Chaos

## Building

Place these files next to the build files or in
`${TMPDIR:-/var/tmp}/linux-packages-cache/warcraft3-wine/` before building:

- `warcraft3.zip` - Zip your patched 'Warcraft III' folder as warcraft3.zip; see README.md.

## Notes

Build from your own installed copy: zip the patched (1.27) `Warcraft III`
folder as `warcraft3.zip`. The Movies folder is disabled because the intro
movies crash the game under Wine.
