# battlenet-wine

The Blizzard Battle.net desktop client, run through gamelaunch (umu/Proton
by default, system wine as a fallback). Like distributions' Steam packages,
this package is only a bootstrap: the first start downloads Blizzard's
current installer into your own Wine prefix, and from then on Battle.net
keeps itself and its games up to date. Nothing from Blizzard is downloaded
when the package is built.

Run it with `battlenet` or from the desktop menu.

This is a Windows game run by `gamelaunch` through umu-launcher (Proton) when
it is installed, otherwise system wine with your distribution's DXVK. Use
`GAMELAUNCH_RUNNER=wine battlenet` to force system wine. Prefixes and saves
live in `~/.local/share/gamelaunch/battlenet/`; the first start takes a while.

## Notes

The first start creates the Wine prefix, downloads Blizzard's current
installer and opens it: pick a language and click Continue, keeping the
default install location (C:/Program Files (x86)/Battle.net). Battle.net then
starts by itself; later starts open it directly. Games you install from
Battle.net go into the same prefix, under
~/.local/share/gamelaunch/battlenet/prefix-umu/.

Each backend has its own prefix, so switching to system wine
(GAMELAUNCH_RUNNER=wine) installs Battle.net, and its games, a second time.

Tested on Fedora 44 with umu-launcher 1.4.4 and UMU-Proton 10.0-4 (software
rendering, no login): installation, the client's own update step and the
login screen work. Logging in and playing games are untested.
