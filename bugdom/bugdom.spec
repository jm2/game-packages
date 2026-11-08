# Built from the 1.3.4 release tarball, with the Pomme submodule fetched as a
# GitHub archive of the commit the release records.
%global pomme_commit ef94150e2dcec522e3099f4d03a4e8f2639f7232

Name:           bugdom
Version:        1.3.4
Release:        1%{?dist}
Summary:        3D action-adventure about a pill bug, from Pangea Software
License:        CC-BY-NC-SA-4.0 AND MIT
URL:            https://github.com/jorio/Bugdom
Source0:        %{url}/archive/1.3.4/Bugdom-%{version}.tar.gz
Source1:        https://github.com/jorio/Pomme/archive/%{pomme_commit}/Pomme-%{pomme_commit}.tar.gz
Source2:        bugdom.desktop
Source3:        bugdom.sh
Source4:        install.sh

ExclusiveArch:  x86_64 aarch64

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  patch
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(sdl2)

Requires:       hicolor-icon-theme

%description
Bugdom is Pangea Software's 3D action-adventure: Rollie McFly the pill bug
sets out to save Bugdom from King Thorax and his Fire Ants.
Updated for modern systems by Iliyas Jorio.


%prep
%autosetup -n Bugdom-%{version}
rmdir extern/Pomme
tar -xf %{SOURCE1} -C extern
mv extern/Pomme-%{pomme_commit} extern/Pomme
cp -p %{SOURCE2} %{SOURCE3} %{SOURCE4} .


%build
# Pomme is linked statically, as upstream builds it.
%cmake -DBUILD_SHARED_LIBS=OFF -Wno-dev
%cmake_build


%install
sh ./install.sh . %{_vpath_builddir} %{buildroot} %{version} %{name}
cp -p extern/Pomme/LICENSE.md Pomme-LICENSE.md


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/bugdom.desktop


%files
%license LICENSE.md Pomme-LICENSE.md
%{_docdir}/%{name}/
%{_bindir}/bugdom
%{_prefix}/lib/bugdom/
%{_datadir}/applications/bugdom.desktop
%{_datadir}/icons/hicolor/512x512/apps/bugdom.png


%changelog
* Sat Nov 07 2026 John-Michael Mulesa <jmulesa@gmail.com> - 1.3.4-1
- Initial RPM package, following the AUR package
