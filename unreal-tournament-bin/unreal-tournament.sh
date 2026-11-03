#!/bin/sh
# Unreal Tournament (GOTY) launcher (OldUnreal 469 native binaries in
# /opt/unreal-tournament).
#
# 469e keeps settings, saves and logs in ~/.utpg/System and creates
# UnrealTournament.ini and User.ini there on the first start, from Default.ini
# and DefUser.ini in /opt/unreal-tournament/System, so nothing is copied here.
# (Use -SETHOMEDIR=<dir> to pick another directory, or -NOHOMEDIR for none.)
set -eu

game=/opt/unreal-tournament

if [ ! -x "$game/System/ut-bin" ]; then
    echo "unreal-tournament: $game/System/ut-bin is missing; reinstall unreal-tournament-bin." >&2
    exit 1
fi
if [ ! -d "$game/Maps" ]; then
    echo "unreal-tournament: no game data in $game; install unreal-tournament-data-gog, -data-steam or -data-archiveorg." >&2
    exit 1
fi

mkdir -p "$HOME/.utpg/System"
cd "$game/System"
exec ./ut-bin "$@"
