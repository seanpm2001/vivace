Summary:	PCI access library.
Name:		libpciaccess
Version:	0.13.3
Release:	1%{?dist}
License:	MIT
URL:		http://www.x.org/
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	ftp://ftp.x.org/pub/individual/lib/%{name}-%{version}.tar.bz2
%define sha1 libpciaccess=74e16b6d9a1d9d28279754010d2c4c4636b72e35
BuildRequires:	pkg-config util-macros 
Provides:	pkgconfig(pciaccess)
%description
The PCI access library.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
Requires:	pkg-config util-macros 
%description	devel
It contains the libraries and header files to create applications 
%prep
%setup -q 
%build
./configure --prefix=%{_prefix}
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_libdir}/*
%exclude %{_libdir}/debug/
%exclude %{_libdir}/*.a
%exclude %{_libdir}/*.la
%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.a
%{_libdir}/*.la
%changelog
*	Tue May 19 2015 Alexey Makhalov <amakhalov@vmware.com> 0.13.3-1
-	initial version
