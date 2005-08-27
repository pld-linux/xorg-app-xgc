Summary:	xgc application
Summary(pl):	Aplikacja xgc
Name:		xorg-app-xgc
Version:	0.99.0
Release:	0.02
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/app/xgc-%{version}.tar.bz2
# Source0-md5:	623999842bebe7b2768fa75cf56eb499
Patch0:		xgc-man.patch
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	pkgconfig >= 0.19
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xgc application.

%description -l pl
Aplikacja xgc.

%prep
%setup -q -n xgc-%{version}
%patch0 -p1

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
%{_sysconfdir}/X11/app-defaults/*
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*.1*
