# tributary-bin

Tributary (<https://github.com/jm2/tributary>) is a Rhythmbox-style music
manager for GNOME, written in Rust with GTK 4 and libadwaita. One library
view browses and plays local music alongside Subsonic/Navidrome, Jellyfin and
Plex servers, DAAP shares and internet radio.

This package repackages upstream's release builds: the `.pkg.tar.zst`
(Arch x86_64; Arch Linux ARM uses the arm64 `.deb`) and the `.deb`
(Debian/Ubuntu). It replaces the former source-built `tributary`
package.

Run `tributary`, or start "Tributary" from the desktop menu. Audio files can
also be opened with it from a file manager.

There is no Fedora package here: on Fedora, use upstream's COPR,
`dnf copr enable jmsqrd/tributary` (package `tributary`), which takes precedence.
