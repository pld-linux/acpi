Summary:	Command-line ACPI client
Summary(pl.UTF-8):	Klient ACPI działający z linii poleceń
Name:		acpi
Version:	1.8
Release:	1
License:	GPL v2+
Group:		Applications/System
Source0:	https://downloads.sourceforge.net/acpiclient/%{name}-%{version}.tar.gz
# Source0-md5:	50804ce5dc27443e649e1ecf089da7b9
URL:		https://acpiclient.sourceforge.net/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
ExclusiveArch:	%{ix86} %{x8664} x32 ia64
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

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/acpi
%{_mandir}/man1/acpi.1*
