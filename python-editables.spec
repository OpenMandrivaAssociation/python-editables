%define module editables

Name:		python-editables
Version:	0.6
Release:	1
Summary:	Editable installations
License:	MIT
Group:		Development/Python
URL:		https://github.com/pfmoore/editables
Source0:	%{URL}/archive/%{version}/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

%description
%{name} supports the building of wheels which, when installed, will expose
packages in a local directory on sys.path in "editable mode".

In other words, changes to the package source will be reflected in the
package visible to Python, without needing a reinstall.

%files
%doc README.md
%{py_puresitedir}/%{module}
%{py_puresitedir}/%{module}-%{version}.dist-info
