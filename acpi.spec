%define 	ftpver	0.07
Summary:	Command-line ACPI client
Summary(pl):	Klient ACPI dzia³aj±cy z linii poleceñ
Name:		acpi
Version:	0.0.7
Release:	1
License:	GPL
Group:		Applications
Source0:	http://grahame.angrygoats.net/source/acpi/%{name}-%{ftpver}.tar.gz
# Source0-md5:	791f1d619955f60e4b5223468f6fb4db
URL:		http://grahame.angrygoats.net/acpi.shtml
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Linux ACPI client is a small command-line program that attempts to
replicate the functionality of the 'old' apm command on ACPI systems.
It includes battery and thermal information.

%description -l pl
Klient Linux ACPI to ma³y program dzia³aj±cy z linii poleceñ, bêd±cy
prób± zast±pienia funkcjonalno¶ci "starego" polecenia apm na systemach
opartych o ACPI. Zawiera informacje o zasilaniu i temperaturze.

%prep
%setup -q -n %{name}-%{ftpver}

%build
%{__aclocal}
%{__autoconf}
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
%doc AUTHORS ChangeLog 
%attr(755,root,root) %{_bindir}/*
