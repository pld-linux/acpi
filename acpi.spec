Summary:	Command-line ACPI client
Summary(pl.UTF-8):	Klient ACPI działający z linii poleceń
Name:		acpi
Version:	0.09
Release:	3
License:	GPL v2+
Group:		Applications/System
Source0:	http://grahame.angrygoats.net/source/acpi/%{name}-%{version}.tar.gz
# Source0-md5:	a5a70595834b487c3a2f9278a3d60768
URL:		http://grahame.angrygoats.net/acpi.shtml
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
