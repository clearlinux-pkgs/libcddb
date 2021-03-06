#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libcddb
Version  : 1.3.2
Release  : 2
URL      : https://sourceforge.net/projects/libcddb/files/libcddb/1.3.2/libcddb-1.3.2.tar.bz2
Source0  : https://sourceforge.net/projects/libcddb/files/libcddb/1.3.2/libcddb-1.3.2.tar.bz2
Summary  : CDDB server access library
Group    : Development/Tools
License  : LGPL-2.0
Requires: libcddb-bin = %{version}-%{release}
Requires: libcddb-lib = %{version}-%{release}
Requires: libcddb-license = %{version}-%{release}
BuildRequires : pkgconfig(libcdio)

%description
WHAT IS LIBCDDB
Libcddb is a library that implements the different protocols (CDDBP,
HTTP, SMTP) to access data on a CDDB server (http://freedb.org).  It
tries to be as cross-platform as possible.  The initial libary will
have a C API.

%package bin
Summary: bin components for the libcddb package.
Group: Binaries
Requires: libcddb-license = %{version}-%{release}

%description bin
bin components for the libcddb package.


%package dev
Summary: dev components for the libcddb package.
Group: Development
Requires: libcddb-lib = %{version}-%{release}
Requires: libcddb-bin = %{version}-%{release}
Provides: libcddb-devel = %{version}-%{release}
Requires: libcddb = %{version}-%{release}

%description dev
dev components for the libcddb package.


%package lib
Summary: lib components for the libcddb package.
Group: Libraries
Requires: libcddb-license = %{version}-%{release}

%description lib
lib components for the libcddb package.


%package license
Summary: license components for the libcddb package.
Group: Default

%description license
license components for the libcddb package.


%prep
%setup -q -n libcddb-1.3.2
cd %{_builddir}/libcddb-1.3.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1604359133
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1604359133
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libcddb
cp %{_builddir}/libcddb-1.3.2/COPYING %{buildroot}/usr/share/package-licenses/libcddb/b256632dcce76559734ff0a23330d2898b7d3a3b
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/cddb_query

%files dev
%defattr(-,root,root,-)
/usr/include/cddb/cddb.h
/usr/include/cddb/cddb_cmd.h
/usr/include/cddb/cddb_config.h
/usr/include/cddb/cddb_conn.h
/usr/include/cddb/cddb_disc.h
/usr/include/cddb/cddb_error.h
/usr/include/cddb/cddb_log.h
/usr/include/cddb/cddb_site.h
/usr/include/cddb/cddb_track.h
/usr/include/cddb/version.h
/usr/lib64/libcddb.so
/usr/lib64/pkgconfig/libcddb.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libcddb.so.2
/usr/lib64/libcddb.so.2.2.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libcddb/b256632dcce76559734ff0a23330d2898b7d3a3b
