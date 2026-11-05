#!/bin/sh
# RVGL (Re-Volt) launcher for the packaged install in /opt/rvgl.
#
# RVGL reads game content from packs: one folder per content package, merged
# in the order of a packlist (this is how RVGL Launcher sets the game up).
# The packages install their packs read-only to /opt/rvgl/packs; this script
# links them into a per-user base folder, writes the packlist and runs RVGL
# with that folder as base and preferences path:
#
#   ~/.local/share/RVGL/packs/<pack>     -> /opt/rvgl/packs/<pack>
#   ~/.local/share/RVGL/packs/local/     your own cars/tracks and editor saves
#   ~/.local/share/RVGL/packs/rvgl.txt   packlist, rewritten on every start
#   ~/.local/share/RVGL/profiles/        settings (rvgl.ini), saves, rvgl.log
#
#   rvgl [RVGL options]   start the game (e.g. rvgl -window, rvgl -lobby)
#   rvgl --fix-cases      lower-case the file names of your own packs
set -eu

sys=/opt/rvgl
data=${XDG_DATA_HOME:-$HOME/.local/share}/RVGL
packs=$data/packs

# Packs in the order RVGL Launcher's "original" preset uses; any other pack
# installed to /opt/rvgl/packs follows them, then the writable local pack.
order="game_files rvgl_assets rvgl_dcpack soundtrack"

fix_cases() { # RVGL needs lower-case file names (upstream's fix_cases script)
    [ -d "$packs" ] || return 0
    # -depth renames the contents of a folder before the folder itself;
    # links to the system packs are not followed.
    find "$packs" -mindepth 1 -depth -name '*[[:upper:]]*' | while IFS= read -r f; do
        base=${f##*/} dir=${f%/*}
        lower=$(printf '%s' "$base" | tr '[:upper:]' '[:lower:]')
        if [ ! -e "$dir/$lower" ]; then
            mv -- "$f" "$dir/$lower"
        elif [ -d "$f" ] && [ ! -L "$f" ] && [ -d "$dir/$lower" ]; then
            # Folders that differ only in case (Cars/ and cars/): merge them.
            # Their contents are lower case already; existing files win.
            cp -R -n -- "$f/." "$dir/$lower/" && rm -rf -- "$f"
        else
            echo "rvgl: not renaming $f: $dir/$lower exists" >&2
        fi
    done
}

if [ "${1:-}" = --fix-cases ]; then
    fix_cases
    exit 0
fi

if [ ! -x "$sys/rvgl" ]; then
    echo "rvgl: $sys/rvgl is missing; reinstall rvgl-bin." >&2
    exit 1
fi
if [ ! -d "$sys/packs/game_files" ]; then
    echo "rvgl: no Re-Volt game data in $sys/packs/game_files; install revolt-data-revoltio or revolt-data-steam." >&2
    exit 1
fi

mkdir -p "$packs/local"

# Drop links to packs that were uninstalled, then link the installed ones.
# A real folder of the same name in ~/.local/share/RVGL/packs is left alone.
for l in "$packs"/*; do
    [ -L "$l" ] || continue
    case $(readlink "$l") in
        "$sys"/packs/*) [ -e "$l" ] || rm -f "$l" ;;
    esac
done
for p in "$sys"/packs/*/; do
    p=${p%/} n=${p##*/}
    if [ -L "$packs/$n" ] || [ ! -e "$packs/$n" ]; then
        ln -sfn "$p" "$packs/$n"
    fi
done

# The packlist. Keep your own packlists under another name and select them
# with "rvgl -packlist <name>"; this one is rewritten on every start.
{
    for n in $order; do
        [ -d "$sys/packs/$n" ] && printf '"%s"\n' "$n"
    done
    for p in "$sys"/packs/*/; do
        p=${p%/} n=${p##*/}
        case " $order " in *" $n "*) continue ;; esac
        printf '"%s"\n' "$n"
    done
    printf '"local" *\n'
} > "$packs/rvgl.txt.new"
mv -f "$packs/rvgl.txt.new" "$packs/rvgl.txt"

packlist="-packlist rvgl"
for a in "$@"; do
    [ "$a" = -packlist ] && packlist=
done

cd "$data"
# Upstream's bundled libunistring.so.2 (distributions ship .so.5).
LD_LIBRARY_PATH=$sys/lib${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}
export LD_LIBRARY_PATH
# shellcheck disable=SC2086 # $packlist is two words or empty
exec "$sys/rvgl" -basepath "$data" -prefpath "$data" $packlist "$@"
