Summary:	A simple-in-use GTK-based text editor
Name:		teagtk
Version:	17.6.3
Release:	%mkrel 1
Epoch:		0
Group:		Editors
License:	GPLv2+
URL:		http://tea-editor.sourceforge.net/
Source0:	http://ovh.dl.sourceforge.net/sourceforge/tea-editor/%{name}-%{version}.tar.bz2

BuildRoot:	%{_tmppath}/%{name}-root
BuildRequires:	gtk+2-devel gtksourceview-devel gnome-vfs2-devel
BuildRequires:	imagemagick aspell-devel
Obsoletes:	tea < %epoch:%version
Provides:	tea = %epoch:%version

%description
Teagtk is a simple-in-use GTK-based text editor.


%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%find_lang %{name}

# icons
mkdir -p %buildroot/{%_liconsdir,%_iconsdir,%_miconsdir}
convert -resize 16x16 pixmaps/tea_icon_v2.png %buildroot/%_miconsdir/%name.png
convert -resize 32x32 pixmaps/tea_icon_v2.png %buildroot/%_iconsdir/%name.png
convert -resize 48x48 pixmaps/tea_icon_v2.png %buildroot/%_liconsdir/%name.png

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=tea
Comment=A simple-in-use GTK-based text editor
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Gtk;TextEditor;Utility;
EOF

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README TODO
%{_bindir}/*
%{_datadir}/%name
%_liconsdir/%name.png
%_miconsdir/%name.png
%_iconsdir/%name.png
%_datadir/applications/*
