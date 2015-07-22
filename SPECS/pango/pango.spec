Summary:	library for laying out and rendering of text.
Name:		pango
Version:	1.36.8
Release:	1
License:	LGPLv2+
URL:		http://www.pango.org
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/1.36/%{name}-%{version}.tar.xz
%define sha1 pango=c6ba02ee8f9d8b22b7cfd74c4b6ae170bebc8d2b
BuildRequires:	cairo-devel libXft-devel gobject-introspection-devel gobject-introspection-python
Requires:	cairo libXft gobject-introspection
%description
Pango is a library for laying out and rendering of text, with an emphasis on internationalization. It can be used anywhere that text layout is needed, though most of the work on Pango so far has been done in the context of the GTK+ widget toolkit.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
Requires:	cairo-devel libXft-devel gobject-introspection-devel gobject-introspection-python
%description	devel
It contains the libraries and header files to create applications 
%prep
%setup -q 
%build
./configure --prefix=%{_prefix} --sysconfdir=%{_sysconfdir}
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%post
pango-querymodules --update-cache
%files
%defattr(-,root,root)
%{_bindir}/*
%{_libdir}/*
%exclude %{_libdir}/debug/
%exclude %{_libdir}/*.la
%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.la
%{_datadir}/*
%changelog
*	Thu May 21 2015 Alexey Makhalov <amakhalov@vmware.com> 1.36.8-1
-	initial version
