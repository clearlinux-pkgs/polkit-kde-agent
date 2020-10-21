#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xEC94D18F7F05997E (jr@jriddell.org)
#
Name     : polkit-kde-agent
Version  : 1.5.20.1
Release  : 26
URL      : https://download.kde.org/stable/plasma/5.20.1/polkit-kde-agent-1-5.20.1.tar.xz
Source0  : https://download.kde.org/stable/plasma/5.20.1/polkit-kde-agent-1-5.20.1.tar.xz
Source1  : https://download.kde.org/stable/plasma/5.20.1/polkit-kde-agent-1-5.20.1.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: polkit-kde-agent-data = %{version}-%{release}
Requires: polkit-kde-agent-license = %{version}-%{release}
Requires: polkit-kde-agent-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : ki18n-dev
BuildRequires : polkit-qt-dev
BuildRequires : qtbase-dev mesa-dev

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


%prep
%setup -q -n polkit-kde-agent-1-5.20.1
cd %{_builddir}/polkit-kde-agent-1-5.20.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1603242562
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1603242562
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/polkit-kde-agent
cp %{_builddir}/polkit-kde-agent-1-5.20.1/COPYING %{buildroot}/usr/share/package-licenses/polkit-kde-agent/7c203dee3a03037da436df03c4b25b659c073976
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
/usr/share/package-licenses/polkit-kde-agent/7c203dee3a03037da436df03c4b25b659c073976

%files locales -f polkit-kde-authentication-agent-1.lang
%defattr(-,root,root,-)

