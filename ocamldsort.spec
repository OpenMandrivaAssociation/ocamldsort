%define name		ocamldsort
%define version		0.15.0
%define release		2

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	A dependency sorter for OCaml source files
License:	GPL
Group:		Development/Other
URL:		http://dimitri.mutu.net/ocaml.html
Source: 	ftp://quatramaran.ens.fr/pub/ara/ocamldsort/%{name}-%{version}.tar.gz
BuildRequires:	ocaml
BuildRequires:	camlp4
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
The ocamldsort command scans a set of Objective Caml source files (.ml and .mli
files), sorts them according to their dependencies and prints the sorted files
in order to link their corresponding .cmo and .cmi files.

%prep
%setup -q

%build
%configure
make

%install
rm -rf %{buildroot}
make install BINDIR=%{buildroot}%{_bindir} MANDIR=%{buildroot}%{_mandir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING INSTALL README THANKS
%{_bindir}/*
%{_mandir}/man1/*



%changelog
* Thu Aug 12 2010 Florent Monnier <blue_prawn@mandriva.org> 0.15.0-1mdv2011.0
+ Revision: 569298
- updated version

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.14.4-4mdv2010.0
+ Revision: 430193
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 0.14.4-3mdv2009.0
+ Revision: 254231
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.14.4-1mdv2008.1
+ Revision: 136633
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Aug 31 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.14.4-1mdv2008.0
+ Revision: 77106
- update to new version 0.14.4


* Thu Oct 05 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.14.3-1mdv2007.0
- first mdv release

