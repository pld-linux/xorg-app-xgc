Summary:	xgc application
Summary(pl.UTF-8):	Aplikacja xgc
Name:		xorg-app-xgc
Version:	1.0.1
Release:	3
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/app/xgc-%{version}.tar.bz2
# Source0-md5:	72fc8dd68f585000c0a542eba0264571
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXt-devel >= 1.0.0
BuildRequires:	xorg-util-util-macros >= 0.99.2
Requires:	xorg-lib-libXt >= 1.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xgc application.

%description -l pl.UTF-8
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
%doc Bugs COPYING ChangeLog
%attr(755,root,root) %{_bindir}/xgc
%{_datadir}/X11/app-defaults/Xgc
%{_mandir}/man1/xgc.1x*
