# quake3-pointrelease-data

The data files of id Software's Quake III Arena 1.32 point release:
baseq3/pak1.pk3 to pak8.pk3 and missionpack/pak1.pk3 to pak3.pk3, installed
to /opt/quake3 next to the retail pak0.pk3 files of the quake3-data packages.
Pure servers require them. They are unpacked from id's Linux point release
installer (linuxq3apoint-1.32b-3.x86.run) without running it.

## Notes

The paks come from id Software's last Linux point release installer,
linuxq3apoint-1.32b-3.x86.run (2003), as mirrored from ftp.idsoftware.com
by ftp.gwdg.de; the AUR quake3 package uses the same file. The build reads
the installer's gzip tar payload directly and never runs it. The same paks
are in ioquake3's quake3-latest-pk3s.zip.

id's point release licence (Q3A_EULA.txt from the installer, a limited use
licence that allows free non-commercial redistribution of the patch) is
installed to /usr/share/licenses/quake3-pointrelease-data/.

The AUR quake3 package installs the same files to /opt/quake3, so the two
can't be installed together. The missionpack paks are only used together
with Team Arena's missionpack/pak0.pk3 (quake3-ta-data).
