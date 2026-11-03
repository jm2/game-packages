# kisakcod-bin

KisakCOD is a native 64-bit reimplementation of the Call of Duty 4: Modern
Warfare (1.8) multiplayer client and dedicated server
(<https://github.com/jm2/kisakcod>). This package is its prebuilt beta
release. It contains no game data.

## Game data

KisakCOD needs your own Steam copy of Call of Duty 4 (1.8): `main/`, `zone/`
and the localization files. Install `cod4-data-steam` (provides `cod4-data`),
which puts the Steam tree in `/opt/cod4`, or point the launcher elsewhere:

    KISAKCOD_COD4_PATH=/path/to/cod4 kisakcod
    kisakcod +set fs_basepath /path/to/cod4

Retail files copied or linked into `~/.config/kisakcod` are found too, and
are searched before `fs_basepath`.

## Running

- `kisakcod`: the multiplayer client. It renders through dxvk-native and
  needs a Vulkan driver.
- `kisakcod-dedi`: the dedicated server. `server.cfg` and logs live in
  `~/.config/kisakcod`.

Profiles, settings and downloads are kept in `~/.config/kisakcod`
(`$XDG_CONFIG_HOME/kisakcod`); nothing is written to `/opt`.

The engine and its bundled runtime are in `/opt/kisakcod`.
