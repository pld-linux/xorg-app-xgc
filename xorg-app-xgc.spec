Summary:	xgc application
Summary(pl):	Aplikacja xgc
Name:		xorg-app-xgc
Version:	0.99.2
Release:	0.1
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC3/app/xgc-%{version}.tar.bz2
# Source0-md5:	247841f01b9196d7ba0dae5f9e941a26
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xgc application.

%description -l pl
Aplikacja xgc.

%prep
%setup -q -n xgc-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Bugs ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_libdir}/X11/app-defaults/*
%{_mandir}/man1/*.1x*
