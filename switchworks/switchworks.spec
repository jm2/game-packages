# Static, stripped Go binaries (CGO_ENABLED=0, -s -w, as upstream builds
# them): there is no debug information to package.
%global debug_package %{nil}

Name:           switchworks
Version:        0.1.7
Release:        1%{?dist}
Summary:        Control plane for coding agents across your machines
License:        GPL-3.0-or-later AND OFL-1.1
URL:            https://github.com/jm2/switchworks
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        install.sh

ExclusiveArch:  x86_64 aarch64
BuildRequires:  golang
BuildRequires:  make
BuildRequires:  systemd-rpm-macros
BuildRequires:  desktop-file-utils
Requires:       hicolor-icon-theme
%{?systemd_requires}

# The tray icon needs a StatusNotifierItem host; GNOME has one through the
# AppIndicator extension.
Suggests:       (gnome-shell-extension-appindicator if gnome-shell)

%description
Switchworks shows every coding-agent session (Codex, Goose and other ACP
agents) on every host in one place, from a browser, a phone or the swk
command line, and lets agents on different machines message each other.

This package installs swk, the swk-tray status icon, systemd user units for
the node and the coordinator, and a system unit that runs the coordinator as
its own switchworks account. Nothing is enabled at install: each user runs
"swk service install" to run the node as themselves, and "swk service
install --system coordinator", run as root, sets up the system coordinator.

%prep
%autosetup -n %{name}-%{version}

%build
# go.mod asks for Go 1.27.3; GOTOOLCHAIN=auto fetches it from proxy.golang.org
# (checked against sum.golang.org) if Fedora's Go is older (local builds only).
export GOTOOLCHAIN=auto GOFLAGS="-mod=readonly -modcacherw"
export GOPATH=%{_builddir}/go GOCACHE=%{_builddir}/go-cache
make build tray VERSION=v%{version}

%install
sh %{SOURCE1} . %{buildroot}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/io.github.jm2.Switchworks.desktop
./swk version | grep -F "v%{version} "

# The account comes from the sysusers.d file (rpm creates it at install).
# Nothing is enabled: no %%systemd_user_post, and Fedora's presets leave the
# system coordinator off. It is restarted on upgrade if it runs.
%post
%systemd_post swk-coordinator.service

%preun
%systemd_preun swk-coordinator.service

%postun
%systemd_postun_with_restart swk-coordinator.service

%files
%license LICENSE internal/web/assets/fonts/OFL-Onest.txt internal/web/assets/fonts/OFL-JetBrainsMono.txt
%{_bindir}/swk
%{_bindir}/swk-tray
%{_userunitdir}/swk-node.service
%{_userunitdir}/swk-coordinator.service
%{_unitdir}/swk-coordinator.service
%{_sysusersdir}/switchworks.conf
%{_datadir}/applications/io.github.jm2.Switchworks.desktop
%{_datadir}/icons/hicolor/*/apps/io.github.jm2.Switchworks.png
%{_datadir}/icons/hicolor/scalable/apps/io.github.jm2.Switchworks.svg
%{_docdir}/switchworks/

%changelog
* Wed Nov 11 2026 John-Michael Mulesa <jmulesa@gmail.com> - 0.1.7-1
- Local RPM build of switchworks 0.1.7
