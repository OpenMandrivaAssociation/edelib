%define devel	%mklibname %name -d
Name:		edelib
Summary:	Equinox Desktop Environment library
Version:	2.1
Release:	1
License:	GPLv2+
Group:		System/Libraries
URL:		http://equinox-project.org/
Source0:	http://downloads.sourceforge.net/project/ede/%{name}/%{version}/%{name}-%{version}.tar.gz
BuildRequires:	jam
BuildRequires:	doxygen
BuildRequires:	fltk-devel
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(pixman-1)
Patch0:		edelib-2.1-compile.patch

%description
edelib is small and portable C++ library for EDE (Equinox Desktop Environment).

Aims are to provide enough background for easier EDE components construction
and development.

%package -n %{devel}
Summary:	Equinox Desktop Environment library
Group:		Development/C++

%description -n %{devel}
edelib is small and portable C++ library for EDE (Equinox Desktop Environment).

Aims are to provide enough background for easier EDE components construction
and development.

%prep
%autosetup -p1

%build
%setup_compile_flags
./configure --prefix=%{buildroot}%{_prefix} --libdir=%{buildroot}%{_libdir}
sed -i 's|%{buildroot}||' pc/*.pc edelib/edelib-config.h
jam

%install
jam install

%files -n %{devel}
%{_bindir}/%{name}-*
%{_libdir}/*.a
%{_includedir}/%{name}
%{_libdir}/pkgconfig/*
%{_libdir}/%{name}
%{_datadir}/edelib
%doc %{_docdir}/%{name}-%{version}.0
