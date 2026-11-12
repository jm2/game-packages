# crossdock-bin

crossdock (<https://github.com/jm2/crossdock>) publishes directories of
built packages as signed apt, pacman, RPM and GooGet repositories, and can
serve them itself. This package repackages upstream's release builds for
x86_64 and aarch64:

- Arch: upstream's `crossdock-x86_64.pkg.tar.zst`; on aarch64, where there
  is none, the arm64 `.deb` (plus `LICENSE` from the tagged source)
- Fedora: upstream's `crossdock-x86_64.rpm` / `crossdock-aarch64.rpm`
- Debian: upstream's `crossdock-amd64.deb` / `crossdock-arm64.deb`

All of them hold the same files (upstream's `build-aux/linux/install-tree.sh`):
`/usr/bin/crossdock`, the `crossdock-serve` and `crossdock-publish`
systemd units, the `crossdock` account (sysusers.d), `/var/lib/crossdock`
(tmpfiles.d), a firewalld service and `/etc/crossdock/crossdock.yaml`, a
config file that upgrades never overwrite. Nothing is enabled at install.
The README is installed as `/usr/share/doc/crossdock-bin/README.md`.

## Replacing the source-built `crossdock` package

`crossdock-bin` provides, conflicts with and replaces `crossdock`. Your
`/etc/crossdock/crossdock.yaml`, the `crossdock` account and
`/var/lib/crossdock` are kept, and units you enabled stay enabled:

- Arch: pacman removes `crossdock` first and saves an edited config as
  `crossdock.yaml.pacsave`; `crossdock-bin`'s install script moves it back
  and leaves the new default as `crossdock.yaml.pacnew`.
- Fedora: the edited config stays and the default becomes
  `crossdock.yaml.rpmnew`. The old package's `%preun` and this package's
  first-install preset would disable the units; the spec notes which
  were enabled or running in `%pre` and restores them after the old
  package is gone.
- Debian: dpkg hands the conffile over to `crossdock-bin`. The old
  package's prerm stops the units; `crossdock-bin` starts the enabled
  ones again. Don't purge the leftover `crossdock` entry (`rc` in
  `dpkg -l`): its postrm (`deb-systemd-helper purge`) would disable the
  units. If you did, enable them again with `systemctl enable`.
