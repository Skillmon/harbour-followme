%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __requires_exclude python\\(abi\\)
%global __provides_exclude application\\(

Name:		harbour-followme
Version:	0.5
Release:	1
Summary:	Follow manga and/or comics
License:	GPLv2+
Group:		Qt/Qt
URL:		https://github.com/alien999999999/harbour-followme
Source0:	%name-%version.tar.bz2
BuildArch:	noarch
Requires:	pyotherside-qml-plugin-python3-qt5 >= 1.3.0
Requires:	sailfishsilica-qt5
Requires:	libsailfishapp-launcher

%description

FollowMe is an app that allows to follow and read various manga and comics
from several sources. The app keeps record of what you have read and can
download them in the background.

%prep
%setup -q

%build

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/86x86/apps %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/%{name}/translations
install %{name}.png %{buildroot}%{_datadir}/icons/hicolor/86x86/apps
install %{name}.desktop %{buildroot}%{_datadir}/applications
install %{name}.svg %{buildroot}%{_datadir}/%{name}
cp -R qml python translations %{buildroot}%{_datadir}/%{name}/

desktop-file-install --delete-original --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*.desktop

%files
%defattr(-,root,root,-)
%{_datadir}/icons/hicolor/86x86/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}
