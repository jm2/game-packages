# carryout-bin

carryout (<https://github.com/jm2/carryout>) downloads Google Takeout
exports: it fetches, resumes and verifies every archive part. This package
repackages upstream's release archives (`carryout_<version>_linux_amd64.tar.gz`
and `_arm64.tar.gz`, which hold the static binary, README.md and LICENSE) for
x86_64 and aarch64. It provides, conflicts with and replaces the
source-built `carryout` package.

The README is installed as `/usr/share/doc/carryout-bin/README.md`.
