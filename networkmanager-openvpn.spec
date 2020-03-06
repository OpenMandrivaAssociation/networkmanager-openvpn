%define url_ver %(echo %{version}|cut -d. -f1,2)
%define _disable_lto 1

Summary:	NetworkManager VPN integration for OpenVPN
Name:		networkmanager-openvpn
Version:	1.8.12
Release:	1
License:	GPLv2+
Group:		System/Base
Url:		http://www.gnome.org/projects/NetworkManager/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/NetworkManager-openvpn/%{url_ver}/NetworkManager-openvpn-%{version}.tar.xz

BuildRequires:	gettext
BuildRequires:	libtool
BuildRequires:	intltool
BuildRequires:	perl-XML-Parser
BuildRequires:	perl
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(gnome-keyring-1)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libsecret-unstable)
BuildRequires:	pkgconfig(libnma)
BuildRequires:	rpm-helper
Requires:	dbus
Requires:	gnome-keyring
Requires:	gtk+3
Requires:	NetworkManager
Requires:	openvpn
Requires:	shared-mime-info
Requires(pre):	rpm-helper

%description
This package contains software for integrating the OpenVPN VPN software
with NetworkManager and the GNOME desktop.

%prep
%setup -qn NetworkManager-openvpn-%{version}
%autopatch -p1

%build
%configure \
	--disable-static \
	--disable-dependency-tracking \
	--enable-more-warnings \
	--enable-lto=no \
	--without-libnm-glib
%make_build

%install
%make_install

%find_lang NetworkManager-openvpn

%pre
%_pre_useradd nm-openvpn %{_localstatedir}/lib/openvpn /bin/false

%files -f NetworkManager-openvpn.lang
%doc AUTHORS ChangeLog README
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/nm-openvpn-service.conf
%{_libdir}/NetworkManager/*.so
%{_libexecdir}/nm-openvpn-auth-dialog
%{_libexecdir}/nm-openvpn-service
%{_libexecdir}/nm-openvpn-service-openvpn-helper
%{_prefix}/lib/NetworkManager/VPN/nm-openvpn-service.name
%{_datadir}/appdata/network-manager-openvpn.metainfo.xml
# For now disabled in upstream
#{_datadir}/applications/nm-openvpn.desktop
#{_datadir}/icons/hicolor/*/apps/*
