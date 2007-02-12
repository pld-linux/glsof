Summary:	GUI for lsof
Summary(pl.UTF-8):   GUI do lsof
Name:		glsof
Version:	0.9.17
Release:	1
License:	GPL
Group:		X11/Applications/System
Source0:	http://dl.sourceforge.net/glsof/%{name}-%{version}.tar.gz
# Source0-md5:	1eb3dafb3929b7cd2ba9cff8643f8689
Patch0:		%{name}-desktop.patch
URL:		http://glsof.sourceforge.net/
BuildRequires:	GConf2-devel
BuildRequires:	gtk+2-devel
BuildRequires:	libgnomeui-devel
BuildRequires:	pkgconfig
Requires:	lsof
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
glsof is a lsof GUI. You can Save output, Refresh (or Automatic
Refresh) output, select fields of output and apply lsof commands.

%description -l pl.UTF-8
glsof to GUI do lsof. Można zachowywać wyjście, odświeżać (lub
automatycznie odświeżać) wyjście, wybierać pola wyjścia i używać
komend lsof.

%prep
%setup -q
%patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_pixmapsdir}/*
%{_desktopdir}/*.desktop
