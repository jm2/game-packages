# yamagi-quake2-rogue

The Quake II Mission Pack 2 (Ground Zero) game library for Yamagi Quake II
(<https://github.com/yquake2/rogue>), built from the latest stable release.

## Game data

The game data is read from `/usr/share/games/quake2/rogue`, which
`quake2-data-gog` and `quake2-data-steam` install together with the base
game. Another install can be given with `-datadir /path/to/quake2` (the
folder containing `baseq2/` and `rogue/`).

## Running

`yamagi-quake2-rogue` starts the engine with `+set game rogue`; the same
works for `yamagi-q2ded`. The game library is installed in
`/usr/lib/yamagi-quake2/rogue`.

Debian's `yamagi-quake2-core` already contains this game library, so this
package has no Debian build.
