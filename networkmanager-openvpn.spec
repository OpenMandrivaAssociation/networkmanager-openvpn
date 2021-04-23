%define url_ver %(echo %{version}|cut -d. -f1,2)
%define _disable_lto 1

Summary:	NetworkManager VPN integration for OpenVPN
Name:		networkmanager-openvpn
Version:	1.8.14
Release:	2
License:	GPLv2+
Group:		System/Base
Url:		http://www.gnome.org/projects/NetworkManager/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/NetworkManager-openvpn/%{url_ver}/NetworkManager-openvpn-%{version}.tar.xz
Source1:	%{name}.sysusers
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
Requires:	dbus
Requires:	gtk+3
Requires:	NetworkManager
Requires:	openvpn
Requires:	shared-mime-info

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
install -D -p -m 644 %{SOURCE1} %{buildroot}%{_sysusersdir}/%{name}.conf

%find_lang NetworkManager-openvpn

%files -f NetworkManager-openvpn.lang
%doc AUTHORS ChangeLog README
%{_sysusersdir}/%{name}.conf
%{_datadir}/dbus-1/system.d/nm-openvpn-service.conf
%{_libdir}/NetworkManager/*.so
%{_libexecdir}/nm-openvpn-auth-dialog
%{_libexecdir}/nm-openvpn-service
%{_libexecdir}/nm-openvpn-service-openvpn-helper
%{_prefix}/lib/NetworkManager/VPN/nm-openvpn-service.name
%{_datadir}/metainfo/network-manager-openvpn.metainfo.xml
