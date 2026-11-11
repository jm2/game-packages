# umu-launcher

[umu](https://github.com/Open-Wine-Components/umu-launcher) runs Windows games
with Proton and the Steam Linux Runtime outside of Steam. gamelaunch uses it by
default (`GAMELAUNCH_RUNNER=umu`), so the Wine game packages here depend on
`umu-launcher` or `wine`.

No distribution packages it (Arch has only an outdated AUR package; Fedora and
Debian none), so this repo builds upstream's release for Arch, Fedora and
Debian, on x86_64 and aarch64.

- Fedora and Arch use the system pyzstd and urllib3. Debian has no
  python3-pyzstd, so its build carries upstream's vendored copy; pyzstd,
  xxhash and cbor2 only enable delta updates of Proton and the runtime.
- On aarch64, umu installs but doesn't yet run x86 Windows games: upstream's
  arm64 runtime support is unfinished (umu-launcher #716, #479).
