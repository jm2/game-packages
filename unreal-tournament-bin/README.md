# unreal-tournament-bin

Native Linux binaries for Unreal Tournament (GOTY) from OldUnreal's community
patch (469e), installed to `/opt/unreal-tournament`. The game data is not
included: install one of

- `unreal-tournament-data-gog` (GOG installer you download yourself),
- `unreal-tournament-data-steam` (Steam, via steamcmd),
- `unreal-tournament-data-archiveorg` (the GOTY CD 1 image from archive.org).

Start the game with `unreal-tournament` or from the desktop menu. Arguments
are passed to the game, e.g. `unreal-tournament -log` or
`unreal-tournament unreal://server.example:7777`.

Settings, saves and logs live in `~/.utpg/System`; the game creates
`UnrealTournament.ini` and `User.ini` there on its first start. Use
`-SETHOMEDIR=<dir>` to use a different directory.

## Upgrading from unreal-tournament-goty-steam

`unreal-tournament-goty-steam` (binaries and Steam data in one package,
installed to `/opt/unreal-tournament-goty`) is retired. This package
replaces it; install `unreal-tournament-data-steam` alongside it for the
data. The command is now `unreal-tournament`.

If you used earlier versions of these packages, `~/.utpg/System` may hold
`Default.ini`/`DefUser.ini` copies and a Windows `UnrealTournament.ini` that
the old launcher copied there. If the game misbehaves (wrong renderer, no
sound), move `UnrealTournament.ini` and `User.ini` away and let the game
recreate them.
