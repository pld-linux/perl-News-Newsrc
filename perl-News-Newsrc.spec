%include	/usr/lib/rpm/macros.perl
%define	pdir	News
%define	pnam	Newsrc
Summary:	News::Newsrc perl module
Summary(pl):	Modu³ perla News::Newsrc
Name:		perl-News-Newsrc
Version:	1.08
Release:	7
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	cd874f7ba91bbb64f3f0f75f2d37893a
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
BuildRequires:	perl-Set-IntSpan
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
News::Newsrc manages newsrc files.

%description -l pl
News::Newsrc zarz±dza plikami newsrc.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/News/Newsrc.pm
%{_mandir}/man3/*
