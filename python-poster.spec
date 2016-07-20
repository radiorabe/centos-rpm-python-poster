%global         srcname  poster

Name:           python-poster
Version:        0.8.1
Release:        1%{?dist}
Summary:        Python library for streaming http uploads and multipart/form-data encoding
License:        BSD
URL:            https://pypi.python.org/pypi/poster
Source0:        https://pypi.python.org/packages/9f/dc/0683a458d21c3d561ab2f71b4fcdd812bf04e55c54e560b0854cea95610e/%{srcname}-%{version}.tar.gz

BuildRequires:  python

BuildArch:      noarch

%{!?py2_build: %global py2_build CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build}
%{!?py2_install: %global py2_install %{__python} setup.py install --skip-build --root %{buildroot}}
%{!?python2_sitelib: %global python2_sitelib %{python_sitelib}}

%description
Python library for streaming http uploads and multipart/form-data encoding

%prep
%autosetup -p1 -n %{srcname}-%{version}


%build
%py2_build

%install
%py2_install
# remove tests again since we don't want to install em
rm -r $RPM_BUILD_ROOT%{python2_sitelib}/tests


%files
%{python2_sitelib}/%{srcname}
%{python2_sitelib}/%{srcname}-%{version}*.egg-info
