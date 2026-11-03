%global debug_package %{nil}
%global __strip /bin/true

Name:           xlln-bin
Version:        1.6.2.1
Release:        1%{?dist}
Summary:        XLiveLessNess GFWL replacement xlive.dll for Wine game packages
License:        LGPL-2.1-only
URL:            https://gitlab.com/GlitchyScripts/xlivelessness
Source0:        https://dl.glitchyscripts.com/xlln/XLiveLessNess-v%{version}-Release.zip
Source1:        install.sh
BuildArch:      noarch
BuildRequires:  unzip

Provides:       xlln = %{version}-%{release}

%description
XLiveLessNess (XLLN) is a rewrite of the Games for Windows - LIVE library
(xlive.dll), restoring LAN and online sessions for GFWL titles. Game packages
in jm2/linux-packages that use GFWL depend on this package; gamelaunch links
xlive.dll and the XLiveLessNess modules into the per-user game directory.

%prep
%setup -q -n XLiveLessNess-v%{version}-Release

%build

%install
sh %{SOURCE1} . %{buildroot}

%files
%license LICENSE.md
%{_prefix}/lib/xlln/
%{_docdir}/xlln/

%changelog
* Mon Nov 02 2026 John-Michael Mulesa <jmulesa@gmail.com> - 1.6.2.1-1
- Initial package of XLiveLessNess v1.6.2.1
