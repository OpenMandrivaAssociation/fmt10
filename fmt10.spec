%define major %(echo %{version}|cut -d. -f1)
%define libname %mklibname %{name} %{major}
%define devel %mklibname -d %{name}

Summary:	Old version of the small, safe and fast formatting library
Name:		fmt10
Version:	10.2.1
Release:	2
Group:		Development/C++
License:	BSD
URL:		https://fmtlib.org
Source0:	https://github.com/fmtlib/fmt/archive/%{version}/fmt-%{version}.tar.gz
# fix tests with FMT_STATIC_THOUSANDS_SEPARATOR (mariadb)
Patch1:		44c3fe1ebb466ab5c296e1a1a6991c7c7b51b72e.diff
BuildSystem:	cmake

%description
fmt is an open-source formatting library for C++. It can be used as a safe
alternative to printf or as a fast alternative to IOStreams.

%package -n %{libname}
Summary:	The libfmt libraries
Group:		Development/C++
# Not really, but we need to have some way to get rid of old
# versioned libnames
Obsoletes:	%{mklibname -d fmt 9} <= 9.1.0-2

%description -n %{libname}
This package contains the library for libfmt

%install -a
# No -devel stuff for compat libraries
rm -rf %{buildroot}%{_includedir} \
	%{buildroot}%{_libdir}/cmake \
	%{buildroot}%{_libdir}/*.so \
	%{buildroot}%{_libdir}/pkgconfig

%files -n %{libname}
%{_libdir}/libfmt.so.%{major}*
