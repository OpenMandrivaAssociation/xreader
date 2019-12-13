%define major			3
%define major_xreaderdocument	3
%define major_xreaderview	3
%define api			1.5
%define gir_major		1.5

%define devname			%mklibname -d %{name}
%define libxreaderdocument	%mklibname xreaderdocument %{major_xreaderdocument}
%define libxreaderview		%mklibname xreaderview %{major_xreaderview}
%define girxreaderdocument	%mklibname xreaderdocument-gir %{gir_major}
%define girxreaderview		%mklibname xreaderview-gir %{gir_major}

Name:           xreader
Version:        2.4.3
Release:        1
Summary:        Simple document viewer
License:        GPLv2 and LGPLv2
Group:          Publishing
Url:            https://github.com/linuxmint/xreader
Source:         https://github.com/linuxmint/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  gnome-common
BuildRequires:  pkgconfig(libtiff-4) >= 3.6
BuildRequires:  pkgconfig(kpathsea)
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(ddjvuapi) >= 3.5.17
BuildRequires:  pkgconfig(gail-3.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.36.0
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 0.6
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtk+-unix-print-3.0)
BuildRequires:  pkgconfig(libgxps) >= 0.2.0
BuildRequires:  pkgconfig(libsecret-1) >= 0.5
BuildRequires:  pkgconfig(libspectre) >= 0.2.0
BuildRequires:  pkgconfig(libxml-2.0) >= 2.5.0
BuildRequires:  pkgconfig(poppler-glib) >= 0.16.0
BuildRequires:  pkgconfig(sm) >= 1.0.0
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(webkit2gtk-4.0) >= 2.4.3
BuildRequires:  pkgconfig(xapp) >= 1.1.0
BuildRequires:  itstool
BuildRequires:  intltool
BuildRequires:  meson
BuildRequires:  mathjax

Requires:       %{name}-backends = %{version}-%{release}
Obsoletes:      nemo-extension-xreader < %{version}-%{release}
Obsoletes:      caja-extension-xreader < %{version}-%{release}

%description
X-Apps Document Reader is a document viewer capable of displaying
multiple and singlepage document formats like PDF and PostScript.

%package -n %{libxreaderdocument}
Summary:        X-Apps Document Reader -- System Library
Group:          System/Libraries
Obsoletes:	%{_lib}xreaderview3_3 < 2.2.2

%description -n %{libxreaderdocument}
X-Apps Document Reader is a document viewer capable of displaying
multiple and singlepage document formats like PDF and PostScript.

%package -n %{libxreaderview}
Summary:        X-Apps Document Reader -- System Library
Group:          System/Libraries
Obsoletes:	%{_lib}xreaderdocument3_3 < 2.2.2

%description -n %{libxreaderview}
X-Apps Document Reader is a document viewer capable of displaying
multiple and singlepage document formats like PDF and PostScript.

%package backends
Summary:        XReader shared libraries (View and Document)
Group:          System/Libraries

%description backends
X-Apps Document Reader is a document viewer capable of displaying
multiple and singlepage document formats like PDF and PostScript.

%package -n %{devname}
Summary:        X-Apps Document Reader development files
Group:          Development/C
Requires:       %{name}-backends = %{version}-%{release}
Requires:       %{libxreaderdocument} = %{version}-%{release}
Requires:       %{libxreaderview} = %{version}-%{release}
Requires:	%{girxreaderdocument} = %{version}-%{release}
Requires:	%{girxreaderview} = %{version}-%{release}

%description -n %{devname}
X-Apps Document Reader is a document viewer capable of displaying
multiple and singlepage document formats like PDF and PostScript.

%package -n %{girxreaderdocument}
Summary:	GObject Introspection interface description for XreaderDocument
Group:		System/Libraries
Requires:	%{libxreaderdocument} = %{version}-%{release}
Obsoletes:	%{_lib}xreader-gir3.0 < 2.2.2

%description -n %{girxreaderdocument}
GObject Introspection interface description for XreaderDocument.

%package -n %{girxreaderview}
Summary:	GObject Introspection interface description for XreaderView
Group:		System/Libraries
Requires:	%{libxreaderview} = %{version}-%{release}
Conflicts:	%{_lib}xreader-gir3.0 < 2.2.1

%description -n %{girxreaderview}
GObject Introspection interface description for XreaderView.

%prep
%autosetup

%build
%meson \
  -Dintrospection=true
%meson_build

%install
%meson_install

%find_lang %{name} --with-gnome

find %{buildroot} -name '*.la' -delete

%files -f %{name}.lang
%license COPYING
%doc AUTHORS README
%{_bindir}/%{name}
%{_bindir}/%{name}-previewer
%{_bindir}/%{name}-thumbnailer
%{_datadir}/%{name}/
%{_libexecdir}/xreaderd
%dir %{_libdir}/%{name}/
%dir %{_libdir}/%{name}/%{major}/

%{_datadir}/thumbnailers/%{name}.thumbnailer
%{_datadir}/dbus-1/services/*.service
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/icons/hicolor/*/*/*
%{_mandir}/man?/*.*

%files -n %{libxreaderview}
%license COPYING
%doc AUTHORS README
%{_libdir}/libxreaderview.so.%{major_xreaderview}{,.*}

%files -n %{libxreaderdocument}
%license COPYING
%doc AUTHORS README
%{_libdir}/libxreaderdocument.so.%{major_xreaderdocument}{,.*}

%files -n %{girxreaderdocument}
%{_libdir}/girepository-1.0/XreaderDocument-%{gir_major}.typelib

%files -n %{girxreaderview}
%{_libdir}/girepository-1.0/XreaderView-%{gir_major}.typelib

%files -n %{devname}
%{_includedir}/%{name}/
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gir-1.0/XreaderDocument-%{gir_major}.gir
%{_datadir}/gir-1.0/XreaderView-%{gir_major}.gir

%files backends
%license COPYING
%doc AUTHORS README
%{_libdir}/%{name}/%{major}/backends/
