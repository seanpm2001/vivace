Summary:	X Font Service client library.
Name:		libFS
Version:	1.0.6
Release:	1%{?dist}
License:	MIT
URL:		http://www.x.org/
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	ftp://ftp.x.org/pub/individual/lib/libFS-1.0.6.tar.bz2
%define sha1 libFS=5e490557674ebef057c3909e2608d7799393b88e
BuildRequires:	xtrans-devel
Requires:	xtrans
%description
X Font Service client library.
%package	devel
Summary:	Header and development files for libFS
Requires:	%{name} = %{version}
Requires:	xtrans-devel
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
%{_datadir}/*
%changelog
*	Mon May 18 2015 Alexey Makhalov <amakhalov@vmware.com> 1.0.6-1
-	initial version
