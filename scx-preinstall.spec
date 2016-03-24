Name: scx-preinstall
Version: 1.0
Release: alt1
Summary: Compatible layer for install agent for SCOM
License:  Public Domain
Group: Monitoring
Packager: Korneechev Evgeniy <ekorneechev@altlinux.org>
BuildArch:i586

BuildRequires: librpm

Requires:glibc >= 2.12
Requires:openssl >= 1.0
Requires:libpam0 >= 1.1.1

%description
%summary

%install
mkdir -p %buildroot%_libdir
ln -sf %_libdir/librpm-4.0.4.so %buildroot%_libdir/librpm.so.1

%files
%_libdir/librpm.so.1


%changelog
* Wed Mar 23 2016 Evgeniy Korneechev <ek@myconnector.ru> 1.0-alt1
- Initial build

