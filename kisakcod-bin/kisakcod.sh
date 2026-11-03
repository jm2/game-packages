#!/bin/sh
# KisakCOD launcher, installed as kisakcod with kisakcod-dedi symlinked to it.
#
# KisakCOD reads the retail Call of Duty 4 (Steam 1.8) tree - main/, zone/
# and the localization files - from fs_basepath. That is KISAKCOD_COD4_PATH
# (default /opt/cod4, where cod4-data-steam installs it). Retail files in the
# per-user path (~/.config/kisakcod) are searched first, and
# "+set fs_basepath <dir>" on the command line overrides both.
# Profiles, configs, logs and downloads go to the per-user path; nothing is
# written to /opt.

KISAKCOD_DIR=/opt/kisakcod
cod4="${KISAKCOD_COD4_PATH:-/opt/cod4}"
# No retail tree there: fall back to upstream's layout, with the install
# folder as fs_basepath and the retail data only in the per-user path.
[ -d "$cod4" ] || cod4=$KISAKCOD_DIR

case "$(basename "$0")" in
    kisakcod-dedi)
        # The server keeps retail's fs_homepath = fs_basepath, which is
        # read-only here, so give it the per-user path as upstream does.
        home="${XDG_CONFIG_HOME:-$HOME/.config}/kisakcod"
        mkdir -p "$home/main" || exit 1
        set -- +set fs_homepath "$home" "$@"
        bin=KisakCOD-dedi
        ;;
    *)
        bin=KisakCOD-mp
        ;;
esac

cd "$KISAKCOD_DIR" || exit 1
exec "$KISAKCOD_DIR/$bin" +set fs_basepath "$cod4" "$@"
