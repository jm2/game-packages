# transom-bin

Transom (<https://github.com/jm2/transom>) is a HiDPI-correct RDP client
built with GTK 4 and libadwaita in Rust, on FreeRDP and the transom-view
display widget.

This package repackages upstream's release `.pkg.tar.zst` (Arch x86_64).

Run `transom`, or start "Transom" from the desktop menu.

Hardware H.264 decoding is optional: install `libva-mesa-driver` (AMD) or
`intel-media-driver` (Intel), plus `vulkan-icd-loader` for GTK's Vulkan
renderer, which shows the hardware-decoded video.

There is no Fedora package here: on Fedora, use upstream's COPR,
`dnf copr enable jmsqrd/transom` (package `transom`), which takes precedence.
