Summary:	On Screen Display (like in TV) for X11
Summary(pl):	Wy¶wietlanie napisów na ekranie podobnie jak w telewizorach (OSD)
Name:		osdsh
Version:	0.5.2
Release:	3
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/sourceforge/%{name}/%{name}%{version}.tar.gz
# Source0-md5:	3363072ceba34b5c84328f8741924199
Source1:	%{name}.desktop
Source2:	osd_keymapconfig.desktop
Source3:	osd_tkosdshconfig.desktop
Patch0:		%{name}-DESTDIR.patch
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

%description -l pl
Wy¶wietla zegar, baterie, po³±czenia oraz g³o¶no¶æ za pomoc± xosdlib.
Opcje mog± byæ zmieniane w czasie pracy i mog± byæ ró¿ne dla ka¿dego
ekranu.

%package devel
Summary:	Header files and documentation for developers of osdsh
Summary(pl):	Pliki nag³ówkowe oraz dokumentcja dla programistów osdsh
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}

%description devel
Files allowing development of osdsh-based applications.

%description devel -l pl
Pliki pozwalaj±ce tworzyæ programy w oparciu o osdsh.

%prep
%setup  -q
%patch0 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT PREFIX=%{_prefix}

install tkosdshconfig		$RPM_BUILD_ROOT%{_bindir}
install HOWTO/keymapconfig	$RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Tools,%{_applnkdir}/Settings}
install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Tools
install %{SOURCE2} $RPM_BUILD_ROOT%{_applnkdir}/Settings
install %{SOURCE3} $RPM_BUILD_ROOT%{_applnkdir}/Settings

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README* data/* HOWTO/{*.html,README}
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*
%{_applnkdir}/*/*

%files devel
%defattr(644,root,root,755)
%attr(644,root,root) %{_libdir}/lib*.so
%{_includedir}/*.h
