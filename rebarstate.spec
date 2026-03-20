%global _cmake_generator "Unix Makefiles"

Name:          ReBarState
Version:       0.3
Release:       %autorelease
Summary:       Resizable BAR for (almost) any UEFI system
License:       MIT
URL:           https://github.com/xCuri0/ReBarUEFI
Source0:       https://github.com/xCuri0/ReBarUEFI/archive/refs/tags/%{version}.tar.gz
Patch0:        https://github.com/xCuri0/ReBarUEFI/commit/a61465bf9d8ee48912e1f62daefd9a40ba9bd3c4.patch

%global project_name ReBarUEFI
%global project_dir %{project_name}-%{version}
%global project_build %{_builddir}/%{project_dir}/%{name}

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  make

%description
A UEFI DXE driver to enable Resizable BAR on systems which don't support it officially.
This provides performance benefits and is even required for Intel Arc GPUs to function optimally.

%prep
%autosetup -S git -n %{project_dir}

%build
cd %{project_build}
%cmake
%cmake_build

%install
#cmake_install
install -D -m 755 %{project_build}/%{__cmake_builddir}/%{name} %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE
%{_bindir}/%{name}

%changelog
{{{ git_dir_changelog }}}
