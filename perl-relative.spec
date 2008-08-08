%define module   relative
%define version    0.04
%define release    %mkrel 2

Name:       perl-%{module}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Load modules with relative names
Url:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module//%{module}-%{version}.tar.gz
BuildRequires: perl(Test::More)
BuildRequires: perl(UNIVERSAL::require)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
This module allows you to load modules using only parts of their name,
relatively to the current module or to a given module. Module names are by
default searched below the current module, but can be searched upper in the
hierarchy using the '..::' syntax.

In order to further loosen the namespace coupling, 'import' returns the
full names of the loaded modules, making object-oriented code easier to
write:

    use relative;

%prep
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README README
%{_mandir}/man3/*
%perl_vendorlib/*

