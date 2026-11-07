# rbdoom-3-bfg-gi-data

The two data packs from RBDOOM-3-BFG's release archive that are not built
from source: _rbdoom_global_illumination_data.pk4, the baked light grids and
environment probes of the Doom 3 BFG campaign maps, and _rbdoom_blood.pk4,
the reflective blood materials those probes were baked for. Installed next
to the retail data in /usr/share/games/doom3bfg/base; extracted at build
time from the upstream Windows release archive (1.6 GB download).

## Notes

Without this package the engine still runs: maps without baked light grids
fall back to plain ambient lighting and generic environment probes.

The packs are upstream's own output (bakeLightGrids/bakeEnvironmentProbes
over id's maps), distributed only inside the Windows release archive. The
archive's LICENSE.md is the engine's GPL-3.0; the release names no separate
terms for these generated files, so the package is marked
LicenseRef-Proprietary like the retail data it is derived from.
