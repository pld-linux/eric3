
%include	/usr/lib/rpm/macros.python
Summary:	Eric3 is a full featured Python IDE
Summary(pl):	Eric3 - pe³nowarto¶ciowe IDE dla Pythona
Name:		eric3
%define		tar_name	eric
Version:	3.3
%define snap 20031115
Release:	0.%{snap}.1
License:	GPL
Group:		X11/Development/Tools
# Source0:	http://www.die-offenbachs.de/detlev/files/%{tar_name}-%{version}.tar.gz
Source0:	http://www.die-offenbachs.de/detlev/snapshots/%{tar_name}-snapshot-%{snap}.tar.gz
# Source0-md5:	ad8b99f617944ef65d08d984a0371c66
URL:		http://www.die-offenbachs.de/detlev/eric3.html
BuildRequires:	python-PyQt-devel >= 3.7
BuildRequires:	qscintilla-devel >= 1.53
BuildRequires:	rpm-pythonprov
BuildRequires:	sip >= 3.7
%pyrequires_eq	python # python-modules ?
Requires:	python-PyQt >= 3.7
Obsoletes:	eric
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Eric3 is a full featured Python IDE that is written in PyQt using the
QScintilla editor widget.

%description -l pl
Eric3 jest pe³nowarto¶ciowym IDE dla Pythona napisanym w PyQt i
u¿ywaj±cym edytora QScintilla.

%prep
# %%setup -q -n %{tar_name}-%{version}.tar.gz
%setup -q -n %{tar_name}-snapshot-%{snap}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_docdir}/%{name}
python install.py -b %{_bindir} -d %{py_sitedir} -i $RPM_BUILD_ROOT
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
#find $RPM_BUILD_ROOT%{py_sitedir} -name \*.py -exec rm {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README eric/Documentation/*
%attr(755,root,root) %{_bindir}/*
%dir %{py_sitedir}/%{name}
%{py_sitedir}/%{name}/*.py[co]
%dir %{py_sitedir}/%{name}/pixmaps
%{py_sitedir}/%{name}/pixmaps/*
%dir %{py_sitedir}/%{name}/Checks
%{py_sitedir}/%{name}/Checks/*.py[co]
%dir %{py_sitedir}/%{name}/Debugger
%{py_sitedir}/%{name}/Debugger/*.py[co]
%dir %{py_sitedir}/%{name}/DesignerTemplates
%{py_sitedir}/%{name}/DesignerTemplates/*.tmpl
%dir %{py_sitedir}/%{name}/DocumentationTools
%{py_sitedir}/%{name}/DocumentationTools/*.py[co]
%dir %{py_sitedir}/%{name}/Examples
%{py_sitedir}/%{name}/Examples/*.py[co]
%dir %{py_sitedir}/%{name}/Examples/Scripting
%dir %{py_sitedir}/%{name}/Helpviewer
%{py_sitedir}/%{name}/Helpviewer/*.py[co]
%dir %{py_sitedir}/%{name}/Icons
%{py_sitedir}/%{name}/Icons/*.py[co]
%dir %{py_sitedir}/%{name}/Preferences
%{py_sitedir}/%{name}/Preferences/*.py[co]
%dir %{py_sitedir}/%{name}/Project
%{py_sitedir}/%{name}/Project/*.py[co]
%dir %{py_sitedir}/%{name}/PyUnit
%{py_sitedir}/%{name}/PyUnit/*.py[co]
%dir %{py_sitedir}/%{name}/Refactoring
%{py_sitedir}/%{name}/Refactoring/*.py[co]
%dir %{py_sitedir}/%{name}/Scripting
%{py_sitedir}/%{name}/Scripting/*.py[co]
%dir %{py_sitedir}/%{name}/QScintilla
%{py_sitedir}/%{name}/QScintilla/*.py[co]
%dir %{py_sitedir}/%{name}/Tools
%{py_sitedir}/%{name}/Tools/*.py[co]
%dir %{py_sitedir}/%{name}/UI
%{py_sitedir}/%{name}/UI/*.py[co]
%dir %{py_sitedir}/%{name}/Utilities
%{py_sitedir}/%{name}/Utilities/*.py[co]
%dir %{py_sitedir}/%{name}/VCS
%{py_sitedir}/%{name}/VCS/*.py[co]
%dir %{py_sitedir}/%{name}/VCS/cvsPackage
%{py_sitedir}/%{name}/VCS/cvsPackage/*.py[co]
%dir %{py_sitedir}/%{name}/VCS/subversionPackage
%{py_sitedir}/%{name}/VCS/subversionPackage/*.py[co]
%dir %{py_sitedir}/%{name}/ViewManager
%{py_sitedir}/%{name}/ViewManager/*.py[co]
%dir %{py_sitedir}/%{name}/Wizards
%{py_sitedir}/%{name}/Wizards/*.py[co]
%{py_sitedir}/%{name}/Wizards/*.e3w
%dir %{py_sitedir}/%{name}/Wizards/ColorDialogWizard
%{py_sitedir}/%{name}/Wizards/ColorDialogWizard/*.py[co]
%dir %{py_sitedir}/%{name}/Wizards/FileDialogWizard
%{py_sitedir}/%{name}/Wizards/FileDialogWizard/*.py[co]
%dir %{py_sitedir}/%{name}/Wizards/FontDialogWizard
%{py_sitedir}/%{name}/Wizards/FontDialogWizard/*.py[co]
%dir %{py_sitedir}/%{name}/Wizards/InputDialogWizard
%{py_sitedir}/%{name}/Wizards/InputDialogWizard/*.py[co]
%dir %{py_sitedir}/%{name}/Wizards/MessageBoxWizard
%{py_sitedir}/%{name}/Wizards/MessageBoxWizard/*.py[co]

# Third party brm/bike - to separate package ?
# I have no idea that is that ...

%dir %{py_sitedir}/%{name}/ThirdParty/
%{py_sitedir}/%{name}/ThirdParty/*.py[co]

%dir %{py_sitedir}/%{name}/ThirdParty/brm
%{py_sitedir}/%{name}/ThirdParty/brm/*.py[co]

%dir %{py_sitedir}/%{name}/ThirdParty/brm/bike
%{py_sitedir}/%{name}/ThirdParty/brm/bike/*.py[co]

%dir %{py_sitedir}/%{name}/ThirdParty/brm/bike/parsing
%{py_sitedir}/%{name}/ThirdParty/brm/bike/parsing/*.py[co]

%dir %{py_sitedir}/%{name}/ThirdParty/brm/bike/query
%{py_sitedir}/%{name}/ThirdParty/brm/bike/query/*.py[co]

%dir %{py_sitedir}/%{name}/ThirdParty/brm/bike/refactor
%{py_sitedir}/%{name}/ThirdParty/brm/bike/refactor/*.py[co]

%dir %{py_sitedir}/%{name}/ThirdParty/brm/bike/transformer
%{py_sitedir}/%{name}/ThirdParty/brm/bike/transformer/*.py[co]



#NOTE: eric3 uses *.py files for it's own purposes
# so do not remove them from package
%{py_sitedir}/%{name}/*.py
%{py_sitedir}/%{name}/*/*.py
%{py_sitedir}/%{name}/*/*/*.py
%{py_sitedir}/%{name}/*/*/*/*.py
%{py_sitedir}/%{name}/*/*/*/*/*.py
