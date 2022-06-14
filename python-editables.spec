Name:		python-editables
Version:	0.3
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/e/editables/editables-%{version}.tar.gz
Summary:	Editable installations
URL:		https://pypi.org/project/editables/
License:	MIT
Group:		Development/Python
BuildRequires:	python-setuptools
BuildArch:	noarch

%description
Editable installations

%prep
%autosetup -p1 -n editables-%{version}

%build
python setup.py build

%install
python setup.py install --skip-build --root=%{buildroot}

%files
%{py_puresitedir}/editables
%{py_puresitedir}/editables*info
