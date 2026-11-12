# carryout-bin

carryout (<https://github.com/jm2/carryout>) downloads Google Takeout
exports: it fetches, resumes and verifies every archive part. This package
repackages upstream's release packages for x86_64 and aarch64: the
`.pkg.tar.zst` on Arch x86_64 and the `.deb` on Debian/Ubuntu. It provides, conflicts with and replaces the
source-built `carryout` package.

The README is installed as `/usr/share/doc/carryout-bin/README.md`.

There is no Fedora package here: on Fedora, use upstream's COPR,
`dnf copr enable jmsqrd/carryout` (package `carryout`), which takes precedence.
