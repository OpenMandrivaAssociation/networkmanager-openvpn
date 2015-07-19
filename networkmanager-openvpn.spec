%define url_ver %(echo %{version}|cut -d. -f1,2)

Summary:	NetworkManager VPN integration for OpenVPN
Name:		networkmanager-openvpn
Epoch:		1
Version:	0.9.8.4
Release:	9
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
BuildRequires:	pkgconfig(libnm-util)
BuildRequires:	pkgconfig(libnm-glib)
BuildRequires:	pkgconfig(libnm-glib-vpn)
BuildRequires:	pkgconfig(gnome-keyring-1)
BuildRequires:	pkgconfig(libpng)
Requires:	dbus
Requires:	gnome-keyring
Requires:	gtk+3
Requires:	NetworkManager
Requires:	openvpn
Requires:	shared-mime-info

%description
This package contains software for integrating the OpenVPN VPN software
with NetworkManager and the GNOME desktop.

%prep
%setup -qn NetworkManager-openvpn-%{version}
%apply_patches

%build
%configure2_5x \
	--disable-static \
	--disable-dependency-tracking \
	--enable-more-warnings
%make

%install
%makeinstall_std

%find_lang NetworkManager-openvpn

%files -f NetworkManager-openvpn.lang
%doc AUTHORS ChangeLog README
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/nm-openvpn-service.conf
%config(noreplace) %{_sysconfdir}/NetworkManager/VPN/nm-openvpn-service.name
%{_libdir}/NetworkManager/libnm-openvpn-properties.so
%{_libexecdir}/nm-openvpn-auth-dialog
%{_libexecdir}/nm-openvpn-service
%{_libexecdir}/nm-openvpn-service-openvpn-helper
%{_datadir}/gnome-vpn-properties/openvpn/nm-openvpn-dialog.ui
# For now disabled in upstream
#{_datadir}/applications/nm-openvpn.desktop
#{_datadir}/icons/hicolor/*/apps/*

