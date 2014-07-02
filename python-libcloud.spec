%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

%global tarball_name apache-libcloud

Name:           python-libcloud
Version:        0.15.0
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
server providers. It was created to make it easy for developers to build 
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
* Wed Jul 2 2014 Erik Johnson <erik@saltstack.com> - 0.15.0-1
- Initial epel7 build
