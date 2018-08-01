PACKAGE_ONE=$1
PKG_OK=$(dpkg-query -W --showformat='${Status}\n' $1|grep "install ok installed")
echo Checking for $1: $PKG_OK
if [ "" == "$PKG_OK" ]; then
  echo "$1 not installed, attempting to set up $1."
  sudo apt-get --force-yes --yes install $1
fi
