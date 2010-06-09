%define upstream_name    relative
%define upstream_version 0.04

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 4

Summary:    Load modules with relative names
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module//%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Test::More)
BuildRequires: perl(UNIVERSAL::require)

BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

Provides: perl(relative)

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
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README META.yml
%{_mandir}/man3/*
%perl_vendorlib/*
