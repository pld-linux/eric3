%include	/usr/lib/rpm/macros.python
Summary:	Eric3 is a full featured Python IDE
Summary(pl):	Eric3 jest pe³nowarto¶ciowym IDE dla Python'a
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
Eric3 is a full featured Python IDE that is written in PyQt using the QScintilla editor widget

%description -l pl
Eric3 jest pe³nowarto¶ciowym IDE dla Python'a napisanym w  PyQt i u¿ywaj±cy edytor QScintilla

#%package devel
#Summary: Files needed to build other bindings based on Qt
#Summary(pl): Pliki nag³ówkowe %{name}
#Requires: %{name} = %{version}
#Group: Development/Languages/Python

#%description devel
#Files needed to build other bindings for C++ classes that inherit from any
#of the Qt classes (e.g. KDE or your own).

#%description devel -l pl
#Files needed to build other bindings for C++ classes that inherit from any
#of the Qt classes (e.g. KDE or your own).

#%package examples
#Summary: Examples for PyQt
#Summary(pl): Przyklady dla PyQt
#Requires: %{name} = %{version}
#Group: Libraries/Python

#%description examples
#Examples code demonstrating how to use the Python bindings for Qt.

#%description examples -l pl
#Przykladowy kod demonstruj±cy jak u¿ywaæ PyQT.

%prep
%setup -q 

%build

#rm -rf $RPM_BUILD_ROOT
#install -d $RPM_BUILD_ROOT%{py_sitedir}
#install -d $RPM_BUILD_ROOT%{_bindir}
python install.py -b $RPM_BUILD_ROOT%{_bindir} -d $RPM_BUILD_ROOT%{py_sitedir} -i temp

%{__make}

%install
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

#%files devel
#%defattr(644,root,root,755)
#%{py_sitedir}/*.py
#%{py_sitedir}/*.py[co]

#%files examples
#%defattr(644,root,root,755)
#%{_examplesdir}/python/%{module}
