Summary:	X11 Authorization Protocol library.
Name:		libXau
Version:	1.0.9
Release:	1%{?dist}
License:	MIT
URL:		http://www.x.org/
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.x.org/pub/individual/lib/%{name}-%{version}.tar.bz2
%define sha1 libXau=ef9b1ad00f958c8b6e30a1bbc11fdfac311c9733
BuildRequires:	xorgproto
%description
The libXau package contains a library implementing the X11 Authorization Protocol. This is useful for restricting client access to the display.

%package	devel
Summary:	Header and development files for libXau
Requires:	%{name} = %{version}
Requires:	xorgproto
%description	devel
It contains the libraries and header files to create applications
%prep
%setup -q
%build
%configure
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%check
make -k check |& tee %{_specdir}/%{name}-check-log || %{nocheck}
%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig
%files
%defattr(-,root,root)
%{_libdir}/*
%exclude %{_libdir}/debug/
%exclude %{_libdir}/pkgconfig/
%files devel
%defattr(-,root,root)
%{_mandir}/*
%{_includedir}/*
%{_libdir}/pkgconfig/
%changelog
* Tue Aug 03 2021 Alexey Makhalov <amakhalov@vmware.com> 1.0.9-1
- Version update
* Fri May 15 2015 Alexey Makhalov <amakhalov@vmware.com> 1.0.8-1
- initial version
