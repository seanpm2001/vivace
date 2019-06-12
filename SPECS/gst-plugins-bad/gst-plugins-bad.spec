Summary:	The GStreamer Bad Plug-ins package contains a set a set of plug-ins that aren't up to par compared to the rest
Name:		gst-plugins-bad
Version:	1.5.1 
Release:	1%{?dist}
License:	LGPLv2
URL:		http://gstreamer.freedesktop.org/
Group:		Applications/Multimedia
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://gstreamer.freedesktop.org/src/%{name}/%{name}-%{version}.tar.xz
%define sha1 gst-plugins-bad=48975aca3cf0bc8a26b79491d70227afb8c72a16
BuildRequires:	gstreamer-plugins-base-devel 
Requires:	gstreamer-plugins-base
%description
The GStreamer Good Plug-ins is a set of plug-ins considered by the GStreamer developers to have good quality code, correct functionality, and the preferred license (LGPL). A wide range of video and audio decoders, encoders, and filters are included. 

%package	devel
Summary:	GStreamer Plugin Library Headers
Group: 		Development/Libraries
Requires:	%{name} = %{version}
Requires:	gstreamer-plugins-base-devel 
%description	devel
The GStreamer Bad Plug-ins package contains a set a set of plug-ins that aren't up to par compared to the rest
%prep
%setup -q 
%build
./configure --prefix=%{_prefix} 
make %{?_smp_mflags}
                                                                       
%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc AUTHORS COPYING README REQUIREMENTS
%{_datadir}/
%{_libdir}/*.so.*
%exclude %{_libdir}/debug/

%files devel
%{_libdir}/*.la
%{_libdir}/gstreamer-1.0/*.la
%{_libdir}/gstreamer-1.0/*.so
%{_libdir}/*.so
%{_libdir}/pkgconfig
%{_libdir}/girepository-1.0
%{_includedir}/gstreamer-1.0
%{_datadir}/locale
%{_datadir}/doc
%{_datadir}/gtk-doc
%{_datadir}/gstreamer-1.0

%changelog
*	Mon Jul 13 2015 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 1.5.1 -1
-	initial version
