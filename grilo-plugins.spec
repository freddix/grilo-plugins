Summary:	Grilo plugins
Name:		grilo-plugins
Version:	0.2.10
Release:	1
License:	LGPL v2.1+
Group:		Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/grilo-plugins/0.2/%{name}-%{version}.tar.xz
# Source0-md5:	5ce7e6909f1778dcad314a3ac99fa6f6
URL:		http://live.gnome.org/Grilo
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib-devel
BuildRequires:	gmime-devel
BuildRequires:	grilo-devel
BuildRequires:	gupnp-av-devel
BuildRequires:	gupnp-devel
BuildRequires:	json-glib-devel
BuildRequires:	libgcrypt-devel
BuildRequires:	libgdata-devel
BuildRequires:	libquvi-devel
BuildRequires:	libsoup-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	pkg-config
BuildRequires:	rest-devel
BuildRequires:	sqlite3-devel
BuildRequires:	totem-pl-parser-devel
BuildRequires:	tracker-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Collection of plugins for Grilo implementing Grilo's API for various
multimedia content providers.

%prep
%setup -q

# kill gnome common deps
sed -i -e 's/GNOME_COMPILE_WARNINGS.*//g'	\
    -i -e 's/GNOME_MAINTAINER_MODE_DEFINES//g'	\
    -i -e 's/GNOME_COMMON_INIT//g'		\
    -i -e 's/GNOME_CXX_WARNINGS.*//g'		\
    -i -e 's/GNOME_DEBUG_CHECK//g' configure.ac

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/grilo-0.2/*.la

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}//grilo-0.2/libgrlfreebox.so
%attr(755,root,root) %{_libdir}//grilo-0.2/libgrlguardianvideos.so
%attr(755,root,root) %{_libdir}//grilo-0.2/libgrlpocket.so
%attr(755,root,root) %{_libdir}/grilo-0.2/libgrlappletrailers.so
%attr(755,root,root) %{_libdir}/grilo-0.2/libgrlbliptv.so
%attr(755,root,root) %{_libdir}/grilo-0.2/libgrlbookmarks.so
%attr(755,root,root) %{_libdir}/grilo-0.2/libgrlfilesystem.so
%attr(755,root,root) %{_libdir}/grilo-0.2/libgrlflickr.so
%attr(755,root,root) %{_libdir}/grilo-0.2/libgrlgravatar.so
%attr(755,root,root) %{_libdir}/grilo-0.2/libgrljamendo.so
%attr(755,root,root) %{_libdir}/grilo-0.2/libgrllastfm-albumart.so
%attr(755,root,root) %{_libdir}/grilo-0.2/libgrllocalmetadata.so
%attr(755,root,root) %{_libdir}/grilo-0.2/libgrlmagnatune.so
%attr(755,root,root) %{_libdir}/grilo-0.2/libgrlmetadatastore.so
%attr(755,root,root) %{_libdir}/grilo-0.2/libgrloptical-media.so
%attr(755,root,root) %{_libdir}/grilo-0.2/libgrlpodcasts.so
%attr(755,root,root) %{_libdir}/grilo-0.2/libgrlraitv.so
%attr(755,root,root) %{_libdir}/grilo-0.2/libgrlshoutcast.so
%attr(755,root,root) %{_libdir}/grilo-0.2/libgrltmdb.so
%attr(755,root,root) %{_libdir}/grilo-0.2/libgrltracker.so
%attr(755,root,root) %{_libdir}/grilo-0.2/libgrlupnp.so
%attr(755,root,root) %{_libdir}/grilo-0.2/libgrlvimeo.so
%attr(755,root,root) %{_libdir}/grilo-0.2/libgrlyoutube.so
%{_libdir}/grilo-0.2/grl-apple-trailers.xml
%{_libdir}/grilo-0.2/grl-bliptv.xml
%{_libdir}/grilo-0.2/grl-bookmarks.xml
%{_libdir}/grilo-0.2/grl-filesystem.xml
%{_libdir}/grilo-0.2/grl-flickr.xml
%{_libdir}/grilo-0.2/grl-freebox.xml
%{_libdir}/grilo-0.2/grl-gravatar.xml
%{_libdir}/grilo-0.2/grl-guardianvideos.xml
%{_libdir}/grilo-0.2/grl-jamendo.xml
%{_libdir}/grilo-0.2/grl-lastfm-albumart.xml
%{_libdir}/grilo-0.2/grl-local-metadata.xml
%{_libdir}/grilo-0.2/grl-magnatune.xml
%{_libdir}/grilo-0.2/grl-metadata-store.xml
%{_libdir}/grilo-0.2/grl-optical-media.xml
%{_libdir}/grilo-0.2/grl-pocket.xml
%{_libdir}/grilo-0.2/grl-podcasts.xml
%{_libdir}/grilo-0.2/grl-raitv.xml
%{_libdir}/grilo-0.2/grl-shoutcast.xml
%{_libdir}/grilo-0.2/grl-tmdb.xml
%{_libdir}/grilo-0.2/grl-tracker.xml
%{_libdir}/grilo-0.2/grl-upnp.xml
%{_libdir}/grilo-0.2/grl-vimeo.xml
%{_libdir}/grilo-0.2/grl-youtube.xml

