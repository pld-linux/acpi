Summary:	Command-line ACPI client
Summary(pl.UTF-8):	Klient ACPI działający z linii poleceń
Name:		acpi
Version:	1.7
Release:	1
License:	GPL v2+
Group:		Applications/System
Source0:	http://downloads.sourceforge.net/acpiclient/%{name}-%{version}.tar.gz
# Source0-md5:	b52ce4ca39bbf7000a1c2de8879f1dcb
Patch0:		%{name}-am.patch
URL:		http://acpiclient.sourceforge.net/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
ExclusiveArch:	%{ix86} %{x8664} ia64
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Linux ACPI client is a small command-line program that attempts to
replicate the functionality of the 'old' apm command on ACPI systems.
It includes battery and thermal information.

%description -l pl.UTF-8
Klient Linux ACPI to mały program działający z linii poleceń, będący
próbą zastąpienia funkcjonalności "starego" polecenia apm na systemach
opartych o ACPI. Zawiera informacje o zasilaniu i temperaturze.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man1

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/acpi
%{_mandir}/man1/acpi.1*
