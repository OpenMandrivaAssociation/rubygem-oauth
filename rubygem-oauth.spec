# Generated from oauth-0.4.4.gem by gem2rpm5 -*- rpm-spec -*-          
%define	rbname	oauth

Summary:	OAuth Core Ruby implementation
Name:		rubygem-%{rbname}

Version:	0.4.4
Release:	3
Group:		Development/Ruby
License:	MIT
URL:		http://%{rbname}.rubyforge.org/
Source0:	http://rubygems.org/gems/%{rbname}-%{version}.gem
BuildRequires:	rubygems 
BuildArch:	noarch

%description
This is a RubyGem for implementing both OAuth clients and servers in Ruby
applications.

%package	doc
Summary:	Documentation for %{name}
Group:		Books/Computer books
Requires:	%{name} = %{EVRD}

%description	doc
Documents, RDoc & RI documentation for %{name}.

%prep
%setup -q

%build
%gem_build -f '(Gemfile|Rakefile|examples|tasks|test)'

%install
rm -rf %{buildroot}
%gem_install

%clean
rm -rf %{buildroot}

%files
%{_bindir}/oauth
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/LICENSE
%{ruby_gemdir}/gems/%{rbname}-%{version}/Gemfile*
%{ruby_gemdir}/gems/%{rbname}-%{version}/Rakefile
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/bin
%{ruby_gemdir}/gems/%{rbname}-%{version}/bin/oauth
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/digest
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/digest/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/oauth
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/oauth/*
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/tasks
%{ruby_gemdir}/gems/%{rbname}-%{version}/tasks/*.rake
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec

%files doc
%doc %{ruby_gemdir}/doc/%{rbname}-%{version}
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/*.rdoc
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/TODO
%{ruby_gemdir}/gems/%{rbname}-%{version}/test/*
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/examples
%{ruby_gemdir}/gems/%{rbname}-%{version}/examples/*.rb


%changelog
* Thu Mar 10 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.4.4-1
+ Revision: 643381
- regenerate spec with gem2rpm5
- new release: 0.4.4

* Fri Dec 17 2010 Rémy Clouard <shikamaru@mandriva.org> 0.3.6-3mdv2011.0
+ Revision: 622496
- rebuild for new rpm-mandriva-setup

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 0.3.6-2mdv2011.0
+ Revision: 614774
- the mass rebuild of 2010.1 packages

  + Per Øyvind Karlsen <peroyvind@mandriva.org>
    - ooops, revert previous incorrect buildrequires change...
    - add missing buildrequires

* Thu Feb 04 2010 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.3.6-1mdv2010.1
+ Revision: 500857
- import rubygem-oauth


* Mon Feb  4 2010 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.3.6-1
- initial release
