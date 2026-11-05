# dirtrally-steam

DiRT Rally (native Linux, Feral) with data via Steam

Run it with `dirtrally` or from the desktop menu.

## Building

Game data comes from Steam via steamcmd, using an account that owns the
game. Either set `STEAM_USER` (steamcmd asks for the password and Steam Guard
code), or download once with `tools/fetch-steam dirtrally-steam` and build offline from
the cache.

## Formats

Not built for:

- Fedora (RPM): the game needs OpenSSL 1.0, libidn11, librtmp0, OpenLDAP 2.4 and GConf, which current Fedora and Debian do not ship
- Debian (.deb): the game needs OpenSSL 1.0, libidn11, librtmp0, OpenLDAP 2.4 and GConf, which current Fedora and Debian do not ship

## Notes

Feral's port needs legacy libraries (openssl 1.0, libidn11, librtmp0, gconf)
that only the AUR still provides; on Fedora/Debian install equivalents
yourself.
