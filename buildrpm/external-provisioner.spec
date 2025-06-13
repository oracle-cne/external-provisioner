

%if 0%{?with_debug}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package %{nil}
%endif

%global app_name                external-provisioner
%global app_name_release        csi-provisioner
%global app_version             5.3.0
%global oracle_release_version  1
%global _buildhost              build-ol%{?oraclelinux}-%{?_arch}.oracle.com

Name:           %{app_name}
Version:        %{app_version}
Release:        %{oracle_release_version}%{?dist}
Summary:        Sidecar container that dynamically provisions volumes by calling CreateVolume and DeleteVolume functions of CSI drivers.
License:        Apache 2.0
Group:          Development/Tools
Url:            https://github.com/oracle-cne/external-provisioner.git
Source:         %{name}-%{version}.tar.bz2
BuildRequires:  golang
BuildRequires:	make

%description
Sidecar container that dynamically provisions volumes by calling CreateVolume and DeleteVolume functions of CSI drivers.

%prep
%setup -q

%build
make build

%install
install -m 755 bin/%{app_name_release} %{buildroot}/%{app_name_release}

%files
%license LICENSE THIRD_PARTY_LICENSES.txt olm/SECURITY.md
/%{app_name_release}

%changelog
* Fri Jun 13 2025 Daniel Krasinski <daniel.krasinski@oracle.com> - 5.3.0-1
- Added Oracle specific build files for CSI external-provisioner.

