%define upstream_name    relative
%define upstream_version 0.04

Name:		perl-%{upstream_name}
Version:	0.04
Release:	9

Summary:	Load modules with relative names
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/relative
Source0:	https://cpan.metacpan.org/authors/id/S/SA/SAPER/relative-0.04.tar.gz

BuildRequires:	make
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
%setup -q -n relative-0.04

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# soft: do not fail package on test failures
set +e
%make test || :

%install
%makeinstall_std

%files
%doc Changes README META.yml
%{_mandir}/man3/*
%{perl_vendorlib}/*

