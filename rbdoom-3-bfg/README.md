# rbdoom-3-bfg

RBDOOM-3-BFG is Robert Beckebans' modernized Doom 3 BFG Edition engine
(Vulkan renderer through NVRHI, PBR, baked global illumination, soft
shadows, retro rendering modes), <https://github.com/RobertBeckebans/RBDOOM-3-BFG>.
This package builds the engine from the release tag.

## Game data

The engine needs the retail `base/` directory of Doom 3 BFG Edition in
`/usr/share/games/doom3bfg/base`. Install `doom3bfg-data-steam` or
`doom3bfg-data-gog` for it. The package adds the engine's own files to
that directory: the SPIR-V shaders compiled during the build
(`renderprogs2/spirv`), configs, entity definitions, extra map entities,
materials and editor textures.

Upstream's Windows release archive also has two data packs that are not
built from source and are not included here:

- `_rbdoom_global_illumination_data.pk4` (1.4 GB): the baked light grids
  and environment probes of the campaign maps (the engine's
  `bakeLightGrids`/`bakeEnvironmentProbes` output).
- `_rbdoom_blood.pk4`: extra blood decals.

To use them, copy them from the release archive into
`~/.local/share/rbdoom3bfg/base/`.

## Running

- `rbdoom-3-bfg` (also `RBDoom3BFG`): the game. It needs a Vulkan driver.
- `rbdmap`: the standalone map compiler.

Configs, saves, screenshots and generated image caches go to
`${XDG_DATA_HOME:-~/.local/share}/rbdoom3bfg`. Files in
`~/.local/share/rbdoom3bfg/base` override the ones in
`/usr/share/games/doom3bfg/base`, and mods go next to it
(`~/.local/share/rbdoom3bfg/<mod>`, started with `+set fs_game <mod>`).

The BFG data has the strings for every language, so the game may start in
another language than you expect. Put `seta sys_lang "english"` (or
french, german, italian, japanese, spanish) into
`~/.local/share/rbdoom3bfg/base/autoexec.cfg` to choose one.
