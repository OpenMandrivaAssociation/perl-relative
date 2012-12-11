%define upstream_name    relative
%define upstream_version 0.04

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6

Summary:	Load modules with relative names
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module//%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Test::More)
BuildRequires:	perl(UNIVERSAL::require)

BuildArch:	noarch
Provides:	perl(relative)

%description
This module allows you to load modules using only parts of their name,
relatively to the current module or to a given module. Module names are by
default searched below the current module, but can be searched upper in the
hierarchy using the '..::' syntax.

In order to further loosen the namespace coupling, 'import' returns the
full names of the loaded modules, making object-oriented code easier to
write.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README META.yml
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 25 2011 Funda Wang <fwang@mandriva.org> 0.40.0-5mdv2011.0
+ Revision: 658904
- rebuild for updated spec-helper

* Wed Jun 09 2010 Jérôme Quelin <jquelin@mandriva.org> 0.40.0-4mdv2011.0
+ Revision: 547335
- reabuild using %%perl_convert_version, provides perl(relative)

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.04-3mdv2010.0
+ Revision: 430534
- rebuild

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.04-2mdv2009.0
+ Revision: 268940
- rebuild early 2009.0 package (before pixel changes)

* Sat May 31 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.04-1mdv2009.0
+ Revision: 213740
- import perl-relative


* Sat May 31 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.04-1mdv2009.0
- first mdv release
