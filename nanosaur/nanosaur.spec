# Built from the v1.4.4 release tarball, with the Pomme submodule fetched as a
# GitHub archive of the commit the release records.
%global pomme_commit fd1cd2cf81a2d39a4e47e76485860a87f0bf33f6

Name:           nanosaur
Version:        1.4.4
Release:        1%{?dist}
Summary:        Cybernetic dinosaur third-person shooter from Pangea Software
License:        CC-BY-NC-SA-4.0 AND MIT AND LicenseRef-Pangea
URL:            https://github.com/jorio/Nanosaur
Source0:        %{url}/archive/v1.4.4/Nanosaur-%{version}.tar.gz
Source1:        https://github.com/jorio/Pomme/archive/%{pomme_commit}/Pomme-%{pomme_commit}.tar.gz
Source2:        nanosaur.desktop
Source3:        nanosaur.sh
Source4:        install.sh
Source5:        pomme-cstdint.patch
Source6:        LICENSE.upstream

ExclusiveArch:  x86_64 aarch64

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  patch
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(sdl2)

Requires:       hicolor-icon-theme

%description
Nanosaur is Pangea Software's third-person shooter: a cybernetic dinosaur
sends eggs to the future before a meteor hits the Earth.
Updated for modern systems by Iliyas Jorio.


%prep
%autosetup -n Nanosaur-%{version}
rmdir extern/Pomme
tar -xf %{SOURCE1} -C extern
mv extern/Pomme-%{pomme_commit} extern/Pomme
# <cstdint> includes for GCC 13+, from Pomme d57c28e.
patch -d extern/Pomme -p1 < %{SOURCE5}
cp -p %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5} %{SOURCE6} .


%build
# Pomme is linked statically, as upstream builds it.
%cmake -DBUILD_SHARED_LIBS=OFF -Wno-dev
%cmake_build


%install
sh ./install.sh . %{_vpath_builddir} %{buildroot} %{version} %{name}
cp -p extern/Pomme/LICENSE.md Pomme-LICENSE.md


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/nanosaur.desktop


%files
%license LICENSE.md Pomme-LICENSE.md LICENSE.upstream
%{_docdir}/%{name}/
%{_bindir}/nanosaur
%{_prefix}/lib/nanosaur/
%{_datadir}/applications/nanosaur.desktop
%{_datadir}/icons/hicolor/512x512/apps/nanosaur.png


%changelog
* Sat Nov 07 2026 John-Michael Mulesa <jmulesa@gmail.com> - 1.4.4-1
- Initial RPM package, following the AUR package
