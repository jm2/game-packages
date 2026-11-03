# trine-gog

Trine Enchanted Edition (native Linux) with data via GOG

Run it with `trine` or from the desktop menu.

## Building

Place these files next to the build files or in
`${TMPDIR:-/var/tmp}/linux-packages-cache/trine-gog/` before building:

- `gog_trine_enchanted_edition_2.0.0.2.sh` - GOG (lgogdownloader: trine_enchanted_edition/en3installer1)

## Notes

libpng12 is only available on Arch (lib32-libpng12/libpng12 from the AUR); on
Fedora/Debian provide it yourself if the game reports it missing.
