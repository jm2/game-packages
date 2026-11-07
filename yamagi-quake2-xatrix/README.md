# yamagi-quake2-xatrix

The Quake II Mission Pack 1 (The Reckoning) game library for Yamagi Quake II
(<https://github.com/yquake2/xatrix>), built from the latest stable release.

## Game data

The game data is read from `/usr/share/games/quake2/xatrix`, which
`quake2-data-gog` and `quake2-data-steam` install together with the base
game. Another install can be given with `-datadir /path/to/quake2` (the
folder containing `baseq2/` and `xatrix/`).

## Running

`yamagi-quake2-xatrix` starts the engine with `+set game xatrix`; the same
works for `yamagi-q2ded`. The game library is installed in
`/usr/lib/yamagi-quake2/xatrix`.

Debian's `yamagi-quake2-core` already contains this game library, so this
package has no Debian build.
