# gamelaunch game config (`/usr/share/gamelaunch/games/<id>.conf`)

A bash fragment of plain assignments, sourced by `gamelaunch`. A copy in
`/etc/gamelaunch/games/<id>.conf` takes precedence (local overrides).

| Key | Default | Meaning |
|---|---|---|
| `GAME_NAME` | id | Human-readable name for messages. |
| `GAME_TYPE` | `wine` | `wine` or `native`. |
| `GAME_DIR` | – | Install directory, e.g. `/opt/dirt2`. Required. `@prefix`: the program lives inside the Wine prefix (a self-updating client such as Battle.net), and `GAME_EXE` and `GAME_WORKDIR` are relative to the prefix's `drive_c`. |
| `GAME_EXE` | – | Program relative to `GAME_DIR`. |
| `GAME_WORKDIR` | dir of exe | Working directory relative to `GAME_DIR`. |
| `GAME_ARGS=( )` | – | Arguments always passed. |
| `VARIANTS=( "flag\|exe\|args\|description" )` | – | Alternate executables chosen with `-flag` (replaces the old getopts blocks). An empty exe keeps `GAME_EXE`. |
| `DEFAULT_VARIANT` | – | Flag used when none is given. |
| `WRITABLE` | `0` | `1`: run from a per-user overlay (real dirs + symlinks into `GAME_DIR`) so the game can create files next to its binaries. |
| `WRITABLE_COPY=( globs )` | – | Files the game rewrites in place; copied (not linked) into the overlay on first use. |
| `NATIVE_ENV=( "K=V" )` | – | Exported for native games. |
| `DXVK` | `1` | Wine backend: link the distro DXVK into the prefix and override d3d8/9/10core/11/dxgi. Ignored under umu (Proton ships DXVK). |
| `UMU_ID` | `umu-default` | umu GAMEID (`umu-<steam appid>` picks up protonfixes). |
| `WINE_ARCH` | `win64` | WINEARCH for new wine-backend prefixes. |
| `WINE_DLL_OVERRIDES` | – | Extra `WINEDLLOVERRIDES` entries. |
| `WINE_ENV=( "K=V" )` | – | Exported for Wine games (e.g. `WINE_LARGE_ADDRESS_AWARE=1`). |
| `PREREQS=( "name\|exe args" )` | – | Run once per prefix from the game root (bundled redistributables, offline). `name\|winetricks:verb...` runs winetricks (umu's bundled copy under umu, system winetricks under wine). |
| `XLLN` | `0` | Game uses XLiveLessNess (`xlive.dll` from xlln-bin); forces `xlive=n`. Combine with `WRITABLE=1` and `WRITABLE_COPY=("XLiveLessNess/*.ini")`. |
| `WINE_PRELOAD=( paths )` | – | Linux libraries added to `LD_PRELOAD` for the Wine/Proton processes (keep them under `/opt` so umu's container sees them). Missing files are skipped. `GAMELAUNCH_NO_PRELOAD=1` turns this off for one run. |
| `WINE_PRELOAD_VARIANTS=( flags )` | all | Only preload for these variants (e.g. not for a dedicated-server variant). |
| `NEEDS_X86_32` | `0` | `1`: a 32-bit x86 native program; on non-x86 hosts it needs FEX (box64 can't run it). |
| `WINE_USER` | – | `hostname`: run as a Windows user named after the machine's short host name (generic names such as `localhost` get `player-<random hex>`), for games that derive a LAN identity from the username. Needs the wine backend, which is then preferred; Proton always reports `steamuser`. `GAMELAUNCH_USER=<name>` overrides the name for one run, for any Wine game. |
| `BOOTSTRAP_URL` | – | With `GAME_DIR=@prefix`: if `GAME_EXE` is missing from the prefix, download this installer (with curl or wget) and run it once. The client then updates itself. Each backend has its own prefix, so switching backend installs the client again. |
| `BOOTSTRAP_FILE` | last URL component | File name to save the installer as. |
| `BOOTSTRAP_ARGS=( )` | – | Arguments for the installer. |
| `LEGACY_DIRS=( paths )` | – | Old prefix locations (e.g. `~/.dirt2/wine`) adopted once by the wine backend. |

Per-user state: `${XDG_DATA_HOME:-~/.local/share}/gamelaunch/<id>/` with
`prefix-umu/`, `prefix-wine/`, `userdata/` (Documents, AppData, Saved Games
shared by both prefixes) and `game/` (the overlay).

On non-x86 hosts (aarch64) x86 code runs through FEX or box64 via
binfmt_misc; on systems with non-4K pages (Apple Silicon) gamelaunch wraps
the game in `muvm --`. `GAMELAUNCH_WRAPPER` overrides the wrapper.

Goldberg player name: for a game with a `steam_settings` folder (gbe-fork),
gamelaunch sets `account_name` in gbe's global user settings to the machine's
short host name in lower case. Wine games keep that file in
`userdata/AppData/Roaming/GSE Saves/settings/configs.user.ini`, native games in
`${XDG_DATA_HOME:-~/.local/share}/GSE Saves/settings/configs.user.ini`. The
name is rewritten on each start while it is unset, gbe's default `gse orca`,
or the name gamelaunch last wrote (recorded in `account_name.gamelaunch` next
to the file), so it follows a renamed host. A name you set yourself is kept.
Generic host names such as `localhost` are not used. `GAMELAUNCH_NO_GBE_NAME=1`
turns this off.
