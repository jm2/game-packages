# prey2006-git

Prey2006 is a source port of Prey (2006): the Prey SDK game code integrated
into a dhewm3-based Doom 3 GPL engine,
<https://github.com/glKarin/Prey2006> (a fork of
FriskTheFallenHuman/Prey2006). Upstream warns that it is unfinished:
the single-player game has known blockers and multiplayer is untested.

## Game data

The engine's base path is `/opt/prey`. It needs the retail
`base/pak000.pk4` to `base/pak004.pk4` there: install `prey-data-steam`
(virtual `prey-data`), or copy the `.pk4` files from your own install into
`/opt/prey/base`. The original game's `gamex86.dll` is not used. This
package adds its own game library (`game<cpu>.so`) and the port's
replacement assets to the same directory. `+set fs_basepath <dir>` points
the engine at another install (the folder that contains `base/`).

## Running

- `prey06`: the game ("Prey (2006)" in the menu).
- `prey06ded`: the dedicated server.

Settings go to `~/.config/prey06`, saves to `~/.local/share/prey06`.

## Licence

The repository has no top-level licence file. The engine is the Doom 3 GPL
source release (GPL-3.0-or-later with id Software's additional terms, text
in `.github/COPYING.txt`, shipped here as the licence). The game code under
`neo/Prey` and `neo/preyengine`, and the assets under `base/` (GUIs,
materials, models, scripts, the SDK's tutorial maps and the logo videos),
come from the Prey SDK and the Prey game by Human Head Studios and 3D
Realms. The SDK was released under its own end-user licence agreement, not
the GPL, and the repository includes neither that text nor any other
licence for these files. The package
licence is therefore `GPL-3.0-or-later AND LicenseRef-Prey-SDK`
(`LicenseRef-Prey-SDK.txt` explains it), and these
packages are only built locally, never published.

## Versions

The PKGBUILD follows the main branch. The RPM and Debian packages build a
pinned commit (`commit` in the spec, `COMMIT` in `debian/rules`, and
`debian/sources`); bump them together.
