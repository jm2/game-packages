# quake3e

Quake3e is an improved Quake III Arena engine based on the id Software
source release, with OpenGL and Vulkan renderers, <https://github.com/ec-/Quake3e>.
This package builds a dated upstream release from source.

## Game data

The engine runs from `/opt/quake3` and uses it as its base directory
(`fs_basepath`), so it finds the data the `quake3-data-*` packages install:

- `quake3-data-gog` (Quake III Arena and Team Arena from GOG), or
  `quake3-data-steam` plus `quake3-ta-data-steam` (Steam): `baseq3/pak0.pk3`
  and `missionpack/pak0.pk3`.
- `quake3-pointrelease-data`, pulled in by those packages: the 1.32 point
  release paks (`baseq3/pak1-8.pk3`, `missionpack/pak1-3.pk3`), which pure
  servers require.

You can also copy `pak0.pk3` from a CD into `/opt/quake3/baseq3` yourself.
`+set fs_basepath <dir>` points the engine at another install (the folder
that contains `baseq3/`); the renderer libraries are still loaded from
`/opt/quake3`.

## Running

- `quake3e`: the client. The "Quake III: Team Arena" menu entry runs
  `quake3e +set fs_game missionpack` and needs Team Arena's data.
- `quake3e-server` (alias `quake3e.ded`): the dedicated server.
  `quake3e-server.service` runs it as a dynamic system user with its state in
  `/var/lib/quake3e-server`; put the server settings and the first map in
  `/var/lib/quake3e-server/.q3a/baseq3/server.cfg`.

The OpenGL renderer is the default. `\cl_renderer vulkan` followed by
`\vid_restart` switches to the Vulkan one, which needs a Vulkan driver.

Settings, downloads and mods go to `~/.q3a`.
