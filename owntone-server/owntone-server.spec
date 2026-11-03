Name:           owntone-server
Version:        29.3
Release:        1%{?dist}
Summary:        DAAP (iTunes), MPD and RSP media server with AirPlay and Chromecast support
License:        GPL-2.0-or-later
URL:            https://github.com/owntone/owntone-server
# The release tarball ships the generated configure script, parsers and web UI.
Source0:        %{url}/releases/download/%{version}/owntone-%{version}.tar.xz
Source1:        install.sh
Source2:        override.conf
Source3:        owntone.sysusers
Source4:        owntone.tmpfiles
Source5:        README.md

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  systemd-rpm-macros
BuildRequires:  libunistring-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libgpg-error-devel
BuildRequires:  libplist-devel
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(avahi-client)
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavfilter)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libconfuse)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libevent)
BuildRequires:  pkgconfig(libprotobuf-c)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libsodium)
BuildRequires:  pkgconfig(libwebsockets)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(mount)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(zlib)

Requires:       avahi
%{?systemd_requires}

%description
OwnTone (formerly forked-daapd) is a DAAP/DACP (iTunes), MPD (Music Player
Daemon) and RSP (Roku) media server. It streams to AirPlay and Chromecast
devices, can be controlled by Apple Remote and MPD clients, and supports
internet radio, Spotify and Last.fm.

%prep
%autosetup -n owntone-%{version}
mkdir pkgfiles
cp -p %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5} pkgfiles/

%build
%configure \
  --with-systemddir=%{_unitdir} \
  --enable-chromecast --with-libwebsockets --with-avahi --with-alsa --with-pulseaudio
%make_build

%install
%make_install
sh %{SOURCE1} pkgfiles %{buildroot} %{name}
# Created by tmpfiles.d; listed as %%ghost so rpm knows who owns it.
install -d %{buildroot}%{_localstatedir}/cache/owntone

%post
%tmpfiles_create %{_tmpfilesdir}/owntone.conf
%systemd_post owntone.service

%preun
%systemd_preun owntone.service

%postun
%systemd_postun_with_restart owntone.service

%files
%license COPYING
%config(noreplace) %{_sysconfdir}/owntone.conf
%{_sbindir}/owntone
%{_libdir}/owntone/
%{_datadir}/owntone/
%{_unitdir}/owntone.service
%{_unitdir}/owntone@.service
%{_unitdir}/owntone.service.d/
%{_sysusersdir}/owntone.conf
%{_tmpfilesdir}/owntone.conf
%ghost %dir %attr(0750,owntone,owntone) %{_localstatedir}/cache/owntone
%{_mandir}/man8/owntone.8*
%{_docdir}/owntone/
%{_docdir}/%{name}/

%changelog
* Mon Nov 02 2026 John-Michael Mulesa <jmulesa@gmail.com> - 29.3-1
- Local RPM build of OwnTone 29.3, running as a sysusers.d owntone user
