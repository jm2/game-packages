# Prebuilt upstream binaries: no debuginfo, no stripping, and no automatic
# provides/requires from the private libraries in /opt/ut2004.
%global debug_package %{nil}
%global __strip /bin/true
%global _build_id_links none
%global __provides_exclude_from ^/opt/ut2004/.*$
%global __requires_exclude_from ^/opt/ut2004/.*$

%global upver 3374
%global preview preview-23
%global upbuild 094b94dc

Name:           ut2004-bin
Version:        %{upver}~preview23
Release:        1%{?dist}
Summary:        Unreal Tournament 2004 ECE native binaries (OldUnreal)
License:        LicenseRef-OldUnreal
URL:            https://github.com/OldUnreal/UT2004Patches
Source0:        %{url}/releases/download/%{upver}-%{preview}/OldUnreal-UT2004Patch%{upver}-Linux-%{upbuild}.tar.bz2
Source1:        https://raw.githubusercontent.com/OldUnreal/UT2004Patches/%{upver}-%{preview}/LICENSE.md#/LICENSE-%{upver}-%{preview}.md
Source2:        install.sh
Source3:        ut2004.sh
Source4:        ut2004.desktop
Source5:        ut2004.png
Source6:        README.md

ExclusiveArch:  x86_64 aarch64
BuildRequires:  desktop-file-utils
BuildRequires:  tar
BuildRequires:  bzip2

Requires:       ut2004-data
# By soname: the private libraries in /opt are excluded from automatic requires.
Requires:       libSDL3.so.0()(64bit)
Requires:       libopenal.so.1()(64bit)
Requires:       libasound.so.2()(64bit)
Requires:       libGL.so.1()(64bit)
Requires:       libstdc++.so.6()(64bit)
Requires:       hicolor-icon-theme
Provides:       ut2004 = %{version}-%{release}
Conflicts:      ut2004-steam
Obsoletes:      ut2004-gog < 3375

%description
Native Linux binaries for Unreal Tournament 2004 from OldUnreal's community
patch, installed to /opt/ut2004. The game data comes from a separate
ut2004-data-gog, ut2004-data-steam or ut2004-data-archiveorg package.

%prep
%setup -q -c -T
mkdir patch
tar -xjf %{SOURCE0} -C patch
cp -p %{SOURCE1} LICENSE.md
cp -p %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5} %{SOURCE6} .

%build

%install
sh install.sh patch . %{buildroot} %{_target_cpu}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/ut2004.desktop

%files
%license LICENSE.md
%doc %{_docdir}/ut2004-bin/README.md
%{_bindir}/ut2004
%{_datadir}/applications/ut2004.desktop
%{_datadir}/icons/hicolor/256x256/apps/ut2004.png
/opt/ut2004/Help/
/opt/ut2004/Sounds/
/opt/ut2004/System/
/opt/ut2004/SystemLocalized/
/opt/ut2004/Textures/
/opt/ut2004/Web/
%dir /opt/ut2004

%changelog
* Mon Nov 02 2026 John-Michael Mulesa <jmulesa@gmail.com> - 3374~preview23-1
- Initial RPM package: OldUnreal 3374-preview-23, system SDL3 and OpenAL
