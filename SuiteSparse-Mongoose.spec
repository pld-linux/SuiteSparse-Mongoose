Summary:	Mongoose Graph Partitioning Library
Summary(pl.UTF-8):	Biblioteka partycjonowania grafów Mongoose
Name:		SuiteSparse-Mongoose
Version:	2.0.4
Release:	1
License:	GPL v3
Group:		Libraries
#Source0Download: https://github.com/ScottKolo/Mongoose/releases
Source0:	https://github.com/ScottKolo/Mongoose/archive/v%{version}/Mongoose-%{version}.tar.gz
# Source0-md5:	c7607c83e481f97eb76a3db0b4015957
Patch0:		Mongoose-suitesparse.patch
Patch1:		Mongoose-static.patch
URL:		https://github.com/ScottKolo/Mongoose
BuildRequires:	SuiteSparse-config-devel >= 5.2.0
BuildRequires:	cmake >= 2.8
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mongoose is a graph partitioning library. Currently, Mongoose only
supports edge partitioning, but in the future a vertex separator
extension will be added.

%description -l pl.UTF-8
Mongoose to biblioteka partycjonowania grafów. Obecnie Mongoose
obsługuje tylko partycjonowanie krawędzi, ale w przyszłości zostanie
dodane rozszerzenie separujące wierzchołki.

%package devel
Summary:	Header files for Mongoose library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Mongoose
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	SuiteSparse-config-devel >= 5.2.0
Requires:	libstdc++-devel >= 6:4.7

%description devel
Header files for Mongoose library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Mongoose.

%package static
Summary:	Static Mongoose library
Summary(pl.UTF-8):	Statyczna biblioteka Mongoose
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Mongoose library.

%description static -l pl.UTF-8
Statyczna biblioteka Mongoose.

%prep
%setup -q -n Mongoose-%{version}
%patch0 -p1
%patch1 -p1

%build
install -d build
cd build
%cmake .. \
	-DCMAKE_INSTALL_INCLUDEDIR=%{_includedir}/suitesparse

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/mongoose
%attr(755,root,root) %{_libdir}/libmongoose.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmongoose.so.2

%files devel
%defattr(644,root,root,755)
%doc Doc/Mongoose_UserGuide.pdf
%attr(755,root,root) %{_libdir}/libmongoose.so
%{_includedir}/suitesparse/Mongoose.hpp

%files static
%defattr(644,root,root,755)
%{_libdir}/libmongoose.a
