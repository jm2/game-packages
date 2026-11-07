# yamagi-quake2

Yamagi Quake II (<https://www.yamagi.org/quake2/>) is an enhanced Quake II
engine focused on single player: the gameplay and graphics stay the same,
but many bugs are fixed and it runs well on modern systems. This package
builds the latest stable release from source with the OpenGL 1.4, OpenGL
3.2, OpenGL ES 3 and software renderers. The Vulkan renderer is in
`yamagi-quake2-ref_vk`.

## Game data

The engine is built with `SYSTEMWIDE` and reads the game data from
`/usr/share/games/quake2`: `baseq2/pak0.pak` - `pak2.pak` (plus `video/`),
and `xatrix/`, `rogue/`, `ctf/` for the mission packs and CTF.
`quake2-data-gog` or `quake2-data-steam` installs it there. It also looks in
`~/.local/share/YamagiQ2` (or `~/.yq2` if that exists), and
`-datadir /path/to/quake2` points it at another install (the folder that
contains `baseq2/`).

The 2023 remaster's data (`rerelease/`) is not supported; use the original
`baseq2` paks.

## Running

- `yamagi-quake2`: the game. The renderer is chosen in the video menu or
  with `+set vid_renderer gl1|gl3|gles3|soft|vk`.
- `yamagi-q2ded`: the dedicated server. `yamagi-q2ded.service` runs it as a
  dynamic system user with its state in `/var/lib/yamagi-q2ded`; add the
  map and settings with `systemctl edit yamagi-q2ded`.
- Mission packs and CTF: `yamagi-quake2-xatrix` (The Reckoning),
  `yamagi-quake2-rogue` (Ground Zero) and `yamagi-quake2-ctf` add the game
  libraries and launchers.

Settings and saves go to `~/.local/share/YamagiQ2`. The binaries, upstream's
`yq2.cfg` defaults and fixed map entity lists (`.ent`) are in
`/usr/lib/yamagi-quake2`.

## Distribution packages

- Debian ships the same release as `yamagi-quake2` / `yamagi-quake2-core`
  (with the mission packs and CTF built in) in testing and unstable, also
  built with `SYSTEMWIDE`, so it reads `/usr/share/games/quake2` too. This
  repository has no Debian build of the engine or the addons; only
  `yamagi-quake2-ref_vk` is built for Debian.
- Fedora's `quake2` package is an older release that reads its data from
  `/usr/lib64/games/quake2` and has no mission packs. It can be installed
  alongside this one (`quake2` vs `yamagi-quake2` commands).
