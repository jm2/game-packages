Name:           gamelaunch
Version:        1.2.0
Release:        2%{?dist}
Summary:        Shared launcher for wine/Proton and native game packages
License:        0BSD
URL:            https://github.com/jm2/game-packages
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
gamelaunch runs the Windows and native games packaged in jm2/game-packages
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
* Wed Nov 11 2026 John-Michael Mulesa <jmulesa@gmail.com> - 1.2.0-2
- Project URL: the repository is now jm2/game-packages

* Sun Nov 08 2026 John-Michael Mulesa <jmulesa@gmail.com> - 1.2.0-1
- WINE_PRELOAD / WINE_PRELOAD_VARIANTS: LD_PRELOAD Linux libraries into Wine games

* Sat Nov 07 2026 John-Michael Mulesa <jmulesa@gmail.com> - 1.1.2-1
- xlln: use /opt/xlln (visible inside umu's container), fall back to /usr/lib/xlln

* Sat Nov 07 2026 John-Michael Mulesa <jmulesa@gmail.com> - 1.1.1-1
- wine: warn when Fedora's wine-dxvk is set to wined3d (no Vulkan at install time)

* Fri Nov 06 2026 John-Michael Mulesa <jmulesa@gmail.com> - 1.1.0-1
- GAME_DIR=@prefix and BOOTSTRAP_URL: self-updating clients installed into the prefix
- umu: judge prefix creation by the prefix, not umu-run's exit status

* Wed Nov 04 2026 John-Michael Mulesa <jmulesa@gmail.com> - 1.0.2-1
- WINE_USER=hostname and GAMELAUNCH_USER: run a Wine game under a chosen Windows username

* Tue Nov 03 2026 John-Michael Mulesa <jmulesa@gmail.com> - 1.0.1-1
- Suppress the wine-mono/gecko prompts when creating a wine-backend prefix
- x86 emulation on aarch64 (FEX/box64, muvm on 16K-page systems)

* Mon Nov 02 2026 John-Michael Mulesa <jmulesa@gmail.com> - 1.0.0-1
- Initial package
