# dhewm3

dhewm3 is a Doom 3 GPL source port with SDL3, OpenAL and 64-bit support,
<https://dhewm3.org/>. This package builds the engine, the dedicated server
and the game libraries for Doom 3 (`base`) and Resurrection of Evil (`d3xp`).

## Game data

The engine's base path is `/opt/doom3`: it looks for the retail
`base/*.pk4` and `d3xp/*.pk4` files there.

- Doom 3: `doom3-data-steam` or `doom3-data-gog` (virtual `doom3-data`).
- Resurrection of Evil: `doom3xp-data-steam`, or `doom3-data-gog`, which
  includes it (virtual `doom3xp-data`).

You can also copy the `.pk4` files from your own install into
`/opt/doom3/base` and `/opt/doom3/d3xp`. `+set fs_basepath <dir>` points
the engine at another install (the folder that contains `base/`).

## Running

- `dhewm3`: Doom 3. The "Doom 3: Resurrection of Evil" menu entry runs
  `dhewm3 +set fs_game d3xp`.
- `dhewm3ded`: the dedicated server.

Settings go to `~/.config/dhewm3`, saves and downloads to
`~/.local/share/dhewm3`. See `Configuration.md` in this directory for the
engine's options.

## Debian

Debian ships dhewm3 itself (`dhewm3`, `dhewm3-doom3`, `dhewm3-d3xp` in
contrib), so this directory has no Debian packaging. Debian's build looks
for data in `/usr/share/games/doom3`, not `/opt/doom3`; run it with
`+set fs_basepath /opt/doom3` to use the data packages from this repository.
