# unreal-tournament-data-archiveorg

Game data for Unreal Tournament: Game of the Year Edition, unpacked from the
GOTY CD 1 image on archive.org and installed to /opt/unreal-tournament. Play
it with the native OldUnreal binaries from unreal-tournament-bin.

## Notes

81 of the CD's maps are UZ-compressed. 469e would try to decompress them into
the read-only /opt/unreal-tournament/Maps on first start and fail, so the
build decompresses them with ucc-bin from OldUnreal's 469e Linux patch (the
same step OldUnreal's installer runs). That means the build runs an OldUnreal
binary for the build machine's architecture (x86_64 or aarch64), and the
patch tarballs are build sources of this package.
