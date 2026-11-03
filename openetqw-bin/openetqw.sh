#!/bin/sh
# openETQW launcher, installed as openetqw with openetqw-dedicated symlinked
# to it.
#
# openETQW loads its game module, shaders and the bundled ET:QW 1.5 patch
# paks from its install directory (fs_cdpath), so it runs from there.
#
# The retail data (base/pak000-pak004.pk4, megatextures, video) is looked up
# in OPENETQW_BASEPATH first (default /opt/etqw, where etqw-data-steam
# installs it), then in the path stored in ~/.local/share/openetqw/basepath.txt,
# the usual install folders and Steam libraries. "+set fs_basepath <dir>"
# overrides all of them.

OPENETQW_DIR=/opt/openetqw
export OPENETQW_BASEPATH="${OPENETQW_BASEPATH:-/opt/etqw}"

case "$(basename "$0")" in
    openetqw-dedicated)
        set -- +set dedicated 1 "$@"
        bin=openETQW-ded_@ARCH@
        ;;
    *)
        bin=openETQW-client_@ARCH@
        ;;
esac

cd "$OPENETQW_DIR" || exit 1
exec "./$bin" "$@"
