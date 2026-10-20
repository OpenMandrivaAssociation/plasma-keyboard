%define plasmaver %(echo %{version} |cut -d. -f1-3)
%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)

Summary:	Virtual keyboard for Plasma
Name:		plasma-keyboard
Version:	6.8.1
Release:	1
License:	LGPLv2+
Group:		Graphical desktop/KDE
URL:		https://invent.kde.org/plasma/plasma-keyboard
Source0:	http://download.kde.org/%{stable}/plasma/%{plasmaver}/%{name}-%{version}.tar.xz

BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Qml)
BuildRequires:	cmake(Qt6VirtualKeyboard)
BuildRequires:	cmake(Qt6WaylandClient)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6KCMUtils)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(PlasmaQuick)
BuildRequires:	pkgconfig(xkbcommon)
BuildRequires:	pkgconfig(wayland-client)
BuildRequires:	cmake(Wayland)
BuildRequires:	cmake(WaylandScanner)
BuildRequires:	cmake(Qt6WaylandScannerTools)
BuildRequires:	pkgconfig(wayland-protocols)

BuildSystem:	cmake
BuildOption:	-DBUILD_TESTING:BOOL=OFF
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

Requires:	%mklibname Qt6VirtualKeyboard

%description
A virtual keyboard based on Qt Virtual Keyboard, designed to integrate
with Plasma via the Wayland input-method-v1 protocol.

%files -f %{name}.lang
%{_bindir}/plasma-keyboard
%{_datadir}/applications/org.kde.plasma.keyboard.desktop
%{_datadir}/applications/kcm_plasmakeyboard.desktop
%{_datadir}/metainfo/org.kde.plasma.keyboard.metainfo.xml
%{_datadir}/plasma/keyboard
%{_datadir}/config.kcfg/plasmakeyboardsettings.kcfg
%{_qtdir}/qml/org/kde/plasma/keyboard
%{_qtdir}/qml/QtQuick/VirtualKeyboard
%{_qtdir}/plugins/plasma/kcms/systemsettings/kcm_plasmakeyboard.so
