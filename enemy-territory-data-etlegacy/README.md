# enemy-territory-data-etlegacy

The original data files of Wolfenstein: Enemy Territory 2.60b (pak0.pk3,
pak1.pk3 and pak2.pk3), the free stand-alone game by Splash Damage and id
Software, installed to /usr/share/enemy-territory/etmain. They are downloaded
from mirror.etlegacy.com/etmain, the copy the ET: Legacy client itself
downloads them from, and are identical to those in the 2.60b Linux full
installer. Play them with ET: Legacy (etlegacy-bin).

## Notes

pak0.pk3 is about 218 MiB. Splash Damage's EULA
(EULA_Wolfenstein_Enemy_Territory.txt) comes from the official 2.60b patch
archive (ET-2.60b.zip, about 4 MB) on the same mirror and is installed to
/usr/share/licenses/enemy-territory-data-etlegacy/.

mp_bin.pk3 (the original 2.60b cgame/ui modules) and the intro video are not
included: ET: Legacy does not use them; it skips the intro when the video is
missing. The install location is the one the AUR's enemy-territory-data uses,
so this package also works with the AUR etlegacy and enemy-territory
packages.
