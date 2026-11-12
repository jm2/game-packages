# cro-mag-rally-net-bin

Cro-Mag Rally is Pangea Software's prehistoric kart racer, ported to modern
systems by Iliyas Jorio. This package is the release build of the jm2 fork
(<https://github.com/jm2/CroMagRally>), which adds multiplayer over a wired
or Wi-Fi local network.

It repackages upstream's release builds: the `.pkg.tar.zst` (Arch x86_64;
Arch Linux ARM uses the aarch64 `.deb`), the `.rpm` (Fedora) and the `.deb`
(Debian/Ubuntu). It replaces the former source-built `cro-mag-rally-net`
package.

## Running

Run `cromagrally` (or `cro-mag-rally`, the command the source-built package
had), or start "Cro-Mag Rally" from the desktop menu. The game data is in
`/usr/share/cromagrally/Data`. The game bundles its own SDL3 in
`/usr/lib/cromagrally`.

## Network play

From the multiplayer menu one player chooses **Host Net Game** and the
others **Join Net Game**. Discovery works within one LAN or Wi-Fi subnet.
The game uses TCP and UDP port 49959; allow both through the host's firewall
if discovery or joining fails, or start every peer with `--port NUMBER` to
use another port. All peers need compatible builds of the game.

Upstream's README is installed as `README.upstream.md`.
