#!/bin/sh
# Bugdom finds its Data folder next to the executable it was
# started as, so run it by its real path.
cd /usr/lib/bugdom || exit 1
exec /usr/lib/bugdom/Bugdom "$@"
