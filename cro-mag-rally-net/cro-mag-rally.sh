#!/bin/sh
# Cro-Mag Rally finds its Data folder next to the executable it was started
# as, so run it by its real path.
cd /usr/lib/cro-mag-rally || exit 1
exec /usr/lib/cro-mag-rally/CroMagRally "$@"
