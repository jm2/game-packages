# wreckfest-gog-dlc1

Wreckfest (GOG) - Season Pass 1

## Building

Place these files next to the build files or in
`${TMPDIR:-/var/tmp}/linux-packages-cache/wreckfest-gog-dlc1/` before building:

- `setup_wreckfest_season_pass_1_1.0o_(79627).exe` - GOG (lgogdownloader: wreckfest_season_pass_1/en1installer0)

## Notes

The installer checksum is not pinned yet: build once and copy the sha256
printed by `makepkg -g` into package.toml.
