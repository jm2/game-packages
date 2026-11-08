#!/bin/sh
# Nanosaur finds its Data folder next to the executable it was
# started as, so run it by its real path.
cd /usr/lib/nanosaur || exit 1
exec /usr/lib/nanosaur/Nanosaur "$@"
