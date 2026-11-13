# Prebuilt upstream binaries: no debuginfo, no stripping, and no automatic
# provides/requires from the private library in /opt/rvgl.
%global debug_package %{nil}
%global __strip /bin/true
%global _build_id_links none
%global __provides_exclude_from ^/opt/rvgl/.*$
%global __requires_exclude_from ^/opt/rvgl/.*$

Name:           rvgl-bin
Version:        23.1030a1
Release:        2%{?dist}
Summary:        RVGL, the cross-platform rewrite of the Re-Volt R/C car racing game
License:        CC-BY-NC-SA-4.0 AND (LGPL-3.0-or-later OR GPL-2.0-or-later)
URL:            https://rvgl.org
Source0:        https://rvgl.org/downloads/rvgl_%{version}_linux.7z
Source1:        install.sh
Source2:        rvgl.sh
Source3:        rvgl.desktop
Source4:        rvgl.xml
Source5:        README.md

ExclusiveArch:  x86_64 aarch64
BuildRequires:  bsdtar
BuildRequires:  desktop-file-utils

Requires:       revolt-data
# By soname: the binary in /opt is excluded from automatic requires.
Requires:       libSDL2-2.0.so.0()(64bit)
Requires:       libSDL2_image-2.0.so.0()(64bit)
Requires:       libopenal.so.1()(64bit)
Requires:       libenet.so.7()(64bit)
Requires:       libvorbisfile.so.3()(64bit)
Requires:       libGL.so.1()(64bit)
Requires:       hicolor-icon-theme
# Owns /usr/lib/firewalld/services.
Requires:       firewalld-filesystem
Recommends:     rvgl-dcpack
Recommends:     rvgl-soundtrack
Suggests:       libsndfile
Suggests:       mpg123-libs
Suggests:       flac-libs
Suggests:       fluidsynth-libs
Provides:       rvgl = %{version}-%{release}
Conflicts:      rvgl

%description
RVGL is the RV Team's cross-platform rewrite of Acclaim's Re-Volt (1999),
the radio-controlled car racing game. This package installs the engine and
RVGL's asset pack to /opt/rvgl and a launcher that keeps settings, saves and
custom content in ~/.local/share/RVGL. The original game data comes from a
separate revolt-data-revoltio or revolt-data-steam package.

%prep
%setup -q -c -T
mkdir rvgl
bsdtar -xf %{SOURCE0} -C rvgl
cp -p %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5} .

%build

%install
sh install.sh rvgl . %{buildroot} %{_target_cpu}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/rvgl.desktop

%files
%license %{_datadir}/licenses/rvgl-bin/
%doc %{_docdir}/rvgl-bin/
%{_bindir}/rvgl
%{_datadir}/applications/rvgl.desktop
%{_datadir}/icons/hicolor/*/apps/rvgl.png
%{_prefix}/lib/firewalld/services/rvgl.xml
/opt/rvgl/

%changelog
* Thu Nov 12 2026 John-Michael Mulesa <jmulesa@gmail.com> - 23.1030a1-2
- Rebuild without set-group-ID bits on its directories (RPM refused to install it beside the data packages)

* Thu Nov 05 2026 John-Michael Mulesa <jmulesa@gmail.com> - 23.1030a1-1
- Initial package: RVGL 23.1030a1 with RVGL Launcher's pack layout
