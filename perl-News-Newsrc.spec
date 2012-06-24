%include	/usr/lib/rpm/macros.perl
Summary:	News-Newsrc perl module
Summary(pl):	Modu� perla News-Newsrc
Name:		perl-News-Newsrc
Version:	1.08
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/News/News-Newsrc-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Set-IntSpan
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
News-Newsrc manages newsrc files.

%description -l pl
News-Newsrc zarz�dza plikami newsrc.

%prep
%setup -q -n News-Newsrc-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/News/Newsrc.pm
%{_mandir}/man3/*
