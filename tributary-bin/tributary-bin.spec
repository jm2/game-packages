# Prebuilt upstream binaries: nothing to strip or extract debuginfo from.
%global debug_package %{nil}
%global __strip /bin/true
%global _build_id_links none

Name:           tributary-bin
Version:        0.7.2
Release:        1%{?dist}
Summary:        Rhythmbox-style media manager with local and remote backends (prebuilt)
License:        GPL-3.0-or-later
URL:            https://github.com/jm2/tributary
# Upstream's release RPMs; only the build architecture's one is unpacked.
# They carry no license file, so it comes from the tagged source.
Source0:        %{url}/releases/download/v%{version}/tributary-x86_64.rpm#/tributary-%{version}-x86_64.rpm
Source1:        %{url}/releases/download/v%{version}/tributary-aarch64.rpm#/tributary-%{version}-aarch64.rpm
Source2:        https://raw.githubusercontent.com/jm2/tributary/v%{version}/LICENSE#/tributary-%{version}-LICENSE
Source3:        install.sh
Source4:        README.md

ExclusiveArch:  x86_64 aarch64

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  rpm
BuildRequires:  tar

Requires:       gtk4 >= 4.16
Requires:       libadwaita >= 1.6
Requires:       gstreamer1-plugins-good
Requires:       gstreamer1-plugins-bad-free
Requires:       gstreamer1-plugins-ugly-free
Requires:       gstreamer1-libav
Requires:       dbus
Requires:       hicolor-icon-theme

Provides:       tributary = %{version}-%{release}
Obsoletes:      tributary < 0.7.2-3
Conflicts:      tributary

%description
Tributary is a Rhythmbox-style music manager for GNOME, written in Rust with
GTK4 and libadwaita. One library view browses and plays local music alongside
Subsonic/Navidrome, Jellyfin and Plex servers, DAAP shares and internet radio.

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
desktop-file-validate %{buildroot}%{_datadir}/applications/io.github.jm2.tributary.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/io.github.jm2.tributary.metainfo.xml

%files
%license LICENSE
%{_bindir}/tributary
%{_datadir}/applications/io.github.jm2.tributary.desktop
%{_metainfodir}/io.github.jm2.tributary.metainfo.xml
%{_datadir}/icons/hicolor/*/apps/io.github.jm2.tributary.png
%{_datadir}/icons/hicolor/scalable/actions/io.github.jm2.tributary-equalizer-symbolic.svg
%{_docdir}/%{name}/

%changelog
* Wed Nov 11 2026 John-Michael Mulesa <jmulesa@gmail.com> - 0.7.2-1
- Repackage upstream's 0.7.2 release RPMs as tributary-bin, replacing the
  source-built tributary package
