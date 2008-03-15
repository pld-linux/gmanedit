#
Summary:	Manpage editor
Name:		gmanedit
Version:	0.4.1
Release:	1
License:	GPL
Group:		Applications
Source0:	http://dl.sourceforge.net/gmanedit2/%{name}-%{version}.tar.gz
# Source0-md5:	69ca2f2ebc7313f62cd6f9d36de27274
URL:		http://sourceforge.net/projects/gmanedit2/
#BuildRequires:	autoconf
#BuildRequires:	automake
BuildRequires:	gtk+2-devel
#BuildRequires:	intltool
#BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gnome Manual Pages Editor is an editor for man pages that runs on X
using the GTK+ libraries.

%prep
%setup -q

%build
# if ac/am/* rebuilding is necessary, do it in this order and add
# appropriate BuildRequires
#%%{__intltoolize}
#%%{__gettextize}
#%%{__libtoolize}
#%%{__aclocal}
#%%{__autoconf}
#%%{__autoheader}
#%%{__automake}
# if not running libtool or automake, but config.sub is too old:
#cp -f /usr/share/automake/config.sub .
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/gmanedit
%{_desktopdir}/gmanedit.desktop
%{_mandir}/man1/gmanedit.1*
%{_pixmapsdir}/gmanedit.png
%{_pixmapsdir}/gmanedit_icon.png
