# balun-bin

Balun (<https://github.com/jm2/balun>) is a lightweight cross-platform
HDHomeRun live TV viewer built with GTK 4, libadwaita and GStreamer. It
finds tuners on the local network, by address or across an approved private
subnet, lists their channel lineups and plays unprotected live channels.

This package repackages upstream's release builds: the `.pkg.tar.zst`
(Arch x86_64; Arch Linux ARM uses the arm64 `.deb`) and the `.deb`
(Debian/Ubuntu). It replaces the former source-built `balun`
package.

Run `balun`, or start "Balun" from the desktop menu.

Playback needs the GStreamer plugins this package depends on: MPEG-TS
demuxing (plugins-bad), the GTK 4 video sink and libav for the MPEG-2,
H.264, AC-3 and AAC decoders.

There is no Fedora package here: on Fedora, use upstream's COPR,
`dnf copr enable jmsqrd/balun` (package `balun`), which takes precedence.
