# beanstalkd rpmbuild

## Create an RPM Build Environment

```
yum install rpmdevtools
rpmdev-setuptree
```

## Install Prerequisites for RPM Creation

```
yum groupinstall 'Development Tools'
```

## Setup

```
echo '%_topdir        /home/vagrant/rpmbuild' > ~/.rpmmacros
```

## Build the RPM

```
./build.sh
```

## References

- http://www.centoscn.com/image-text/config/2014/1201/4215.html
