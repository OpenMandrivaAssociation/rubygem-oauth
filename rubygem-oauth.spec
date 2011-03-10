# Generated from oauth-0.4.4.gem by gem2rpm5 -*- rpm-spec -*-          
%define	rbname	oauth

Summary:	OAuth Core Ruby implementation
Name:		rubygem-%{rbname}

Version:	0.4.4
Release:	1
Group:		Development/Ruby
License:	MIT
URL:		http://%{oname}.rubyforge.org/
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
