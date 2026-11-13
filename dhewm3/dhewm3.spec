# Builds the base and d3xp (Resurrection of Evil) game libraries and the
# dedicated server, against SDL3. The engine's base path is /opt/doom3, where
# the doom3-data-* and doom3xp-data-* packages install the retail .pk4 files.
# Fedora doesn't package dhewm3; Debian does (no debian/ here).

Name:           dhewm3
Version:        1.5.5
Release:        2%{?dist}
Summary:        Doom 3 source port with SDL3, OpenAL and 64-bit support
# Engine: GPL-3.0-or-later with id Software's additional terms. Bundled:
# Dear ImGui and miniz (MIT), stb_image (MIT OR Unlicense), minizip (Zlib).
License:        GPL-3.0-or-later AND MIT AND Zlib AND (MIT OR Unlicense)
URL:            https://dhewm3.org/
Source0:        https://github.com/dhewm/dhewm3/archive/%{version}/dhewm3-%{version}.tar.gz
Source1:        d3make.sh
Source2:        org.dhewm3.Dhewm3.desktop
Source3:        org.dhewm3.Dhewm3.d3xp.desktop
Source4:        README.md

ExclusiveArch:  x86_64 aarch64

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  cmake(SDL3)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(zlib)

Requires:       hicolor-icon-theme
Requires:       doom3-data
Recommends:     doom3xp-data
Provides:       bundled(imgui)
Provides:       bundled(miniz)
Provides:       bundled(minizip)
Provides:       bundled(stb_image)

%description
dhewm3 is a Doom 3 GPL source port with SDL3, OpenAL and 64-bit support. This
package contains the engine, the dedicated server and the game libraries for
Doom 3 and its Resurrection of Evil expansion. It looks for the retail .pk4
files in /opt/doom3/base and /opt/doom3/d3xp, where the Steam and GOG data
packages of this repository install them.


%prep
%autosetup -n dhewm3-%{version}
cp -p %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} .


%build
%set_build_flags
sh ./d3make.sh build . %{_vpath_builddir} %{_lib}


%install
sh ./d3make.sh install . %{_vpath_builddir} %{buildroot} %{name}
install -Dm644 neo/libs/imgui/LICENSE.txt LICENSE.imgui.txt


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.dhewm3.Dhewm3.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/org.dhewm3.Dhewm3.d3xp.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/org.dhewm3.Dhewm3.metainfo.xml


%files
%license COPYING.txt LICENSE.imgui.txt
%{_docdir}/%{name}/
%{_bindir}/dhewm3
%{_bindir}/dhewm3ded
%{_libdir}/dhewm3/
%dir /opt/doom3
%dir /opt/doom3/base
%dir /opt/doom3/d3xp
/opt/doom3/base/gamepad.cfg
/opt/doom3/d3xp/gamepad-d3xp.cfg
%{_datadir}/applications/org.dhewm3.Dhewm3.desktop
%{_datadir}/applications/org.dhewm3.Dhewm3.d3xp.desktop
%{_datadir}/icons/hicolor/128x128/apps/org.dhewm3.Dhewm3.png
%{_datadir}/icons/hicolor/256x256/apps/org.dhewm3.Dhewm3.png
%{_datadir}/icons/hicolor/scalable/apps/org.dhewm3.Dhewm3.svg
%{_metainfodir}/org.dhewm3.Dhewm3.metainfo.xml


%changelog
* Thu Nov 12 2026 John-Michael Mulesa <jmulesa@gmail.com> - 1.5.5-2
- Rebuild without set-group-ID bits on its directories (RPM refused to install it beside the data packages)

* Fri Nov 06 2026 John-Michael Mulesa <jmulesa@gmail.com> - 1.5.5-1
- Initial RPM package
