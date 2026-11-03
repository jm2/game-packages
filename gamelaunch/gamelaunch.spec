Name:           gamelaunch
Version:        1.0.0
Release:        1%{?dist}
Summary:        Shared launcher for wine/Proton and native game packages
License:        0BSD
URL:            https://github.com/jm2/linux-packages
Source0:        gamelaunch
Source1:        gamelaunch.conf.5.md
Source2:        LICENSE
BuildArch:      noarch

Requires:       bash
Requires:       coreutils
Requires:       findutils
Recommends:     umu-launcher
Suggests:       wine
Suggests:       wine-dxvk

%description
gamelaunch runs the Windows and native games packaged in jm2/linux-packages
from a per-game config in /usr/share/gamelaunch/games. Windows games run
through umu-launcher (Proton) when it is installed, or through system wine
with the distribution's DXVK. Prefixes, saves and a writable per-user copy of
the game directory live under ~/.local/share/gamelaunch.

%prep
%setup -q -c -T
cp -p %{SOURCE0} %{SOURCE1} %{SOURCE2} .

%build

%install
install -Dm755 gamelaunch -t %{buildroot}%{_bindir}/
install -dm755 %{buildroot}%{_datadir}/gamelaunch/games %{buildroot}%{_sysconfdir}/gamelaunch/games

%files
%license LICENSE
%doc gamelaunch.conf.5.md
%{_bindir}/gamelaunch
%dir %{_datadir}/gamelaunch
%dir %{_datadir}/gamelaunch/games
%dir %{_sysconfdir}/gamelaunch
%dir %{_sysconfdir}/gamelaunch/games

%changelog
* Mon Nov 02 2026 John-Michael Mulesa <jmulesa@gmail.com> - 1.0.0-1
- Initial package
