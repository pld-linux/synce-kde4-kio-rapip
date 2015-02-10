Summary:	SynCE kio-rapip module for KDE4
Summary(pl.UTF-8):	Moduł SynCE kio-rapip dla KDE4
Name:		synce-kde4-kio-rapip
Version:	0.4
Release:	0.1
License:	MIT
Group:		X11/Applications/Networking
Source0:	http://downloads.sourceforge.net/synce/kde4-kio-rapip-%{version}.tar.gz
# Source0-md5:	8411e62bcf7936c2fc9dddc4150c9f96
URL:		http://www.synce.org/
BuildRequires:	cmake >= 2.0
BuildRequires:	kde4-kdelibs-devel >= 4
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRequires:	shared-mime-info >= 0.20
BuildRequires:	synce-core-lib-devel >= 0.17
Requires:	synce-core-lib >= 0.17
Obsoletes:	synce-kde
Obsoletes:	synce-kde-agsync
Obsoletes:	synce-kde-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RAPIP is the short form for "RAPI-Protocol". It is a full featured
KIOSlave used to browse through the PDA file system via the SynCE
infrastructure, and to copy files to and from the PDA by drag and drop
via Konqueror.

%description -l pl.UTF-8
RAPIP to skrót od "RAPI-Protocol" (protokół RAPI). Ten pakiet zawiera
w pełni funkcjonalny moduł KIOSlave służący do przeglądania systemu
plików PDA poprzez infrastrukturę SynCE oraz kopiowania plików na i z
urządzenia PDA poprzez przeciąganie i upuszczanie w Konquerorze.

%prep
%setup -q -n kde4-kio-rapip-%{version}

%build
install -d build
cd build
%cmake ..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files -f kcemirror.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog* LICENSE NEWS.kio-rapip README
%attr(755,root,root) %{_libdir}/kde4/kio_rapip.so
%{_datadir}/kde4/services/rapip.protocol
%{_datadir}/kde4/services/synce.protocol
%{_datadir}/mime/packages/synce-kde4-kio-rapip.xml
%{_iconsdir}/hicolor/*/apps/rapip.png
%{_iconsdir}/hicolor/*/apps/rapip_bw.png
