# trine2-gog

Trine 2: Complete Story (native Linux) with data via GOG

Run it with `trine2` or from the desktop menu.

## Building

Place these files next to the build files or in
`${TMPDIR:-/var/tmp}/linux-packages-cache/trine2-gog/` before building:

- `gog_trine_2_complete_story_2.0.0.5.sh` - GOG (lgogdownloader: trine_2_complete_story/en3installer2)

## Notes

libpng12 is only available on Arch (lib32-libpng12/libpng12 from the AUR); on
Fedora/Debian provide it yourself if the game reports it missing.
