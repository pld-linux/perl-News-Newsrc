#
# Conditional build:
%bcond_with	tests	# perform "make test"
#
%define		pdir	News
%define		pnam	Newsrc
Summary:	News::Newsrc - Perl module to manage newsrc files
Summary(pl.UTF-8):	News::Newsrc - moduł Perla do zarządzania plikami newsrc
Name:		perl-News-Newsrc
Version:	1.09
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/News/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	224d0cc957d67313afc1edcb56eecb28
URL:		http://search.cpan.org/dist/News-Newsrc/
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-Set-IntSpan
BuildRequires:	perl-devel >= 1:5.8.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
News::Newsrc manages newsrc files.

%description -l pl.UTF-8
News::Newsrc zarządza plikami newsrc.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/News/Newsrc.pm
%{_mandir}/man3/*
