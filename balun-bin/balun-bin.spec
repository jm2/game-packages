# Prebuilt upstream binaries: nothing to strip or extract debuginfo from.
%global debug_package %{nil}
%global __strip /bin/true
%global _build_id_links none

Name:           balun-bin
Version:        0.2.1
Release:        1%{?dist}
Summary:        Lightweight cross-platform HDHomeRun live TV viewer (prebuilt binary)
License:        GPL-3.0-or-later
URL:            https://github.com/jm2/balun
# Upstream's release RPMs; only the build architecture's one is unpacked.
Source0:        %{url}/releases/download/v%{version}/balun-x86_64.rpm#/balun-%{version}-x86_64.rpm
Source1:        %{url}/releases/download/v%{version}/balun-aarch64.rpm#/balun-%{version}-aarch64.rpm
Source2:        https://raw.githubusercontent.com/jm2/balun/v%{version}/LICENSE#/balun-%{version}-LICENSE
Source3:        install.sh
Source4:        README.md

ExclusiveArch:  x86_64 aarch64

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  rpm
BuildRequires:  tar

Requires:       gtk4 >= 4.16
Requires:       libadwaita >= 1.6
Requires:       gstreamer1 >= 1.20
Requires:       gstreamer1-plugins-base
Requires:       gstreamer1-plugins-good
Requires:       gstreamer1-plugins-bad-free
Requires:       gstreamer1-plugin-gtk4
Requires:       gstreamer1-plugin-libav
Requires:       hicolor-icon-theme

Provides:       balun = %{version}-%{release}
Obsoletes:      balun < 0.2.1-2
Conflicts:      balun

%description
Balun is a lightweight cross-platform HDHomeRun live TV viewer built with
GTK 4, libadwaita and GStreamer. It discovers tuners on the local network or
on an approved private subnet, lists their channel lineups and plays
unprotected live channels.

This package repackages upstream's release RPM.

%prep
%setup -q -c -T
mkdir root
%ifarch x86_64
rpm2archive -n %{SOURCE0} | tar -xf - -C root
%endif
%ifarch aarch64
rpm2archive -n %{SOURCE1} | tar -xf - -C root
%endif
cp -p %{SOURCE2} LICENSE
cp -p %{SOURCE3} %{SOURCE4} .

%build
# Prebuilt binaries; nothing to build.

%install
sh ./install.sh root %{buildroot} %{name}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/io.github.jm2.Balun.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/io.github.jm2.Balun.metainfo.xml

%files
%license LICENSE
%{_bindir}/balun
%{_datadir}/applications/io.github.jm2.Balun.desktop
%{_metainfodir}/io.github.jm2.Balun.metainfo.xml
%{_datadir}/icons/hicolor/*/apps/io.github.jm2.Balun.png
%{_datadir}/icons/hicolor/scalable/apps/io.github.jm2.Balun.svg
%{_datadir}/icons/hicolor/symbolic/apps/io.github.jm2.Balun-symbolic.svg
%{_docdir}/%{name}/

%changelog
* Wed Nov 11 2026 John-Michael Mulesa <jmulesa@gmail.com> - 0.2.1-1
- Repackage upstream's 0.2.1 release RPMs as balun-bin, replacing the
  source-built balun package
