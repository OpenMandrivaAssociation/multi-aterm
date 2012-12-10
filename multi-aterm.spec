Summary:	Light tabbed terminal emulator
Name:		multi-aterm
Version:	0.2.1
Release:	%{mkrel 4}
Source0:	http://www.nongnu.org/materm/%{name}-%{version}.tar.bz2
Source1:	multi-aterm.png
License:	GPLv2+
Group:		Terminals
URL:		http://www.nongnu.org/materm/materm.html
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	libx11-devel
BuildRequires:	libxt-devel
BuildRequires:	xpm-devel
BuildRequires:	imagemagick

%description
Multi-aterm is a terminal emulator like rxvt, xterm, eterm, aterm 
- It's a terminal emulator which is small and fast with efficent
pseudo-transparency, like aterm.
- It's also a tabbed terminal emulator.
- It's a terminal emulator not requiring GNOME or KDE libs, just
written in X-lib (for people not using GNOME nor KDE).

%prep
%setup -q

%build
%configure2_5x --enable-keepscrolling --enable-mousewheel --enable-transparency --enable-xterm-scroll --enable-fading --enable-half-shadow --enable-swapscreen --with-xpm=/usr
%make

%install
rm -rf %{buildroot}
%makeinstall_std

mkdir -p %{buildroot}%{_iconsdir}/hicolor/{16x16,32x32,48x48}/apps
install -m644 %{SOURCE1} %{buildroot}%{_iconsdir}/hicolor/48x48/apps/%{name}.png
convert -scale 32x32 %{SOURCE1} %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png
convert -scale 16x16 %{SOURCE1} %{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{name}.png

mkdir -p %{buildroot}%{_datadir}/applications
cat << EOF > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Exec=%{_bindir}/%{name}
Icon=%{name}
Categories=System;TerminalEmulator;
Name=Multi-aterm
Comment=Light tabbed terminal emulator
EOF

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc doc/TODO AUTHORS ChangeLog
%{_mandir}/man1/*
%{_datadir}/applications/mandriva-*.desktop
%{_bindir}/multi-aterm
%{_iconsdir}/hicolor/*/apps/%{name}.png



%changelog
* Sat Feb 05 2011 Funda Wang <fwang@mandriva.org> 0.2.1-4mdv2011.0
+ Revision: 636300
- BR xt
- tighten BR

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.2.1-3mdv2011.0
+ Revision: 430119
- rebuild

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Sat Sep 06 2008 Adam Williamson <awilliamson@mandriva.org> 0.2.1-2mdv2009.0
+ Revision: 281786
- don't package COPYING
- drop old KDE desktop entry
- fix and improve menu entry
- fd.o icons
- use makeinstall_std macro
- use Mandriva optflags
- set --with-xpm parameter to configure (fixes build)
- no need to set prefix when using configure2_5x macro
- use configure2_5x
- streamline and re-wrap description
- br ImageMagick
- source location
- new license policy
- tabs
- useful summary
- drop unnecessary defines

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - auto convert menu to XDG
    - BR xpm-devel
    - kill re-definition of %%buildroot on Pixel's request
    - use %%mkrel
    - buildrequires X11-devel instead of XFree86-devel
    - import multi-aterm

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Mon Feb 13 2006 Jerome Soyer <saispo@mandriva.org> 0.2.1-1mdk
- New release 0.2.1

* Mon Aug 29 2005 Marcel Pol <mpol@mandriva.org> 0.1-3mdk
- rebuild

* Fri Apr 30 2004 Marcel Pol <mpol@mandrake.org> 0.1-2mdk
- new url

* Fri Dec 26 2003 Marcel Pol <mpol@mandrake.org> 0.1-1mdk
- 0.1
- 64bit buildrequires

* Sat Aug 30 2003 Marcel Pol <mpol@gmx.net> 0.0.4-4mdk
- buildrequires xfree86-devel
- change description (not in "I" form)

* Mon Aug 25 2003 antoine Ginies <guibo@guiboserv.guibland.com> 0.0.4-3mdk
- add buildrequires libxpm4-devel (thx r1)
- add post for menu

* Mon Aug 25 2003 antoine Ginies <guibo@guiboserv.guibland.com> 0.0.4-2mdk
- add a menu entry

* Mon Aug 25 2003 antoine Ginies <aginies@mandrakesoft.com> 0.0.4-1mdk
- first release for mandrakesoft


# end of file
