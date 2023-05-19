#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
#
Name     : pypi-httpx
Version  : 0.24.1
Release  : 45
URL      : https://files.pythonhosted.org/packages/f8/2a/114d454cb77657dbf6a293e69390b96318930ace9cd96b51b99682493276/httpx-0.24.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/f8/2a/114d454cb77657dbf6a293e69390b96318930ace9cd96b51b99682493276/httpx-0.24.1.tar.gz
Summary  : The next generation HTTP client.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-httpx-bin = %{version}-%{release}
Requires: pypi-httpx-license = %{version}-%{release}
Requires: pypi-httpx-python = %{version}-%{release}
Requires: pypi-httpx-python3 = %{version}-%{release}
Requires: pypi(charset_normalizer)
BuildRequires : buildreq-distutils3
BuildRequires : pypi(charset_normalizer)
BuildRequires : pypi(hatch_fancy_pypi_readme)
BuildRequires : pypi(hatchling)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
<p align="center">
<a href="https://www.python-httpx.org/"><img width="350" height="208" src="https://raw.githubusercontent.com/encode/httpx/master/docs/img/butterfly.png" alt='HTTPX'></a>
</p>

%package bin
Summary: bin components for the pypi-httpx package.
Group: Binaries
Requires: pypi-httpx-license = %{version}-%{release}

%description bin
bin components for the pypi-httpx package.


%package license
Summary: license components for the pypi-httpx package.
Group: Default

%description license
license components for the pypi-httpx package.


%package python
Summary: python components for the pypi-httpx package.
Group: Default
Requires: pypi-httpx-python3 = %{version}-%{release}

%description python
python components for the pypi-httpx package.


%package python3
Summary: python3 components for the pypi-httpx package.
Group: Default
Requires: python3-core
Provides: pypi(httpx)
Requires: pypi(certifi)
Requires: pypi(httpcore)
Requires: pypi(idna)
Requires: pypi(sniffio)

%description python3
python3 components for the pypi-httpx package.


%prep
%setup -q -n httpx-0.24.1
cd %{_builddir}/httpx-0.24.1
pushd ..
cp -a httpx-0.24.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1684513023
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
pypi-dep-fix.py . httpcore
pypi-dep-fix.py . rfc3986
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pypi-dep-fix.py . httpcore
pypi-dep-fix.py . rfc3986
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-httpx
cp %{_builddir}/httpx-%{version}/LICENSE.md %{buildroot}/usr/share/package-licenses/pypi-httpx/2f9a422e6ae22185bd3e9cdaec727ac95ab47bbb || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
pypi-dep-fix.py %{buildroot} httpcore
pypi-dep-fix.py %{buildroot} rfc3986
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/httpx

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-httpx/2f9a422e6ae22185bd3e9cdaec727ac95ab47bbb

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
