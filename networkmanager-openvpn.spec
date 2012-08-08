%define nm_version          0.9.2.0
%define openvpn_version     2.1
%define shared_mime_version 0.16-3

Summary:	NetworkManager VPN integration for OpenVPN
Name:		networkmanager-openvpn
Epoch:		1
Version:	0.9.6.0
Release:	1
License:	GPLv2+
Group:		System/Base
URL:		http://www.gnome.org/projects/NetworkManager/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/NetworkManager-openvpn/NetworkManager-openvpn-%{version}.tar.xz
# ubuntu
Patch0:	gtk_table_to_gtk_grid.patch

BuildRequires: gettext
BuildRequires: gnome-common
BuildRequires: intltool
BuildRequires: libtool
BuildRequires: perl-XML-Parser
BuildRequires: perl
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(libnm-util) >= %{nm_version}
BuildRequires: pkgconfig(libnm-glib) >= %{nm_version}
BuildRequires: pkgconfig(libnm-glib-vpn) >= %{nm_version}
BuildRequires: pkgconfig(gconf-2.0)
BuildRequires: pkgconfig(libgnomeui-2.0)
BuildRequires: pkgconfig(gnome-keyring-1)
BuildRequires: pkgconfig(libpng15)
Requires: gtk+3
Requires: dbus
Requires: NetworkManager   >= %{nm_version}
Requires: openvpn          >= %{openvpn_version}
Requires: shared-mime-info >= %{shared_mime_version}
Requires: GConf2
Requires: gnome-keyring

%description
This package contains software for integrating the OpenVPN VPN software
with NetworkManager and the GNOME desktop.

%prep
%setup -qn NetworkManager-openvpn-%{version}
%apply_patches

%build
%configure2_5x \
	--disable-static \
	--disable-dependency-tracking

%make

%install
rm -rf %{buildroot}
%makeinstall_std

rm -f %{buildroot}%{_libdir}/NetworkManager/*.la

%find_lang NetworkManager-openvpn

%files -f NetworkManager-openvpn.lang
%doc AUTHORS ChangeLog README
%{_libdir}/NetworkManager/libnm-openvpn-properties.so
%{_libexecdir}/nm-openvpn-auth-dialog
%{_libexecdir}/nm-openvpn-service
%{_libexecdir}/nm-openvpn-service-openvpn-helper
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/nm-openvpn-service.conf
%config(noreplace) %{_sysconfdir}/NetworkManager/VPN/nm-openvpn-service.name
%{_datadir}/gnome-vpn-properties/openvpn/nm-openvpn-dialog.ui
# For now disabled in upstream
#{_datadir}/applications/nm-openvpn.desktop
#{_datadir}/icons/hicolor/*/apps/*
