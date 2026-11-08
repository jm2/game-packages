# Built from the v2.1.0 release tarball, with the Pomme submodule fetched as a
# GitHub archive of the commit the release records.
%global pomme_commit 6e4ea042ba9e7e525d3930e45662be15605153c4

Name:           nanosaur2
Version:        2.1.0
Release:        1%{?dist}
Summary:        Sequel to Nanosaur, from Pangea Software
License:        CC-BY-NC-SA-4.0 AND MIT
URL:            https://github.com/jorio/Nanosaur2
Source0:        %{url}/archive/v2.1.0/Nanosaur2-%{version}.tar.gz
Source1:        https://github.com/jorio/Pomme/archive/%{pomme_commit}/Pomme-%{pomme_commit}.tar.gz
Source2:        nanosaur2.desktop
Source3:        nanosaur2.sh
Source4:        install.sh
Source5:        pomme-cstdint.patch

ExclusiveArch:  x86_64 aarch64

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  patch
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(sdl2)

Requires:       hicolor-icon-theme

%description
Nanosaur 2: Hatchling is Pangea Software's sequel to Nanosaur, a flying
shooter starring a cybernetic pterodactyl.
Updated for modern systems by Iliyas Jorio.


%prep
%autosetup -n Nanosaur2-%{version}
rmdir extern/Pomme
tar -xf %{SOURCE1} -C extern
mv extern/Pomme-%{pomme_commit} extern/Pomme
# <cstdint> includes for GCC 13+, from Pomme d57c28e.
patch -d extern/Pomme -p1 < %{SOURCE5}
cp -p %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5} .


%build
# Pomme is linked statically, as upstream builds it.
%cmake -DBUILD_SHARED_LIBS=OFF -Wno-dev
%cmake_build


%install
sh ./install.sh . %{_vpath_builddir} %{buildroot} %{version} %{name}
cp -p extern/Pomme/LICENSE.md Pomme-LICENSE.md


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/nanosaur2.desktop


%files
%license LICENSE.md Pomme-LICENSE.md
%{_docdir}/%{name}/
%{_bindir}/nanosaur2
%{_prefix}/lib/nanosaur2/
%{_datadir}/applications/nanosaur2.desktop
%{_datadir}/icons/hicolor/256x256/apps/nanosaur2.png


%changelog
* Sat Nov 07 2026 John-Michael Mulesa <jmulesa@gmail.com> - 2.1.0-1
- Initial RPM package, following the AUR package
