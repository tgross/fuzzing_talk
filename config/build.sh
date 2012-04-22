#!/bin/bash

workon fuzzing
export $FUZZING=~/whatever #fill in your working environment here

# force 32-bit execution in your virtual environment
cp $VIRTUAL_ENV/bin/python $VIRTUAL_ENV/bin/python.old
lipo -remove x86_64 $VIRTUAL_ENV/bin/python.old -output $VIRTUAL_ENV/bin/python

# get wxPython working
wget http://downloads.sourceforge.net/wxpython/wxPython2.8-osx-unicode-2.8.12.1-universal-py2.6.dmg
open wxPython2.8-osx-unicode-2.8.12.1-universal-py2.6.dmg

wget http://www.klake.org/~jt/misc/libdasm-1.5.tar.gz
tar -xf libdasm-1.5.tar.gz
cd ./libdasm-1.5/pydasm
python setup.py install

cd $FUZZING
wget http://pydot.googlecode.com/files/pydot-1.0.2.zip
unzip pydot-1.0.2.zip
cd pydot-1.0.2
python setup.py install

cd $FUZZING
wget http://downloads.sourceforge.net/project/mysql-python/mysql-python/1.2.2/MySQL-python-1.2.2.tar.gz

cd $FUZZING
wget http://www.informatik.uni-bremen.de/uDrawGraph/download/uDrawGraph-3.1.1-4-macosx-i386.tar.gz
tar -xf uDrawGraph-3.1.1-4-macosx-i386.tar.gz
cd uDrawGraph-3.1

# install and patch PaiMei
cd -
svn checkout http://paimei.googlecode.com/svn/trunk/ paimei-read-only
cd $FUZZING/paimei-read-only/pydbg
patch my_ctypes < $FUZZING/config/my_ctypes.patch
cd $FUZZING paimei-read-only/MacOSX/macdll
xcodebuild -target macdll -configuration debug

mkdir $VIRTUAL_ENV/lib/python2.6/site-packages/util
cp build/Debug/libmacdll.dylib $VIRTUAL_ENV/lib/python2.6/site-packages/util
cp build/Debug/libmacdll.dylib ../../pydbg/
cp build/Debug/libmacdll.dylib ../../console/
cd ..
chmod +x macsetup.sh
./macsetup.sh
cd ..
python setup.py install

# note that we don't really care about PaiMei for our purposes, which is good because it's a total pain in the ass to get running.
