#!/bin/sh
# Unreal Tournament 2004 launcher (OldUnreal native binaries in /opt/ut2004).
#
# Settings, saves and logs live in ~/.ut2004/System. The game writes UT2004.ini
# and User.ini there itself on the first start, from Default.ini/DefUser.ini in
# /opt/ut2004/System, so nothing is copied here.
set -eu

game=/opt/ut2004
user=$HOME/.ut2004/System

if [ ! -x "$game/System/UT2004" ]; then
    echo "ut2004: $game/System/UT2004 is missing; reinstall ut2004-bin." >&2
    exit 1
fi
if [ ! -d "$game/Maps" ]; then
    echo "ut2004: no game data in $game; install ut2004-data-gog, ut2004-data-steam or ut2004-data-archiveorg." >&2
    exit 1
fi

mkdir -p "$user"

# GOG copies ship the CD key in their goggame script. Extract it once, if the
# user has no key yet; failures here must not stop the game from starting.
if [ ! -s "$user/CDkey" ]; then
    for script in "$game"/GOG/goggame-*.script; do
        [ -f "$script" ] || continue
        key=$(grep -B1 -F '"CDKey"' "$script" | sed -n 's/.*"valueData": *"\([A-Za-z0-9-]*\)".*/\1/p' | head -n1) || key=
        if [ -n "$key" ]; then
            (umask 077 && printf '%s\n' "$key" > "$user/CDkey")
        fi
        break
    done
fi

cd "$game/System"
exec ./UT2004 "$@"
