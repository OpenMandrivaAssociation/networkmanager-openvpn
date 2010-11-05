%define nm_version          0.8.2
%define dbus_version        1.1
%define gtk2_version        2.10.0
%define openvpn_version     2.1
%define shared_mime_version 0.16-3

Summary: NetworkManager VPN integration for OpenVPN
Name: networkmanager-openvpn
Epoch:   1
Version: 0.8.2
Release: %mkrel 1
License: GPLv2+
URL: http://www.gnome.org/projects/NetworkManager/
Group: System/Base
Source: http://download.gnome.org/sources/NetworkManager-openvpn/0.8/NetworkManager-openvpn-%version.tar.bz2
BuildRequires: gtk2-devel >= %{gtk2_version}
BuildRequires: dbus-devel >= %{dbus_version}
BuildRequires: libnm-util-devel >= %{nm_version}
BuildRequires: libnm-glib-devel >= %{nm_version}
BuildRequires: libnm-glib-vpn-devel >= %{nm_version}
BuildRequires: glib2-devel
BuildRequires: libGConf2-devel
BuildRequires: gnomeui2-devel
BuildRequires: libgnome-keyring-devel
BuildRequires: libglade2.0-devel
BuildRequires: libpng-devel
BuildRequires: perl-XML-Parser
BuildRequires: libtool intltool gettext
BuildRequires: perl
BuildRequires: gnome-common
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils
Requires: gtk2             >= %{gtk2_version}
Requires: dbus             >= %{dbus_version}
Requires: NetworkManager   >= %{nm_version}
Requires: openvpn          >= %{openvpn_version}
Requires: shared-mime-info >= %{shared_mime_version}
Requires: GConf2
Requires: gnome-keyring
BuildRoot: %{_tmppath}/%{name}-%{version}

%description
This package contains software for integrating the OpenVPN VPN software
with NetworkManager and the GNOME desktop.

%prep
%setup -q -n NetworkManager-openvpn-%{version}

%build
if [ ! -f configure ]; then
  ./autogen.sh
fi
%configure2_5x --disable-static --disable-dependency-tracking
%make

%install
rm -rf %{buildroot}
%makeinstall_std

rm -f %{buildroot}%{_libdir}/NetworkManager/*.la

%find_lang NetworkManager-openvpn

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post
%{update_desktop_database}
%update_icon_cache hicolor

%postun
%{clean_desktop_database}
%clean_icon_cache hicolor
%endif

%files -f NetworkManager-openvpn.lang
%defattr(-, root, root)
%doc AUTHORS ChangeLog README
%{_libdir}/NetworkManager/libnm-openvpn-properties.so
%{_libexecdir}/nm-openvpn-auth-dialog
%{_libexecdir}/nm-openvpn-service
%{_libexecdir}/nm-openvpn-service-openvpn-helper
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/nm-openvpn-service.conf
%config(noreplace) %{_sysconfdir}/NetworkManager/VPN/nm-openvpn-service.name
%{_datadir}/gnome-vpn-properties/openvpn/nm-openvpn-dialog.glade
# For now disabled in upstream
#{_datadir}/applications/nm-openvpn.desktop
#{_datadir}/icons/hicolor/*/apps/*
