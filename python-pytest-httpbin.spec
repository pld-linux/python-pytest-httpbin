#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	py.test plugin to test HTTP libraries against a local copy of httpbin
Summary(pl.UTF-8):	Wtyczka py.test do testowania bibliotek HTTP względem lokalnej kopii httpbin
Name:		python-pytest-httpbin
Version:	0.2.3
Release:	2
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.python.org/simple/pytest-httpbin/
Source0:	https://files.pythonhosted.org/packages/source/p/pytest-httpbin/pytest-httpbin-%{version}.tar.gz
# Source0-md5:	b8ebb8e2fbac1a445fb5d044f7fec556
URL:		https://github.com/kevin1024/pytest-httpbin
%if %{with python2}
BuildRequires:	python-modules >= 1:2.6
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
py.test plugin to test HTTP libraries against a local copy of httpbin.

%description -l pl.UTF-8
Wtyczka py.test do testowania bibliotek HTTP względem lokalnej kopii
httpbin.

%package -n python3-pytest-httpbin
Summary:	py.test plugin to test HTTP libraries against a local copy of httpbin
Summary(pl.UTF-8):	Wtyczka py.test do testowania bibliotek HTTP względem lokalnej kopii httpbin
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.4

%description -n python3-pytest-httpbin
py.test plugin to test HTTP libraries against a local copy of httpbin.

%description -n python3-pytest-httpbin -l pl.UTF-8
Wtyczka py.test do testowania bibliotek HTTP względem lokalnej kopii
httpbin.

%prep
%setup -q -n pytest-httpbin-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean -x version.py
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc DESCRIPTION.rst
%{py_sitescriptdir}/pytest_httpbin
%{py_sitescriptdir}/pytest_httpbin-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-pytest-httpbin
%defattr(644,root,root,755)
%doc DESCRIPTION.rst
%{py3_sitescriptdir}/pytest_httpbin
%{py3_sitescriptdir}/pytest_httpbin-%{version}-py*.egg-info
%endif
