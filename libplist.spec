%define major	4
%define api	2.0

%define oldlibname %mklibname plist %{api} 3
%define libname %mklibname plist
%define devname %mklibname -d plist
%define oldlibnamecxx %mklibname plist++ %{api} 3
%define libnamecxx %mklibname plist++
%define devnamecxx %mklibname -d plist++

#define	git	20211124

Summary:	Library for manipulating Apple Binary and XML Property Lists
Name:		libplist
Version:	2.4.0
Release:	%{?git:0.%{git}.}1
Group:		System/Libraries
License:	LGPLv2+
Url:		http://www.libimobiledevice.org/
Source0:	https://github.com/libimobiledevice/libplist/releases/download/%{version}/libplist-%{version}.tar.bz2
BuildRequires:	make
BuildRequires:	python-cython0
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(python)

%description
libplist is a library for manipulating Apple Binary and XML Property Lists.

%package -n %{libname}
Group:		System/Libraries
Summary:	Library for manipulating Apple Binary and XML Property Lists
Suggests:	%{name} >= %{version}-%{release}
Obsoletes:	%{oldlibname} < %{EVRD}

%description -n %{libname}
libplist is a library for manipulating Apple Binary and XML Property Lists.

%package -n %{devname}
Summary:	Development package for libplist
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
%{name}, development headers and libraries.

%package -n %{libnamecxx}
Summary:	C++ binding for libplist
Group:		Development/C++
Suggests:	%{name} >= %{version}-%{release}
Obsoletes:	%{oldlibnamecxx} < %{EVRD}

%description -n %{libnamecxx}
C++ bindings for %{name}.

%package -n %{devnamecxx}
Summary:	Development package for libplist++
Group:		Development/C++
Requires:	%{libnamecxx} = %{version}-%{release}
Provides:	%{name}++-devel = %{version}-%{release}

%description -n %{devnamecxx}
%name, C++ development headers and libraries.

%package -n python-plist
Summary:	Python package for libplist
Group:		Development/Python
Requires:	python
BuildRequires:	pkgconfig(python)
#BuildRequires:	swig

%description -n python-plist
%{name}, python libraries and support.

%prep
%autosetup -p1
autoreconf -fiv

%configure \
	--disable-static

%build
%make_build

%install
%make_install

%files
%doc AUTHORS COPYING.LESSER
%{_bindir}/plistutil
%{_mandir}/man1/plistutil.1*

%files -n %{libname}
%{_libdir}/%{name}-%{api}.so.%{major}{,.*}

%files -n %{devname}
%{_includedir}/plist
%{_libdir}/pkgconfig/%{name}-%{api}.pc
%{_libdir}/%{name}-%{api}.so

%files -n %{libnamecxx}
%{_libdir}/%{name}++-%{api}.so.%{major}{,.*}

%files -n %{devnamecxx}
%exclude %{_includedir}/plist/plist.h
%{_libdir}/pkgconfig/%{name}++-%{api}.pc
%{_libdir}/%{name}++-%{api}.so

%files -n python-plist
%{python_sitearch}/plist.so
