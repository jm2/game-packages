# openq4-bin

openQ4 (<https://github.com/themuffinator/openQ4>) replaces the Quake 4
engine and game binaries with a GPL engine and SDK-licensed game modules.
This package is its prebuilt binary release, plus the Quake 4 1.4.2 patch
paks (pak013.pk4 - pak022.pk4) from id Software's Linux point release.

## Game data

openQ4 needs the retail Quake 4 data (pak001.pk4 - pak012.pk4 and
zpak_<language>.pk4). Either install `quake4-data-gog` or
`quake4-data-steam` (both install to `/opt/quake4`), or keep a Steam/GOG
install of Quake 4, which openQ4 detects automatically.

Another install can be selected with

    OPENQ4_QUAKE4_PATH=/path/to/quake4 openq4
    openq4 +set fs_basepath /path/to/quake4

(the folder containing `q4base/`).

## Running

- `openq4`: the game
- `openq4-steamdeck`: the Steam Deck profile
- `openq4-dedicated`: the dedicated server

Saves, configs and logs are written to `~/.local/share/openq4`.

The Quake 4 patch paks are covered by id Software's license, shipped as
`Quake4-License.txt` with the package's license files.
