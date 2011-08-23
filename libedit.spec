%define snap 20080712

Summary:	The NetBSD Editline library
Name:		libedit
Version:	2.11
Release:	4.%{snap}cvs.1%{?dist}
License:	BSD
Group:		System Environment/Libraries
URL:		http://www.thrysoee.dk/editline/
Source0:	http://www.thrysoee.dk/editline/%{name}-%{snap}-%{version}.tar.gz

BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires: 	gawk
BuildRequires: 	ncurses-devel

%description
Libedit is an autotool- and libtoolized port of the NetBSD Editline library.
It provides generic line editing, history, and tokenization functions, similar
to those found in GNU Readline.

%package devel
Summary:	Development files for %{name}
Group:		Development/Libraries

Requires:	%{name} = %{version}-%{release}
Requires:	pkgconfig
Requires:	ncurses-devel

%description devel
This package contains development files for %{name}.

%prep
%setup -q -n %{name}-%{snap}-%{version}

# Suppress rpmlint error.
iconv --from-code ISO8859-1 --to-code UTF-8 ./ChangeLog \
  --output ChangeLog.utf-8 && mv ChangeLog.utf-8 ./ChangeLog

%build
%configure --disable-static

# Trying to omit unused direct shared library dependencies leads to
# undefined non-weak symbols.

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make install INSTALL="%{__install} -p" DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name "*.la" -delete

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc ChangeLog COPYING THANKS
%{_libdir}/%{name}.so.*

%files devel
%defattr(-,root,root,-)
%doc examples/fileman.c examples/test.c
%doc %{_mandir}/man3/*
%doc %{_mandir}/man5/editrc.5*
%{_includedir}/histedit.h
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%dir %{_includedir}/editline
%{_includedir}/editline/readline.h

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 2.11-4.20080712cvs.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.11-4.20080712cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.11-3.20080712cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jan 22 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 2.11-2.20080712cvs
- Add ncurses-devel requires to -devel subpackage (BZ#481252)

* Sun Jul 28 2008 Debarshi Ray <rishi@fedoraproject.org> - 2.11-1.20080712cvs
- Version bump to 20080712-2.11.

* Sat Feb 16 2008 Debarshi Ray <rishi@fedoraproject.org> - 2.10-4.20070831cvs
- Rebuilding with gcc-4.3 in Rawhide.

* Sun Nov 04 2007 Debarshi Ray <rishi@fedoraproject.org> - 2.10-3.20070831cvs
- Removed 'Requires: ncurses-devel'.

* Sat Nov 03 2007 Debarshi Ray <rishi@fedoraproject.org> - 2.10-2.20070831cvs
- Changed character encoding of ChangeLog from ISO8859-1 to UTF-8.

* Sun Sep 03 2007 Debarshi Ray <rishi@fedoraproject.org> - 2.10-1.20070831cvs
- Initial build. Imported SPEC from Rawhide.
