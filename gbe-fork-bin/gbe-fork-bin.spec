# Prebuilt upstream binaries (and Windows DLLs): nothing to strip or debuginfo.
%global debug_package %{nil}
%global __strip /bin/true
%global _build_id_links none
# Private libraries for game packages, not system providers; the 32-bit and
# arm64 copies must not pull in foreign-arch dependencies.
%global __provides_exclude_from ^%{_prefix}/lib/gbe-fork/.*$
%global __requires_exclude_from ^%{_prefix}/lib/gbe-fork/.*$

%global tag release-2026_09_27

Name:           gbe-fork-bin
Version:        2026.09.27
Release:        2%{?dist}
Summary:        Goldberg Steam Emulator (gbe_fork) prebuilt steam_api for game packages
License:        LGPL-3.0-or-later
URL:            https://github.com/Detanup01/gbe_fork
Source0:        %{url}/releases/download/%{tag}/emu-win-release-vs26.7z#/emu-win-release-vs26-%{version}.7z
Source1:        %{url}/releases/download/%{tag}/emu-linux-release.tar.bz2#/emu-linux-release-%{version}.tar.bz2
Source2:        https://raw.githubusercontent.com/Detanup01/gbe_fork/%{tag}/LICENSE#/LICENSE-%{version}
Source3:        install.sh

ExclusiveArch:  x86_64 aarch64
BuildRequires:  bsdtar

Requires:       libstdc++
Provides:       gbe-fork = %{version}-%{release}
Provides:       goldberg-emu = %{version}-%{release}

%description
Prebuilt release of gbe_fork, the maintained fork of Mr_Goldberg's Steam
emulator. Game packages in jm2/linux-packages link their steam_api(64).dll or
libsteam_api.so to the copies in /opt/gbe-fork (Windows) and
/usr/lib/gbe-fork (Linux), so an emulator update
reaches every game without rebuilding it. Also ships gbe-steam-interfaces,
which writes steam_interfaces.txt for an original steam_api library.

%prep
%setup -q -c -T
mkdir win lin
bsdtar -xf %{SOURCE0} -C win
bsdtar -xf %{SOURCE1} -C lin
cp -p %{SOURCE2} LICENSE

%build

%install
%ifarch aarch64
sh %{SOURCE3} win lin %{buildroot} ARM64
%else
sh %{SOURCE3} win lin %{buildroot} x64
%endif

%files
%license LICENSE
%{_bindir}/gbe-generate-interfaces
%{_bindir}/gbe-lobby-connect
%{_bindir}/gbe-steam-interfaces
%{_prefix}/lib/gbe-fork/
/opt/gbe-fork/
%{_datadir}/gbe-fork/
%{_docdir}/gbe-fork/

%changelog
* Sat Nov 07 2026 John-Michael Mulesa <jmulesa@gmail.com> - 2026.09.27-2
- Move the Windows builds to /opt/gbe-fork so umu/Proton's container can see them

* Mon Nov 02 2026 John-Michael Mulesa <jmulesa@gmail.com> - 2026.09.27-1
- Initial package of gbe_fork release-2026_09_27 (vs26 Windows build)
