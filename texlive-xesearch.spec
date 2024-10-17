Name:		texlive-xesearch
Version:	51908
Release:	2
Summary:	A string finder for XeTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/xetex/generic/xesearch
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xesearch.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xesearch.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package finds strings (e.g. (parts of) words or phrases)
and manipulates them (apply any macro), thus turning each word
or phrase into a possible command. It is written in plain XeTeX
and should thus work with any format (it is known to work with
LaTeX and ConTeXt). The main application for the moment is
XeIndex, an automatic index for XeLaTeX, but examples are given
of simple use to check spelling, count words, and highlight
syntax of programming languages.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/xetex/xesearch/t-xesearch.tex
%{_texmfdistdir}/tex/xetex/xesearch/xesearch.sty
%doc %{_texmfdistdir}/doc/xetex/xesearch/README
%doc %{_texmfdistdir}/doc/xetex/xesearch/xesearch.pdf
%doc %{_texmfdistdir}/doc/xetex/xesearch/xesearch.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
