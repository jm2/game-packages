# rvgl-bin

RVGL, the community rewrite of Acclaim's Re-Volt (1999), as released by the
RV Team at <https://rvgl.org>. It is installed to `/opt/rvgl`. This package
contains the engine and RVGL's own asset pack, but not the original game.
Install one of the game data packages:

- `revolt-data-revoltio`: the original game files, downloaded at build time
  from Re-Volt I/O (`distribute.re-volt.io`), as RVGL Launcher does;
- `revolt-data-steam`: the files of your Steam copy (app 287310), via steamcmd.

These are optional:

- `rvgl-dcpack`: the Dreamcast content pack (the Rooftops track and 14 cars);
- `rvgl-soundtrack`: the original soundtrack (Dreamcast version). Without it
  the game has no music, unless your data package brings its own (Steam's
  copy does).

Start the game with `rvgl` or from the desktop menu. Arguments go to RVGL,
e.g. `rvgl -window`, `rvgl -nointro`, `rvgl -lobby 192.168.1.10`. The full
list is in the [RVGL documentation](https://re-volt.gitlab.io/rvgl-docs/).

## Where things are

RVGL loads its content from packs, one folder per content package, merged
in the order of a packlist (the same layout RVGL Launcher creates). The
packages install their packs read-only to `/opt/rvgl/packs`. On each start
`rvgl` links them into `~/.local/share/RVGL/packs/`, writes the packlist
`packs/rvgl.txt` and runs the game with `~/.local/share/RVGL` as its base and
preferences folder:

| Path under `~/.local/share/RVGL` | What |
| --- | --- |
| `profiles/` | settings (`rvgl.ini`), player profiles, the log `rvgl.log` |
| `times/`, `replays/`, `cache/` | best times, saved replays, shader cache |
| `packs/local/` | your own cars and tracks, and editor saves |
| `packs/rvgl.txt` | the packlist; rewritten on every start |

The load order is `game_files`, `rvgl_assets`, `rvgl_dcpack`, `soundtrack`,
any other pack in `/opt/rvgl/packs`, then `local`. Files in a later pack win.

Custom content goes into `packs/local/` (for example
`packs/local/cars/<car>/`). RVGL needs lower-case file names: after copying
content in, run `rvgl --fix-cases`, which lower-cases the names of everything
under `~/.local/share/RVGL/packs` (the linked system packs are left alone).
For more than one content set, put each in its own folder under
`~/.local/share/RVGL/packs/`, write your own packlist (for example
`packs/online.txt` listing `"game_files"`, `"rvgl_assets"`, your packs and
`"local" *`) and start the game with `rvgl -packlist online`.

## Multiplayer and LAN

The host of a multiplayer session listens on **UDP 2310** (change it with
`-serverport <port>`; the clients then need the same port). The LAN search
(`rvgl -lobby 0`, or searching from the Join Game menu) is a broadcast to
UDP 2310 on the local network, so the same port serves both. Clients connect
out from a random UDP port, or the one set by `LocalPort` in
`profiles/rvgl.ini` (or `-port`), and players also connect to each other
directly (peer-to-peer, with UDP hole punching).

- To host on a machine running firewalld, open the port with the bundled
  service: `sudo firewall-cmd --permanent --add-service=rvgl` and then
  `sudo firewall-cmd --reload`. Without firewalld, allow UDP 2310 in.
- `rvgl -lobby` starts hosting a session; `rvgl -lobby <host ip>` (or
  `<ip>:<port>`) joins one, and `rvgl -lobby 0` searches the LAN. The same is
  in the menu under Multi-Player.
- If players can see the host but not each other, set a fixed `LocalPort`
  in `profiles/rvgl.ini` on each client and allow that UDP port as well.

## Discord

`rvgl -register /usr/bin/rvgl` registers the `discord-472158403830218762://`
URI so that Discord can launch the game into a lobby. Register the
`/usr/bin/rvgl` launcher, not `/opt/rvgl/rvgl`: started directly, the engine
can't find the packs.

## Notes

- SDL2, SDL2_image, OpenAL Soft, ENet and libvorbis come from the
  distribution. Upstream's bundled `libunistring.so.2` is kept in
  `/opt/rvgl/lib` because distributions now ship only `libunistring.so.5`.
  `libsndfile`, `mpg123`, `flac` and `fluidsynth` are optional; RVGL loads
  them for custom music in those formats.
- RVGL's own files are covered by CC BY-NC-SA 4.0 (see
  `/usr/share/licenses/rvgl-bin/`, which also has the licenses of the
  libraries built into it). The Re-Volt game data is not free software.
- The upstream `setup` and `fix_cases` scripts are not installed: the
  packaged data is already lower case, the folders the game writes to are
  per user, and `rvgl --fix-cases` covers your own content.
