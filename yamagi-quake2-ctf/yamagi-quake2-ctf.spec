%global mod ctf

Name:           yamagi-quake2-%{mod}
Version:        1.13
Release:        1%{?dist}
Summary:        Threewave Capture the Flag for Yamagi Quake II
License:        GPL-2.0-or-later
URL:            https://www.yamagi.org/quake2/
Source0:        https://deponie.yamagi.org/quake2/quake2-%{mod}-%{version}.tar.xz
Source1:        install.sh
Source2:        yamagi-quake2-%{mod}.sh
Source3:        yamagi-quake2-%{mod}.desktop
Source4:        README.md

ExclusiveArch:  x86_64 aarch64

BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  make

Requires:       yamagi-quake2

%description
The game library for Threewave Capture the Flag, for the
Yamagi Quake II engine. The game data is read from
/usr/share/games/quake2/%{mod} (quake2-data-gog or quake2-data-steam).


%prep
%autosetup -n quake2-%{mod}-%{version}
cp -p %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} .


%build
%set_build_flags
sh ./install.sh build .


%install
sh ./install.sh install . %{buildroot} %{name} %{buildroot}%{_licensedir}/%{name}


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/yamagi-quake2-%{mod}.desktop


%files
%{_licensedir}/%{name}/
%{_docdir}/%{name}/
%dir %{_prefix}/lib/yamagi-quake2/%{mod}
%{_prefix}/lib/yamagi-quake2/%{mod}/game.so
%{_bindir}/yamagi-quake2-%{mod}
%{_datadir}/applications/yamagi-quake2-%{mod}.desktop


%changelog
* Fri Nov 06 2026 John-Michael Mulesa <jmulesa@gmail.com> - 1.13-1
- Initial RPM package
