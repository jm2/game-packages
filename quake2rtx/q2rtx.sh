#!/bin/sh
# Quake II RTX launcher. The engine uses /usr/share/quake2rtx as its base
# directory and ${XDG_DATA_HOME:-~/.local/share}/quake2rtx for user data
# (configs, saves, and the retail paks if you import them).
data="${XDG_DATA_HOME:-$HOME/.local/share}/quake2rtx"

# Releases before 1.8 used ~/.quake2rtx; move it into place once.
if [ -d "$HOME/.quake2rtx" ] && [ ! -e "$data" ]; then
    mkdir -p "${data%/*}" && mv "$HOME/.quake2rtx" "$data"
fi
mkdir -p "$data/baseq2"

# On the first launch, offer to import the paks of a retail Quake II install.
if [ ! -f "$data/.retail_checked" ]; then
    DEST_DIR="$data" /usr/share/quake2rtx/bin/find-retail-paks.sh
    touch "$data/.retail_checked"
fi

exec /usr/share/quake2rtx/bin/q2rtx "$@"
