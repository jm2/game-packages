# A prebuilt Java jar: nothing to compile, strip or debuginfo.
%global debug_package %{nil}
%global ver    2.12.1
%global bnum   1283
%global commit 8c61d73988ff3c1a30a001bdc798ac7833376c5e

Name:           geysermc-bin
Version:        %{ver}^b%{bnum}
Release:        1%{?dist}
Summary:        Lets Minecraft: Bedrock Edition clients join Java Edition servers
License:        MIT
URL:            https://geysermc.org/
Source0:        https://download.geysermc.org/v2/projects/geyser/versions/%{ver}/builds/%{bnum}/downloads/standalone#/Geyser-Standalone-%{ver}-b%{bnum}.jar
Source1:        https://raw.githubusercontent.com/GeyserMC/Geyser/%{commit}/LICENSE#/LICENSE-%{commit}
Source2:        install.sh
Source3:        config.yml
Source4:        geysermc.service
Source5:        geysermc.sysusers
Source6:        geysermc.tmpfiles
Source7:        README.md

BuildArch:      noarch
BuildRequires:  systemd-rpm-macros
Requires:       java-headless >= 1:21
Provides:       geysermc = %{version}-%{release}
%{?systemd_requires}

%description
Geyser is a proxy that bridges Minecraft: Bedrock Edition and Minecraft: Java
Edition, so Bedrock clients (consoles, mobile, Windows) can join Java servers.
This package ships the standalone jar from download.geysermc.org (pinned
build) with a systemd service that runs it as the geysermc system user.

%prep
%setup -q -c -T
cp -p %{SOURCE0} %{SOURCE3} %{SOURCE4} %{SOURCE5} %{SOURCE6} %{SOURCE7} .
cp -p %{SOURCE1} LICENSE

%build

%install
sh %{SOURCE2} . Geyser-Standalone-%{ver}-b%{bnum}.jar %{buildroot} %{name}

%post
%tmpfiles_create %{_tmpfilesdir}/geysermc.conf
%systemd_post geysermc.service

%preun
%systemd_preun geysermc.service

%postun
%systemd_postun_with_restart geysermc.service

%files
%license LICENSE
%dir %attr(0770,root,geysermc) %{_sysconfdir}/geysermc
%config(noreplace) %{_sysconfdir}/geysermc/config.yml
%{_datadir}/geysermc/
%{_unitdir}/geysermc.service
%{_sysusersdir}/geysermc.conf
%{_tmpfilesdir}/geysermc.conf
%{_docdir}/%{name}/

%changelog
* Mon Nov 02 2026 John-Michael Mulesa <jmulesa@gmail.com> - 2.12.1^b1283-1
- Pin Geyser 2.12.1 build 1283; run as the geysermc user from /var/lib/geysermc
