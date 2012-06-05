%define devel	%mklibname %name -d
Name:		edelib
Summary:	Equinox Desktop Environment library
Version:	2.0
Release:	1
License:	GPLv2+
Group:		System/Libraries
URL:		http://equinox-project.org/
Source0:	http://downloads.sourceforge.net/project/ede/%{name}/%{version}/%{name}-%{version}.tar.gz
BuildRequires:	jam
BuildRequires:	doxygen
BuildRequires:	fltk-devel

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
%setup -q

%build
./configure --prefix=%{buildroot}/usr --libdir=%{buildroot}%{_libdir}
sed -i 's|%{buildroot}||' *.pc edelib/edelib-config.h
jam

%install
jam install

%files -n %{devel}
%{_bindir}/%{name}-*
%{_libdir}/*.a
%{_includedir}/%{name}
%{_libdir}/pkgconfig/*
%{_libdir}/%{name}
%doc %{_docdir}/%{name}-2.0.0
