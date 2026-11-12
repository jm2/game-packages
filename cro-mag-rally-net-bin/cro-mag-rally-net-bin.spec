# Prebuilt upstream binaries: nothing to strip or extract debuginfo from.
%global debug_package %{nil}
%global __strip /bin/true
%global _build_id_links none
# The bundled SDL3 in /usr/lib/cromagrally is private: don't advertise it as
# a system-wide provide, and don't require its soname from the system.
%global __provides_exclude_from ^%{_prefix}/lib/cromagrally/.*$
%global __requires_exclude ^libSDL3\\.so.*$

Name:           cro-mag-rally-net-bin
Version:        3.2.0
Release:        1%{?dist}
Summary:        Prehistoric kart racer from Pangea Software (LAN build, prebuilt binary)
# Game (CC-BY-NC-SA-4.0) and the bundled SDL3, Pomme and support code; see
# THIRD-PARTY-LICENSES.md.
License:        CC-BY-NC-SA-4.0 AND Zlib AND MIT AND LGPL-2.1-or-later AND BSD-3-Clause AND BSL-1.0 AND CC0-1.0 AND Apache-2.0 AND SunPro
URL:            https://github.com/jm2/CroMagRally
# Upstream's release RPMs; only the build architecture's one is unpacked.
Source0:        %{url}/releases/download/v%{version}/CroMagRally-%{version}-linux-x86_64.rpm
Source1:        %{url}/releases/download/v%{version}/CroMagRally-%{version}-linux-aarch64.rpm
Source2:        install.sh
Source3:        README.md

ExclusiveArch:  x86_64 aarch64

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  rpm
BuildRequires:  tar

Requires:       hicolor-icon-theme
# The bundled SDL3 dlopen()s its video and audio backends.
Recommends:     libX11
Recommends:     libXcursor
Recommends:     libXext
Recommends:     libXfixes
Recommends:     libXi
Recommends:     libXrandr
Recommends:     libwayland-client
Recommends:     libxkbcommon
Recommends:     libdecor
Recommends:     (pulseaudio-libs or alsa-lib)

Provides:       cro-mag-rally-net = %{version}-%{release}
Obsoletes:      cro-mag-rally-net < 3.2.0-2
Conflicts:      cro-mag-rally-net
Provides:       cro-mag-rally = %{version}-%{release}
Conflicts:      cro-mag-rally

%description
Cro-Mag Rally is Pangea Software's prehistoric kart racer, ported to modern
systems by Iliyas Jorio. This build of the jm2 fork adds multiplayer over a
wired or Wi-Fi local network.

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
cp -p %{SOURCE2} %{SOURCE3} .


%build
# Prebuilt binaries; nothing to build.


%install
sh ./install.sh root %{buildroot} %{_docdir}/%{name} %{_defaultlicensedir}/%{name}


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/io.jor.cromagrally.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/io.jor.cromagrally.metainfo.xml


%files
%license %{_defaultlicensedir}/%{name}/
%{_docdir}/%{name}/
%{_bindir}/cromagrally
%{_bindir}/cro-mag-rally
%{_prefix}/lib/cromagrally/
%{_datadir}/cromagrally/
%{_datadir}/applications/io.jor.cromagrally.desktop
%{_metainfodir}/io.jor.cromagrally.metainfo.xml
%{_datadir}/icons/hicolor/512x512/apps/io.jor.cromagrally.png


%changelog
* Wed Nov 11 2026 John-Michael Mulesa <jmulesa@gmail.com> - 3.2.0-1
- Repackage upstream's 3.2.0 release RPMs as cro-mag-rally-net-bin, replacing
  the source-built cro-mag-rally-net package
