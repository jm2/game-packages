# Built from the v3.0.2 release tarball, with the Pomme submodule fetched as a
# GitHub archive of the commit the release records.
%global pomme_commit ad9cc177d2187f67bd00cb6cf2b3045ef91c577b

Name:           mightymike
Version:        3.0.2
Release:        1%{?dist}
Summary:        Top-down action game in a toy store gone mad, from Pangea Software
License:        CC-BY-NC-SA-4.0 AND MIT
URL:            https://github.com/jorio/mightymike
Source0:        %{url}/archive/v3.0.2/mightymike-%{version}.tar.gz
Source1:        https://github.com/jorio/Pomme/archive/%{pomme_commit}/Pomme-%{pomme_commit}.tar.gz
Source2:        mightymike.desktop
Source3:        mightymike.sh
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
Mighty Mike (originally Power Pete) is Pangea Software's top-down action
game: rescue the Fuzzy Puppies from a toy store gone mad.
Updated for modern systems by Iliyas Jorio.


%prep
%autosetup -n MightyMike-%{version}
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
desktop-file-validate %{buildroot}%{_datadir}/applications/mightymike.desktop


%files
%license LICENSE.md Pomme-LICENSE.md
%{_docdir}/%{name}/
%{_bindir}/mightymike
%{_prefix}/lib/mightymike/
%{_datadir}/applications/mightymike.desktop
%{_datadir}/icons/hicolor/512x512/apps/mightymike.png


%changelog
* Sat Nov 07 2026 John-Michael Mulesa <jmulesa@gmail.com> - 3.0.2-1
- Initial RPM package, following the AUR package
