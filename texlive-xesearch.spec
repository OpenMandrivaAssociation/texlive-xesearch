# revision 16041
# category Package
# catalog-ctan /macros/xetex/generic/xesearch
# catalog-date 2009-11-18 12:12:09 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-xesearch
Version:	20091118
Release:	1
Summary:	A string finder for XeTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/xetex/generic/xesearch
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xesearch.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xesearch.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package finds strings (e.g. (parts of) words or phrases)
and manipulates them (apply any macro), thus turning each word
or phrase into a possible command. It is written in plain XeTeX
and should thus work with any format (it is known to work with
LaTeX and ConTeXt). The main application for the moment is
XeIndex, an automatic index for XeLaTeX, but examples are given
of simple use to check spelling, count words, and highlight
syntax of programming languages.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/xetex/xesearch/t-xesearch.tex
%{_texmfdistdir}/tex/xetex/xesearch/xesearch.sty
%doc %{_texmfdistdir}/doc/xetex/xesearch/README
%doc %{_texmfdistdir}/doc/xetex/xesearch/xesearch.pdf
%doc %{_texmfdistdir}/doc/xetex/xesearch/xesearch.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
