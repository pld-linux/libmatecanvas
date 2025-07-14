# NOTE: this package is deprecated, meant for MATE <= 1.4 compatibility only
#
# Conditional build:
%bcond_without	apidocs		# disable gtk-doc
#
Summary:	MateCanvas widget
Summary(pl.UTF-8):	Widget MateCanvas
Name:		libmatecanvas
Version:	1.4.0
Release:	1
License:	LGPL v2+
Group:		X11/Libraries
Source0:	http://pub.mate-desktop.org/releases/1.4/%{name}-%{version}.tar.xz
# Source0-md5:	4d37944defbc3518337a73141d51aa14
Patch0:		%{name}-am.patch
URL:		http://mate.desktop.org/
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake >= 1:1.9
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gail-devel >= 1.20.0
BuildRequires:	glib2-devel >= 1:2.10.0
BuildRequires:	gettext-tools >= 0.10.40
BuildRequires:	gtk+2-devel >= 2:2.12.0
%{?with_apidocs:BuildRequires:	gtk-doc >= 1.8}
BuildRequires:	gtk-doc-automake >= 1.8
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libart_lgpl-devel >= 2.3.19
BuildRequires:	libglade2-devel >= 1:2.6.2
BuildRequires:	libtool >= 1:1.4.3
BuildRequires:	mate-common
BuildRequires:	pango-devel >= 1:1.0.1
BuildRequires:	perl-base
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	gail >= 1.20.0
Requires:	glib2 >= 1:2.10.0
Requires:	gtk+2 >= 2:2.12.0
Requires:	libart_lgpl >= 2.3.19
Requires:	libglade2 >= 1:2.6.2
Requires:	pango >= 1:1.0.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The canvas widget allows you to create custom displays using stock
items such as circles, lines, text, and so on. It was originally a
port of the Tk canvas widget but has evolved quite a bit over time.
libmatecanvas is a fork of libgnomecanvas.

%description -l pl.UTF-8
Widget canvas pozwala tworzyć własne widoki przy użyciu zgromadzonych
rzeczy takich jak koła, linie, tekst itp. Oryginalnie był to port
widgetu Tk canvas, ale od tamtego czasu nieco wyewoluował.
libmatecanvas to odgałęzienie pakietu libgnomecanvas.

%package devel
Summary:	libmatecanvas header files
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libmatecanvas
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gail-devel >= 1.20.0
Requires:	glib2-devel >= 1:2.10.0
Requires:	gtk+2-devel >= 2:2.12.0
Requires:	libart_lgpl-devel >= 2.3.19
Requires:	libglade2-devel >= 1:2.6.2
Requires:	pango-devel >= 1:1.0.1

%description devel
Development part of libmatecanvas - header files.

%description devel -l pl.UTF-8
Część libmatecanvas dla programistów - pliki nagłówkowe.

%package apidocs
Summary:	libmatecanvas API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki libmatecanvas
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
libmatecanvas API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki libmatecanvas.

%prep
%setup -q
%patch -P0 -p1

%build
%{__gtkdocize}
%{__glib_gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-glade \
	%{?with_apidocs:--enable-gtk-doc} \
	--disable-static \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libglade/2.0/*.la \
	$RPM_BUILD_ROOT%{_libdir}/*.la

%{__mv} $RPM_BUILD_ROOT%{_datadir}/locale/{sr@ije,sr@ijekavian}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libmatecanvas-2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmatecanvas-2.so.0
%attr(755,root,root) %{_libdir}/libglade/2.0/libgladematecanvas.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmatecanvas-2.so
%{_includedir}/libmatecanvas-2.0
%{_pkgconfigdir}/libmatecanvas-2.0.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libmatecanvas
