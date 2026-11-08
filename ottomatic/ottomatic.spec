# Built from the 4.0.1 release tarball, with the Pomme submodule fetched as a
# GitHub archive of the commit the release records.
%global pomme_commit ad9cc177d2187f67bd00cb6cf2b3045ef91c577b

Name:           ottomatic
Version:        4.0.1
Release:        1%{?dist}
Summary:        3D action game starring a robot, from Pangea Software
License:        CC-BY-NC-SA-4.0 AND MIT
URL:            https://github.com/jorio/ottomatic
Source0:        %{url}/archive/4.0.1/ottomatic-%{version}.tar.gz
Source1:        https://github.com/jorio/Pomme/archive/%{pomme_commit}/Pomme-%{pomme_commit}.tar.gz
Source2:        ottomatic.desktop
Source3:        ottomatic.sh
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
Otto Matic is Pangea Software's 3D action game: the robot Otto saves the
Earth from the Giant Brain from Planet X.
Updated for modern systems by Iliyas Jorio.


%prep
%autosetup -n OttoMatic-%{version}
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
desktop-file-validate %{buildroot}%{_datadir}/applications/ottomatic.desktop


%files
%license LICENSE.md Pomme-LICENSE.md
%{_docdir}/%{name}/
%{_bindir}/ottomatic
%{_prefix}/lib/ottomatic/
%{_datadir}/applications/ottomatic.desktop
%{_datadir}/icons/hicolor/512x512/apps/ottomatic.png


%changelog
* Sat Nov 07 2026 John-Michael Mulesa <jmulesa@gmail.com> - 4.0.1-1
- Initial RPM package, following the AUR package
