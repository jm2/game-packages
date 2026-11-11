#!/bin/sh
# openETQW launcher, installed as openetqw with openetqw-dedicated symlinked
# to it.
#
# The engine searches fs_basepath before fs_cdpath, so the ET:QW 1.5 patch
# paks (pak005-pak008, zpak_english001-003, in /opt/openetqw/base) must sit on
# fs_basepath: if the retail tree were fs_basepath, its pak000-pak004 would
# shadow the 1.5 scripts and maps fail to load. So the install directory, with
# the game module and patch paks, is fs_basepath, and the retail data
# (base/pak000-pak004.pk4, megatextures, video) is fs_cdpath. That is the
# first of:
#   - "+set fs_basepath <dir>" on the command line (taken as the retail dir)
#   - OPENETQW_BASEPATH
#   - /opt/etqw, where etqw-data-steam installs it
#   - the folder saved in ~/.local/share/openetqw/basepath.txt
# If none has base/pak000.pk4, openETQW runs with its own search (Steam
# libraries, install folders, a folder chooser) and saves the folder it finds
# to basepath.txt, which this launcher uses from the next start.

OPENETQW_DIR=/opt/openetqw

case "$(basename "$0")" in
    openetqw-dedicated) bin=openETQW-ded_@ARCH@ ded=1 ;;
    *)                  bin=openETQW-client_@ARCH@ ded= ;;
esac

# Take "+set fs_basepath <dir>" out of the arguments as the retail dir.
retail= n=$#
while [ "$n" -gt 0 ]; do
    a=$1; shift; n=$((n - 1))
    if [ "$a" = +set ] && [ "$n" -ge 2 ] && [ "$1" = fs_basepath ]; then
        retail=$2; shift 2; n=$((n - 2))
        continue
    fi
    set -- "$@" "$a"
done

has_data() { [ -n "$1" ] && [ -f "$1/base/pak000.pk4" ]; }
saved="${XDG_DATA_HOME:-$HOME/.local/share}/openetqw/basepath.txt"
if [ -z "$retail" ]; then
    for d in "${OPENETQW_BASEPATH:-}" /opt/etqw "$(head -n 1 "$saved" 2>/dev/null)"; do
        if has_data "$d"; then retail=$d; break; fi
    done
fi

[ -n "$ded" ] && set -- +set dedicated 1 "$@"
cd "$OPENETQW_DIR" || exit 1
if has_data "$retail"; then
    unset OPENETQW_BASEPATH
    exec "./$bin" +set fs_basepath "$OPENETQW_DIR" +set fs_cdpath "$retail" "$@"
fi
if [ -n "$retail" ]; then
    echo "openetqw: no base/pak000.pk4 in $retail" >&2
    exec "./$bin" +set fs_basepath "$retail" "$@"
fi
exec "./$bin" "$@"
