# Prebuilt upstream binaries: nothing to strip or extract debuginfo from.
%global debug_package %{nil}
%global __strip /bin/true
%global _build_id_links none
# The bundled runtime in /opt/kisakcod/lib is private: don't advertise it as
# system-wide provides, and don't require its sonames from the system.
%global __provides_exclude_from ^/opt/kisakcod/.*$
%global __requires_exclude ^(libSDL3|libopenal|libavformat|libavcodec|libavutil|libdxvk_d3d9)\\.so.*$

# Upstream names its archives by architecture tag.
%ifarch x86_64
%global kcarch x64
%endif
%ifarch aarch64
%global kcarch arm64
%endif

Name:           kisakcod-bin
Version:        0.1.0
Release:        1%{?dist}
Summary:        Native Call of Duty 4 multiplayer client and server (binary release)
License:        GPL-3.0-only AND BSD-3-Clause AND Zlib AND LGPL-2.1-or-later AND LGPL-2.0-or-later
URL:            https://github.com/jm2/kisakcod
Source0:        %{url}/releases/download/v%{version}/kisakcod-%{version}-linux-x64-client.tar.xz
Source1:        %{url}/releases/download/v%{version}/kisakcod-%{version}-linux-arm64-client.tar.xz
Source2:        kisakcod.sh
Source3:        kisakcod.desktop
Source4:        install.sh
Source5:        README.md

ExclusiveArch:  x86_64 aarch64

BuildRequires:  desktop-file-utils
BuildRequires:  tar
BuildRequires:  xz

Requires:       hicolor-icon-theme
# dxvk-native dlopen()s the Vulkan loader, which rpmbuild cannot see.
Requires:       vulkan-loader
# SDL3 dlopen()s its video and audio backends.
Recommends:     libX11
Recommends:     libXcursor
Recommends:     libXext
Recommends:     libXfixes
Recommends:     libXi
Recommends:     libXrandr
Recommends:     libXScrnSaver
Recommends:     libwayland-client
Recommends:     libwayland-cursor
Recommends:     libwayland-egl
Recommends:     libxkbcommon
Recommends:     libdecor
Recommends:     pulseaudio-libs
Suggests:       cod4-data

Provides:       kisakcod = %{version}-%{release}
Conflicts:      kisakcod

%description
KisakCOD is a native 64-bit reimplementation of the Call of Duty 4: Modern
Warfare (1.8) multiplayer client and dedicated server. It bundles its runtime
(SDL3, OpenAL Soft, Bink-only FFmpeg, dxvk-native) and renders through Vulkan.

It contains no game data: it needs your own Steam copy of Call of Duty 4,
which it reads from /opt/cod4 (cod4-data-steam) by default. Set
KISAKCOD_COD4_PATH or pass "+set fs_basepath <dir>" to use another location.


%prep
%setup -q -c -T
%ifarch x86_64
tar -xf %{SOURCE0}
%endif
%ifarch aarch64
tar -xf %{SOURCE1}
%endif
# The x64 archive unpacks to kisakcod-<ver>-linux-amd64, arm64 to -linux-arm64.
mv kisakcod-%{version}-linux-* kisakcod
cp -p %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5} .
cp -p kisakcod/LICENSE LICENSE


%build
# Prebuilt binaries; nothing to build.


%install
sh ./install.sh kisakcod %{buildroot} %{name}


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/kisakcod.desktop


%files
%license LICENSE
%{_docdir}/%{name}/
/opt/kisakcod/
%{_bindir}/kisakcod
%{_bindir}/kisakcod-dedi
%{_datadir}/applications/kisakcod.desktop
%{_datadir}/icons/hicolor/scalable/apps/kisakcod.svg


%changelog
* Mon Nov 02 2026 John-Michael Mulesa <jmulesa@gmail.com> - 0.1.0-1
- Initial package of the KisakCOD 0.1.0 binary release
