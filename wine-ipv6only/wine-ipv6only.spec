Name:           wine-ipv6only
Version:        1.0.0
Release:        2%{?dist}
Summary:        LD_PRELOAD library that forces IPV6_V6ONLY for Wine games
License:        0BSD
URL:            https://github.com/jm2/game-packages
Source0:        ipv6only.c
Source1:        Makefile
Source2:        LICENSE
ExclusiveArch:  x86_64

BuildRequires:  gcc
BuildRequires:  make

%description
Some Windows games bind a dual-stack IPv6 socket and then an IPv4 socket on
the same port. Windows allows that; Linux refuses the IPv4 bind, so under Wine
the game can't host LAN games. gamelaunch preloads this library (from
/opt/wine-ipv6only, which umu's container can see) for the games that need
it; it forces IPV6_V6ONLY=1 so both sockets bind as they do on Windows.

%prep
%setup -q -c -T
cp -p %{SOURCE0} %{SOURCE1} %{SOURCE2} .

%build
%make_build CFLAGS="%{optflags}" LDFLAGS="%{build_ldflags}"

%install
%make_install

%files
%license LICENSE
/opt/wine-ipv6only/

%changelog
* Wed Nov 11 2026 John-Michael Mulesa <jmulesa@gmail.com> - 1.0.0-2
- Project URL: the repository is now jm2/game-packages

* Sun Nov 08 2026 John-Michael Mulesa <jmulesa@gmail.com> - 1.0.0-1
- Initial package
