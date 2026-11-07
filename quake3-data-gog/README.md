# quake3-data-gog

Quake III Arena and Team Arena data via GOG

## Building

Place these files next to the build files or in
`${TMPDIR:-/var/tmp}/linux-packages-cache/quake3-data-gog/` before building:

- `setup_quake3_2.0.0.2.exe` - GOG (lgogdownloader: quake_iii_arena_and_team_arena/en1installer1)

## Notes

baseq3/pak0.pk3 and missionpack/pak0.pk3 for ioquake3-based engines such as
quake3e. The 1.32 point release paks (baseq3/pak1-8.pk3,
missionpack/pak1-3.pk3) come from quake3-pointrelease-data, which this
package depends on.
