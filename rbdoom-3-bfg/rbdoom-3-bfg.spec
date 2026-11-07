# Built from the v1.6.0 tag. The tag's archive has empty nvrhi and ShaderMake
# submodule directories, so they are fetched as archives of the commits the
# tag records (nvrhi's Vulkan-Headers and RTXMU submodules aren't needed).
# The HLSL shaders are compiled to SPIR-V with DXC, which Fedora doesn't
# package: the build uses Microsoft's Linux DXC release, which exists for
# x86_64 only, so this package is x86_64 only (it would need a DXC source
# build on aarch64). DXC is a build tool only and isn't shipped.

# The AUR package builds without LTO as well.
%global _lto_cflags %{nil}

%global nvrhi_commit fc4cfe69b9f65c7a0ba6509a52303efaba0a0e8c
%global shadermake_commit 13867771f6142f35690a5e2103c1e1efdd90cb0e
# Upstream's icon, added after the tag on the flatpak branch.
%global icon_commit 0fc10ab97b26c0db0900b403e26d7e6b8f8baee1
%global dxc_version 1.9.2609
%global dxc_archive linux_dxc_2026_09_28.x86_x64.tar.gz

Name:           rbdoom-3-bfg
Version:        1.6.0
Release:        2%{?dist}
Summary:        Doom 3 BFG Edition with modern engine features (Vulkan, PBR, baked GI)
# Engine GPL-3.0-or-later; nvrhi, ShaderMake, imgui, rapidjson, ispc_texcomp
# MIT; Intel's masked occlusion culling Apache-2.0; libbinkdec
# LGPL-2.1-or-later; minizip, mikktspace Zlib; oggvorbis BSD-3-Clause.
License:        GPL-3.0-or-later AND MIT AND Apache-2.0 AND LGPL-2.1-or-later AND Zlib AND BSD-3-Clause
URL:            https://github.com/RobertBeckebans/RBDOOM-3-BFG
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/RBDOOM-3-BFG-%{version}.tar.gz
Source1:        https://github.com/RobertBeckebans/nvrhi/archive/%{nvrhi_commit}.tar.gz#/nvrhi-%{nvrhi_commit}.tar.gz
Source2:        https://github.com/RobertBeckebans/ShaderMake/archive/%{shadermake_commit}.tar.gz#/ShaderMake-%{shadermake_commit}.tar.gz
Source3:        https://raw.githubusercontent.com/RobertBeckebans/RBDOOM-3-BFG/%{icon_commit}/install/desktop/RBDOOM-3-BFG.png#/rbdoom-3-bfg.png
Source4:        https://github.com/microsoft/DirectXShaderCompiler/releases/download/v%{dxc_version}/%{dxc_archive}
Source5:        install.sh
Source6:        rbdoom-3-bfg.sh
Source7:        rbdoom-3-bfg.desktop
Source8:        README.md
# rbdmap fails to link with GCC (speculative devirtualization)
Patch0:         rbdmap-gcc-link.patch

ExclusiveArch:  x86_64

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  ispc
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  vulkan-headers
BuildRequires:  pkgconfig(zlib)

Requires:       doom3bfg-data
Suggests:       rbdoom-3-bfg-gi-data
Requires:       hicolor-icon-theme
# The engine dlopens libvulkan.so.1 (vulkan.hpp's dynamic loader).
Requires:       vulkan-loader%{?_isa}
Provides:       bundled(nvrhi)
Provides:       bundled(imgui)
Provides:       bundled(libbinkdec)
Provides:       bundled(rapidjson)

%description
RBDOOM-3-BFG is Robert Beckebans' modernized Doom 3 BFG Edition engine,
with Vulkan rendering through NVIDIA's NVRHI, physically based rendering,
baked global illumination, soft shadows and retro rendering modes. It needs the
retail Doom 3 BFG Edition data (doom3bfg-data) and a Vulkan driver.


%prep
%autosetup -p1 -n RBDOOM-3-BFG-%{version}
tar -xf %{SOURCE1} -C neo/extern/nvrhi --strip-components=1
tar -xf %{SOURCE2} -C neo/extern/ShaderMake --strip-components=1
mkdir dxc && tar -xf %{SOURCE4} -C dxc
# The packaging files go to pkg/: README.md would replace upstream's.
mkdir pkg && cp -p %{SOURCE3} %{SOURCE5} %{SOURCE6} %{SOURCE7} %{SOURCE8} pkg/


%build
# libs/moc replaces CMAKE_CXX_FLAGS, losing the -fPIE that Fedora adds
# through its hardening specs, hence CMAKE_POSITION_INDEPENDENT_CODE.
%global _vpath_srcdir neo
%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DBUILD_SHARED_LIBS=OFF \
    -DCMAKE_POSITION_INDEPENDENT_CODE=ON \
    -DCMAKE_SKIP_RPATH=ON \
    -DFFMPEG=OFF \
    -DBINKDEC=ON \
    -DUSE_DX12=OFF \
    -DUSE_VULKAN=ON \
    -DWINDOWS10=OFF \
    -DUSE_PRECOMPILED_HEADERS=OFF \
    -DUSE_SYSTEM_ZLIB=ON \
    -DUSE_SYSTEM_RAPIDJSON=OFF \
    -DNVRHI_INSTALL=OFF \
    -DDXC_SPIRV_PATH=$PWD/dxc/bin/dxc \
    -Wno-dev
%cmake_build


%install
sh pkg/install.sh . %{__cmake_builddir} %{buildroot} %{name} %{buildroot}%{_licensedir}/%{name} pkg/rbdoom-3-bfg.png


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/rbdoom-3-bfg.desktop


%files
%license %{_licensedir}/%{name}/
%doc %{_docdir}/%{name}/
%{_bindir}/rbdoom-3-bfg
%{_bindir}/RBDoom3BFG
%{_bindir}/rbdmap
%{_prefix}/lib/rbdoom-3-bfg/
%dir %{_datadir}/games/doom3bfg
%{_datadir}/games/doom3bfg/base/
%{_datadir}/applications/rbdoom-3-bfg.desktop
%{_datadir}/icons/hicolor/256x256/apps/rbdoom-3-bfg.png


%changelog
* Sat Nov 07 2026 John-Michael Mulesa <jmulesa@gmail.com> - 1.6.0-2
- Suggest rbdoom-3-bfg-gi-data, the release's baked GI and blood packs

* Fri Nov 06 2026 John-Michael Mulesa <jmulesa@gmail.com> - 1.6.0-1
- Initial RPM package, built from the v1.6.0 tag
