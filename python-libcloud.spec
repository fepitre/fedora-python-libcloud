%define pybasever 2.6
%define __python_ver 26
%define __python %{_bindir}/python%{?pybasever}

%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

%global tarball_name apache-libcloud
%global _module_name libcloud

Name:           python-libcloud
Version:        0.14.1
Release:        1%{?dist}
Summary:        A Python library to address multiple cloud provider APIs

Group:          Development/Languages
License:        ASL 2.0
URL:            http://libcloud.apache.org/
Source0:        http://pypi.python.org/packages/source/a/apache-libcloud/%{tarball_name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch

Requires:       python26
BuildRequires:  python26 python26-distribute

%description
libcloud is a client library for interacting with many of the popular cloud 
server providers.  It was created to make it easy for developers to build 
products that work between any of the services that it supports.

%prep
%setup -qn %{tarball_name}-%{version}


%build
echo %{python_sitelib}
%{__python} setup.py build


%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

 
%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc LICENSE README.rst
%{python_sitelib}/*


%changelog
* Mon Mar 24 2014 Erik Johnson <erik@saltstack.com> - 0.14.1-1
- Initial build of 0.14.1 for EL5

* Mon Feb 10 2014 Daniel Bruno <dbruno@fedoraproject.org> - 0.14.1-1
- Release 0.14.1 includes some bug-fixes, improvements and new features

* Fri Jan 31 2014 Daniel Bruno <dbruno@fedoraproject.org> - 0.14.0-1
- Libcloud new release 0.14.0

* Fri Jan 03 2014 Daniel Bruno <dbruno@fedoraproject.org> - 0.13.3-1
- Security Fix - BUG: 1047867 1047868

* Thu Sep 19 2013 Daniel Bruno <dbruno@fedoraproject.org> - 0.13.2-11
- Some bug fixes from Upstream

* Mon Sep 09 2013 Daniel Bruno <dbruno@fedoraproject.org> - 0.13.1-10
- Update to upstream release 0.13.1

* Mon Jul 01 2013 Daniel Bruno dbruno@fedoraproject.org - 0.13.0-9
- Update to upstream release 0.13.0, more details on Release Notes.

* Thu May 16 2013 Daniel Bruno dbruno@fedoraproject.org - 0.12.4-8
- Update to upstream version 0.12.4

* Tue Mar 26 2013 Daniel Bruno dbruno@fedoraproject.org - 0.12.3-6
- Update to upstream version 0.12.3

* Tue Feb 19 2013 Daniel Bruno dbruno@fedoraproject.org - 0.12.1-5
- Update to upstream version 0.12.1

* Wed Oct 10 2012 Daniel Bruno dbruno@fedoraproject.org - 0.11.3-4
- Update to 0.11.3

* Thu Aug 02 2012 Daniel Bruno dbruno@fedoraproject.org - 0.11.1-3
- Updating to upstream release 0.11.1

* Fri Jun 15 2012 Daniel Bruno dbruno@fedoraproject.org - 0.9.1-2
- Update to upstream version 0.10.1

* Mon Apr 16 2012 Daniel Bruno dbruno@fedoraproject.org - 0.9.1-1
- update to 0.9.1

* Mon Mar 26 2012 Daniel Bruno dbruno@fedoraproject.org - 0.8.0-4
- Updating release to 0.8.0

* Fri Dec 30 2011 Daniel Bruno dbruno@fedoraproject.org - 0.6.2-3
- Standardizing the description

* Tue Nov 22 2011 Daniel Bruno dbruno@fedoraproject.org - 0.6.2-2
- First build package build
