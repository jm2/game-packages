# Upstream's static, stripped Go binary (CGO_ENABLED=0, -s -w): nothing to
# strip or extract debug information from.
%global debug_package %{nil}
%global __strip /bin/true
%global _build_id_links none

Name:           carryout-bin
Version:        0.2.0
Release:        1%{?dist}
Summary:        Download helper for Google Takeout exports (binary release)
License:        GPL-3.0-or-later
URL:            https://github.com/jm2/carryout
%ifarch x86_64
Source0:        %{url}/releases/download/v%{version}/carryout_%{version}_linux_amd64.tar.gz
%endif
%ifarch aarch64
Source0:        %{url}/releases/download/v%{version}/carryout_%{version}_linux_arm64.tar.gz
%endif
Source1:        install.sh

ExclusiveArch:  x86_64 aarch64
BuildRequires:  tar
BuildRequires:  gzip

# Replaces the source-built carryout package (last built as 0.2.0-1).
Provides:       carryout = %{version}-%{release}
Obsoletes:      carryout < 0.2.0-2
Conflicts:      carryout

%description
carryout picks up a Google Takeout order. Given one download request copied
as cURL from the browser and the export's file list, it fetches every
archive part, pauses for fresh cookies when the session expires instead of
burning download attempts, resumes interrupted parts, and verifies each
archive as it streams.

This package repackages upstream's release binary.

%prep
# The archive has no top-level directory.
%setup -q -c

%build
# Prebuilt binary; nothing to build.

%install
sh %{SOURCE1} . %{buildroot} %{_docdir}/%{name}

%check
test "$(./carryout version)" = "carryout %{version}"

%files
%license LICENSE
%{_bindir}/carryout
%{_docdir}/%{name}/

%changelog
* Wed Nov 11 2026 John-Michael Mulesa <jmulesa@gmail.com> - 0.2.0-1
- Repackage upstream's carryout 0.2.0 release archive (replaces the source-built carryout package)
