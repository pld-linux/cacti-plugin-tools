%define		plugin	tools
%include	/usr/lib/rpm/macros.perl
Summary:	Plugin for Cacti - Tools
Summary(pl.UTF-8):	Wtyczka do Cacti - Tools
Name:		cacti-plugin-tools
Version:	0.3
Release:	1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://mirror.cactiusers.org/downloads/plugins/%{plugin}-%{version}.zip
# Source0-md5:	b09190195d81852d208fb01a8a9f65c9
URL:		http://www.cactiusers.org/
BuildRequires:	rpm-perlprov
Requires:	cacti
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		cactidir		/usr/share/cacti
%define		plugindir		%{cactidir}/plugins/%{plugin}

%description
Plugin for Cacti - Tools.

%description -l pl.UTF-8
Wtyczka do Cacti - Tools.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a . $RPM_BUILD_ROOT%{plugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{plugindir}
