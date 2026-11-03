# lilium-voyager-git

Lilium Voyager is an ioquake3-based engine for Star Trek Voyager: Elite
Force Holomatch (multiplayer), <https://clover.moe/lilium-voyager/>.

## Game data

The engine looks for the retail `baseEF/*.pk3` files in
`/opt/lilium-voyager/baseEF`. Either install `eliteforce-data-gog`, which
puts the GOG copy there, or copy the `.pk3` files from your CD or GOG
install into that directory yourself. `+set fs_basepath <dir>` points the
engine at another install (the folder that contains `baseEF/`).

## Running

- `lilium-voyager`: the client (`liliumvoyhm` is kept as an alias).
- `lilium-voyager-server`: the dedicated server (alias `liliumvoyded`).
  `lilium-voyager-server.service` runs it as a dynamic system user with its
  state in `/var/lib/lilium-voyager-server`.

Settings and downloads go to `~/.local/share/lilium-voyager`.
