# minimetro-hib

Mini Metro, the minimalist subway layout game by Dinosaur Polo Club, from the
DRM-free Linux build in your Humble Bundle library.

Run it with `minimetro` or from the desktop menu.

## Building

Place these files next to the build files or in
`${TMPDIR:-/var/tmp}/linux-packages-cache/minimetro-hib/` before building:

- `MiniMetro-release-57-linux.tar.gz` - Humble Bundle

## Notes

Download the Linux tarball from your Humble library and save it as
`MiniMetro-release-57-linux.tar.gz` (rename it if Humble's name differs).
Its checksum is not pinned yet: after the first successful build, copy the
sha256 of the tarball into package.toml.

Settings and saves live in `~/.config/unity3d/Dinosaur Polo Club/Mini Metro/`.
