# TODO:
# - separate packages (eg. brm, KdeQt - with R: python-PyKDE)
#
%define		tar_name	eric
Summary:	Eric3 is a full featured Python IDE
Summary(pl):	Eric3 - pe³nowarto¶ciowe IDE dla Pythona
Name:		eric3
Version:	3.9.1
Release:	1
License:	GPL
Group:		X11/Development/Tools
Source0:	http://dl.sourceforge.net/eric-ide/%{tar_name}-%{version}.tar.gz
# Source0-md5:	7f62b297fa094e547faca7966ccd133d
Source1:	%{name}.desktop
URL:		http://www.die-offenbachs.de/detlev/eric3.html
BuildRequires:	python-PyQt >= 3.15
BuildRequires:	qscintilla-devel >= 1:1.5
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
Requires:	python-PyQt >= 3.15
Requires:	python-devel-tools
Obsoletes:	eric
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Eric3 is a full featured Python IDE that is written in PyQt using the
QScintilla editor widget.

%description -l pl
Eric3 jest pe³nowarto¶ciowym IDE dla Pythona napisanym w PyQt i
u¿ywaj±cym edytora QScintilla.

%package doc
Summary:	Documentation for Eric3
Summary(pl):	Dodatkowa dokumentacja dla Eric3
Group:		X11/Development/Tools
Requires:	%{name} = %{version}-%{release}

%description doc
Documentation for Eric3.

%description doc -l pl
Dodatkowa dokumentacja dla Eric3.

%prep
%setup -q -n %{tar_name}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_docdir}/%{name},%{_pixmapsdir},%{_desktopdir}}

python install.py -c -b %{_bindir} -d %{py_sitedir} -i $RPM_BUILD_ROOT

%py_comp $RPM_BUILD_ROOT%{py_sitedir}/*
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}/*

cp $RPM_BUILD_ROOT%{py_sitedir}/%{name}/icons/default/eric.png $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.png
install %SOURCE1 $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

# NOTE: eric3 uses *.py files for it's own purposes
# so do not remove them from package

%files
%defattr(644,root,root,755)
%doc HISTORY README* THANKS
%attr(755,root,root) %{_bindir}/*
%{py_sitedir}/eric3config.py
%{py_sitedir}/sitecustomize.py
%{py_sitedir}/%{name}
%exclude %{py_sitedir}/%{name}/Documentation
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png

%files doc
%defattr(644,root,root,755)
%dir %{py_sitedir}/%{name}/Documentation
%{py_sitedir}/%{name}/Documentation/mod_python.*
%{py_sitedir}/%{name}/Documentation/Source
