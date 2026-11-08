# Built from the v4.0.0 release tarball, with the Pomme submodule fetched as a
# GitHub archive of the commit the release records.
%global pomme_commit c6a38eab19a11847024a13f9b3e2af0c2d908c3e

Name:           bugdom2
Version:        4.0.0
Release:        1%{?dist}
Summary:        Sequel to Bugdom, from Pangea Software
License:        CC-BY-NC-SA-4.0 AND MIT
URL:            https://github.com/jorio/Bugdom2
Source0:        %{url}/archive/v4.0.0/Bugdom2-%{version}.tar.gz
Source1:        https://github.com/jorio/Pomme/archive/%{pomme_commit}/Pomme-%{pomme_commit}.tar.gz
Source2:        bugdom2.desktop
Source3:        bugdom2.sh
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
Bugdom 2 is Pangea Software's sequel to Bugdom: Skip the grasshopper tracks
down the Bully Bee to get his knapsack back.
Updated for modern systems by Iliyas Jorio.


%prep
%autosetup -n Bugdom2-%{version}
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
desktop-file-validate %{buildroot}%{_datadir}/applications/bugdom2.desktop


%files
%license LICENSE.md Pomme-LICENSE.md
%{_docdir}/%{name}/
%{_bindir}/bugdom2
%{_prefix}/lib/bugdom2/
%{_datadir}/applications/bugdom2.desktop
%{_datadir}/icons/hicolor/512x512/apps/bugdom2.png


%changelog
* Sat Nov 07 2026 John-Michael Mulesa <jmulesa@gmail.com> - 4.0.0-1
- Initial RPM package, following the AUR package
