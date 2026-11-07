# Fedora's own quake2 package is an older Yamagi release that reads its data
# from /usr/lib64/games/quake2; this one reads /usr/share/games/quake2
# (quake2-data-gog/-steam) and has the mission pack game libraries as
# separate packages. Both can be installed side by side.

Name:           yamagi-quake2
Version:        8.70
Release:        1%{?dist}
Summary:        Enhanced Quake II engine optimized for modern systems
# Bundled: Info-ZIP unzip, miniz (MIT), GLAD (MIT), stb (MIT OR Unlicense),
# zlib-licensed bits; the engine itself is GPL-2.0-or-later.
License:        GPL-2.0-or-later AND Info-ZIP AND Zlib AND MIT AND (MIT OR Unlicense)
URL:            https://www.yamagi.org/quake2/
Source0:        https://deponie.yamagi.org/quake2/quake2-%{version}.tar.xz
Source1:        install.sh
Source2:        yamagi-quake2.desktop
Source3:        yamagi-q2ded.service
Source4:        README.md

ExclusiveArch:  x86_64 aarch64

BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconf-pkg-config
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(sdl3)

Requires:       hicolor-icon-theme
Requires:       quake2-data
# OpenAL and cURL are loaded at run time.
Recommends:     openal-soft
Recommends:     libcurl
Suggests:       yamagi-quake2-ref_vk
Suggests:       yamagi-quake2-xatrix
Suggests:       yamagi-quake2-rogue
Suggests:       yamagi-quake2-ctf
Provides:       yquake2 = %{version}-%{release}
Provides:       bundled(miniz)
Provides:       bundled(stb_image)
Provides:       bundled(stb_vorbis)

%description
Yamagi Quake II is an enhanced Quake II engine focused on single player:
the gameplay and graphics are unchanged, but many bugs are fixed. It is
built with the OpenGL 1.4, OpenGL 3.2, OpenGL ES 3 and software renderers,
and reads the game data from /usr/share/games/quake2.


%prep
%autosetup -n quake2-%{version}
cp -p %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} .


%build
%set_build_flags
sh ./install.sh build .


%install
sh ./install.sh install . %{buildroot} %{name} %{buildroot}%{_licensedir}/%{name}


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/yamagi-quake2.desktop


%post
%systemd_post yamagi-q2ded.service

%preun
%systemd_preun yamagi-q2ded.service

%postun
%systemd_postun_with_restart yamagi-q2ded.service


%files
%{_licensedir}/%{name}/
%{_docdir}/%{name}/
%dir %{_prefix}/lib/yamagi-quake2
%{_prefix}/lib/yamagi-quake2/quake2
%{_prefix}/lib/yamagi-quake2/q2ded
%{_prefix}/lib/yamagi-quake2/ref_*.so
%{_prefix}/lib/yamagi-quake2/baseq2/
%{_bindir}/yamagi-quake2
%{_bindir}/yamagi-q2ded
%{_unitdir}/yamagi-q2ded.service
%{_datadir}/applications/yamagi-quake2.desktop
%{_datadir}/icons/hicolor/512x512/apps/yamagi-quake2.png
%{_datadir}/icons/hicolor/scalable/apps/yamagi-quake2.svg


%changelog
* Fri Nov 06 2026 John-Michael Mulesa <jmulesa@gmail.com> - 8.70-1
- Initial RPM package
