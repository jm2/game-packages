# Upstream's static, stripped Go binaries (CGO_ENABLED=0, -s -w): nothing to
# strip or extract debug information from.
%global debug_package %{nil}
%global __strip /bin/true
%global _build_id_links none

Name:           switchworks-bin
Version:        0.1.7
Release:        1%{?dist}
Summary:        Control plane for coding agents across your machines (binary release)
License:        GPL-3.0-or-later AND OFL-1.1
URL:            https://github.com/jm2/switchworks
# Upstream's own RPM for this architecture, repackaged.
%ifarch x86_64
Source0:        %{url}/releases/download/v%{version}/switchworks-x86_64.rpm#/switchworks-%{version}-release-x86_64.rpm
%endif
%ifarch aarch64
Source0:        %{url}/releases/download/v%{version}/switchworks-aarch64.rpm#/switchworks-%{version}-release-aarch64.rpm
%endif
Source1:        install.sh

ExclusiveArch:  x86_64 aarch64
BuildRequires:  rpm
BuildRequires:  tar
BuildRequires:  gzip
BuildRequires:  systemd-rpm-macros
BuildRequires:  desktop-file-utils
Requires:       hicolor-icon-theme
%{?systemd_requires}

# The tray icon needs a StatusNotifierItem host; GNOME has one through the
# AppIndicator extension.
Suggests:       (gnome-shell-extension-appindicator if gnome-shell)

# Replaces the source-built switchworks package (last built as 0.1.7-1).
Provides:       switchworks = %{version}-%{release}
Obsoletes:      switchworks < 0.1.7-2
Conflicts:      switchworks

%description
Switchworks shows every coding-agent session (Codex, Goose and other ACP
agents) on every host in one place, from a browser, a phone or the swk
command line, and lets agents on different machines message each other.

This package repackages upstream's release binaries. It installs swk, the
swk-tray status icon, systemd user units for the node and the coordinator,
and a system unit that runs the coordinator as its own switchworks account.
Nothing is enabled at install: each user runs "swk service install" to run
the node as themselves, and "swk service install --system coordinator", run
as root, sets up the system coordinator.

%prep
%setup -q -c -T
mkdir release
rpm2archive - < %{SOURCE0} | tar -xzf - -C release

%build
# Prebuilt binaries; nothing to build.

%install
sh %{SOURCE1} release %{buildroot} %{_docdir}/%{name} %{_defaultlicensedir}/%{name}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/io.github.jm2.Switchworks.desktop
release/usr/bin/swk version | grep -F "v%{version} "

# The account comes from the sysusers.d file (rpm creates it at install).
# Nothing is enabled: no %%systemd_user_post, and Fedora's presets leave the
# system coordinator off. It is restarted on upgrade if it runs.
#
# Replacing the source-built switchworks package would disable the system
# coordinator twice: this package's %%systemd_post applies the preset (off)
# on its first install, and the old package's %%preun disables and stops it,
# as on removal. So %%pre notes whether it is enabled or running, that is
# restored once the old package is gone, and %%posttrans drops the note.
%pre
if [ "$1" -eq 1 ]; then
    mkdir -p %{_localstatedir}/lib/rpm-state/%{name}
    u=swk-coordinator.service
    {
        systemctl --quiet is-enabled "$u" 2>/dev/null && echo "enable $u"
        systemctl --quiet is-active "$u" 2>/dev/null && echo "start $u"
    } > %{_localstatedir}/lib/rpm-state/%{name}/units || :
fi

%post
%systemd_post swk-coordinator.service

%preun
%systemd_preun swk-coordinator.service

%postun
%systemd_postun_with_restart swk-coordinator.service

%triggerpostun -- switchworks < 0.1.7-2
state=%{_localstatedir}/lib/rpm-state/%{name}/units
if [ -s "$state" ]; then
    [ -d /run/systemd/system ] && systemctl daemon-reload || :
    while read -r action u; do
        if [ "$action" = enable ]; then
            systemctl --quiet --no-reload enable "$u" || :
        elif [ -d /run/systemd/system ]; then
            systemctl --quiet start "$u" || :
        fi
    done < "$state"
fi

%posttrans
rm -rf %{_localstatedir}/lib/rpm-state/%{name}

%files
%license %{_defaultlicensedir}/%{name}/
%{_bindir}/swk
%{_bindir}/swk-tray
%{_userunitdir}/swk-node.service
%{_userunitdir}/swk-coordinator.service
%{_unitdir}/swk-coordinator.service
%{_sysusersdir}/switchworks.conf
%{_datadir}/applications/io.github.jm2.Switchworks.desktop
%{_datadir}/icons/hicolor/*/apps/io.github.jm2.Switchworks.png
%{_datadir}/icons/hicolor/scalable/apps/io.github.jm2.Switchworks.svg
%{_docdir}/%{name}/

%changelog
* Wed Nov 11 2026 John-Michael Mulesa <jmulesa@gmail.com> - 0.1.7-1
- Repackage upstream's switchworks 0.1.7 release RPM (replaces the source-built switchworks package)
