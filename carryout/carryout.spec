# Built like upstream's release archives: a static, stripped binary
# (CGO_ENABLED=0, -s -w), so there is no debug information to package.
%global debug_package %{nil}

Name:           carryout
Version:        0.2.0
Release:        1%{?dist}
Summary:        Download helper for Google Takeout exports
License:        GPL-3.0-or-later
URL:            https://github.com/jm2/carryout
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        install.sh

ExclusiveArch:  x86_64 aarch64
BuildRequires:  golang >= 1.24

%description
carryout picks up a Google Takeout order. Given one download request copied
as cURL from the browser and the export's file list, it fetches every
archive part, pauses for fresh cookies when the session expires instead of
burning download attempts, resumes interrupted parts, and verifies each
archive as it streams.

%prep
%autosetup -n %{name}-%{version}

%build
# Standard library only: nothing is downloaded.
export GOPATH=%{_builddir}/gopath GOCACHE=%{_builddir}/gocache GOFLAGS="-mod=readonly"
# Upstream's release workflow sets the version with -X main.version.
CGO_ENABLED=0 go build -trimpath -ldflags "-s -w -X main.version=%{version}" -o carryout .

%install
sh %{SOURCE1} . %{buildroot}

%check
test "$(./carryout version)" = "carryout %{version}"

%files
%license LICENSE
%{_bindir}/carryout
%{_docdir}/carryout/

%changelog
* Wed Nov 11 2026 John-Michael Mulesa <jmulesa@gmail.com> - 0.2.0-1
- Local RPM build of carryout 0.2.0
