Name:           balun
Version:        0.2.1
Release:        1%{?dist}
Summary:        Lightweight cross-platform HDHomeRun live TV viewer
License:        GPL-3.0-or-later
URL:            https://github.com/jm2/balun
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        install.sh

ExclusiveArch:  x86_64 aarch64
BuildRequires:  cargo >= 1.98
BuildRequires:  rust >= 1.98
BuildRequires:  gcc
BuildRequires:  pkgconf-pkg-config
BuildRequires:  pkgconfig(gtk4) >= 4.16
BuildRequires:  pkgconfig(libadwaita-1) >= 1.6
BuildRequires:  pkgconfig(gstreamer-1.0) >= 1.20
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

Requires:       gtk4 >= 4.16
Requires:       libadwaita >= 1.6
Requires:       gstreamer1 >= 1.20
Requires:       gstreamer1-plugins-base
Requires:       gstreamer1-plugins-good
Requires:       gstreamer1-plugins-bad-free
Requires:       gstreamer1-plugin-gtk4
Requires:       gstreamer1-plugin-libav
Requires:       hicolor-icon-theme

%description
Balun is a lightweight cross-platform HDHomeRun live TV viewer built with
GTK 4, libadwaita and GStreamer. It discovers tuners on the local network or
on an approved private subnet, lists their channel lineups and plays
unprotected live channels.

%prep
%autosetup -n %{name}-%{version}

%build
# Crates are fetched from crates.io (local builds only).
export CARGO_HOME=%{_builddir}/cargo-home
# Keep symbols so rpm can split them into -debuginfo and strip the binary.
export CARGO_PROFILE_RELEASE_STRIP=false CARGO_PROFILE_RELEASE_DEBUG=line-tables-only
# Fedora's RUSTFLAGS ask for one codegen unit and full debug info, which with
# the crate's LTO takes a lot of memory in one rustc process. rustc uses the
# last value given for a -C option, so these override them and keep the rest.
export RUSTFLAGS="${RUSTFLAGS:-} -Ccodegen-units=16 -Cdebuginfo=line-tables-only"
cargo build --release --locked --features desktop --bin balun

%install
sh %{SOURCE1} . %{buildroot}

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
%{_docdir}/balun/

%changelog
* Wed Nov 11 2026 John-Michael Mulesa <jmulesa@gmail.com> - 0.2.1-1
- Local RPM build of balun 0.2.1
