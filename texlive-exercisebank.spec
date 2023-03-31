Name:		texlive-exercisebank
Version:	50448
Release:	2
Summary:	Creating and managing exercises, and reusing them as composed sets
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/exercisebank
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/exercisebank.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/exercisebank.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package makes it easier to maintain and edit your exercise
sets. Exercises are saved as separate files containing part
problems. These files can be used to make sets, and you can
cherry-pick or exclude certain part problems as you see fit.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/exercisebank
%doc %{_texmfdistdir}/doc/latex/exercisebank

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
