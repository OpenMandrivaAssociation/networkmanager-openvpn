%define url_ver %(echo %{version}|cut -d. -f1,2)

Summary:	NetworkManager VPN integration for OpenVPN
Name:		networkmanager-openvpn
Version:	1.12.0
Release:	1
License:	GPLv2+
Group:		System/Base
Url:		https://www.gnome.org/projects/NetworkManager/
Source0:	https://ftp.gnome.org/pub/GNOME/sources/NetworkManager-openvpn/%{url_ver}/NetworkManager-openvpn-%{version}.tar.xz
Source1:	%{name}.sysusers

BuildRequires:	gettext
BuildRequires:	libtool
BuildRequires:	intltool
BuildRequires:	perl-XML-Parser
BuildRequires:	perl
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(gtk4)
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(gnome-keyring-1)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libsecret-unstable)
BuildRequires:	pkgconfig(libnma)
Requires:	dbus
Requires:	NetworkManager
Requires:	openvpn
Requires:	shared-mime-info

%description
This package contains software for integrating the OpenVPN VPN software
with NetworkManager and the GNOME desktop.

%package gtk
Summary:	GTK frontend for configuring OpenVPN connections with NetworkManager
Group:		Tools
Requires:	%{name} = %{EVRD}
Supplements:	networkmanager-applet

%description gtk
GTK frontend for configuring OpenVPN connections with NetworkManager

%prep
%autosetup -p1 -n NetworkManager-openvpn-%{version}
%configure \
	--disable-static \
	--disable-dependency-tracking \
	--enable-more-warnings \
	--without-libnm-glib \
	--with-gtk4=yes

%build
%make_build

%install
%make_install
install -D -p -m 644 %{SOURCE1} %{buildroot}%{_sysusersdir}/%{name}.conf

%find_lang NetworkManager-openvpn

%files -f NetworkManager-openvpn.lang
%doc AUTHORS README
%{_sysusersdir}/%{name}.conf
%{_datadir}/dbus-1/system.d/nm-openvpn-service.conf
%{_libdir}/NetworkManager/libnm-vpn-plugin-openvpn.so
%{_libexecdir}/nm-openvpn-service
%{_libexecdir}/nm-openvpn-service-openvpn-helper
%{_prefix}/lib/NetworkManager/VPN/nm-openvpn-service.name
%{_datadir}/metainfo/network-manager-openvpn.metainfo.xml

%files gtk
%{_libdir}/NetworkManager/libnm-vpn-plugin-openvpn-editor.so
%{_libdir}/NetworkManager/libnm-gtk4-vpn-plugin-openvpn-editor.so
%{_libexecdir}/nm-openvpn-auth-dialog
