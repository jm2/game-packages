# Upstream (NVIDIA/Q2RTX) was archived after 1.8.1, so this is the final
# release. Built from the v1.8.1 tag against the system zlib, curl, SDL2 and
# OpenAL; the glslang, Vulkan-Headers, stb and tinyobjloader submodules are
# fetched as archives of the commits the tag records. The media archives
# come from the release tarball.

# The release tarball is mostly already-compressed pkz (zip) media.
%global _binary_payload w3.zstdio

%global stb_commit 5c205738c191bcb0abc65c4febfa9bd25ff35234
%global tinyobj_commit 46d333d0165427b22895d05e278736bc9ef84365
%global vkheaders_commit d4a196d8c84e032d27f999adcea3075517c1c97f
%global glslang_commit 99ee11b0106b48f06fb9e2a324ba928b8316cc33

Name:           quake2rtx
Version:        1.8.1
Release:        1%{?dist}
Summary:        Ray-traced version of Quake II (built from source)
# glslang and Vulkan-Headers are only used at build time (shader compiler,
# headers); stb and tinyobjloader are header-only (public domain / MIT).
License:        GPL-2.0-only AND LicenseRef-Quake2-Demo AND MIT AND (MIT OR Unlicense)
URL:            https://github.com/NVIDIA/Q2RTX
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/Q2RTX-%{version}.tar.gz
Source1:        https://github.com/nothings/stb/archive/%{stb_commit}.tar.gz#/stb-%{stb_commit}.tar.gz
Source2:        https://github.com/syoyo/tinyobjloader-c/archive/%{tinyobj_commit}.tar.gz#/tinyobjloader-c-%{tinyobj_commit}.tar.gz
Source3:        https://github.com/KhronosGroup/Vulkan-Headers/archive/%{vkheaders_commit}.tar.gz#/Vulkan-Headers-%{vkheaders_commit}.tar.gz
Source4:        https://github.com/KhronosGroup/glslang/archive/%{glslang_commit}.tar.gz#/glslang-%{glslang_commit}.tar.gz
Source5:        %{url}/releases/download/v%{version}/q2rtx-%{version}-linux.tar.gz
Source6:        q2rtx.sh
Source7:        q2rtx.desktop
Source8:        install.sh

ExclusiveArch:  x86_64 aarch64

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  python3
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(zlib)

Requires:       bash
Requires:       hicolor-icon-theme
Recommends:     (zenity or kdialog)
Provides:       bundled(glslang)
Obsoletes:      quake2rtx-bin < 1.8.1-3

%description
Quake II RTX is NVIDIA's path-traced remaster of Quake II, based on Q2VKPT
and Q2PRO. It ships the shareware episode; the full game's paks can be
imported from a retail install on the first launch. Needs a Vulkan driver
with ray tracing support.


%prep
%autosetup -n Q2RTX-%{version}
for sm in stb:%{SOURCE1} tinyobjloader-c:%{SOURCE2} Vulkan-Headers:%{SOURCE3} glslang:%{SOURCE4}; do
    rm -rf "extern/${sm%%%%:*}" && mkdir "extern/${sm%%%%:*}"
    tar -xf "${sm#*:}" -C "extern/${sm%%%%:*}" --strip-components=1
done
# The build writes q2rtx/q2rtxded into the source root, so keep the release
# (which unpacks to q2rtx/) out of the way.
mkdir release && tar -xf %{SOURCE5} -C release
cp -p %{SOURCE6} %{SOURCE7} %{SOURCE8} .


%build
%cmake \
    -DUSE_SYSTEM_ZLIB=ON \
    -DUSE_SYSTEM_CURL=ON \
    -DUSE_SYSTEM_SDL2=ON \
    -DUSE_SYSTEM_OPENAL=ON \
    -DCMAKE_SKIP_RPATH=ON \
    -DBUILD_SHARED_LIBS=OFF \
    -Wno-dev
%cmake_build


%install
sh ./install.sh . release/q2rtx %{buildroot} %{name} %{buildroot}%{_licensedir}/%{name}


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/q2rtx.desktop


%files
%{_licensedir}/%{name}/
%{_docdir}/%{name}/
%{_datadir}/quake2rtx/
%{_bindir}/q2rtx
%{_bindir}/q2rtxded
%{_bindir}/quake2rtx
%{_bindir}/quake2rtx-find-retail-paks
%{_datadir}/applications/q2rtx.desktop
%{_datadir}/icons/hicolor/256x256/apps/q2rtx.png


%changelog
* Mon Nov 02 2026 John-Michael Mulesa <jmulesa@gmail.com> - 1.8.1-1
- Initial RPM package, built from the v1.8.1 tag
