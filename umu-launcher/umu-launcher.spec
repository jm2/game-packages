# Based on upstream's packaging/rpm/umu-launcher.spec (1.4.4), without the
# Fedora <= 42 branches and with a plain release number.
Name:           umu-launcher
Version:        1.4.4
Release:        1%{?dist}
Summary:        Unified Launcher for Windows games on Linux, running Proton outside of Steam
License:        GPL-3.0-only
URL:            https://github.com/Open-Wine-Components/umu-launcher
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz

# The delta-update module (umu_delta, Rust) is a native library.
ExclusiveArch:  x86_64 aarch64

BuildRequires:  make
BuildRequires:  cargo
BuildRequires:  scdoc
BuildRequires:  python3-devel
BuildRequires:  python3-build
BuildRequires:  python3-installer
BuildRequires:  python3-hatchling
BuildRequires:  python3-hatch-vcs
BuildRequires:  python3-wheel
BuildRequires:  python3-pyzstd
BuildRequires:  python3-urllib3
BuildRequires:  python3-xlib

Requires:       python3
Requires:       python3-xlib
Requires:       python3-urllib3
Requires:       python3-pyzstd
Recommends:     python3-cbor2
Recommends:     python3-xxhash
Recommends:     python3-truststore

%description
umu is the Unified Launcher for Windows games on Linux: it runs games with
Proton and the Steam Linux Runtime, with the game fixes Proton has in Steam,
outside of Steam.

%prep
%autosetup -p 1

%build
./configure.sh --prefix=/usr --use-system-pyzstd --use-system-urllib
make

%install
make DESTDIR=%{buildroot} PYTHONDIR=%{python3_sitelib} install
%py3_shebang_fix %{buildroot}%{_bindir}/umu-run

%files
%license LICENSE
%{_bindir}/umu-run
%{_mandir}/man*/umu*
%{python3_sitelib}/umu*

%changelog
* Wed Nov 11 2026 John-Michael Mulesa <jmulesa@gmail.com> - 1.4.4-1
- Package 1.4.4 for Fedora x86_64 and aarch64 (upstream ships no Fedora 45 build)
