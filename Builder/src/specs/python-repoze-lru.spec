%global modname repoze.lru
%global realversion 0.7
%global rpmversion <rpm.version>
%global packager <ericsson.rstate>
%global realname python-repoze-lru

%if 0%{?fedora}
%global with_python3 1
%endif

Name:           EXTRlitppythonrepozelru_CXP9041762
Version:        %{rpmversion}
Release:        3%{?dist}
Summary:        A tiny LRU cache implementation and decorator

Group:          Development/Libraries
License:        BSD
Source0:        repoze.lru-%{realversion}.z

Provides:       %{realname} = %{realversion}

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python-setuptools-devel

%if 0%{?with_python3}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%endif

%description
repoze.lru is a LRU (least recently used) cache implementation. Keys and values
that are not used frequently will be evicted from the cache faster than keys
and values that are used frequently.


%if 0%{?with_python3}
%package -n python3-repoze-lru
Summary:        A tiny LRU cache implementation and decorator
Group:          Development/Libraries

%description -n python3-repoze-lru
repoze.lru is a LRU (least recently used) cache implementation. Keys and values
that are not used frequently will be evicted from the cache faster than keys
and values that are used frequently.
%endif


%prep
%setup -q -n %{modname}-%{realversion}
rm -rf %{modname}.egg-info

%if 0%{?with_python3}
rm -rf %{py3dir}
cp -a . %{py3dir}
%endif

%build
%{__python} setup.py build
%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py build
popd
%endif

%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py install -O1 --skip-build --root %{buildroot}
popd
%endif

%check
%{__python} setup.py test

%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py test
popd
%endif

%files
#%doc README.txt LICENSE.txt
%{python_sitelib}/repoze/lru
%{python_sitelib}/%{modname}-%{realversion}*

%if 0%{?with_python3}
%files -n python3-repoze-lru
#%doc README.txt LICENSE.txt
%{python3_sitelib}/repoze/lru
%{python3_sitelib}/%{modname}-%{realversion}*
%endif

%changelog
* Mon Feb 11 2013 Ralph Bean <rbean@redhat.com> - 0.4-3
- Removed clean section.
- Removed defattr.
- Removed removing of buildroot in install section.
- Added removal of egg-info in prep section.
- Added python3 subpackage.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Mar 13 2012 Luke Macken <lmacken@redhat.com> - 0.4-1
- Update to 0.4

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jan  2 2010 Luke Macken <lmacken@redhat.com> - 0.3-1
- Initial package
