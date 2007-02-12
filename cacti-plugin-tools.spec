%define		namesrc	tools
%include	/usr/lib/rpm/macros.perl
Summary:	Plugin for Cacti - Tools
Summary(pl.UTF-8):	Wtyczka do Cacti - Tools
Name:		cacti-plugin-tools
Version:	0.2
Release:	1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://cactiusers.net/downloads/plugins/%{namesrc}-%{version}.tar.gz
# Source0-md5:	cfd226593d826ad12dd72ed76f27332d
URL:		http://www.cactiusers.org/
#BuildRequires:	rpm-perlprov
Requires:	cacti
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		webcactipluginroot /usr/share/cacti/plugins/%{namesrc}

%description
Plugin for Cacti - Tools.

%description -l pl.UTF-8
Wtyczka do Cacti - Tools.

%prep
%setup -q -n %{namesrc}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{webcactipluginroot}
cp -aRf * $RPM_BUILD_ROOT%{webcactipluginroot}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#%doc 
%{webcactipluginroot}
