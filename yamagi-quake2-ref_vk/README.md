# yamagi-quake2-ref_vk

The Vulkan renderer for Yamagi Quake II (<https://github.com/yquake2/ref_vk>),
a port of vkQuake2's renderer, built from the latest stable release. It is
installed next to the engine as `/usr/lib/yamagi-quake2/ref_vk.so`.

Select it in the video menu, or with `+set vid_renderer vk` (then
`vid_restart` from the console). `r_validation 1` turns on the Vulkan
validation layers, if they are installed.

On Debian the package is called `yamagi-quake2-ref-vk` (no underscores in
Debian package names) and works with Debian's own `yamagi-quake2`, which
uses the same `/usr/lib/yamagi-quake2` directory but ships only the OpenGL
renderers. On Arch and Fedora it goes with this repository's
`yamagi-quake2`.
