#!/bin/sh
# Billy Frontier finds its Data folder next to the executable it was
# started as, so run it by its real path.
cd /usr/lib/billy-frontier || exit 1
exec /usr/lib/billy-frontier/BillyFrontier "$@"
