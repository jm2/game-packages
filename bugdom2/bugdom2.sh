#!/bin/sh
# Bugdom 2 finds its Data folder next to the executable it was
# started as, so run it by its real path.
cd /usr/lib/bugdom2 || exit 1
exec /usr/lib/bugdom2/Bugdom2 "$@"
