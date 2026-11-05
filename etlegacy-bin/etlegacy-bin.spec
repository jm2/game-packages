# Prebuilt upstream binaries: nothing to strip or extract debuginfo from.
%global debug_package %{nil}
%global __strip /bin/true
%global _build_id_links none
# The game modules and Omni-Bot are private to /opt/etlegacy; the system
# libraries they need (libc, libstdc++, libGL) are still required.
%global __provides_exclude_from ^/opt/etlegacy/.*$

Name:           etlegacy-bin
Version:        2.86.2
Release:        1%{?dist}
Summary:        Open-source Wolfenstein: Enemy Territory compatible engine (binary release)
License:        GPL-3.0-or-later AND LicenseRef-Omni-bot
URL:            https://www.etlegacy.com/
# Only published on etlegacy.com (the GitHub tags have no assets).
Source0:        https://www.etlegacy.com/download/file/785#/etlegacy-v%{version}-x86_64.tar.gz
Source1:        https://www.etlegacy.com/download/file/796#/etlegacy-v%{version}-aarch64.tar.gz
Source2:        etl.sh
Source3:        install.sh
Source4:        etlegacy.desktop
Source5:        etlegacy-server.service
Source6:        etlegacy.xml
Source7:        README.md

ExclusiveArch:  x86_64 aarch64

BuildRequires:  desktop-file-utils
BuildRequires:  gzip
BuildRequires:  systemd-rpm-macros
BuildRequires:  tar

Requires:       enemy-territory-data
Requires:       hicolor-icon-theme
# The aarch64 build has its renderer built in and dlopen()s GL.
Requires:       libGL.so.1()(64bit)
# dlopen()ed by the bundled SDL and OpenAL support, so not picked up
# automatically.
Recommends:     libX11
Recommends:     libXcursor
Recommends:     libXext
Recommends:     libXfixes
Recommends:     libXi
Recommends:     libXrandr
Recommends:     libXScrnSaver
Recommends:     libwayland-client
Recommends:     libwayland-cursor
Recommends:     libwayland-egl
Recommends:     libxkbcommon
Recommends:     pulseaudio-libs
Suggests:       openal-soft

Provides:       etlegacy = %{version}-%{release}
Conflicts:      etlegacy

%description
ET: Legacy is an open-source engine for Wolfenstein: Enemy Territory 2.60b
with its own Legacy mod (Omni-Bot, WolfAdmin, ETTV). This is upstream's
prebuilt release in /opt/etlegacy, with the etl client, the etlded dedicated
server (and a systemd unit and firewalld service for it). The original game
data (pak0-pak2.pk3) comes from enemy-territory-data in
/usr/share/enemy-territory/etmain.

The 64-bit engine only joins servers whose mod has a 64-bit build (ETrun,
ETJump, N!tmod, Legacy, ...).


%prep
%setup -q -c -T
%ifarch x86_64
tar -xf %{SOURCE0}
%endif
%ifarch aarch64
tar -xf %{SOURCE1}
%endif
cp -p %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5} %{SOURCE6} %{SOURCE7} .


%build
# Prebuilt binaries; nothing to build.


%install
sh ./install.sh etlegacy-v%{version}-%{_arch} %{buildroot} %{_arch} %{name} \
    %{buildroot}%{_licensedir}/%{name}


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/etlegacy.desktop


%post
%systemd_post etlegacy-server.service

%preun
%systemd_preun etlegacy-server.service

%postun
%systemd_postun_with_restart etlegacy-server.service


%files
%{_licensedir}/%{name}/
%{_docdir}/%{name}/
/opt/etlegacy/
%{_bindir}/etl
%{_bindir}/etlded
%{_mandir}/man6/etl.6*
%{_mandir}/man6/etlded.6*
%{_unitdir}/etlegacy-server.service
%{_prefix}/lib/firewalld/services/etlegacy.xml
%{_datadir}/applications/etlegacy.desktop
%{_datadir}/icons/hicolor/scalable/apps/etlegacy.svg


%changelog
* Thu Nov 05 2026 John-Michael Mulesa <jmulesa@gmail.com> - 2.86.2-1
- Initial package of the ET: Legacy 2.86.2 binary release
