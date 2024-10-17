%define name tinyfugue
%define version 5.0
%define pre b8
%define fver 50%pre
%define fname tf-%fver
%define rel 0.%pre.5

Summary: Flexible, screen-oriented MUD client, for use with any type of MUD
Name: %{name}
Version: %{version}
Release: %mkrel %rel
URL: https://tinyfugue.sourceforge.net/
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


%changelog
* Thu Dec 08 2011 GÃ¶tz Waschk <waschk@mandriva.org> 5.0-0.b8.5mdv2012.0
+ Revision: 738852
- yearly rebuild

* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 5.0-0.b8.4mdv2011.0
+ Revision: 615219
- the mass rebuild of 2010.1 packages

* Mon Apr 12 2010 Funda Wang <fwang@mandriva.org> 5.0-0.b8.3mdv2010.1
+ Revision: 533635
- rebuild

* Tue Jun 30 2009 GÃ¶tz Waschk <waschk@mandriva.org> 5.0-0.b8.2mdv2010.0
+ Revision: 391008
- fix URL
- update license
- fix configure call

* Fri Dec 21 2007 Olivier Blin <blino@mandriva.org> 5.0-0.b8.1mdv2009.0
+ Revision: 136546
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Aug 01 2007 GÃ¶tz Waschk <waschk@mandriva.org> 5.0-0.b8.1mdv2008.0
+ Revision: 57476
- new version
- Import tinyfugue



* Mon Jul 31 2006 Götz Waschk <waschk@mandriva.org> 5.0-0.b7.1mdv2007.0
- new version

* Fri Mar 17 2006 Götz Waschk <waschk@mandriva.org> 5.0-0.b6.3mdk
- rebuild for new openssl

* Thu Apr 28 2005 Götz Waschk <waschk@mandriva.org> 5.0-0.b6.2mdk
- hardcode the lib directory

* Tue Apr 26 2005 Götz Waschk <waschk@mandriva.org> 5.0-0.b6.1mdk
- new version

* Thu Jun 24 2004 Götz Waschk <waschk@linux-mandrake.com> 5.0-0.b4.1mdk
- initial package
