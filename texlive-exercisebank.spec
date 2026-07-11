%global tl_name exercisebank
%global tl_revision 50448

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.3.0
Release:	%{tl_revision}.1
Summary:	Creating and managing exercises, and reusing them as composed sets
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/exercisebank
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/exercisebank.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/exercisebank.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package makes it easier to maintain and edit your exercise sets.
Exercises are saved as separate files containing part problems. These
files can be used to make sets, and you can cherry-pick or exclude
certain part problems as you see fit.

