# Prebuilt upstream binaries: no debuginfo, no stripping, and no automatic
# provides/requires from the private libraries in /opt/unreal-tournament.
%global debug_package %{nil}
%global __strip /bin/true
%global _build_id_links none
# Upstream links ut-bin/ucc-bin with RUNPATH "--strip-all:$ORIGIN" (a linker
# flag typo); $ORIGIN still works, so skip the rpath check instead of patching ELFs.
%global __brp_check_rpaths %{nil}
%global __provides_exclude_from ^/opt/unreal-tournament/.*$
%global __requires_exclude_from ^/opt/unreal-tournament/.*$

Name:           unreal-tournament-bin
Version:        469e
Release:        1%{?dist}
Summary:        Unreal Tournament 99 (GOTY) native binaries (OldUnreal)
License:        LicenseRef-OldUnreal
URL:            https://github.com/OldUnreal/UnrealTournamentPatches
Source0:        %{url}/releases/download/v%{version}/OldUnreal-UTPatch%{version}-Linux-amd64.tar.bz2
Source1:        %{url}/releases/download/v%{version}/OldUnreal-UTPatch%{version}-Linux-arm64.tar.bz2
Source2:        install.sh
Source3:        unreal-tournament.sh
Source4:        unreal-tournament.desktop
Source5:        unreal-tournament.png
Source6:        README.md

ExclusiveArch:  x86_64 aarch64
BuildRequires:  desktop-file-utils
BuildRequires:  tar
BuildRequires:  bzip2

Requires:       unreal-tournament-data
# By soname: the private libraries in /opt are excluded from automatic requires.
Requires:       libSDL2-2.0.so.0()(64bit)
Requires:       libopenal.so.1()(64bit)
Requires:       libasound.so.2()(64bit)
Requires:       libGL.so.1()(64bit)
# libfmod and the bundled SDL2_ttf
Requires:       libstdc++.so.6()(64bit)
Requires:       libfreetype.so.6()(64bit)
Requires:       hicolor-icon-theme
Provides:       unreal-tournament = %{version}-%{release}
Obsoletes:      unreal-tournament-goty-steam < 469f

%description
Native Linux binaries for Unreal Tournament (GOTY) from OldUnreal's community
patch, installed to /opt/unreal-tournament. The game data comes from a
separate unreal-tournament-data-gog, -data-steam or -data-archiveorg package.

%prep
%setup -q -c -T
mkdir patch
%ifarch aarch64
tar -xjf %{SOURCE1} -C patch
%else
tar -xjf %{SOURCE0} -C patch
%endif
install -m644 patch/LICENSE.md LICENSE.md
cp -p %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5} %{SOURCE6} .

%build

%install
sh install.sh patch . %{buildroot} %{_target_cpu}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/unreal-tournament.desktop

%files
%license LICENSE.md
%doc %{_docdir}/unreal-tournament-bin/
%{_bindir}/unreal-tournament
%{_datadir}/applications/unreal-tournament.desktop
%{_datadir}/icons/hicolor/256x256/apps/unreal-tournament.png
/opt/unreal-tournament/Help/
/opt/unreal-tournament/System/
/opt/unreal-tournament/SystemLocalized/
/opt/unreal-tournament/Textures/
/opt/unreal-tournament/Web/
%dir /opt/unreal-tournament

%changelog
* Mon Nov 02 2026 John-Michael Mulesa <jmulesa@gmail.com> - 469e-1
- Initial RPM package: OldUnreal 469e
