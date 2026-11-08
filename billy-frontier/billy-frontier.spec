# Built from the v1.1.1 release tarball, with the Pomme submodule fetched as a
# GitHub archive of the commit the release records.
%global pomme_commit 9fae17d7715314a3a20259ac2e87aa500a977695

Name:           billy-frontier
Version:        1.1.1
Release:        1%{?dist}
Summary:        Cowboys-in-space arcade shooter from Pangea Software
License:        CC-BY-NC-SA-4.0 AND MIT
URL:            https://github.com/jorio/BillyFrontier
Source0:        %{url}/archive/v1.1.1/BillyFrontier-%{version}.tar.gz
Source1:        https://github.com/jorio/Pomme/archive/%{pomme_commit}/Pomme-%{pomme_commit}.tar.gz
Source2:        billy-frontier.desktop
Source3:        billy-frontier.sh
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
Billy Frontier is Pangea Software's "cowboys in space" arcade action game:
duels, stampedes and shooting galleries on a frontier planet.
Updated for modern systems by Iliyas Jorio.


%prep
%autosetup -n BillyFrontier-%{version}
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
desktop-file-validate %{buildroot}%{_datadir}/applications/billy-frontier.desktop


%files
%license LICENSE.md Pomme-LICENSE.md
%{_docdir}/%{name}/
%{_bindir}/billy-frontier
%{_prefix}/lib/billy-frontier/
%{_datadir}/applications/billy-frontier.desktop
%{_datadir}/icons/hicolor/128x128/apps/billy-frontier.png


%changelog
* Sat Nov 07 2026 John-Michael Mulesa <jmulesa@gmail.com> - 1.1.1-1
- Initial RPM package, following the AUR package
