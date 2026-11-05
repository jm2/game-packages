# knockoutcity-wine

Knockout City Private Server Edition (high-res client) using Wine

Run it with `knockoutcity` or from the desktop menu.

This is a Windows game run by `gamelaunch` through umu-launcher (Proton) when
it is installed, otherwise system wine with your distribution's DXVK. Use
`GAMELAUNCH_RUNNER=wine knockoutcity` to force system wine. Prefixes and saves
live in `~/.local/share/gamelaunch/knockoutcity/`; the first start takes a while.

## Notes

The high-resolution client from Velan's original download
(KnockoutCity-HighRes-10.0-269701.zip, 24 GB), which Velan no longer hosts;
the build fetches the Internet Archive's byte-identical capture and checks its
sha256. The Archive is slow for a file this size: if the download fails, put
the zip next to the build files (or in the fetch cache) and build again.

Run `knockoutcity` to host a game on this PC or join a server announced on
the LAN (see knockoutcity-server for options, ports and settings). There is
no Debian package: two data files are each larger than a .deb can hold.
