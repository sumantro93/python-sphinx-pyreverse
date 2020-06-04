# Created by pyp2rpm-3.3.4
%global pypi_name sphinx-pyreverse

Name:           python-%{pypi_name}
Version:        0.0.13
Release:        1%{?dist}
Summary:        A simple sphinx extension to generate UML diagrams with pyreverse

License:        GPLv3
URL:            https://github.com/alendit/sphinx-pyreverse
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(docutils)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sphinx)

%description
Sphinx-pyreverse A simple sphinx extension to generate a UML diagram from
python modules.Install Install with::: pip install -e git+ Add
"sphinx_pyreverse" to the extensions list in your conf.py (make sure it is in
the PYTHONPATH).Call the directive with path to python module as content. The
:classes: and :packages: flags specify which UML diagrams to show.:: .. uml::
{{modulename}} :classes:...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(docutils)
Requires:       python3dist(sphinx)
%description -n python3-%{pypi_name}
Sphinx-pyreverse A simple sphinx extension to generate a UML diagram from
python modules.Install Install with::: pip install -e git+ Add
"sphinx_pyreverse" to the extensions list in your conf.py (make sure it is in
the PYTHONPATH).Call the directive with path to python module as content. The
:classes: and :packages: flags specify which UML diagrams to show.:: .. uml::
{{modulename}} :classes:...


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%doc README.rst
%{python3_sitelib}/sphinx_pyreverse
%{python3_sitelib}/sphinx_pyreverse-%{version}-py%{python3_version}.egg-info

%changelog
* Thu Jun 04 2020 sumantrom - 0.0.13-1
- Initial package.
