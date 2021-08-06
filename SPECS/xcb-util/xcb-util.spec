Summary:	provides extension libraries on top of libxcb.
Name:		xcb-util
Version:	0.4.0
Release:	1%{?dist}
License:	MIT
URL:		http://xcb.freedesktop.org/
Group:		Development/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://xcb.freedesktop.org/dist/%{name}-%{version}.tar.bz2
%define sha1 xcb-util=7f2e9b7efcc2c34eb1d6ae312c3d73b075832e46
BuildRequires:	libxcb-devel
Requires:	libxcb
%description
The XCB util modules provides a number of libraries which sit on top
of libxcb, the core X protocol library, and some of the extension
libraries. These experimental libraries provide convenience functions
and interfaces which make the raw X protocol more usable. Some of the
libraries also provide client-side code which is not strictly part of
the X protocol but which have traditionally been provided by Xlib.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
Requires:	libxcb-devel
%description	devel
It contains the libraries and header files to create applications
%prep
%setup -q
%build
%configure
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_libdir}/*
%exclude %{_libdir}/debug/
%exclude %{_libdir}/pkgconfig/
%exclude %{_libdir}/*.a
%exclude %{_libdir}/*.la
%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/pkgconfig/
%{_libdir}/*.a
%{_libdir}/*.la
%changelog
* Fri May 15 2015 Alexey Makhalov <amakhalov@vmware.com> 0.4.0-1
- initial version
