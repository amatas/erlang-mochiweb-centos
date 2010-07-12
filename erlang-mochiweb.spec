%global debug_package %{nil}
%global realname mochiweb


Name:		erlang-%{realname}
Version:	1.3
Release:	0.4.20100507svn159%{?dist}
Summary:	An Erlang library for building lightweight HTTP servers
Group:		Development/Libraries
License:	MIT
URL:		http://code.google.com/p/mochiweb/
## svn export -r 97 http://mochiweb.googlecode.com/svn/trunk/ erlang-mochiweb-1.3
## tar cfz erlang-mochiweb-1.3.tar.gz erlang-mochiweb-1.3
Source0:	%{name}-%{version}.tar.gz
Patch1:		erlang-mochiweb-0001-Fix-for-EPEL-5-erlang-R12B-5.patch
Patch2:		erlang-mochiweb-0002-Fix-for-Erlang-OTP-R14A.patch
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildRequires:	erlang
Requires:	erlang-compiler
Requires:	erlang-crypto
Requires:	erlang-erts
Requires:	erlang-eunit
Requires:	erlang-inets
Requires:	erlang-kernel
Requires:	erlang-ssl
Requires:	erlang-stdlib
Requires:	erlang-syntax_tools
Requires:	erlang-xmerl
Provides:	%{realname} = %{version}-%{release}

%description
An Erlang library for building lightweight HTTP servers.


%prep
%setup -q
%if 0%{?el5}
%patch1 -p1 -b .epel
touch -r src/mochiglobal.erl.epel src/mochiglobal.erl
touch -r src/mochiweb.app.src.epel src/mochiweb.app.src
%endif
%patch2 -p1 -b .R14A
chmod 755 scripts/new_mochiweb.erl


%build
%if 0%{?el5}
# required on EPEL to suppress failures while autogenerating with old erlang
cp -arv src/mochiweb.app.src ebin/mochiweb.app
%endif
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT

# base binary modules
install -D -m 644 ebin/%{realname}.app $RPM_BUILD_ROOT%{_libdir}/erlang/lib/%{realname}-%{version}/ebin/%{realname}.app
install -m 644 ebin/*.beam $RPM_BUILD_ROOT%{_libdir}/erlang/lib/%{realname}-%{version}/ebin/

# skeleton files
cp -arv priv $RPM_BUILD_ROOT%{_libdir}/erlang/lib/%{realname}-%{version}
cp -arv scripts $RPM_BUILD_ROOT%{_libdir}/erlang/lib/%{realname}-%{version}
cp -arv support $RPM_BUILD_ROOT%{_libdir}/erlang/lib/%{realname}-%{version}

%check
%if 0%{?el5}
echo "Does not supported currently due to old erlang"
%else
make test
%endif


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc LICENSE README examples
%dir %{_libdir}/erlang/lib/%{realname}-%{version}
%dir %{_libdir}/erlang/lib/%{realname}-%{version}/ebin
%{_libdir}/erlang/lib/%{realname}-%{version}/ebin/mochifmt.beam
%{_libdir}/erlang/lib/%{realname}-%{version}/ebin/mochifmt_records.beam
%{_libdir}/erlang/lib/%{realname}-%{version}/ebin/mochifmt_std.beam
%{_libdir}/erlang/lib/%{realname}-%{version}/ebin/mochiglobal.beam
%{_libdir}/erlang/lib/%{realname}-%{version}/ebin/mochihex.beam
%{_libdir}/erlang/lib/%{realname}-%{version}/ebin/mochijson.beam
%{_libdir}/erlang/lib/%{realname}-%{version}/ebin/mochijson2.beam
%{_libdir}/erlang/lib/%{realname}-%{version}/ebin/mochilists.beam
%{_libdir}/erlang/lib/%{realname}-%{version}/ebin/mochinum.beam
%{_libdir}/erlang/lib/%{realname}-%{version}/ebin/mochitemp.beam
%{_libdir}/erlang/lib/%{realname}-%{version}/ebin/mochiutf8.beam
%{_libdir}/erlang/lib/%{realname}-%{version}/ebin/mochiweb.app
%{_libdir}/erlang/lib/%{realname}-%{version}/ebin/mochiweb.beam
%{_libdir}/erlang/lib/%{realname}-%{version}/ebin/mochiweb_app.beam
%{_libdir}/erlang/lib/%{realname}-%{version}/ebin/mochiweb_charref.beam
%{_libdir}/erlang/lib/%{realname}-%{version}/ebin/mochiweb_cookies.beam
%{_libdir}/erlang/lib/%{realname}-%{version}/ebin/mochiweb_cover.beam
%{_libdir}/erlang/lib/%{realname}-%{version}/ebin/mochiweb_echo.beam
%{_libdir}/erlang/lib/%{realname}-%{version}/ebin/mochiweb_headers.beam
%{_libdir}/erlang/lib/%{realname}-%{version}/ebin/mochiweb_html.beam
%{_libdir}/erlang/lib/%{realname}-%{version}/ebin/mochiweb_http.beam
%{_libdir}/erlang/lib/%{realname}-%{version}/ebin/mochiweb_io.beam
%{_libdir}/erlang/lib/%{realname}-%{version}/ebin/mochiweb_mime.beam
%{_libdir}/erlang/lib/%{realname}-%{version}/ebin/mochiweb_multipart.beam
%{_libdir}/erlang/lib/%{realname}-%{version}/ebin/mochiweb_request.beam
%{_libdir}/erlang/lib/%{realname}-%{version}/ebin/mochiweb_response.beam
%{_libdir}/erlang/lib/%{realname}-%{version}/ebin/mochiweb_skel.beam
%{_libdir}/erlang/lib/%{realname}-%{version}/ebin/mochiweb_socket.beam
%{_libdir}/erlang/lib/%{realname}-%{version}/ebin/mochiweb_socket_server.beam
%{_libdir}/erlang/lib/%{realname}-%{version}/ebin/mochiweb_sup.beam
%{_libdir}/erlang/lib/%{realname}-%{version}/ebin/mochiweb_util.beam
%{_libdir}/erlang/lib/%{realname}-%{version}/ebin/reloader.beam
%{_libdir}/erlang/lib/%{realname}-%{version}/priv
%{_libdir}/erlang/lib/%{realname}-%{version}/scripts
%{_libdir}/erlang/lib/%{realname}-%{version}/support


%changelog
* Mon Jul 12 2010 Peter Lemenkov <lemenkov@gmail.com> 1.3-0.4.20100507svn159
- Rebuild with new Erlang
- Simplified spec-file

* Mon Jun  7 2010 Peter Lemenkov <lemenkov@gmail.com> 1.3-0.3.20100507svn159
- Added %%check target and fixed mochiweb:test()
- Fix EL-5 build

* Mon Jun  7 2010 Peter Lemenkov <lemenkov@gmail.com> 1.3-0.2.20100507svn159
- Removed accidentally added macro

* Mon May 31 2010 Peter Lemenkov <lemenkov@gmail.com> 1.3-0.1.20100507svn159
- New pre-release version (from VCS).

* Thu May 13 2010 Peter Lemenkov <lemenkov@gmail.com> 0-0.1.svn154
- Initial package
