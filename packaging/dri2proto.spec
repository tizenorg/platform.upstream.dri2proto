Name:     dri2proto
Summary:  X.Org X11 Protocol dri2proto
Version:  2.8
Release:  1
Group:    Development/System
License:  MIT
URL:      http://www.x.org
Source0:  %{name}-%{version}.tar.bz2

BuildRequires: pkgconfig
BuildRequires: pkgconfig(xorg-macros)

%description
%{summary}

%prep
%setup -q

%build

%configure --disable-static \
             --libdir=%{_datadir} \
             --without-xmlto

make %{?jobs:-j%jobs}

%install
%make_install

%remove_docs

%files
%license COPYING
%defattr(-,root,root,-)
%{_includedir}/X11/extensions/*.h
%{_datadir}/pkgconfig/*.pc
