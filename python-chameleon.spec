#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define 	module	chameleon
Summary:	Fast HTML/XML Template Compiler
Name:		python-%{module}
Version:	2.11
Release:	2
License:	BSD-derived (http://www.repoze.org/LICENSE.txt)
Group:		Libraries/Python
Source0:	http://pypi.python.org/packages/source/C/Chameleon/Chameleon-%{version}.tar.gz
# Source0-md5:	df72458bf3dd26a744dcff5ad555c34b
URL:		http://pypi.python.org/pypi/Chameleon
BuildRequires:	python-distribute
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Chameleon is an HTML/XML template engine for Python. It uses the page
templates language.

%prep
%setup -q -n Chameleon-%{version}

%build
%py_build

%{?with_tests:%{__python} setup.py test}

%install
rm -rf $RPM_BUILD_ROOT
%py_install

%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/%{module}/tests

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.rst COPYRIGHT.txt LICENSE.txt README.rst
%dir %{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}/*.py[co]
%{py_sitescriptdir}/%{module}/zpt
%{py_sitescriptdir}/Chameleon-%{version}-py*.egg-info
