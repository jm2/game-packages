# trine3-gog

Trine 3: The Artifacts of Power (native Linux) with data via GOG

Run it with `trine3` or from the desktop menu.

## Building

Place these files next to the build files or in
`${TMPDIR:-/var/tmp}/linux-packages-cache/trine3-gog/` before building:

- `gog_trine_3_the_artifacts_of_power_2.2.0.4.sh` - GOG (lgogdownloader: trine_3_the_artifacts_of_power/en3installer4)

## Notes

libpng12 is only available on Arch (lib32-libpng12/libpng12 from the AUR); on
Fedora/Debian provide it yourself if the game reports it missing.
