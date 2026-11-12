# Prebuilt upstream binaries: nothing to strip or extract debuginfo from.
%global debug_package %{nil}
%global __strip /bin/true
%global _build_id_links none
# The engine modules are private to /opt/openq4; don't advertise them as
# system-wide library provides.
%global __provides_exclude_from ^/opt/openq4/.*$
# The payload is mostly already-compressed pk4 (zip) data; the default
# high zstd level only burns build time.
%global _binary_payload w3.zstdio
%global _source_payload w3.zstdio

%global q4ver 1.4.2

# Upstream names its binaries and modules by architecture tag.
%ifarch x86_64
%global oq4arch x64
%endif
%ifarch aarch64
%global oq4arch arm64
%endif

Name:           openq4-bin
Version:        0.14.1
Release:        1%{?dist}
Summary:        Open-source Quake 4 engine and game code replacement (binary release)
License:        GPL-3.0-or-later AND LicenseRef-Quake4-SDK AND LicenseRef-Quake4-EULA
URL:            https://github.com/themuffinator/openQ4
Source0:        %{url}/releases/download/v%{version}/openq4-%{version}-linux-x64.tar.xz
# The arm64 archive carries a -preview suffix.
Source1:        %{url}/releases/download/v%{version}/openq4-%{version}-linux-arm64-preview.tar.xz
# Quake 4 1.4.2 Linux point release, for the patch paks (pak013-pak022).
Source2:        https://aur.slashbunny.com/quake4/quake4-linux-%{q4ver}.x86.run
Source3:        openq4.sh
Source4:        README.md

ExclusiveArch:  x86_64 aarch64

BuildRequires:  desktop-file-utils
BuildRequires:  gzip
BuildRequires:  sed
BuildRequires:  tar
BuildRequires:  xz

Requires:       hicolor-icon-theme
# dlopen()ed at runtime, so not picked up by the automatic ELF dependencies.
Recommends:     vulkan-loader
Recommends:     libwayland-client
Recommends:     libwayland-cursor
Recommends:     libwayland-egl
Recommends:     libxkbcommon
Recommends:     libdecor

Provides:       openq4 = %{version}-%{release}
Conflicts:      openq4

%description
openQ4 replaces the Quake 4 engine and game binaries with a GPL engine and
SDK-licensed game modules, keeping the original game playable on modern
systems with widescreen, high refresh rate, controller and renderer
improvements.

This package includes the Quake 4 1.4.2 patch paks (pak013.pk4 - pak022.pk4)
extracted from id Software's Linux point release. You still need the retail
Quake 4 data (pak001.pk4 - pak012.pk4 and zpak_<language>.pk4) from Steam or
GOG. openQ4 looks in /opt/quake4 first, then in Steam and GOG installs; set
OPENQ4_QUAKE4_PATH or pass "+set fs_basepath <dir>" to use another location.


%prep
%setup -q -c -T
%ifarch x86_64
tar -xf %{SOURCE0}
%endif
%ifarch aarch64
tar -xf %{SOURCE1}
%endif
mv openq4-%{version}-linux-%{oq4arch}* openq4

# Unpack the makeself archive without running its installer.
sh %{SOURCE2} --noexec --nox11 --target quake4-%{q4ver}

cp -p openq4/LICENSE LICENSE
cp -pr openq4/licenses licenses
install -m 644 quake4-%{q4ver}/License.txt Quake4-License.txt


%build
# Prebuilt binaries; nothing to build.


%install
cd openq4

# Engine, renderers and openQ4 runtime content
install -D -m 755 -t %{buildroot}/opt/openq4/ \
    openQ4-client_%{oq4arch} openQ4-ded_%{oq4arch} renderer-*_%{oq4arch}.so
install -D -m 644 -t %{buildroot}/opt/openq4/ VERSION.txt
install -D -m 755 -t %{buildroot}/opt/openq4/baseoq4/ baseoq4/*.so
install -D -m 644 -t %{buildroot}/opt/openq4/baseoq4/ baseoq4/*.pk4 baseoq4/mod.json
# Startup splash, loaded relative to the working directory
install -D -m 644 -t %{buildroot}/opt/openq4/assets/splash/ assets/splash/*.bmp

# Quake 4 1.4.2 patch paks, mounted from the q4base overlay
install -D -m 644 -t %{buildroot}/opt/openq4/q4base/ \
    ../quake4-%{q4ver}/q4base/pak0??.pk4 \
    ../quake4-%{q4ver}/q4base/q4cmp_pak001.pk4 \
    ../quake4-%{q4ver}/q4base/zpak_english_0?.pk4 \
    ../quake4-%{q4ver}/us/q4base/*.pk4

# Launcher and its dedicated server / Steam Deck aliases
install -d %{buildroot}%{_bindir}
sed 's/@ARCH@/%{oq4arch}/g' %{SOURCE3} > %{buildroot}%{_bindir}/openq4
chmod 755 %{buildroot}%{_bindir}/openq4
ln -s openq4 %{buildroot}%{_bindir}/openq4-dedicated
ln -s openq4 %{buildroot}%{_bindir}/openq4-steamdeck

# Desktop files, pointed at the launcher
install -d %{buildroot}%{_datadir}/applications
for desktop in share/applications/*.desktop; do
    sed -e 's/^Exec=openQ4-steamdeck/Exec=openq4-steamdeck/' \
        -e 's/^Exec=openQ4-client_.*/Exec=openq4/' "$desktop" \
        > %{buildroot}%{_datadir}/applications/"${desktop##*/}"
done

# Icons
for icon in share/icons/hicolor/*/apps/openq4.*; do
    install -D -m 644 "$icon" %{buildroot}%{_prefix}/"$icon"
done

# Documentation
install -d %{buildroot}%{_docdir}/%{name}
install -m 644 README.html CONTRIBUTORS.md LICENSING.md %{SOURCE4} %{buildroot}%{_docdir}/%{name}/
cp -r --no-preserve=ownership docs %{buildroot}%{_docdir}/%{name}/


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/openq4.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/openq4-steamdeck.desktop


%files
%license LICENSE licenses/ Quake4-License.txt
%{_docdir}/%{name}/
/opt/openq4/
%{_bindir}/openq4
%{_bindir}/openq4-dedicated
%{_bindir}/openq4-steamdeck
%{_datadir}/applications/openq4.desktop
%{_datadir}/applications/openq4-steamdeck.desktop
%{_datadir}/icons/hicolor/*/apps/openq4.png
%{_datadir}/icons/hicolor/scalable/apps/openq4.svg


%changelog
* Thu Nov 12 2026 John-Michael Mulesa <jmulesa@gmail.com> - 0.14.1-1
- Update to openQ4 0.14.1 (new pak0-pak2 content packs)
- Install the startup splash and the bundled license files

* Wed Nov 04 2026 John-Michael Mulesa <jmulesa@gmail.com> - 0.13.2-2
- Ship README.md; make Quake4-License.txt world-readable

* Sun Oct 25 2026 John-Michael Mulesa <jmulesa@gmail.com> - 0.13.2-1
- Initial package of the openQ4 0.13.2 binary release
