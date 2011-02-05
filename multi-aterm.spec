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

