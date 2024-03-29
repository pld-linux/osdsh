Summary:	On Screen Display (like in TV) for X11
Summary(pl.UTF-8):	Wyświetlanie napisów na ekranie podobnie jak w telewizorach (OSD)
Name:		osdsh
Version:	0.5.2
Release:	3
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/osdsh/%{name}%{version}.tar.gz
# Source0-md5:	3363072ceba34b5c84328f8741924199
Source1:	%{name}.desktop
Source2:	osd_keymapconfig.desktop
Source3:	osd_tk%{name}config.desktop
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-cc.patch
URL:		http://sourceforge.net/projects/osdsh/
BuildRequires:	XFree86-devel
BuildRequires:	apmd-devel
BuildRequires:	gtk+-devel
BuildRequires:	xosd-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
Display clock, battery, connection and volume with the xosdlib. The
options can be changed while running and can be different for each
display.

%description -l pl.UTF-8
Wyświetla zegar, baterie, połączenia oraz głośność za pomocą xosdlib.
Opcje mogą być zmieniane w czasie pracy i mogą być różne dla każdego
ekranu.

%package devel
Summary:	Header files and documentation for developers of osdsh
Summary(pl.UTF-8):	Pliki nagłówkowe oraz dokumentcja dla programistów osdsh
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Files allowing development of osdsh-based applications.

%description devel -l pl.UTF-8
Pliki pozwalające tworzyć programy w oparciu o osdsh.

%prep
%setup  -q
%patch0 -p1
%patch1 -p1

%build
mv data/README data/README.data
mv HOWTO/README HOWTO/README.howto

%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT PREFIX=%{_prefix}

install tkosdshconfig		$RPM_BUILD_ROOT%{_bindir}
install HOWTO/keymapconfig	$RPM_BUILD_ROOT%{_bindir}

install %{SOURCE1} %{SOURCE2} %{SOURCE3} $RPM_BUILD_ROOT%{_desktopdir}

rm -rf $RPM_BUILD_ROOT/usr/doc

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README* data/* HOWTO/{*.html,README.howto}
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*
%{_desktopdir}/*.desktop

%files devel
%defattr(644,root,root,755)
%{_libdir}/lib*.so
%{_includedir}/*.h
