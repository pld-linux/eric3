# TODO: Add Documentation dir to %doc 
%include	/usr/lib/rpm/macros.python
Summary:	Eric3 is a full featured Python IDE
Summary(pl):	Eric3 - pe³nowarto¶ciowe IDE dla Pythona
Name:		eric
Version:	3.2
Release:	0.1
License:	GPL
Group:		X11/Development/Tools
Source0:	http://www.die-offenbachs.de/detlev/files/%{name}-%{version}.tar.gz
# Source0-md5:	d512d91cf04ce58420e0001952bd45b2
URL:		http://www.die-offenbachs.de/detlev/eric3.html
BuildRequires:	python-PyQt-devel >= 3.7
BuildRequires:	qscintilla-devel >= 1.53
BuildRequires:	rpm-pythonprov
BuildRequires:	sip >= 3.7
#%%requires_eq	sip # not so sure if it's needed in runtime
%pyrequires_eq	python # python-modules ?
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

%install
rm -rf $RPM_BUILD_ROOT
python install.py -b $RPM_BUILD_ROOT%{_bindir} -d $RPM_BUILD_ROOT%{py_sitedir} -x
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
find $RPM_BUILD_ROOT%{py_sitedir} -name \*.py -exec rm {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README eric/Documentation/*
%attr(755,root,root) %{_bindir}/*
%dir %{py_sitedir}/eric3
%{py_sitedir}/eric3/*.py[co]
%dir %{py_sitedir}/eric3/pixmaps
%{py_sitedir}/eric3/pixmaps/*
%dir %{py_sitedir}/eric3/Checks
%{py_sitedir}/eric3/Checks/*.py[co]
%dir %{py_sitedir}/eric3/Debugger
%{py_sitedir}/eric3/Debugger/*.py[co]
%dir %{py_sitedir}/eric3/DocumentationTools
%{py_sitedir}/eric3/DocumentationTools/*.py[co]
%dir %{py_sitedir}/eric3/Examples
%{py_sitedir}/eric3/Examples/*.py[co]
%dir %{py_sitedir}/eric3/Helpviewer
%{py_sitedir}/eric3/Helpviewer/*.py[co]
%dir %{py_sitedir}/eric3/Icons
%{py_sitedir}/eric3/Icons/*.py[co]
%dir %{py_sitedir}/eric3/Preferences
%{py_sitedir}/eric3/Preferences/*.py[co]
%dir %{py_sitedir}/eric3/Project
%{py_sitedir}/eric3/Project/*.py[co]
%dir %{py_sitedir}/eric3/PyUnit
%{py_sitedir}/eric3/PyUnit/*.py[co]
%dir %{py_sitedir}/eric3/QScintilla
%{py_sitedir}/eric3/QScintilla/*.py[co]
%dir %{py_sitedir}/eric3/Tools
%{py_sitedir}/eric3/Tools/*.py[co]
%dir %{py_sitedir}/eric3/UI
%{py_sitedir}/eric3/UI/*.py[co]
%dir %{py_sitedir}/eric3/Utilities
%{py_sitedir}/eric3/Utilities/*.py[co]
%dir %{py_sitedir}/eric3/VCS
%{py_sitedir}/eric3/VCS/*.py[co]
%dir %{py_sitedir}/eric3/VCS/cvsPackage
%{py_sitedir}/eric3/VCS/cvsPackage/*.py[co]
%dir %{py_sitedir}/eric3/VCS/subversionPackage
%{py_sitedir}/eric3/VCS/subversionPackage/*.py[co]
%dir %{py_sitedir}/eric3/ViewManager
%{py_sitedir}/eric3/ViewManager/*.py[co]
%dir %{py_sitedir}/eric3/Wizards
%{py_sitedir}/eric3/Wizards/*.py[co]
%{py_sitedir}/eric3/Wizards/*.e3w
%dir %{py_sitedir}/eric3/Wizards/ColorDialogWizard
%{py_sitedir}/eric3/Wizards/ColorDialogWizard/*.py[co]
%dir %{py_sitedir}/eric3/Wizards/FileDialogWizard
%{py_sitedir}/eric3/Wizards/FileDialogWizard/*.py[co]
%dir %{py_sitedir}/eric3/Wizards/FontDialogWizard
%{py_sitedir}/eric3/Wizards/FontDialogWizard/*.py[co]
%dir %{py_sitedir}/eric3/Wizards/InputDialogWizard
%{py_sitedir}/eric3/Wizards/InputDialogWizard/*.py[co]
%dir %{py_sitedir}/eric3/Wizards/MessageBoxWizard
%{py_sitedir}/eric3/Wizards/MessageBoxWizard/*.py[co]
