# doom-eternal-wine-gog

DOOM Eternal using Wine with data via GOG

Run it with `doom-eternal` or from the desktop menu.

This is a Windows game run by `gamelaunch` through umu-launcher (Proton) when
it is installed, otherwise system wine with your distribution's DXVK. Use
`GAMELAUNCH_RUNNER=wine doom-eternal` to force system wine. Prefixes and saves
live in `~/.local/share/gamelaunch/doom-eternal/`; the first start takes a while.

## Building

Place these files next to the build files or in
`${TMPDIR:-/var/tmp}/linux-packages-cache/doom-eternal-wine-gog/` before building:

- `setup_doom_eternal_20260414-233123-rotten-tiger_(90172).exe` - GOG (lgogdownloader: doom_eternal/en1installer0)
- `setup_doom_eternal_cosplay_slayer_master_collection_cosmetic_pack_20260414-233123-rotten-tiger_(90172).exe` - GOG (lgogdownloader: doom_eternal/doom_eternal_cosplay_slayer_master_collection_cosmetic_pack/en1installer0)
- `setup_doom_eternal_series_one_cosmetic_pack_20260414-233123-rotten-tiger_(90172).exe` - GOG (lgogdownloader: doom_eternal/doom_eternal_series_one_cosmetic_pack/en1installer0)
- `setup_doom_eternal_series_three_cosmetic_pack_20260414-233123-rotten-tiger_(90172).exe` - GOG (lgogdownloader: doom_eternal/doom_eternal_series_three_cosmetic_pack/en1installer0)
- `setup_doom_eternal_mullet_slayer_master_collection_cosmetic_pack_20260414-233123-rotten-tiger_(90172).exe` - GOG (lgogdownloader: doom_eternal/doom_eternal_mullet_slayer_master_collection_cosmetic_pack/en1installer0)
- `setup_doom_eternal_series_six_cosmetic_pack_20260414-233123-rotten-tiger_(90172).exe` - GOG (lgogdownloader: doom_eternal/doom_eternal_series_six_cosmetic_pack/en1installer0)
- `setup_doom_eternal_series_two_cosmetic_pack_20260414-233123-rotten-tiger_(90172).exe` - GOG (lgogdownloader: doom_eternal/doom_eternal_series_two_cosmetic_pack/en1installer0)
- `setup_doom_eternal_the_ancient_gods_-_part_two_20260414-233123-rotten-tiger_(90172).exe` - GOG (lgogdownloader: doom_eternal/doom_eternal_the_ancient_gods_part_two/en1installer0)
- `setup_doom_eternal_series_four_cosmetic_pack_20260414-233123-rotten-tiger_(90172).exe` - GOG (lgogdownloader: doom_eternal/doom_eternal_series_four_cosmetic_pack/en1installer0)
- `setup_doom_eternal_doomicorn_master_collection_cosmetic_pack_20260414-233123-rotten-tiger_(90172).exe` - GOG (lgogdownloader: doom_eternal/doom_eternal_doomicorn_master_collection_cosmetic_pack/en1installer0)
- `setup_doom_eternal_the_ancient_gods_-_part_one_20260414-233123-rotten-tiger_(90172).exe` - GOG (lgogdownloader: doom_eternal/doom_eternal_the_ancient_gods_part_one/en1installer0)
- `setup_doom_eternal_deluxe_edition_content_20260414-233123-rotten-tiger_(90172).exe` - GOG (lgogdownloader: doom_eternal/doom_eternal_deluxe_edition_content/en1installer0)
- `setup_doom_eternal_series_seven_cosmetic_pack_20260414-233123-rotten-tiger_(90172).exe` - GOG (lgogdownloader: doom_eternal/doom_eternal_series_seven_cosmetic_pack/en1installer0)
- `setup_doom_eternal_rip_and_tear_pack_20260414-233123-rotten-tiger_(90172).exe` - GOG (lgogdownloader: doom_eternal/doom_eternal_rip_and_tear_pack/en1installer0)
- `setup_doom_eternal_series_five_cosmetic_pack_20260414-233123-rotten-tiger_(90172).exe` - GOG (lgogdownloader: doom_eternal/doom_eternal_series_five_cosmetic_pack/en1installer0)
- `setup_doom_eternal_20260414-233123-rotten-tiger_(90172)-1.bin` - GOG (lgogdownloader: doom_eternal/en1installer1)
- `setup_doom_eternal_20260414-233123-rotten-tiger_(90172)-2.bin` - GOG (lgogdownloader: doom_eternal/en1installer2)
- `setup_doom_eternal_20260414-233123-rotten-tiger_(90172)-3.bin` - GOG (lgogdownloader: doom_eternal/en1installer3)
- `setup_doom_eternal_20260414-233123-rotten-tiger_(90172)-4.bin` - GOG (lgogdownloader: doom_eternal/en1installer4)
- `setup_doom_eternal_20260414-233123-rotten-tiger_(90172)-5.bin` - GOG (lgogdownloader: doom_eternal/en1installer5)
- `setup_doom_eternal_20260414-233123-rotten-tiger_(90172)-6.bin` - GOG (lgogdownloader: doom_eternal/en1installer6)
- `setup_doom_eternal_20260414-233123-rotten-tiger_(90172)-7.bin` - GOG (lgogdownloader: doom_eternal/en1installer7)
- `setup_doom_eternal_20260414-233123-rotten-tiger_(90172)-8.bin` - GOG (lgogdownloader: doom_eternal/en1installer8)
- `setup_doom_eternal_20260414-233123-rotten-tiger_(90172)-9.bin` - GOG (lgogdownloader: doom_eternal/en1installer9)
- `setup_doom_eternal_20260414-233123-rotten-tiger_(90172)-10.bin` - GOG (lgogdownloader: doom_eternal/en1installer10)
- `setup_doom_eternal_20260414-233123-rotten-tiger_(90172)-11.bin` - GOG (lgogdownloader: doom_eternal/en1installer11)
- `setup_doom_eternal_20260414-233123-rotten-tiger_(90172)-12.bin` - GOG (lgogdownloader: doom_eternal/en1installer12)
- `setup_doom_eternal_20260414-233123-rotten-tiger_(90172)-13.bin` - GOG (lgogdownloader: doom_eternal/en1installer13)
- `setup_doom_eternal_20260414-233123-rotten-tiger_(90172)-14.bin` - GOG (lgogdownloader: doom_eternal/en1installer14)
- `setup_doom_eternal_20260414-233123-rotten-tiger_(90172)-15.bin` - GOG (lgogdownloader: doom_eternal/en1installer15)
- `setup_doom_eternal_20260414-233123-rotten-tiger_(90172)-16.bin` - GOG (lgogdownloader: doom_eternal/en1installer16)
- `setup_doom_eternal_20260414-233123-rotten-tiger_(90172)-17.bin` - GOG (lgogdownloader: doom_eternal/en1installer17)
- `setup_doom_eternal_20260414-233123-rotten-tiger_(90172)-18.bin` - GOG (lgogdownloader: doom_eternal/en1installer18)
- `setup_doom_eternal_20260414-233123-rotten-tiger_(90172)-19.bin` - GOG (lgogdownloader: doom_eternal/en1installer19)
- `setup_doom_eternal_20260414-233123-rotten-tiger_(90172)-20.bin` - GOG (lgogdownloader: doom_eternal/en1installer20)
- `setup_doom_eternal_20260414-233123-rotten-tiger_(90172)-21.bin` - GOG (lgogdownloader: doom_eternal/en1installer21)
- `setup_doom_eternal_20260414-233123-rotten-tiger_(90172)-22.bin` - GOG (lgogdownloader: doom_eternal/en1installer22)

## Formats

Not built for:

- Debian (.deb): base/gameresources_0_1.streamdb is one 11.77 GiB file, over the ~9.3 GiB size limit of a .deb member

## Notes

The GOG build is DRM-free (campaign and The Ancient Gods; GOG does not include
BATTLEMODE). Vulkan only.

There is no working Debian build: base/gameresources_0_1.streamdb is a single
11.77 GiB file, larger than the ~9.3 GiB a .deb archive member can hold, so the
data can't be split into deb parts. Use the Arch or Fedora package.
