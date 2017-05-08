#
# spec file for package obs-testpackage
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

Name:           obs-testpackage
Version:	0.0.1
Release:	0
License:	GPL-2.0 and GPL-3.0
Summary:	This package is only for testing services in open-build-service
Url:		https://github.com/M0ses/obs-testpackage.git
Group:		Productivity/Networking/Web/Utilities
Source:		%{name}-%{version}.tar.xz
#Patch:
#BuildRequires:
#PreReq:
#Provides:
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description

%prep
%setup -q

%build
make

%install
make install DESTDIR=%{buildroot} %{?_smp_mflags}

%post

%postun

%files
%defattr(-,root,root)
%doc README.md
/non-existant-file

%changelog

