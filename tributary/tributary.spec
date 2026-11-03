Name:           tributary
Version:        0.7.2
Release:        1%{?dist}
Summary:        Rhythmbox-style media manager with unified local and remote backends
License:        GPL-3.0-or-later
URL:            https://github.com/jm2/tributary
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        install.sh

ExclusiveArch:  x86_64 aarch64
BuildRequires:  cargo
BuildRequires:  rust >= 1.94
BuildRequires:  gcc
BuildRequires:  pkgconf-pkg-config
BuildRequires:  glib2-devel
BuildRequires:  pkgconfig(gtk4) >= 4.16
BuildRequires:  pkgconfig(libadwaita-1) >= 1.6
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

Requires:       gtk4 >= 4.16
Requires:       libadwaita >= 1.6
Requires:       gstreamer1-plugins-good
Requires:       gstreamer1-plugins-bad-free
Requires:       gstreamer1-plugins-ugly-free
Requires:       gstreamer1-libav
Requires:       dbus
Requires:       hicolor-icon-theme

%description
Tributary is a Rhythmbox-style music manager for GNOME, written in Rust with
GTK4 and libadwaita. One library view browses and plays local music alongside
Subsonic/Navidrome, Jellyfin and Plex servers, DAAP shares and internet radio.

%prep
%autosetup -n %{name}-%{version}

%build
# Crates are fetched from crates.io (local builds only).
export CARGO_HOME=%{_builddir}/cargo-home
# Keep symbols so rpm can split them into -debuginfo and strip the binary.
export CARGO_PROFILE_RELEASE_STRIP=false CARGO_PROFILE_RELEASE_DEBUG=line-tables-only
cargo build --release --locked

%install
sh %{SOURCE1} . %{buildroot}

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
%{_docdir}/tributary/

%changelog
* Mon Nov 02 2026 John-Michael Mulesa <jmulesa@gmail.com> - 0.7.2-1
- Local RPM build of tributary 0.7.2
