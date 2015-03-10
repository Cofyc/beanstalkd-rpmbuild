Name: beanstalkd
Version: 1.10
Release: 1%{?dist}
Summary: beanstalkd 1.10

Group: Applications/Databases
License: MIT
URL: https://github.com/kr/beanstalkd
Source0: %{name}-%{version}.tar.gz
Source1: %{name}.service

BuildRequires: gcc
Requires: gcc

%description


%prep
%setup -q

%build
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} PREFIX=/usr
%{__install} -p -D -m 0755 %{SOURCE1} %{buildroot}/etc/systemd/system/%{name}.service
mkdir -p %{buildroot}/var/lib/%{name}

%pre
if [ $1 == 1 ]; then
    /usr/sbin/groupadd -f %{name}
    /usr/sbin/useradd -r -g %{name} %{name} -s /sbin/nologin 2> /dev/null
fi

%post
if [ $1 == 1 ]; then
    systemctl daemon-reload
    systemctl stop %{name}
fi

%preun
if [ $1 == 0 ];then
    /usr/sbin/userdel -r %{name} 2> /dev/null
    systemctl stop %{name}
fi
%postun

%clean
#rm -rf %{buildroot}

%files
%defattr(-,%{name},%{name},0755)
/var/lib/%{name}
%attr(0644,root,root) /etc/systemd/system/%{name}.service
%attr(0755,root,root) /usr/bin/%{name}

%doc

%changelog
