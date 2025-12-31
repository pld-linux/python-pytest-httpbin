#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_with	python3 # CPython 3.x module (built from python3-pytest-httpbin.spec)

Summary:	py.test plugin to test HTTP libraries against a local copy of httpbin
Summary(pl.UTF-8):	Wtyczka py.test do testowania bibliotek HTTP względem lokalnej kopii httpbin
Name:		python-pytest-httpbin
# keep 1.x here for python2 support
Version:	1.0.2
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.python.org/simple/pytest-httpbin/
Source0:	https://files.pythonhosted.org/packages/source/p/pytest-httpbin/pytest-httpbin-%{version}.tar.gz
# Source0-md5:	cd17b8252c4e88d0372d6286663ce6d9
URL:		https://github.com/kevin1024/pytest-httpbin
%if %{with python2}
BuildRequires:	python-modules >= 1:2.6
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-httpbin
BuildRequires:	python-pytest
BuildRequires:	python-requests
BuildRequires:	python-six
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-httpbin
BuildRequires:	python3-pytest
BuildRequires:	python3-requests
BuildRequires:	python3-six
%endif
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

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS=pytest_httpbin.plugin \
%{__python} -m pytest tests -k 'not test_redirect_location_is_https_for_secure_server'
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS=pytest_httpbin.plugin \
%{__python3} -m pytest tests
%endif
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
%doc DESCRIPTION.rst README.md
%{py_sitescriptdir}/pytest_httpbin
%{py_sitescriptdir}/pytest_httpbin-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-pytest-httpbin
%defattr(644,root,root,755)
%doc DESCRIPTION.rst README.md
%{py3_sitescriptdir}/pytest_httpbin
%{py3_sitescriptdir}/pytest_httpbin-%{version}-py*.egg-info
%endif
