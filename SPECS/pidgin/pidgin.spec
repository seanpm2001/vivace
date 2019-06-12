Summary:	An instant messaging program
Name:		pidgin 
Version:	2.10.11
Release:	1%{?dist}
License:	GPL
URL:		http://anjuta.org/
Group:		Applications/Internet
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://downloads.sourceforge.net/project/%{name}/%{name}/%{version}/%{name}-%{version}.tar.bz2
%define sha1 pidgin=5e0062b81bdb01300804e12bc0b6a04a91984631
BuildRequires:	gtk2-devel pkg-config libxml2-devel gettext intltool ncurses-devel cyrus-sasl libgnome-keyring-devel nss-devel dbus GConf-devel perl python2-devel libtool libstdc++-devel gtk-doc openssl-devel 
Requires:	ncurses GConf perl nss gtk2 libxml2 openssl python2 libstdc++ libgnome-keyring
%description
Pidgin is an instant messaging program which lets you log in to accounts on multiple chat networks simultaneously. 

%package devel
Summary:        Headers, Documentation, and Libraries for Pidgin
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       glib-devel
Requires:       gtk2-devel

%description devel
Header, library and documentation for developing pidgin plugins

%prep
%setup -q 
%build
./configure 	--prefix=%{_prefix} \
		--disable-static \
		--disable-screensaver \
		--disable-gtkspell \
		--disable-gstreamer \
		--disable-vv \
		--disable-idn \
		--disable-meanwhile \
		--disable-avahi \
		--disable-nm \
		--disable-tcl
		

make %{?_smp_mflags}
%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install

ln -s pidgin/logo.png %{buildroot}%{_datadir}/pixmaps/%{name}.png

%clean
rm -rf %{buildroot}

%post
update-mime-database %{_datadir}/mime &> /dev/null 
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null 

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null 
/sbin/ldconfig


%postun
update-mime-database %{_datadir}/mime &> /dev/null 
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null 
/sbin/ldconfig

%files 
%defattr(-,root,root)
%doc AUTHORS COPYING COPYRIGHT ChangeLog NEWS README doc/the_penguin.txt
%{_bindir}
%{_libdir}
%exclude %{_libdir}/debug
%exclude %{_libdir}/*.la
%exclude %{_libdir}/*.so
%exclude %{_libdir}/*.so.0
%exclude %{_libdir}/pkgconfig
%dir %{_datadir}/appdata
%{_datadir}/appdata/pidgin.appdata.xml
%{_prefix}%{_sysconfdir}/gconf
%{_datadir}/pixmaps
%{_datadir}/icons
%{_datadir}/applications
%{_datadir}/sounds/purple/
%{_mandir}/man1/%{name}.*

%files devel
%defattr(-,root,root)
%{_includedir}
%{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/*.so.0
%{_libdir}/pkgconfig
%{_datadir}/man
%{_datadir}/purple
%{_datadir}/locale
%{_datadir}/aclocal
%changelog
*	Wed Jul 08 2015 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 2.10.11-1
-	initial version
