%define		plugin	tools
%define		php_min_version 5.0.0
%include	/usr/lib/rpm/macros.php
Summary:	Plugin for Cacti - Network Tools
Summary(pl.UTF-8):	Wtyczka do Cacti - Tools
Name:		cacti-plugin-%{plugin}
Version:	0.3
Release:	2
License:	GPL v2
Group:		Applications/WWW
Source0:	http://mirror.cactiusers.org/downloads/plugins/%{plugin}-%{version}.tar.gz
# Source0-md5:	3011d05efeca1a0d3485fe6f7d328bc1
URL:		http://www.cactiusers.org/
BuildRequires:	rpmbuild(macros) >= 1.554
Requires:	cacti
Requires:	php-common >= 4:%{php_min_version}
Requires:	php-pcre
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		cactidir		/usr/share/cacti
%define		plugindir		%{cactidir}/plugins/%{plugin}

%description
This plugin adds Network Tools to the Utilities section of Cacti.

%description -l pl.UTF-8
Wtyczka do Cacti - Tools.

%prep
%setup -qc
mv %{plugin}/{LICENSE,README} .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a %{plugin}/* $RPM_BUILD_ROOT%{plugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{plugindir}
