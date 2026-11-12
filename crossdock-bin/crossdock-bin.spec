# Upstream's static, stripped Go binary (CGO_ENABLED=0, -s -w): nothing to
# strip or extract debug information from.
%global debug_package %{nil}
%global __strip /bin/true
%global _build_id_links none

Name:           crossdock-bin
Version:        0.2.1
Release:        1%{?dist}
Summary:        Publish packages as signed apt, pacman, RPM and GooGet repositories
License:        GPL-3.0-or-later
URL:            https://github.com/jm2/crossdock
# Upstream's own RPM for this architecture, repackaged.
%ifarch x86_64
Source0:        %{url}/releases/download/v%{version}/crossdock-x86_64.rpm#/crossdock-%{version}-release-x86_64.rpm
%endif
%ifarch aarch64
Source0:        %{url}/releases/download/v%{version}/crossdock-aarch64.rpm#/crossdock-%{version}-release-aarch64.rpm
%endif
Source1:        install.sh

ExclusiveArch:  x86_64 aarch64
BuildRequires:  rpm
BuildRequires:  tar
BuildRequires:  gzip
BuildRequires:  systemd-rpm-macros
%{?systemd_requires}
Requires(pre):  systemd
# Signing and xz/zstd decoding are native. gpg is only needed to sign
# from a GnuPG keyring or smartcard (signing.gnupg_home).
Suggests:       gnupg2

# Replaces the source-built crossdock package (last built as 0.2.1-1).
Provides:       crossdock = %{version}-%{release}
Obsoletes:      crossdock < 0.2.1-2
Conflicts:      crossdock

%description
crossdock takes one directory of built packages per format and publishes
them as signed, static package repositories. Each publish swaps in
atomically. It includes a read-only HTTP server, so no web server is
required.

This package repackages upstream's release binary. It installs crossdock,
systemd units for the server (crossdock-serve, LAN-only on port 8080) and
for automatic publishing (crossdock-publish.path), the crossdock account,
/var/lib/crossdock, and a firewalld service definition. Nothing is enabled
at install.

%prep
%setup -q -c -T
mkdir release
rpm2archive - < %{SOURCE0} | tar -xzf - -C release
cp -p release/usr/share/licenses/crossdock/LICENSE LICENSE

%build
# Prebuilt binary; nothing to build.

%install
sh %{SOURCE1} release %{buildroot} %{_docdir}/%{name}

%check
release/usr/bin/crossdock version | grep -F "crossdock v%{version} "

# As upstream's spec: %%pre creates the crossdock account from the sysusers.d
# line this package ships (newer rpm also creates it from the file itself).
# Presets leave the units off; the server restarts on upgrade if it runs, and
# everything stops and is disabled on removal.
#
# Replacing the source-built crossdock package would disable its units
# twice: this package's %%systemd_post applies the presets (off) on its first
# install, and the old package's %%preun disables and stops every unit, as on
# removal. So %%pre notes which units are enabled or running, they are
# restored once the old package is gone, and %%posttrans drops the note.
%pre
systemd-sysusers --replace=%{_sysusersdir}/crossdock.conf - <<'EOF' || :
u crossdock - "crossdock repository publisher" /var/lib/crossdock
EOF
if [ "$1" -eq 1 ]; then
    mkdir -p %{_localstatedir}/lib/rpm-state/%{name}
    for u in crossdock-serve.service crossdock-publish.path crossdock-publish.timer; do
        systemctl --quiet is-enabled "$u" 2>/dev/null && echo "enable $u"
        systemctl --quiet is-active "$u" 2>/dev/null && echo "start $u"
    done > %{_localstatedir}/lib/rpm-state/%{name}/units || :
fi

%post
%tmpfiles_create crossdock.conf
%systemd_post crossdock-serve.service crossdock-publish.service crossdock-publish.path crossdock-publish.timer

%preun
%systemd_preun crossdock-serve.service crossdock-publish.service crossdock-publish.path crossdock-publish.timer

%postun
%systemd_postun_with_restart crossdock-serve.service
%systemd_postun crossdock-publish.service crossdock-publish.path crossdock-publish.timer

%triggerpostun -- crossdock < 0.2.1-2
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
%license LICENSE
%{_bindir}/crossdock
%{_unitdir}/crossdock-serve.service
%{_unitdir}/crossdock-publish.service
%{_unitdir}/crossdock-publish.path
%{_unitdir}/crossdock-publish.timer
%{_sysusersdir}/crossdock.conf
%{_tmpfilesdir}/crossdock.conf
%dir %{_prefix}/lib/firewalld
%dir %{_prefix}/lib/firewalld/services
%{_prefix}/lib/firewalld/services/crossdock.xml
%dir %{_sysconfdir}/crossdock
%config(noreplace) %{_sysconfdir}/crossdock/crossdock.yaml
%{_docdir}/%{name}/

%changelog
* Wed Nov 11 2026 John-Michael Mulesa <jmulesa@gmail.com> - 0.2.1-1
- Repackage upstream's crossdock 0.2.1 release RPM (replaces the source-built crossdock package)
