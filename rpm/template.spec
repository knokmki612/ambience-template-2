Name:       ambience-template

Summary:    Template ambience
Version:    0.0.1
Release:    1
Group:      System/GUI/Other
License:    TBD
Source0:    %{name}-%{version}.tar.bz2
BuildArch:      noarch
BuildRequires:  qt5-qttools
BuildRequires:  qt5-qttools-linguist
BuildRequires:  qt5-qmake

Requires:   ambienced
Requires:   sailfish-version >= 2.0.0

%description
This is a template ambience description

%prep
%setup -q -n %{name}-%{version}

%build

%qmake5

make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%qmake5_install

%post
systemctl-user restart ambienced.service

%postun
systemctl-user restart ambienced.service

%files
%defattr(-,root,root,-)
%{_datadir}/ambience/template/
