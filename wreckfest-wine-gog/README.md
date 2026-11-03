# wreckfest-wine-gog

Wreckfest using Wine with data via GOG

Run it with `wreckfest-gog` or from the desktop menu.

This is a Windows game run by `gamelaunch` through umu-launcher (Proton) when
it is installed, otherwise system wine with your distribution's DXVK. Use
`GAMELAUNCH_RUNNER=wine wreckfest-gog` to force system wine. Prefixes and saves
live in `~/.local/share/gamelaunch/wreckfest-gog/`; the first start takes a while.

`wreckfest-gog -h` lists the available modes:

- `-m`: 64-bit Wreckfest_x64.exe (default)
- `-l`: legacy 32-bit Wreckfest.exe

## Building

Place these files next to the build files or in
`${TMPDIR:-/var/tmp}/linux-packages-cache/wreckfest-wine-gog/` before building:

- `setup_wreckfest_1.0o_(79627).exe` - GOG (lgogdownloader: wreckfest/en1installer0)
- `setup_wreckfest_1.0o_(79627)-1.bin` - GOG (lgogdownloader: wreckfest/en1installer1)
- `setup_wreckfest_1.0o_(79627)-2.bin` - GOG (lgogdownloader: wreckfest/en1installer2)
- `setup_wreckfest_1.0o_(79627)-3.bin` - GOG (lgogdownloader: wreckfest/en1installer3)
- `setup_wreckfest_1.0o_(79627)-4.bin` - GOG (lgogdownloader: wreckfest/en1installer4)
- `setup_wreckfest_1.0o_(79627)-5.bin` - GOG (lgogdownloader: wreckfest/en1installer5)
- `setup_wreckfest_1.0o_(79627)-6.bin` - GOG (lgogdownloader: wreckfest/en1installer6)
- `setup_wreckfest_1.0o_(79627)-7.bin` - GOG (lgogdownloader: wreckfest/en1installer7)
- `setup_wreckfest_1.0o_(79627)-8.bin` - GOG (lgogdownloader: wreckfest/en1installer8)

## Notes

Season Pass DLC: install wreckfest-gog-dlc1 / wreckfest-gog-dlc2, which add
their files to /opt/wreckfest-gog.
