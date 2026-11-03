# minimetro-steam

Mini Metro, the minimalist subway layout game by Dinosaur Polo Club, from the
Linux depot of the Steam release. The Steam build is DRM-free: it runs without
the Steam client, so no Steam emulator is involved.

Run it with `minimetro` or from the desktop menu.

## Building

Game data comes from Steam via steamcmd, using an account that owns the
game. Either set `STEAM_USER` (steamcmd asks for the password and Steam Guard
code), or download once with `tools/fetch-steam minimetro-steam` and build offline from
the cache.

## Notes

The Steam build runs without Steam: PCGamingWiki says so, and the game's own
code only checks whether Steam is running (it never calls
SteamAPI_RestartAppIfNecessary). Steam Workshop content needs the client.

Settings and saves live in `~/.config/unity3d/Dinosaur Polo Club/Mini Metro/`.
