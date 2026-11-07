%global debug_package %{nil}
%global __strip /bin/true

Name:           agelanserver-companion-bin
Version:        1.5.0.0
Release:        2%{?dist}
Summary:        ageServerLauncherCompanion DLLs for AoE II/III: DE and AoM: Retold (Wine)
License:        AGPL-3.0-only
URL:            https://github.com/luskaner/ageServerLauncherCompanion
Source0:        %{url}/releases/download/v%{version}/ageServerLauncherCompanion_full_release_v%{version}.zip
Source1:        https://raw.githubusercontent.com/luskaner/ageServerLauncherCompanion/v%{version}/LICENSE#/LICENSE-%{version}
Source2:        install.sh
Source3:        README.md
BuildArch:      noarch
BuildRequires:  unzip
Provides:       agelanserver-companion = %{version}-%{release}

%description
Windows DLLs from luskaner's ageServerLauncherCompanion, loaded into Age of
Empires II/III: DE and Age of Mythology: Retold by the Goldberg emulator so the
games use an ageLANServer without editing /etc/hosts or the system trust store.

%prep
%setup -q -c -T
unzip -q %{SOURCE0}
cp -p %{SOURCE1} LICENSE
cp -p %{SOURCE3} .

%build

%install
sh %{SOURCE2} . %{buildroot}

%files
%license LICENSE
%{_prefix}/lib/agelanserver-companion/
/opt/agelanserver-companion/
%{_docdir}/agelanserver-companion-bin/

%changelog
* Sat Nov 07 2026 John-Michael Mulesa <jmulesa@gmail.com> - 1.5.0.0-2
- Move the DLLs to /opt/agelanserver-companion so umu/Proton's container can see them

* Mon Nov 02 2026 John-Michael Mulesa <jmulesa@gmail.com> - 1.5.0.0-1
- Initial package
