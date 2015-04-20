Summary:	xgc application - X graphics demo
Summary(pl.UTF-8):	Aplikacja xgc - program demonstracyjny grafiki X
Name:		xorg-app-xgc
Version:	1.0.5
Release:	1
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/app/xgc-%{version}.tar.bz2
# Source0-md5:	025a3717040232ad49b1dd027884f182
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXt-devel >= 1.0.0
BuildRequires:	xorg-util-util-macros >= 1.8
Requires:	xorg-lib-libXt >= 1.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xgc application is an X11 graphics demo that shows various features
of the X11 core protocol graphics primitives.

%description -l pl.UTF-8
Aplikacja xgc to program demonstracyjny grafiki X11, pokazujący różne
cechy prymitywów graficznych podstawowego protokołu X11.

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
%doc Bugs COPYING ChangeLog README
%attr(755,root,root) %{_bindir}/xgc
%{_datadir}/X11/app-defaults/Xgc
%{_datadir}/X11/app-defaults/Xgc-color
%{_mandir}/man1/xgc.1*
