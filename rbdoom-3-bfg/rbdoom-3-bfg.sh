#!/bin/sh
# RBDOOM-3-BFG launcher. The retail Doom 3 BFG data (doom3bfg-data) and the
# engine's own files share /usr/share/games/doom3bfg/base; configs, saves,
# screenshots and generated caches go to
# ${XDG_DATA_HOME:-~/.local/share}/rbdoom3bfg. Passing the base path keeps the
# engine from picking up a stray base/ directory in the working directory.
basepath=/usr/share/games/doom3bfg
if [ ! -e "$basepath/base/_common.resources" ]; then
    echo "rbdoom-3-bfg: no Doom 3 BFG data in $basepath/base;" \
        "install doom3bfg-data-steam or doom3bfg-data-gog" >&2
fi
exec /usr/lib/rbdoom-3-bfg/RBDoom3BFG +set fs_basepath "$basepath" "$@"
