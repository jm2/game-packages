# UNPUBLISHED: the openETQW v0.1.0 release on jm2/openETQW is still a draft,
# so Source0/Source1 return 404 until it is published. To build before then,
# put the two linux tarballs from
#   gh release download v0.1.0 -R jm2/openETQW -p 'openetqw-0.1.0-linux-x64.tar.xz' -p 'openetqw-0.1.0-linux-arm64.tar.xz'
# into the SOURCES directory.

# Prebuilt upstream binaries: nothing to strip or extract debuginfo from.
%global debug_package %{nil}
%global __strip /bin/true
%global _build_id_links none
# The engine's bundled SDL3 and its modules are private to /opt/openetqw.
%global __provides_exclude_from ^/opt/openetqw/.*$
%global __requires_exclude ^libSDL3\\.so.*$
# The payload is mostly already-compressed pk4 (zip) data.
%global _binary_payload w3.zstdio

%global commit 90bc0382eaf7280ca3745ddfbb998420b2ce6571
%global etqwver 1.5

# Upstream names its binaries and modules by architecture tag.
%ifarch x86_64
%global oearch x64
%endif
%ifarch aarch64
%global oearch arm64
%endif

Name:           openetqw-bin
Version:        0.1.0
Release:        1%{?dist}
Summary:        Open-source Enemy Territory: QUAKE Wars engine (binary release)
License:        GPL-3.0-or-later AND LicenseRef-ETQW-SDK-EULA AND LicenseRef-ETQW-EULA AND LicenseRef-ETQW-Retail AND Zlib AND MIT AND BSD-3-Clause AND BSD-2-Clause AND Apache-2.0
URL:            https://github.com/jm2/openETQW
Source0:        %{url}/releases/download/v%{version}/openetqw-%{version}-linux-x64.tar.xz
Source1:        %{url}/releases/download/v%{version}/openetqw-%{version}-linux-arm64.tar.xz
# ET:QW 1.5 Linux client patch, for the patch paks (pak005-pak008).
Source2:        https://cdn.splashdamage.com/downloads/games/etqw/ETQW-client-%{etqwver}-full.x86.run
Source3:        https://raw.githubusercontent.com/jm2/openETQW/%{commit}/tools/build/linux/openetqw.desktop
Source4:        https://raw.githubusercontent.com/jm2/openETQW/%{commit}/assets/icons/etqw_icon.png
Source5:        openetqw.sh
Source6:        install.sh
Source7:        README.md

ExclusiveArch:  x86_64 aarch64

BuildRequires:  bsdtar
BuildRequires:  desktop-file-utils
BuildRequires:  patchelf
BuildRequires:  tar
BuildRequires:  xz

Requires:       hicolor-icon-theme
# dlopen()ed at runtime (Vulkan is the default renderer, SDL3's video and
# audio backends, the folder chooser), so not picked up automatically.
Recommends:     vulkan-loader
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
Recommends:     (zenity or kdialog)
Suggests:       etqw-data

Provides:       openetqw = %{version}-%{release}
Conflicts:      openetqw

%description
openETQW is an open-source engine for Enemy Territory: QUAKE Wars 1.5, with
a Vulkan renderer (OpenGL fallback), dedicated server and the retail game
module rebuilt from id Software's ET:QW SDK.

This package includes the ET:QW 1.5 patch paks (pak005.pk4 - pak008.pk4 and
the English zpaks) extracted from id Software's Linux 1.5 client patch. You
still need the retail base data (base/pak000.pk4 - pak004.pk4, megatextures,
video). openETQW looks in /opt/etqw first, then in Steam, retail and Wine
installs; set OPENETQW_BASEPATH or pass "+set fs_basepath <dir>" to use
another location.


%prep
%setup -q -c -T
%ifarch x86_64
tar -xf %{SOURCE0}
%endif
%ifarch aarch64
tar -xf %{SOURCE1}
%endif
mv openetqw-%{version}-linux-%{oearch} openetqw
# The patch is a MojoSetup archive (shell stub + zip).
mkdir etqw-%{etqwver}
bsdtar -xf %{SOURCE2} -C etqw-%{etqwver} \
    'data/base/pak00[5-8].pk4' 'data/base/zpak_english00[1-3].pk4' data/EULA.txt
cp -p %{SOURCE3} %{SOURCE4} %{SOURCE5} %{SOURCE6} %{SOURCE7} .


%build
# Prebuilt binaries; nothing to build.


%install
sh ./install.sh openetqw etqw-%{etqwver}/data %{buildroot} %{oearch} %{name} \
    %{buildroot}%{_licensedir}/%{name}


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/openetqw.desktop


%files
%{_licensedir}/%{name}/
%{_docdir}/%{name}/
/opt/openetqw/
%{_bindir}/openetqw
%{_bindir}/openetqw-dedicated
%{_datadir}/applications/openetqw.desktop
%{_datadir}/icons/hicolor/256x256/apps/openetqw.png


%changelog
* Mon Nov 02 2026 John-Michael Mulesa <jmulesa@gmail.com> - 0.1.0-1
- Initial package of the openETQW 0.1.0 binary release (unpublished draft)
