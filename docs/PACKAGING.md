# Packaging conventions

Every package directory builds three ways: `PKGBUILD` (Arch), `<name>.spec`
(Fedora/RPM, built locally with rpmbuild) and `debian/` (Debian/Ubuntu, built
locally with dpkg-buildpackage). Nothing here can go to Copr/OBS/PPA: most
packages contain proprietary game data or prebuilt third-party binaries.

## Two kinds of package

1. **Generated** (`package.toml` present): game and game-data packages. Edit
   `package.toml` (and any `extra_files` it lists), then run
   `tools/gen.py <dir>`. It writes `build.sh`, `PKGBUILD`, the spec,
   `debian/*`, `README.md`, and for games `<id>.conf` and `<id>.desktop`. Never
   hand-edit generated files; `tools/gen.py --check` fails in CI if they drift.
   The shared logic is in `tools/pkgtool.sh` (copied into each `build.sh`).
   The schema is documented in `tools/gen.py`; copy an existing package of
   the same family as a starting point.
2. **Hand-maintained** (no `package.toml`): engines, source ports, the shared
   runtime packages and non-game software. When the install logic is more
   than a few lines, put it in a shared `install.sh` in the package directory
   that all three formats call (see `gbe-fork-bin/`, `xlln-bin/`) so the formats
   can't drift.

## Common rules

- Maintainer: `John-Michael Mulesa <jmulesa at gmail dot com>` (PKGBUILD
  comment), `John-Michael Mulesa <jmulesa@gmail.com>` (spec/debian).
- Licenses: SPDX identifiers (`GPL-2.0-or-later`, `LicenseRef-Proprietary`
  for game data, ...). No bare `GPL` or `custom`.
- Quote `"${pkgdir}"`/`"${srcdir}"`; prefer `install -Dm644 file -t dir/`.
- Checksums: real `sha256sums` for every file that has fixed content; `SKIP`
  only for VCS sources. Local files are checksummed too.
- Icons go to `/usr/share/icons/hicolor/<size>/apps/`, not `pixmaps`.
- Desktop files: `Type=Application`, `Exec=<command>` (no absolute path),
  `Categories=Game;...` (no `Application` category). They must pass
  `desktop-file-validate`.
- No world-writable install dirs (`chmod o+w`/`777`/`666`). Games that write
  next to their binaries use gamelaunch's per-user overlay (`WRITABLE=1`).
- No `.install` echo banners: user-facing notes go in the package README
  (`/usr/share/doc/<pkg>/README.md`), which RPM and Debian also ship.
- Drop `i686` from `arch` (Arch has no i686 port); 32-bit runtime libraries are
  `lib32-*` (Arch), `foo(x86-32)` (Fedora) and `foo:i386` (Debian).
- Prebuilt binaries: `options=('!strip' '!debug')`, `%global debug_package %{nil}`
  plus `__provides_exclude_from`/`__requires_exclude_from` for private library
  dirs, and empty `override_dh_strip override_dh_dwz override_dh_shlibdeps` in
  `debian/rules`.
- Large payloads: `%global _binary_payload w3.zstdio` and
  `dh_builddeb -- -Zzstd -z1`. A .deb can't exceed about 9.3 GiB (ar header
  limit), so generated packages with more data than that set `[deb] parts = N`
  to split it into `<name>-dataN` packages.
- Debian source format is `3.0 (native)`; upstream files are listed in
  `debian/sources` and fetched by `debian/fetch-sources` (master copy:
  `tools/debian-fetch-sources`), which `debian/rules` calls before building.
- `gbe-fork-bin`: Goldberg is never vendored. Generated packages declare
  `[gbe] libs = [...]`; the original library's interfaces are recorded at build
  time and the library is replaced by a symlink into `/opt/gbe-fork` (Windows
  builds; umu's pressure-vessel container hides `/usr`) or `/usr/lib/gbe-fork`
  (Linux builds).
- `xlln-bin`: GFWL games set `[xlln] enabled = true`; gamelaunch links
  XLiveLessNess into the per-user game directory.

## Versions of Steam packages

Steam packages have no hand-written version. At build time pkgtool reads
the Steam build ID from steamcmd's `appmanifest` and the game's own version
from the download:

- Unity games: the bundle version in `*_Data/globalgamemanagers` (their exe
  carries the Unity engine version, so it is never used);
- other Windows games: the FileVersion of the main exe (`[launcher] exe`).

The version is `<game version>.b<build ID>` (`2.57.1.b25333770`), or
`0.b<build ID>` when the game carries no version. The build ID makes every
Steam update an upgrade even when the game's own version doesn't change.
Arch sets it in `pkgver()`, Debian through `dh_gencontrol -v`, and the RPM
spec computes it before the build from the cached download, so RPM builds of
Steam packages need `tools/fetch-steam` first. GOG/Humble/data-url packages
keep the version in `package.toml`, which their pinned installer checksums
make exact.

## aarch64

- Native arm64 upstream binaries or source builds: list `aarch64` in all three
  formats (Arch here means Arch Linux ARM users running makepkg).
- Generated game packages contain x86 code. On Fedora aarch64 it runs through
  FEX (`fex-emu`, with `fex-emu-rootfs-fedora`, `fex-emu-thunks` and `muvm`
  recommended); on Debian arm64 through `fex-emu | box64`. gamelaunch checks
  that binfmt emulation is registered and wraps games in `muvm` on 16K-page
  systems. Wine games require umu-launcher there (the distros' arm64 Wine
  can't run x86 Windows programs). x86 library dependencies of native games
  apply to x86_64 only.
- Per package: `aarch64 = false` opts out (Feral ports, which need AUR-only x86
  libraries); `native32 = true` marks 32-bit x86 native games, which FEX can
  run but box64 can't, so they get no Debian arm64 build.
- Arch PKGBUILDs of emulated packages stay x86_64: Arch has no aarch64 port and
  Arch Linux ARM packages neither FEX nor box64.
- No emulation for engines that have (or should get) source ports: build them
  natively instead (quake2rtx is source-only; daikatana-bin was dropped).

## Testing

`tools/container-build <dir> [arch|fedora|debian|all] [extra deps]` builds
in clean podman containers and runs namcap / rpmlint / lintian. Game packages
need their data: point `PT_CACHE` at a cache directory (real data from
`tools/fetch-steam`, or a fake tree for build-logic tests), set
`LOCAL="gamelaunch xlln-bin gbe-fork-bin"` to preinstall locally built
dependencies, and `NODEPS=1` on Arch where makedepends are AUR-only (steamcmd).

## Building the repos

`tools/build-all` builds every package for Arch and Fedora, one at a time,
and hands them to `tools/promote`, which moves them into crossdock's incoming
directories and removes the old versions. It can be rerun after a failure.
Fedora builds target one release (`FEDORA_RELEASE`, default 45), and a single
repo serves them all: only native packages depend on the release at all.

Set `TMPDIR`, `PT_CACHE` and `OUT` first, on a disk with room for the largest
game several times over. podman needs `/etc/subuid` and `/etc/subgid` entries
for the user.
