# switchworks-bin

Switchworks (<https://github.com/jm2/switchworks>) is a control plane for
coding agents across your machines. This package repackages upstream's
release builds for x86_64 and aarch64:

- Arch: upstream's `switchworks-x86_64.pkg.tar.zst`; on aarch64, where there
  is none, the arm64 `.deb` (plus `LICENSE` from the tagged source)
- Debian: upstream's `switchworks-amd64.deb` / `switchworks-arm64.deb`

All of them hold the same files (upstream's `build-aux/linux/install-tree.sh`):
`swk`, `swk-tray`, the `swk-node` and `swk-coordinator` systemd user units,
the system `swk-coordinator` unit and its `switchworks` account
(sysusers.d), the tray's desktop entry and icons. Nothing is enabled at
install: each user runs `swk service install` for their node, and
`swk service install --system coordinator`, run as root, sets up the system
coordinator. The README is installed as
`/usr/share/doc/switchworks-bin/README.md`; the OFL texts of the fonts the
web UI embeds are with the license files (Debian: the doc directory).

## Replacing the source-built `switchworks` package

`switchworks-bin` provides, conflicts with and replaces `switchworks`. The
`switchworks` account and `/var/lib/switchworks` are kept.

- Debian: the old package's prerm stops a running system coordinator and
  `switchworks-bin` (like upstream's .deb) starts nothing at install, so
  start it again with `systemctl start swk-coordinator`. Don't purge the
  leftover `switchworks` entry (`rc` in `dpkg -l`): its postrm would
  disable the unit.

There is no Fedora package here: on Fedora, use upstream's COPR,
`dnf copr enable jmsqrd/switchworks` (package `switchworks`), which takes precedence.
