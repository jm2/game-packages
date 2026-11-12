# Built from the same pinned commit as the PKGBUILD, with its Pomme submodule
# fetched as a GitHub archive of the commit the superproject records.
%global commit 04f65c36f6db0218be3869d40fb26f17d8109de8
%global pomme_commit 0251ee2d5654bd1d33a2b3f35a5ebfd47f97e8e7
# No LTO, as upstream: with -ffp-contract=off it keeps floating-point results
# identical across LAN peers (lockstep netcode).
%global _lto_cflags %{nil}

Name:           cro-mag-rally-net
Version:        3.2.0
Release:        1%{?dist}
Summary:        Prehistoric kart racer from Pangea Software (experimental LAN build)
License:        CC-BY-NC-SA-4.0 AND MIT
URL:            https://github.com/jm2/CroMagRally
Source0:        %{url}/archive/%{commit}/CroMagRally-%{commit}.tar.gz
Source1:        https://github.com/jm2/Pomme/archive/%{pomme_commit}/Pomme-%{pomme_commit}.tar.gz
Source2:        cro-mag-rally.desktop
Source3:        cro-mag-rally.sh
Source4:        install.sh

ExclusiveArch:  x86_64 aarch64

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(gl)
BuildRequires:  SDL3-devel

Requires:       hicolor-icon-theme
Provides:       cro-mag-rally = %{version}-%{release}
Conflicts:      cro-mag-rally

%description
Cro-Mag Rally is Pangea Software's prehistoric kart racer, updated for modern
systems by Iliyas Jorio. This build adds experimental LAN multiplayer.


%prep
%autosetup -n CroMagRally-%{commit}
rmdir extern/Pomme
tar -xf %{SOURCE1} -C extern
mv extern/Pomme-%{pomme_commit} extern/Pomme
cp -p %{SOURCE2} %{SOURCE3} %{SOURCE4} .


%build
# Pomme is linked statically, as upstream builds it; SDL3 comes from the system
# (upstream defaults to building its extern/SDL3 submodule).
%cmake -DBUILD_SHARED_LIBS=OFF -DBUILD_SDL_FROM_SOURCE=OFF -DBUILD_TESTING=OFF -Wno-dev
%cmake_build


%install
sh ./install.sh . %{_vpath_builddir} %{buildroot} %{version} %{name}
cp -p extern/Pomme/LICENSE.md Pomme-LICENSE.md


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/cro-mag-rally.desktop


%files
%license LICENSE.md Pomme-LICENSE.md
%{_docdir}/%{name}/
%{_bindir}/cro-mag-rally
%{_prefix}/lib/cro-mag-rally/
%{_datadir}/applications/cro-mag-rally.desktop
%{_datadir}/icons/hicolor/256x256/apps/cro-mag-rally.png
%{_datadir}/icons/hicolor/512x512/apps/cro-mag-rally.png


%changelog
* Wed Nov 04 2026 John-Michael Mulesa <jmulesa@gmail.com> - 3.2.0-1
- Update to 3.2.0 (commit 04f65c3, Pomme 0251ee2)
- Build against the system SDL3 and without the test suite; no LTO, as upstream

* Mon Nov 02 2026 John-Michael Mulesa <jmulesa@gmail.com> - 3.0.2-5
- Initial RPM package, built from commit 1345101 of jm2/CroMagRally
