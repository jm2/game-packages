Name:           yamagi-quake2-ref_vk
Version:        1.0.12
Release:        1%{?dist}
Summary:        Vulkan renderer for Yamagi Quake II
# volk is MIT, stb is MIT OR Unlicense.
License:        GPL-2.0-or-later AND MIT AND (MIT OR Unlicense)
URL:            https://github.com/yquake2/ref_vk
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/ref_vk-%{version}.tar.gz
Source1:        README.md

ExclusiveArch:  x86_64 aarch64

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconf-pkg-config
BuildRequires:  vulkan-headers
BuildRequires:  pkgconfig(sdl3)

Requires:       yamagi-quake2 >= 8.70
# The Vulkan loader is opened at run time through SDL.
Requires:       vulkan-loader
Provides:       bundled(volk)
Provides:       bundled(stb_image)

%description
The vkQuake2 Vulkan renderer ported to Yamagi Quake II. Select it in the
video menu or with "+set vid_renderer vk".


%prep
%autosetup -n ref_vk-%{version}
cp -p %{SOURCE1} README.package.md


%build
%set_build_flags
%make_build VERBOSE=1


%install
install -Dm755 release/ref_vk.so %{buildroot}%{_prefix}/lib/yamagi-quake2/ref_vk.so
install -Dm644 README.package.md %{buildroot}%{_docdir}/%{name}/README.md
install -m644 README.md %{buildroot}%{_docdir}/%{name}/README.ref_vk.md


%files
%license LICENSE
%{_docdir}/%{name}/
%{_prefix}/lib/yamagi-quake2/ref_vk.so


%changelog
* Fri Nov 06 2026 John-Michael Mulesa <jmulesa@gmail.com> - 1.0.12-1
- Initial RPM package
