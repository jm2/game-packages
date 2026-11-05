# simcity-3000-gog

SimCity 3000 Unlimited (Loki Linux port) with data via GOG

Run it with `simcity3000` or from the desktop menu.

## Building

Place these files next to the build files or in
`${TMPDIR:-/var/tmp}/linux-packages-cache/simcity-3000-gog/` before building:

- `setup_simcity_3000_unlimited_2.0.949(a)_ddrawfix_(77026).exe` - GOG (lgogdownloader: simcity_3000/en1installer0)

## Notes

Runs Loki's native SimCity 3000 Unlimited 2.0a with the GOG data. Sound uses
OSS: enable the OSS proxy daemon with `sudo systemctl enable --now osspd`.
`apps/sc3u.exe` is GOG's patched Windows executable (unused by the Linux
binary, but it allows higher resolutions if you run the game under Wine).
libSimBABld.so is removed because it breaks startup; the building architect
tool may not work.
