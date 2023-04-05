#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
#
# Source0 file verified with key 0xD7574483BB57B18D (jr@jriddell.org)
#
Name     : polkit-kde-agent
Version  : 1.5.27.4.1
Release  : 66
URL      : https://download.kde.org/stable/plasma/5.27.4/polkit-kde-agent-1-5.27.4.1.tar.xz
Source0  : https://download.kde.org/stable/plasma/5.27.4/polkit-kde-agent-1-5.27.4.1.tar.xz
Source1  : https://download.kde.org/stable/plasma/5.27.4/polkit-kde-agent-1-5.27.4.1.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : CC0-1.0 GPL-2.0
Requires: polkit-kde-agent-data = %{version}-%{release}
Requires: polkit-kde-agent-license = %{version}-%{release}
Requires: polkit-kde-agent-locales = %{version}-%{release}
Requires: polkit-kde-agent-services = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : polkit-qt-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
No detailed description available

%package data
Summary: data components for the polkit-kde-agent package.
Group: Data

%description data
data components for the polkit-kde-agent package.


%package license
Summary: license components for the polkit-kde-agent package.
Group: Default

%description license
license components for the polkit-kde-agent package.


%package locales
Summary: locales components for the polkit-kde-agent package.
Group: Default

%description locales
locales components for the polkit-kde-agent package.


%package services
Summary: services components for the polkit-kde-agent package.
Group: Systemd services

%description services
services components for the polkit-kde-agent package.


%prep
%setup -q -n polkit-kde-agent-1-5.27.4.1
cd %{_builddir}/polkit-kde-agent-1-5.27.4.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1680713523
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1680713523
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/polkit-kde-agent
cp %{_builddir}/polkit-kde-agent-1-5.27.4.1/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/polkit-kde-agent/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/polkit-kde-agent-1-5.27.4.1/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/polkit-kde-agent/3e8971c6c5f16674958913a94a36b1ea7a00ac46 || :
pushd clr-build
%make_install
popd
%find_lang polkit-kde-authentication-agent-1

%files
%defattr(-,root,root,-)
/usr/lib64/libexec/polkit-kde-authentication-agent-1

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.polkit-kde-authentication-agent-1.desktop
/usr/share/knotifications5/policykit1-kde.notifyrc
/usr/share/xdg/autostart/polkit-kde-authentication-agent-1.desktop

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/polkit-kde-agent/3e8971c6c5f16674958913a94a36b1ea7a00ac46
/usr/share/package-licenses/polkit-kde-agent/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/user/plasma-polkit-agent.service

%files locales -f polkit-kde-authentication-agent-1.lang
%defattr(-,root,root,-)

