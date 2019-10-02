#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-calibrate
Version  : 1.7.5
Release  : 15
URL      : https://cran.r-project.org/src/contrib/calibrate_1.7.5.tar.gz
Source0  : https://cran.r-project.org/src/contrib/calibrate_1.7.5.tar.gz
Summary  : Calibration of Scatterplot and Biplot Axes
Group    : Development/Tools
License  : GPL-2.0
BuildRequires : buildreq-R

%description
variable vectors in scatterplots and biplots. Also provides some functions for multivariate analysis
	     such principal coordinate analysis.

%prep
%setup -q -c -n calibrate

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1570021999

%install
export SOURCE_DATE_EPOCH=1570021999
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library calibrate
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library calibrate
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library calibrate
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc calibrate || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/calibrate/DESCRIPTION
/usr/lib64/R/library/calibrate/INDEX
/usr/lib64/R/library/calibrate/Meta/Rd.rds
/usr/lib64/R/library/calibrate/Meta/data.rds
/usr/lib64/R/library/calibrate/Meta/features.rds
/usr/lib64/R/library/calibrate/Meta/hsearch.rds
/usr/lib64/R/library/calibrate/Meta/links.rds
/usr/lib64/R/library/calibrate/Meta/nsInfo.rds
/usr/lib64/R/library/calibrate/Meta/package.rds
/usr/lib64/R/library/calibrate/Meta/vignette.rds
/usr/lib64/R/library/calibrate/NAMESPACE
/usr/lib64/R/library/calibrate/R/calibrate
/usr/lib64/R/library/calibrate/R/calibrate.rdb
/usr/lib64/R/library/calibrate/R/calibrate.rdx
/usr/lib64/R/library/calibrate/data/calves.rda
/usr/lib64/R/library/calibrate/data/goblets.rda
/usr/lib64/R/library/calibrate/data/heads.rda
/usr/lib64/R/library/calibrate/data/linnerud.rda
/usr/lib64/R/library/calibrate/data/spaindist.rda
/usr/lib64/R/library/calibrate/data/storks.rda
/usr/lib64/R/library/calibrate/doc/CalibrationGuide.R
/usr/lib64/R/library/calibrate/doc/CalibrationGuide.Rnw
/usr/lib64/R/library/calibrate/doc/CalibrationGuide.pdf
/usr/lib64/R/library/calibrate/doc/index.html
/usr/lib64/R/library/calibrate/help/AnIndex
/usr/lib64/R/library/calibrate/help/aliases.rds
/usr/lib64/R/library/calibrate/help/calibrate.rdb
/usr/lib64/R/library/calibrate/help/calibrate.rdx
/usr/lib64/R/library/calibrate/help/paths.rds
/usr/lib64/R/library/calibrate/html/00Index.html
/usr/lib64/R/library/calibrate/html/R.css
