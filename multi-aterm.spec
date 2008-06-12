%define name multi-aterm
%define version 0.2.1
%define release  %mkrel 1

Summary: Multi aterm terminal
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
Source1: multi-aterm.png
License: GPL
Group: Terminals
URL: http://www.nongnu.org/materm/materm.html
#packager: Antoine Ginies <aginies@mandrakesoft.com>
BuildRoot: %{_tmppath}/%{name}-buildroot
Prefix: %{_prefix}
BuildRequires: X11-devel xpm-devel

%description
Multi-aterm is a firstly a terminal emulator like rxvt, xterm, eterm, aterm 
There are many terminals emulators, so why writing another one ?
- It's a terminal emulator which is small and fast with efficent pseudo 
  transparency, like aterm.
- It's also a tabbed terminal emulator like GMT (gnome-multi-terminal).
- It's a terminal emulator not requiring GNOME or KDE libs, just written in 
  X-lib (for people not using GNOME nor KDE)

%prep
%setup -q

%build
%configure --prefix=%{_prefix} --enable-keepscrolling --enable-mousewheel --enable-transparency --enable-xterm-scroll --enable-fading --enable-half-shadow --enable-swapscreen
%make

%install
rm -rf $RPM_BUILD_ROOT
%make DESTDIR=$RPM_BUILD_ROOT install

mkdir -p ${RPM_BUILD_ROOT}%{_datadir}/pixmaps
install -m644 %{SOURCE1} ${RPM_BUILD_ROOT}%{_datadir}/pixmaps/

(mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Exec=%{_bindir}/%{name}
Icon=%{_datadir}/pixmaps/%name.png
Categories=TerminalEmulator;Systenalm;Utility;
Name=Multi-aterm
Comment=Multi-aterm
EOF
)

(mkdir -p %{buildroot}%{_datadir}/applnk/Multimedia/
cat << EOF > %{buildroot}%{_datadir}/applnk/Multimedia/%{name}.desktop
[Desktop Entry]
Name="Multi-aterm" \
Comment="Multi-aterm" \
TryExec="%{name}" \
Exec="multi-aterm" \
Icon="%{_datadir}/pixmaps/%{name}.png" \
Terminal="0" \
Type="Application"
EOF
)

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc doc/TODO COPYING AUTHORS ChangeLog
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applnk/Multimedia/%{name}.desktop
%{_mandir}/man1/*
%{_datadir}/applications/mandriva-*.desktop
%{_bindir}/multi-aterm

