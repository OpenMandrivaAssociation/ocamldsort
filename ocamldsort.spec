%define name		ocamldsort
%define version		0.15.0
%define release		%mkrel 1

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

