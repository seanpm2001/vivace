Summary:	X11 libXpm runtime library.
Name:		libXpm
Version:	3.5.13
Release:	1%{?dist}
License:	MIT
URL:		http://www.x.org/
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	ftp://ftp.x.org/pub/individual/lib/%{name}-%{version}.tar.bz2
%define sha1 libXpm=38b1a2728adb49f4e255aba1530f51789815ffc4
BuildRequires:	libXext-devel libXt-devel libXau-devel
Requires:	libXext libXt libXau
Provides:	libxpm
Provides:	pkgconfig(xpm)
%description
The X11 libXpm runtime library.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
Requires:	libXext-devel libXt-devel libXau-devel
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
%{_bindir}/*
%{_libdir}/*
%exclude %{_libdir}/debug/
%exclude %{_libdir}/pkgconfig/
%exclude %{_libdir}/*.a
%exclude %{_libdir}/*.la
%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/pkgconfig/
%{_datadir}/*
%changelog
* Tue Aug 03 2021 Alexey Makhalov <amakhalov@vmware.com> 3.5.13-1
- Version update
* Tue May 19 2015 Alexey Makhalov <amakhalov@vmware.com> 3.5.11-1
- initial version
