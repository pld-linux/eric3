# TODO:
# - separate packages (eg. brm, KdeQt - with R: python-PyKDE)
#
%define		tar_name	eric
Summary:	Eric3 is a full featured Python IDE
Summary(pl):	Eric3 - pe³nowarto¶ciowe IDE dla Pythona
Name:		eric3
Version:	3.7.2
Release:	1
License:	GPL
Group:		X11/Development/Tools
Source0:	http://dl.sourceforge.net/eric-ide/%{tar_name}-%{version}.tar.gz
# Source0-md5:	b0b1114cd823cb149844ac95dcf5b4ac
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
%dir %{py_sitedir}/%{name}
%{py_sitedir}/%{name}/default.e3k
%{py_sitedir}/%{name}/eric3.api
%{py_sitedir}/%{name}/*.py*
%{py_sitedir}/%{name}/pixmaps
%{py_sitedir}/%{name}/DTDs
%dir %{py_sitedir}/%{name}/Checks
%{py_sitedir}/%{name}/Checks/*.py*
%{py_sitedir}/%{name}/DebugClients
%dir %{py_sitedir}/%{name}/Debugger
%{py_sitedir}/%{name}/Debugger/*.py*
%{py_sitedir}/%{name}/Debugger/Cyclops
%{py_sitedir}/%{name}/DesignerTemplates
%dir %{py_sitedir}/%{name}/DocumentationTools
%{py_sitedir}/%{name}/DocumentationTools/*.py*
%{py_sitedir}/%{name}/Examples
%dir %{py_sitedir}/%{name}/Helpviewer
%{py_sitedir}/%{name}/Helpviewer/*.py*
%dir %{py_sitedir}/%{name}/Graphics
%{py_sitedir}/%{name}/Graphics/*.py*
%{py_sitedir}/%{name}/icons
%{py_sitedir}/%{name}/KdeQt
%dir %{py_sitedir}/%{name}/Preferences
%{py_sitedir}/%{name}/Preferences/*.py*
%dir %{py_sitedir}/%{name}/Project
%{py_sitedir}/%{name}/Project/*.py*
%dir %{py_sitedir}/%{name}/PyUnit
%{py_sitedir}/%{name}/PyUnit/*.py*
%dir %{py_sitedir}/%{name}/QScintilla
%{py_sitedir}/%{name}/QScintilla/*.py*
%dir %{py_sitedir}/%{name}/Refactoring
%{py_sitedir}/%{name}/Refactoring/*.py*
%dir %{py_sitedir}/%{name}/Scripting
%{py_sitedir}/%{name}/Scripting/*.py*
%{py_sitedir}/%{name}/Tools
%dir %{py_sitedir}/%{name}/UI
%{py_sitedir}/%{name}/UI/*.py*
%{py_sitedir}/%{name}/Utilities
%dir %{py_sitedir}/%{name}/VCS
%{py_sitedir}/%{name}/VCS/*.py*
%dir %{py_sitedir}/%{name}/VCS/cvsPackage
%{py_sitedir}/%{name}/VCS/cvsPackage/*.py*
%dir %{py_sitedir}/%{name}/VCS/subversionPackage
%{py_sitedir}/%{name}/VCS/subversionPackage/*.py*
%dir %{py_sitedir}/%{name}/ViewManager
%{py_sitedir}/%{name}/ViewManager/*.py*
%dir %{py_sitedir}/%{name}/Wizards
%{py_sitedir}/%{name}/Wizards/*.py*
%dir %{py_sitedir}/%{name}/Wizards/ColorDialogWizard
%{py_sitedir}/%{name}/Wizards/ColorDialogWizard/*.py*
%dir %{py_sitedir}/%{name}/Wizards/FileDialogWizard
%{py_sitedir}/%{name}/Wizards/FileDialogWizard/*.py*
%dir %{py_sitedir}/%{name}/Wizards/FontDialogWizard
%{py_sitedir}/%{name}/Wizards/FontDialogWizard/*.py*
%dir %{py_sitedir}/%{name}/Wizards/InputDialogWizard
%{py_sitedir}/%{name}/Wizards/InputDialogWizard/*.py*
%dir %{py_sitedir}/%{name}/Wizards/MessageBoxWizard
%{py_sitedir}/%{name}/Wizards/MessageBoxWizard/*.py*
%dir %{py_sitedir}/%{name}/Wizards/PyRegExpWizard
%{py_sitedir}/%{name}/Wizards/PyRegExpWizard/*.py*
%dir %{py_sitedir}/%{name}/Wizards/QRegExpWizard
%{py_sitedir}/%{name}/Wizards/QRegExpWizard/*.py*
%dir %{py_sitedir}/%{name}/XML
%{py_sitedir}/%{name}/XML/*.py*

# Third party brm/bike - to separate package ?
# I have no idea what is that ...
%dir %{py_sitedir}/%{name}/ThirdParty
%{py_sitedir}/%{name}/ThirdParty/*.py*
%dir %{py_sitedir}/%{name}/ThirdParty/brm
%{py_sitedir}/%{name}/ThirdParty/brm/*.py*
%{py_sitedir}/%{name}/ThirdParty/brm/bike

# Eric documentation
%dir %{py_sitedir}/%{name}/Documentation
%{py_sitedir}/%{name}/Documentation/mod_python.*
%{py_sitedir}/%{name}/Documentation/Source

%{_pixmapsdir}/%{name}.png
%{_desktopdir}/%{name}.desktop
