# rvgl-dcpack

The content of the Dreamcast version of Re-Volt for RVGL: the Rooftops track
and 14 additional cars (including BigVolt and BossVolt), with the Dreamcast
car selection layout. Installed as RVGL's rvgl_dcpack pack in
/opt/rvgl/packs/rvgl_dcpack, downloaded at build time from Re-Volt I/O.

## Notes

The pack is loaded after the game data, so its car selection layout
(levels/frontend/frontend.fob, with BigVolt and BossVolt) replaces the
original one, as with RVGL Launcher. The alternative Dreamcast car box
layout is in levels/frontend/custom/dc; to use it, copy its two files to
~/.local/share/RVGL/packs/local/levels/frontend/custom/.

Like the game data, this content comes from Acclaim's Re-Volt and is hosted
by Re-Volt I/O without a license to redistribute it. The download URL is not
versioned: when a new rvgl_dcpack is published the checksum stops matching.
