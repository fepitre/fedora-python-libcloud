%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

%global tarball_name apache-libcloud

Name:           python-libcloud
Version:        1.1.0
Release:        1%{?dist}
Summary:        A Python library to address multiple cloud provider APIs

Group:          Development/Languages
License:        ASL 2.0
URL:            http://libcloud.apache.org/
Source0:        http://pypi.python.org/packages/source/a/apache-libcloud/%{tarball_name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch

BuildRequires:  python-setuptools

BuildRequires:  python2-devel

%description
libcloud is a client library for interacting with many of the popular cloud 
server providers.  It was created to make it easy for developers to build 
products that work between any of the services that it supports.

%prep
%setup -qn %{tarball_name}-%{version}

%build
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
* Tue Jul 12 2016 Daniel Bruno <dbruno@fedoraproject.org> - 1.1.0-1
- Python Libcloud 1.1.0 release

* Sun Jan 24 2016 Daniel Bruno <dbruno@fedoraprojec.org> - 0.20.1-1
- This is a bug-fix release of the 0.20 series.

* Thu Jan 07 2016 Daniel Bruno dbruno@fedoraproject.org - 0.20.0-1
- Release 0.20.0 with new features and improvements

* Mon Aug 10 2015 Daniel Bruno <dbruno@fedoraproject.org> - 0.18.0-1
- Apache Libcloud 0.18.0 release with bug fixes and new features

* Fri Feb 20 2015 Daniel Bruno <dbruno@fedoraproject.org> - 0.17.0-1
- Apache Libcloud 0.17.0 release

* Wed Nov 12 2014 Daniel Bruno <dbruno@fedoraproject.org> - 0.16.0-1
- First release in the 0.16 series

* Mon Jul 21 2014 Daniel Bruno <dbruno@fedoraproject.org - 0.15.1-2
- Libcloud 0.15.1 bug-fix release

* Fri Jun 27 2014 Daniel Bruno <dbruno@fedoraproject.org> - 0.15.0-1
- First release in the 0.15 series which it brings many new features,
  improvements and bug fixes

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

