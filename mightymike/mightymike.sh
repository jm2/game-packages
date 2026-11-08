#!/bin/sh
# Mighty Mike finds its Data folder next to the executable it was
# started as, so run it by its real path.
cd /usr/lib/mightymike || exit 1
exec /usr/lib/mightymike/MightyMike "$@"
