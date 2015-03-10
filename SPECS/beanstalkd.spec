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
make install DESTDIR=%{buildroot}
%{__install} -p -D -m 0755 %{SOURCE1} %{buildroot}/etc/systemd/system/%{name}.service

%pre
if [ $1 == 1 ];then
    /usr/sbin/useradd -r %{name} -g %{name} -s /sbin/nologin 2> /dev/null
fi
mkdir /var/lib/beanstalkd

%post

%preun
if [ $1 == 0 ];then
    /usr/sbin/userdel -r %{name} 2> /dev/null
    systemctl stop %{name}
fi
%postun

%clean
rm -rf %{buildroot}

%files
%attr(0755,root,root) /etc/systemd/system/%{name}.service
%attr(0755,beanstalkd,beanstalkd) /var/lib/%{name}

%doc


%changelog

