#!/bin/sh
# Nanosaur 2 finds its Data folder next to the executable it was
# started as, so run it by its real path.
cd /usr/lib/nanosaur2 || exit 1
exec /usr/lib/nanosaur2/Nanosaur2 "$@"
