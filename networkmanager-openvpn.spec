%define nm_version          0.9.6.0
%define openvpn_version     2.1
%define shared_mime_version 0.16-3
%define gtk3_version        3.0

Summary:	NetworkManager VPN integration for OpenVPN
Name:		networkmanager-openvpn
Epoch:		1
Version:	0.9.6.0
Release:	2
License:	GPLv2+
Group:		System/Base
URL:		http://www.gnome.org/projects/NetworkManager/
Source0:	http://download.gnome.org/sources/NetworkManager-openvpn/0.8/NetworkManager-openvpn-%{version}.tar.xz
# ubuntu
#Patch0:	gtk_table_to_gtk_grid.patch

BuildRequires: gettext
BuildRequires: intltool
BuildRequires: libtool
BuildRequires: perl-XML-Parser
BuildRequires: perl
BuildRequires: pkgconfig(gtk+-3.0) >= %{gtk3_version}
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(libnm-util) >= %{nm_version}
BuildRequires: pkgconfig(libnm-glib) >= %{nm_version}
BuildRequires: pkgconfig(libnm-glib-vpn) >= %{nm_version}
BuildRequires: pkgconfig(gnome-keyring-1)
BuildRequires: pkgconfig(libpng15)
Requires: gtk+3             >= %{gtk3_version}
Requires: dbus
Requires: NetworkManager   >= %{nm_version}
Requires: openvpn          >= %{openvpn_version}
Requires: shared-mime-info >= %{shared_mime_version}
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
	--disable-dependency-tracking \
	--enable-more-warnings
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


%changelog
* Sat Feb 25 2012 Matthew Dawkins <mattydaw@mandriva.org> 1:0.9.2.0-1
+ Revision: 780679
- added p0 to fix gtk3 deprecated build failures
- move to build 0.9.2.0
- cleaned up spec

* Sun Nov 13 2011 Oden Eriksson <oeriksson@mandriva.com> 1:0.8.6.0-1
+ Revision: 730415
- 0.8.6.0
- 0.9.2.0

* Thu Apr 21 2011 Funda Wang <fwang@mandriva.org> 1:0.8.4-1
+ Revision: 656403
- bump req
- new version 0.8.4

* Sat Mar 05 2011 Andrey Borzenkov <arvidjaar@mandriva.org> 1:0.8.3.995-1
+ Revision: 642104
- update to 0.8.4-beta1

* Fri Nov 05 2010 Andrey Borzenkov <arvidjaar@mandriva.org> 1:0.8.2-1mdv2011.0
+ Revision: 593782
- 0.8.2 final

* Thu Nov 04 2010 Andrey Borzenkov <arvidjaar@mandriva.org> 1:0.8.1.999-1mdv2011.0
+ Revision: 593133
- update to 0.8.2-rc1

  + Funda Wang <fwang@mandriva.org>
    - New version 0.8.1

* Sat Jul 17 2010 Andrey Borzenkov <arvidjaar@mandriva.org> 1:0.8.0.997-1mdv2011.0
+ Revision: 554752
- new version 0.8.1-beta1

* Fri Feb 26 2010 Andrey Borzenkov <arvidjaar@mandriva.org> 1:0.8-1mdv2010.1
+ Revision: 511475
- disable icons for now as well
- desktop file is disabled upstream for now
- new version

* Sat Jan 23 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1:0.7.999-1mdv2010.1
+ Revision: 495350
- new version

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 1:0.7.0-12mdv2010.0
+ Revision: 440327
- rebuild

* Sun Nov 30 2008 Funda Wang <fwang@mandriva.org> 1:0.7.0-11mdv2009.1
+ Revision: 308371
- 0.7.0 final

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild early 2009.0 package (before pixel changes)

* Mon May 19 2008 David Walluck <walluck@mandriva.org> 1:0.7.0-10.svn3632.1mdv2009.0
+ Revision: 209014
- import networkmanager-openvpn


* Mon May 05 2008 Dan Williams <dcbw@redhat.com> 1:0.7.0-10.svn3632
- Fix issue with location of the VPN plugin

* Thu May 01 2008 Dan Williams <dcbw@redhat.com> 1:0.7.0-10.svn3627
- Update for compat with new NM bits

* Wed Apr 23 2008 Christoph Höger <choeger@cs.tu-berlin.de> 1:0.7.0-10.svn3549
- (Hopefully) Fix generation of nm-openvpn-service.name (#443389)
 
* Wed Apr 09 2008 Dan Williams <dcbw@redhat.com> 1:0.7.0-9.svn3549
- Update for compat with new NM bits

* Mon Mar 03 2008 Tim Niemueller <tim@niemueller.de> 1:0.7.0-9.svn3302
- Mute %%post and %%postun scripts

* Fri Feb 08 2008 Tim Niemueller <tim@niemueller.de> 1:0.7.0-8.svn3302
- Update to latest SVN snapshot
- Fixes rhbz#429816 (port was not saved correctly)
- Respects DNS search string from OpenVPN server

* Fri Jan 18 2008 Tim Niemueller <tim@niemueller.de> 1:0.7.0-7.svn3169
- Use install -p during "make install" to fix #342701

* Thu Dec 13 2007 Tim Niemueller <tim@niemueller.de> 1:0.7.0-6.svn3169
- Update to latest SVN snapshot

* Thu Dec  6 2007 Dan Williams <dcbw@redhat.com> 1:0.7.0-5.svn3140
- Update to latest SVN snapshot to get stuff working

* Fri Nov 23 2007 Tim Niemueller <tim@niemueller.de> 1:0.7.0-4.svn3047
- BuildRequire libtool and glib2-devel since we call autogen.sh now

* Fri Nov 23 2007 Tim Niemueller <tim@niemueller.de> 1:0.7.0-3.svn3047
- Fixed #320941
- Call autogen, therefore BuildRequire gnome-common
- Use plain 3047 from repo and use a patch, we cannot use trunk at the
  moment since it is in flux and incompatible with NM available for F8

* Wed Oct 31 2007 Tim Niemueller <tim@niemueller.de> 1:0.7.0-2.svn3047.fc8
- BuildRequire gettext

* Tue Oct 30 2007 Tim Niemueller <tim@niemueller.de> 1:0.7.0-1.svn3047.fc8
- Upgrade to trunk, needed to be compatible with NM 0.7.0, rebuild for F-8

* Fri Sep 15 2006 Tim Niemueller <tim@niemueller.de> 0.3.2-7
- Rebuild for FC6

* Sat Aug 19 2006 Tim Niemueller <tim@niemueller.de> 0.3.2-5
- Added perl-XML-Parser as a build requirement, needed for intltool

* Tue Aug 15 2006 Tim Niemueller <tim@niemueller.de> 0.3.2-4
- Added instructions how to build the source package
- removed a rm line

* Wed Aug 09 2006 Tim Niemueller <tim@niemueller.de> 0.3.2-3
- Added URL

* Fri Aug 04 2006 Tim Niemueller <tim@niemueller.de> 0.3.2-2
- Upgrade to current upstream version (0.3.2 on 0.6 branch)

* Mon Jul 10 2006 Tim Niemueller <tim@niemueller.de> 0.3.2-1
- Upgraded to 0.3.2 for 0.6 branch

* Tue Dec 06 2005 Tim Niemueller <tim@niemueller.de> 0.3-1
- Initial revision based on NetworkManager-vpnc spec

