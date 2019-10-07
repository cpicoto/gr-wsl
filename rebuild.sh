#!/bin/bash
cd ~
mkdir ~/runtime-xdg
echo Enter your user password to execute sudo command:
sudo apt update
sudo apt upgrade 

cd ~/libfec
git pull
./configure
make clean
make
sudo make install
cd ~/gr-kiss
git pull
mkdir build
cd build
cmake ..
make clean
make
sudo make install
cd ~/gr-lilacsat
git pull
mkdir build
cd build
cmake ..
make clean
make
sudo make install
cd ~/gr-csp
git pull
mkdir build
cd build
cmake ..
make clean
make
sudo make install
cd ~/gr-satellites
git pull
mkdir build
cd build
cmake ..
make clean
make
sudo make install
sudo ldconfig
cd ..
./compile_hierarchical.sh

#Graphics QT won't work in WSL if the next line fails
sudo strip --remove-section=.note.ABI-tag /usr/lib/x86_64-linux-gnu/libQt5Core.so.5.1*






