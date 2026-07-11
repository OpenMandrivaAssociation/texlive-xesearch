%global tl_name xesearch
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.2
Release:	%{tl_revision}.1
Summary:	A string finder for XeTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/xetex/generic/xesearch
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xesearch.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xesearch.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package finds strings (e.g. (parts of) words or phrases) and
manipulates them (apply any macro), thus turning each word or phrase
into a possible command. It is written in plain XeTeX and should thus
work with any format (it is known to work with LaTeX and ConTeXt). The
main application for the moment is XeIndex, an automatic index for
XeLaTeX, but examples are given of simple use to check spelling, count
words, and highlight syntax of programming languages.

