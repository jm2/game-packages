#!/bin/sh
# Shared install step for the PKGBUILD, the RPM spec and debian/rules.
#   install.sh <extracted windows release> <extracted linux release> <destdir> <host arch: x64|ARM64>
set -eu
win=$1 lin=$2 dest=$3 host=$4
lib=$dest/usr/lib/gbe-fork

# Windows: regular and experimental steam_api builds, the ColdClientLoader set, tools.
# These live under /opt, not /usr: umu/Proton runs games in a pressure-vessel
# container that replaces /usr with the Steam Runtime, so a game's
# steam_api64.dll symlink into /usr/lib would dangle there. /opt stays visible.
win_lib=$lib
lib=$dest/opt/gbe-fork
for flavour in regular experimental; do
    sub=win; [ "$flavour" = experimental ] && sub=win-experimental
    for a in x86 x64; do
        install -d "$lib/$sub/$a"
        for f in "$win/release/$flavour/$a"/*.dll; do install -m644 "$f" "$lib/$sub/$a/"; done
    done
done
install -d "$lib/win-steamclient/extra_dlls"
for f in "$win"/release/steamclient_experimental/*.dll "$win"/release/steamclient_experimental/*.exe; do
    install -m644 "$f" "$lib/win-steamclient/"
done
install -m644 "$win"/release/steamclient_experimental/extra_dlls/*.dll "$lib/win-steamclient/extra_dlls/"
install -m644 "$win/release/steamclient_experimental/ColdClientLoader.ini" "$lib/win-steamclient/ColdClientLoader.EXAMPLE.ini"
install -Dm644 "$win/release/steam_old_lib/Steam.dll" "$lib/win-old/Steam.dll"
install -d "$lib/win-tools"
install -m644 "$win"/release/tools/generate_interfaces/*.exe "$win"/release/tools/lobby_connect/*.exe "$lib/win-tools/"
lib=$win_lib
# Compatibility links for game packages built before the move (plain Wine only).
# One link per file: replacing a directory with a symlink breaks upgrades.
for sub in win win-experimental; do
    for a in x86 x64; do
        install -d "$lib/$sub/$a"
        for f in "$dest/opt/gbe-fork/$sub/$a"/*.dll; do ln -s "/opt/gbe-fork/$sub/$a/${f##*/}" "$lib/$sub/$a/"; done
    done
done

# Linux: libsteam_api.so / steamclient.so for every architecture, tools.
for flavour in regular experimental; do
    sub=linux; [ "$flavour" = experimental ] && sub=linux-experimental
    for a in x86 x64 ARM64; do
        d=$(echo "$a" | tr 'A-Z' 'a-z')
        install -d "$lib/$sub/$d"
        install -m755 "$lin/release/$flavour/$a"/*.so "$lib/$sub/$d/"
    done
done
install -d "$lib/linux-tools"
install -m755 "$lin"/release/tools/generate_interfaces/generate_interfaces_* \
              "$lin"/release/tools/lobby_connect/lobby_connect_* "$lib/linux-tools/"
install -d "$lib/linux-tools/steamclient_loader"
install -m755 "$lin/release/tools/steamclient_loader/steamclient_loader.sh" "$lib/linux-tools/steamclient_loader/"
install -m644 "$lin"/release/tools/steamclient_loader/*.txt "$lib/linux-tools/steamclient_loader/"

# Example steam_settings for game packages to start from, and docs.
install -d "$dest/usr/share/gbe-fork"
cp -r --no-preserve=ownership "$lin/release/steam_settings.EXAMPLE" "$dest/usr/share/gbe-fork/"
doc=$dest/usr/share/doc/gbe-fork
install -d "$doc/windows" "$doc/linux"
install -m644 "$lin/release/CHANGELOG.md" "$lin/release/CREDITS.md" "$doc/"
install -m644 "$win/release/README.release.md" "$doc/windows/"
find "$win/release" -mindepth 2 -name 'README*.md' -exec install -m644 {} "$doc/windows/" \;
install -m644 "$lin/release/README.release.md" "$doc/linux/"
find "$lin/release" -mindepth 2 -name 'README*.md' -exec install -m644 {} "$doc/linux/" \;

# Command-line wrappers for the host architecture.
install -d "$dest/usr/bin"
for tool in generate_interfaces lobby_connect; do
    cat > "$dest/usr/bin/gbe-${tool%%_*}-${tool#*_}" <<WRAP
#!/bin/sh
exec /usr/lib/gbe-fork/linux-tools/${tool}_${host} "\$@"
WRAP
    chmod 755 "$dest/usr/bin/gbe-${tool%%_*}-${tool#*_}"
done
# gbe-steam-interfaces <original steam_api(64).dll|libsteam_api.so> <output dir>
cat > "$dest/usr/bin/gbe-steam-interfaces" <<'WRAP'
#!/bin/sh
# Write steam_interfaces.txt for the ORIGINAL steam_api library into <output dir>.
set -eu
[ $# -eq 2 ] || { echo "usage: gbe-steam-interfaces <original steam_api library> <output dir>" >&2; exit 2; }
lib=$(realpath "$1"); mkdir -p "$2"; cd "$2"
/usr/bin/gbe-generate-interfaces "$lib" >/dev/null
[ -s steam_interfaces.txt ] || { echo "gbe-steam-interfaces: no interfaces found in $lib" >&2; exit 1; }
WRAP
chmod 755 "$dest/usr/bin/gbe-steam-interfaces"
