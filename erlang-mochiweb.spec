%global debug_package %{nil}
%global realname mochiweb


Name:		erlang-%{realname}
Version:	1.3
Release:	0.2.20100507svn159%{?dist}
Summary:	An Erlang library for building lightweight HTTP servers
Group:		Development/Libraries
License:	MIT
## svn export -r 159 http://mochiweb.googlecode.com/svn/trunk/ erlang-mochiweb-1.3
## tar cfz erlang-mochiweb-1.3.tar.gz erlang-mochiweb-1.3
URL:		http://code.google.com/p/mochiweb/
Source:		%{name}-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildRequires:	erlang
%if 0%{?el5}
Requires:	erlang
%else
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
%endif
Provides:	%{realname} = %{version}-%{release}

%description
An Erlang library for building lightweight HTTP servers.


%prep
%setup -q
chmod 755 scripts/new_mochiweb.erl


%build
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT

# base binary modules
install -D -m 644 ebin/%{realname}.app $RPM_BUILD_ROOT%{_libdir}/erlang/lib/%{realname}-%{version}/ebin/%{realname}.app
install -m 644 ebin/*.beam $RPM_BUILD_ROOT%{_libdir}/erlang/lib/%{realname}-%{version}/ebin/

# skeleton files
cp -arv priv $RPM_BUILD_ROOT%{_libdir}/erlang/lib/%{realname}-%{version}
cp -arv scripts $RPM_BUILD_ROOT%{_libdir}/erlang/lib/%{realname}-%{version}

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

%changelog
* Mon Jun  7 2010 Peter Lemenkov <lemenkov@gmail.com> 1.3-0.2.20100507svn159
- Removed accidentally added macro

* Mon May 31 2010 Peter Lemenkov <lemenkov@gmail.com> 1.3-0.1.20100507svn159
- New pre-release version (from VCS).

* Thu May 13 2010 Peter Lemenkov <lemenkov@gmail.com> 0-0.1.svn154
- Initial package
