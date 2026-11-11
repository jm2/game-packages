# openetqw-bin

openETQW is an open-source engine for Enemy Territory: QUAKE Wars 1.5
(<https://github.com/jm2/openETQW>). This package is its prebuilt release:
the client, the dedicated server, the game module (id Software's ET:QW SDK
code, under the SDK EULA) and the engine's shaders, in `/opt/openetqw`.

## Game data

openETQW needs the retail ET:QW data patched to 1.5. This package already
includes the 1.5 patch paks (`pak005.pk4` - `pak008.pk4` and the English
`zpak_english001-003.pk4`), extracted from id Software's Linux 1.5 client
patch. You still need the base game's `base/pak000.pk4` - `pak004.pk4`,
`zpak_<language>000.pk4`, `megatextures/` and `video/`:

- install `etqw-data-steam` (provides `etqw-data`), which puts them in
  `/opt/etqw`, or
- point it at an install yourself:

      OPENETQW_BASEPATH=/path/to/etqw openetqw
      openetqw +set fs_basepath /path/to/etqw

The launcher runs the engine with `/opt/openetqw` as `fs_basepath` and the
retail folder as `fs_cdpath`. The engine searches `fs_basepath` first, so the
1.5 patch paks take priority over the retail `pak000-pak004`. If the retail
folder were `fs_basepath` instead, its old scripts would win and maps would
fail to load. Without any of the above, openETQW searches Steam, retail and
Wine installs on its own and saves the folder in `basepath.txt` (see below);
the launcher uses that folder from the next start.

The engine checks at start-up that the official 1.5 paks are present and
unmodified.

## Running

- `openetqw`: the client (Vulkan, with OpenGL as a fallback).
- `openetqw-dedicated`: the dedicated server.

Configs, logs and the shader cache go to `~/.local/share/openetqw`
(`$XDG_DATA_HOME/openetqw`); nothing is written to `/opt`. If no data is
found, the client asks for the ET:QW folder (with zenity or kdialog) and
stores the answer in `basepath.txt` there.
