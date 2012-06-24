# TODO:
# - separate packages (eg. brm, KdeQt - with BR python-PyKDE)
#
%define		tar_name	eric
Summary:	Eric3 is a full featured Python IDE
Summary(pl):	Eric3 - pe�nowarto�ciowe IDE dla Pythona
Name:		eric3
Version:	3.6.0
Release:	0.1
License:	GPL
Group:		X11/Development/Tools
Source0:	http://dl.sourceforge.net/sourceforge/eric-ide/%{tar_name}-%{version}.tar.gz
# Source0-md5:	a9cfd9179d2420843520b2a279a6cf54
Source1:	%{name}.desktop
URL:		http://www.die-offenbachs.de/detlev/eric3.html
BuildRequires:	python-PyQt >= 3.13
BuildRequires:	qscintilla-devel >= 1:1.4
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
Requires:	python-PyQt >= 3.13
Requires:	python-devel-tools
Obsoletes:	eric
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Eric3 is a full featured Python IDE that is written in PyQt using the
QScintilla editor widget.

%description -l pl
Eric3 jest pe�nowarto�ciowym IDE dla Pythona napisanym w PyQt i
u�ywaj�cym edytora QScintilla.

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

%files
%defattr(644,root,root,755)
%doc HISTORY README* THANKS
%attr(755,root,root) %{_bindir}/*
%dir %{py_sitedir}/
%{py_sitedir}/eric3config.py
%{py_sitedir}/sitecustomize.py
%dir %{py_sitedir}/%{name}
%{py_sitedir}/%{name}/*.py[co]
%dir %{py_sitedir}/%{name}/pixmaps
%{py_sitedir}/%{name}/pixmaps/*
%dir %{py_sitedir}/%{name}/DTDs
%{py_sitedir}/%{name}/DTDs/*.dtd
%dir %{py_sitedir}/%{name}/Checks
%{py_sitedir}/%{name}/Checks/*.py[co]
%dir %{py_sitedir}/%{name}/Debugger
%{py_sitedir}/%{name}/Debugger/*.py[co]
%dir %{py_sitedir}/%{name}/Debugger/Cyclops
%{py_sitedir}/%{name}/Debugger/Cyclops/*.py[co]
%dir %{py_sitedir}/%{name}/DesignerTemplates
%{py_sitedir}/%{name}/DesignerTemplates/*.tmpl
%dir %{py_sitedir}/%{name}/DocumentationTools
%{py_sitedir}/%{name}/DocumentationTools/*.py[co]
%dir %{py_sitedir}/%{name}/Examples
%{py_sitedir}/%{name}/Examples/*.py[co]
%dir %{py_sitedir}/%{name}/Examples/Scripting
%{py_sitedir}/%{name}/Examples/Scripting/*.py[co]
%dir %{py_sitedir}/%{name}/Helpviewer
%{py_sitedir}/%{name}/Helpviewer/*.py[co]
%dir %{py_sitedir}/%{name}/Graphics
%{py_sitedir}/%{name}/Graphics/*.py[co]
%{py_sitedir}/%{name}/icons
%dir %{py_sitedir}/%{name}/KdeQt
%{py_sitedir}/%{name}/KdeQt/*.py[co]
%dir %{py_sitedir}/%{name}/Preferences
%{py_sitedir}/%{name}/Preferences/*.py[co]
%dir %{py_sitedir}/%{name}/Project
%{py_sitedir}/%{name}/Project/*.py[co]
%dir %{py_sitedir}/%{name}/PyUnit
%{py_sitedir}/%{name}/PyUnit/*.py[co]
%dir %{py_sitedir}/%{name}/QScintilla
%{py_sitedir}/%{name}/QScintilla/*.py[co]
%dir %{py_sitedir}/%{name}/Refactoring
%{py_sitedir}/%{name}/Refactoring/*.py[co]
%dir %{py_sitedir}/%{name}/Scripting
%{py_sitedir}/%{name}/Scripting/*.py[co]
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
#%%{py_sitedir}/%{name}/Wizards/*.e3w
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
%dir %{py_sitedir}/%{name}/Wizards/PyRegExpWizard
%{py_sitedir}/%{name}/Wizards/PyRegExpWizard/*.py[co]
%dir %{py_sitedir}/%{name}/Wizards/QRegExpWizard
%{py_sitedir}/%{name}/Wizards/QRegExpWizard/*.py[co]
%dir %{py_sitedir}/%{name}/XML
%{py_sitedir}/%{name}/XML/*.py[co]

# Third party brm/bike - to separate package ?
# I have no idea what is that ...
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

# NOTE: eric3 uses *.py files for it's own purposes
# so do not remove them from package
%{py_sitedir}/%{name}/*.py
%{py_sitedir}/%{name}/*/*.py
%{py_sitedir}/%{name}/*/*/*.py
%{py_sitedir}/%{name}/*/*/*/*.py
%{py_sitedir}/%{name}/*/*/*/*/*.py

# Eric documentation
%dir %{py_sitedir}/%{name}/Documentation
%{py_sitedir}/%{name}/Documentation/mod_python.*
%{py_sitedir}/%{name}/Documentation/Source

%{_pixmapsdir}/%{name}.png
%{_desktopdir}/%{name}.desktop
