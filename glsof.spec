Summary:	GUI for lsof
Summary(pl):	GUI do lsof
Name:		glsof
Version:	0.9.16
Release:	1
License:	GPL
Group:		X11/Applications/System
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	5ad5f2a6908be713753d9826c38e3e2c
Source1:	%{name}.desktop
Patch0:		%{name}-autorefresh.patch
URL:		http://glsof.sourceforge.net/
BuildRequires:	gtk+2-devel >= 2.0.0
BuildRequires:	libxml2-devel
BuildRequires:	pkgconfig
Requires:	lsof
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
glsof is a lsof GUI. You can Save output, Refresh (or Automatic
Refresh) output, select fields of output and apply lsof commands.

%description -l pl
glsof to GUI do lsof. Mo¿esz zachowywaæ wyj¶cie, od¶wie¿aæ (lub
automatycznie od¶wie¿aæ) wyj¶cie, wybieraæ pola wyj¶cia i u¿ywaæ
komend lsof.

%prep
%setup -q
%patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install pixmaps/logo.png $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.png
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_pixmapsdir}/*
%{_desktopdir}/*
