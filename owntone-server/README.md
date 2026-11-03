# owntone-server

OwnTone (formerly forked-daapd) is a DAAP (iTunes), MPD and RSP media server
with AirPlay, Chromecast, Spotify and Last.fm support.

- Point `directories` in `/etc/owntone.conf` at your music library. The
  `owntone` user must be able to read it.
- Start it with `systemctl enable --now owntone`. The web interface is on
  port 3689.
- The service runs as the `owntone` system user (created from
  `/usr/lib/sysusers.d/owntone.conf`, member of `audio`), not as root: see
  `/usr/lib/systemd/system/owntone.service.d/override.conf`. The database
  and cache live in `/var/cache/owntone`, the log in `/var/log/owntone.log`
  (both created by `/usr/lib/tmpfiles.d/owntone.conf`).
- mDNS announcements need `avahi-daemon` running.
- Upstream documentation is in `/usr/share/doc/owntone/`.
- Fedora builds against `ffmpeg-free`; install RPM Fusion's `ffmpeg-libs`
  for formats it leaves out.
