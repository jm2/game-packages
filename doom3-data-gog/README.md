# doom3-data-gog

Doom 3 and Resurrection of Evil data via GOG

## Building

Place these files next to the build files or in
`${TMPDIR:-/var/tmp}/linux-packages-cache/doom3-data-gog/` before building:

- `setup_doom_3_1.3.1_(62814).exe` - GOG (lgogdownloader: doom_3_classic/en1installer0)
- `setup_doom_3_1.3.1_(62814)-1.bin` - GOG (lgogdownloader: doom_3_classic/en1installer1)

## Notes

GOG's original DOOM 3 (doom_3_classic, part of the DOOM 3 bundle) includes
Resurrection of Evil, so this package installs both base/*.pk4 and
d3xp/*.pk4 for dhewm3 and other Doom 3 engines.
