# geysermc-bin

The standalone GeyserMC jar (build 1288 of Geyser 2.12.1, pinned by sha256),
which lets Minecraft: Bedrock Edition clients join a Minecraft: Java Edition
server.

- Edit `/etc/geysermc/config.yml` (at least `java.address`/`java.port` and
  `java.auth-type`), then `systemctl enable --now geysermc`. Bedrock clients
  connect on UDP port 19132.
- The service runs as the `geysermc` system user. Logs, caches, resource
  packs, extensions and keys are in `/var/lib/geysermc`; `logs/latest.log`
  there, or `journalctl -u geysermc`.
- Geyser migrates and rewrites `config.yml` itself when a newer version needs
  new settings, so `/etc/geysermc` is writable by the `geysermc` group.
- Upgrading from the AUR package (whose config was `config-version: 4`):
  Geyser migrates an old config on its first start.
- Needs Java 21 or newer.
