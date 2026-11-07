# The PKGBUILD follows the main branch; this spec builds a pinned commit of it
# (bump commit/snapdate and the Version together). The engine's base path is
# /opt/prey, where prey-data-steam installs the retail .pk4 files.
%global commit 1d9d18d733946d2315886410d6642f4977f0971b
%global shortcommit %(c=%{commit}; echo ${c:0:8})
%global snapdate 20261101

Name:           prey2006-git
Version:        0^%{snapdate}git%{shortcommit}
Release:        1%{?dist}
Summary:        Prey (2006) source port based on dhewm3 and the Prey SDK
# Engine: Doom 3 GPL (GPL-3.0-or-later with id's additional terms). Game code
# and base/ assets: Prey SDK, no licence text in the repository (README.md).
# Bundled: Dear ImGui, miniz (MIT), stb_image (MIT OR Unlicense), minizip and
# mikktspace (Zlib).
License:        GPL-3.0-or-later AND LicenseRef-Prey-SDK AND MIT AND Zlib AND (MIT OR Unlicense)
URL:            https://github.com/glKarin/Prey2006
Source0:        %{url}/archive/%{commit}/Prey2006-%{commit}.tar.gz
Source1:        preymake.sh
Source2:        README.md
Source3:        LicenseRef-Prey-SDK.txt

ExclusiveArch:  x86_64 aarch64

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gcc-c++
# CMakeModules/GitBranch.cmake requires git (the branch is left empty in a tarball).
BuildRequires:  git-core
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(zlib)

Requires:       hicolor-icon-theme
Requires:       prey-data
Provides:       prey2006 = %{version}-%{release}
Conflicts:      prey2006
Provides:       bundled(imgui)
Provides:       bundled(miniz)
Provides:       bundled(minizip)
Provides:       bundled(stb_image)

%description
Prey2006 integrates the Prey (2006) SDK game code with a dhewm3-based Doom 3
GPL engine. It is unfinished: upstream lists known blockers and multiplayer
is untested. It needs the retail base/pak000.pk4 to pak004.pk4 files in
/opt/prey/base (prey-data-steam installs them).


%prep
%autosetup -n Prey2006-%{commit}
cp -p %{SOURCE1} %{SOURCE2} %{SOURCE3} .


%build
%set_build_flags
sh ./preymake.sh build . %{_vpath_builddir}


%install
sh ./preymake.sh install . %{_vpath_builddir} %{buildroot} %{name}
install -Dm644 .github/COPYING.txt COPYING.txt
install -Dm644 neo/libs/imgui/LICENSE.txt LICENSE.imgui.txt


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/io.github.friskthefallenhuman.prey2006.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/io.github.friskthefallenhuman.prey2006.metainfo.xml


%files
%license COPYING.txt LICENSE.imgui.txt LicenseRef-Prey-SDK.txt
%{_docdir}/%{name}/
%{_bindir}/prey06
%{_bindir}/prey06ded
/opt/prey/
%{_datadir}/applications/io.github.friskthefallenhuman.prey2006.desktop
%{_datadir}/icons/hicolor/256x256/apps/io.github.friskthefallenhuman.prey2006.png
%{_datadir}/icons/hicolor/scalable/apps/io.github.friskthefallenhuman.prey2006.svg
%{_metainfodir}/io.github.friskthefallenhuman.prey2006.metainfo.xml


%changelog
* Fri Nov 06 2026 John-Michael Mulesa <jmulesa@gmail.com> - 0^20261101git1d9d18d7-1
- Initial RPM package, built from commit 1d9d18d of glKarin/Prey2006
