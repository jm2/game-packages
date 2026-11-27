# umu-launcher

[umu](https://github.com/Open-Wine-Components/umu-launcher) runs Windows games
with Proton and the Steam Linux Runtime outside of Steam. gamelaunch uses it by
default (`GAMELAUNCH_RUNNER=umu`), so the Wine game packages here depend on
`umu-launcher` or `wine`.

Arch has it in multilib, which the Wine games need anyway for their lib32
dependencies, so there is no PKGBUILD here. Fedora and Debian don't package it,
so this repo builds upstream's release for them, on x86_64 and aarch64.

- Fedora uses the system pyzstd and urllib3. Debian has no python3-pyzstd, so
  its build carries upstream's vendored copy; pyzstd, xxhash and cbor2 only
  enable delta updates of Proton and the runtime.
- On aarch64, umu installs but doesn't yet run x86 Windows games: upstream's
  arm64 runtime support is unfinished (umu-launcher #716, #479).
