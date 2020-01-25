#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define	pdir	Filesys
%define	pnam	Virtual-Async-Dispatcher
Summary:	perl(Filesys::Virtual::Async::Dispatcher)
Name:		perl-Filesys-Virtual-Async-Dispatcher
Version:	0.01
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Filesys/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	de5133e55de1250f1e4a0d1d1bb47112
URL:		http://search.cpan.org/dist/Filesys-Virtual-Async-Dispatcher/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Filesys::Virtual::Async)
BuildRequires:	perl-Test-Simple >= 0.86
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module allows you to have arbitrary combinations of
Filesys::Virtual::Async objects mounted and expose a single
filesystem. The dispatcher will correctly map methods to the proper
object based on their path in the filesystem. This works similar to
the way linux manages mounts in a single "visible" filesystem.

It might be a bit confusing on how the paths work at first. I'm sure
with a bit of experimentation and looking at the documentation for the
Filesys::Virtual::Async::XYZ subclass, you'll get it!

This module makes extensive use of the functions in File::Spec to be
portable, so it might trip you up if you are developing on a linux box
and trying to mount '/foo' on a win32 box :)

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Filesys/Virtual/Async/*.pm
#%%{perl_vendorlib}/Filesys/Virtual/Async/Dispatcher
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
