%define	oname	oauth

Summary:	OAuth Core Ruby implementation
Name:		rubygem-%{oname}
Version:	0.4.4
Release:	%mkrel 1
License:	MIT
Group:		Development/Ruby
URL:		http://%{oname}.rubyforge.org/
Source0:	http://gems.rubyforge.org/gems/%{oname}-%{version}.gem
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	ruby-RubyGems
Requires:	ruby rubygem-ruby-hmac
BuildArch:	noarch

%description
This is a RubyGem for implementing both OAuth clients and servers in Ruby
applications.

%prep
%setup -q

%build
%gem_build

%install
rm -rf %{buildroot}
%{gem_install} --bindir %{buildroot}%{_bindir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
%{ruby_gemdir}/gems/%{oname}-%{version}
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec
%{_bindir}/oauth

