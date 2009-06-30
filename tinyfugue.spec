%define name tinyfugue
%define version 5.0
%define pre b8
%define fver 50%pre
%define fname tf-%fver
%define rel 0.%pre.2

Summary: Flexible, screen-oriented MUD client, for use with any type of MUD
Name: %{name}
Version: %{version}
Release: %mkrel %rel
URL: http://tinyfugue.sourceforge.net/
Source0: http://ftp.tcp.com/pub/mud/Clients/tinyfugue/%{fname}.tar.bz2
License: GPLv2+
Group: Games/Adventure
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: openssl-devel
BuildRequires: termcap-devel

%description
TinyFugue, aka "tf", is a flexible, screen-oriented MUD client, for
use with any type of MUD. TinyFugue is one of the most popular and
powerful mud clients.

%prep
%setup -q -n %fname

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %buildroot%_bindir
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc CHANGES README CREDITS
%_bindir/tf
%_datadir/tf-lib
