%include	/usr/lib/rpm/macros.python
Summary:	Eric3 is a full featured Python IDE
Summary(pl):	Eric3 - pe³nowarto¶ciowe IDE dla Pythona
Name:		eric
Version:	3.0.1
Release:	1
License:	GPL
Group:		X11/Development/Tools
Source0:	http://www.die-offenbachs.de/detlev/files/%{name}-%{version}.tar.gz
URL:		http://www.die-offenbachs.de/detlev/eric3.html
BuildRequires:	python-PyQt-devel >= 2.2.1
BuildRequires:	qt-devel >= 3.0.2
BuildRequires:  qt-static >= 3.0.2
BuildRequires:	rpm-pythonprov
BuildRequires:	sip >= 3.5
%requires_eq	sip
%pyrequires_eq	python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Eric3 is a full featured Python IDE that is written in PyQt using the
QScintilla editor widget.

%description -l pl
Eric3 jest pe³nowarto¶ciowym IDE dla Pythona napisanym w PyQt i
u¿ywaj±cy edytora QScintilla.

%prep
%setup -q 

%build
python install.py -b $RPM_BUILD_ROOT%{_bindir} -d $RPM_BUILD_ROOT%{py_sitedir} -i temp

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/python/%{module}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
cp -R examples3/* $RPM_BUILD_ROOT%{_examplesdir}/python/%{module}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README THANKS doc/%{module}/*
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{py_sitedir}/lib*.so*
