#!/bin/sh
# ET: Legacy launcher, installed as etl with etlded symlinked to it.
#
# The engine (/opt/etlegacy) loads etmain/ and the legacy mod from
# fs_basepath, which defaults to the current directory, so set it here (a
# later "+set fs_basepath <dir>" on the command line still wins).
# etmain/pak0-2.pk3 there link to the original Wolfenstein: Enemy Territory
# 2.60b data in /usr/share/enemy-territory/etmain (enemy-territory-data). Configs, downloaded mods and logs go to
# ~/.etlegacy (fs_homepath), which overrides files in /opt/etlegacy.

dir=/opt/etlegacy
data=/usr/share/enemy-territory/etmain

case "$(basename "$0")" in
    etlded*)
        bin=etlded.@ARCH@
        ;;
    *)
        bin=etl.@ARCH@
        # et://host[:port] links from the desktop entry or a browser
        case "${1:-}" in
            et://*) u=$1; shift; set -- +connect "$u" "$@" ;;
        esac
        ;;
esac

if [ ! -e "$data/pak0.pk3" ]; then
    echo "$(basename "$0"): $data/pak0.pk3 is missing; install enemy-territory-data (enemy-territory-data-etlegacy)." >&2
fi

exec "$dir/$bin" +set fs_basepath "$dir" "$@"
