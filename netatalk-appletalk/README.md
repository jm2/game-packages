# netatalk-appletalk

Netatalk 4 (AFP file server) built with the AppleTalk transport
(`-Dwith-appletalk=true`), for classic Macs and Apple II clients. It
replaces the old `netatalk-ddp` (Netatalk 2.2) and the AUR `netatalk`.

- Configuration: `/etc/afp.conf` (AFP volumes), `/etc/atalkd.conf`
  (AppleTalk interfaces), `/etc/papd.conf` (printers shared to Macs),
  `/etc/macipgw.conf`.
- AppleTalk needs the kernel's `appletalk` module (`modprobe appletalk`).
- systemd units are upstream's: `atalkd.service` (was `atalk.service` in
  netatalk-ddp), `netatalk.service` (afpd and cnid_metad; there is no
  separate `netatalk-cnid.service` any more), `papd.service` (was
  `pap.service`), `timelord.service`, `a2boot.service`, `macipgw.service`.
  Re-enable the ones you used after upgrading from netatalk-ddp.
- Netatalk 2 configuration (`/etc/netatalk/AppleVolumes.default`,
  `afpd.conf`, ...) is not read any more; move shares to `/etc/afp.conf`.
  CNID databases are kept in `/var/lib/netatalk/CNID`.
- The CUPS `pap` backend (`/usr/lib/cups/backend/pap`) prints to AppleTalk
  printers.
- Spotlight uses the CNID and Xapian backends (no LocalSearch/TinySPARQL).
  TCP wrappers and the MySQL CNID backend are not built.
