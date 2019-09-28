#!/bin/bash
echo Installing gnuradio on WSL
echo Enter your user passwprd to execute sudo command:
cd ~
sudo apt update
sudo apt upgrade 
sudo apt install make cmake git xterm python-pip synaptic swig doxygen direwolf libboost-all-dev libqt5widgets5 libqt5gui5 libqt5dbus5 libqt5network5 libqt5core5a
pip install construct requests
git clone https://github.com/daniestevez/gr-satellites
git clone https://github.com/daniestevez/gr-kiss
git clone https://github.com/daniestevez/libfec
git clone https://github.com/daniestevez/gr-csp
git clone https://github.com/bg2bhc/gr-lilacsat.git

cd libfec
./configure
make
sudo make install
cd ..
cd gr-kiss
mkdir build
cd build
cmake ..
make
sudo make install
cd ../..
cd gr-satellites
mkdir build
cd build
cmake ..
make
sudo make install
sudo ldconfig
cd ..
./compile_hierarchical.sh
cd ../gr-csp
mkdir build
cd build
cmake ..
make
sudo make install
cd ../..
cd gr-lilacsat
mkdir build
cd build
cmake ..
make
sudo make install



