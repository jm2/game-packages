# The PKGBUILD follows the git master branch; this spec builds a pinned
# commit of it (bump commit/snapdate and the Version together).
%global commit 51fccb9b01faa8694b00be36a6262ff73b876d5a
%global shortcommit %(c=%{commit}; echo ${c:0:8})
%global snapdate 20261031

Name:           lilium-voyager-git
Version:        0^%{snapdate}git%{shortcommit}
Release:        1%{?dist}
Summary:        An ioquake3-based Voyager: Elite Force source port
License:        GPL-2.0-or-later
URL:            https://clover.moe/lilium-voyager/
Source0:        https://github.com/zturtleman/lilium-voyager/archive/%{commit}/lilium-voyager-%{commit}.tar.gz
Source1:        q3make.sh
Source2:        lilium-voyager.desktop
Source3:        lilium-voyager-server.service
Source4:        README.md

ExclusiveArch:  x86_64 aarch64

BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconf-pkg-config
# The Makefile looks pkg-config up with which.
BuildRequires:  which
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(mad)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(opusfile)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(vorbisfile)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  systemd-rpm-macros

Requires:       hicolor-icon-theme
Suggests:       eliteforce-data
Suggests:       mumble
Provides:       lilium-voyager = %{version}-%{release}
Conflicts:      lilium-voyager

%description
Lilium Voyager is an ioquake3-based engine for Star Trek Voyager: Elite Force
Holomatch (multiplayer), with widescreen support (ZTM's Flexible Display),
modern renderers and the original gameplay. It needs the retail baseEF pk3
files in /opt/lilium-voyager/baseEF (eliteforce-data-gog installs them).


%prep
%autosetup -n lilium-voyager-%{commit}
cp -p %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} .


%build
%set_build_flags
sh ./q3make.sh build .


%install
sh ./q3make.sh install . %{buildroot} %{name}


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/lilium-voyager.desktop


%post
%systemd_post lilium-voyager-server.service

%preun
%systemd_preun lilium-voyager-server.service

%postun
%systemd_postun_with_restart lilium-voyager-server.service


%files
%license COPYING.txt
%{_docdir}/%{name}/
%dir /opt/lilium-voyager
%dir /opt/lilium-voyager/baseEF
/opt/lilium-voyager/lilium-voyager
/opt/lilium-voyager/lilium-voyager-server
/opt/lilium-voyager/lilium-voyager-renderer-*.so
%{_bindir}/lilium-voyager
%{_bindir}/lilium-voyager-server
%{_bindir}/liliumvoyhm
%{_bindir}/liliumvoyded
%{_unitdir}/lilium-voyager-server.service
%{_datadir}/applications/lilium-voyager.desktop
%{_datadir}/icons/hicolor/256x256/apps/lilium-voyager.png
%{_datadir}/icons/hicolor/scalable/apps/lilium-voyager.svg


%changelog
* Mon Nov 02 2026 John-Michael Mulesa <jmulesa@gmail.com> - 0^20261031git51fccb9b-1
- Initial RPM package, built from commit 51fccb9 of zturtleman/lilium-voyager
