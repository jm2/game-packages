#!/bin/sh
# Otto Matic finds its Data folder next to the executable it was
# started as, so run it by its real path.
cd /usr/lib/ottomatic || exit 1
exec /usr/lib/ottomatic/OttoMatic "$@"
