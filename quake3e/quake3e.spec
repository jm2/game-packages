# Upstream publishes dated stable releases (tags like 2026-10-14) next to a
# rolling "latest" build; this builds the newest dated release (bump the
# tag and Version together).
%global tag 2026-10-14

# The renderer libraries are private plugins of the engine.
%global __provides_exclude_from ^/opt/quake3/.*\\.so$

Name:           quake3e
Version:        2026.10.14
Release:        2%{?dist}
Summary:        Improved Quake III Arena engine with OpenGL and Vulkan renderers
License:        GPL-2.0-or-later
URL:            https://github.com/ec-/Quake3e
Source0:        %{url}/archive/refs/tags/%{tag}.tar.gz#/Quake3e-%{tag}.tar.gz
Source1:        q3emake.sh
Source2:        quake3e.desktop
Source3:        quake3e-teamarena.desktop
Source4:        quake3e-server.service
Source5:        README.md

ExclusiveArch:  x86_64 aarch64

BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconf-pkg-config
# The Makefile looks pkg-config up with which.
BuildRequires:  which
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(vorbisfile)
BuildRequires:  systemd-rpm-macros

Requires:       hicolor-icon-theme
# libGL and libvulkan are loaded at run time.
Requires:       libglvnd-glx%{?_isa}
Requires:       quake3-data
Recommends:     vulkan-loader%{?_isa}
Suggests:       quake3-ta-data

%description
Quake3e is an improved Quake III Arena engine based on the id Software source
release, with OpenGL and Vulkan renderers, a faster QVM compiler, better
network code and many fixes, while staying compatible with the original game
and mods. It runs from /opt/quake3, where the quake3-data packages install
the retail baseq3 and missionpack paks.


%prep
%autosetup -n Quake3e-%{tag}
cp -p %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5} .


%build
%set_build_flags
sh ./q3emake.sh build .


%install
sh ./q3emake.sh install . %{buildroot} %{name}


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/quake3e.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/quake3e-teamarena.desktop


%post
%systemd_post quake3e-server.service

%preun
%systemd_preun quake3e-server.service

%postun
%systemd_postun_with_restart quake3e-server.service


%files
%license COPYING.txt
%{_docdir}/%{name}/
%dir /opt/quake3
/opt/quake3/quake3e
/opt/quake3/quake3e.ded
/opt/quake3/quake3e_opengl_*.so
/opt/quake3/quake3e_vulkan_*.so
%{_bindir}/quake3e
%{_bindir}/quake3e-server
%{_bindir}/quake3e.ded
%{_unitdir}/quake3e-server.service
%{_datadir}/applications/quake3e.desktop
%{_datadir}/applications/quake3e-teamarena.desktop
%{_datadir}/icons/hicolor/32x32/apps/quake3e.png
%{_datadir}/icons/hicolor/scalable/apps/quake3e.svg


%changelog
* Wed Nov 11 2026 John-Michael Mulesa <jmulesa@gmail.com> - 2026.10.14-2
- README: Team Arena data now comes with quake3-data-steam

* Fri Nov 06 2026 John-Michael Mulesa <jmulesa@gmail.com> - 2026.10.14-1
- Initial RPM package, built from the 2026-10-14 release
