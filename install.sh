#!/bin/bash
cd ~
mkdir -f ~/runtime-xdg
echo "export DISPLAY=127.0.0.1:0.0" >>~/.bashrc
echo "export PULSE_SERVER=tcp:127.0.0.1;" >>~/.bashrc
echo "export XDG_RUNTIME_DIR=~/runtime-xdg" >>~/.bashrc
echo Installing gnuradio on WSL
echo Enter your user password to execute sudo command:
sudo apt update
sudo apt upgrade 
sudo apt -y install make cmake git xterm python-pip synaptic swig doxygen direwolf libboost-all-dev libqt5widgets5 libqt5gui5 libqt5dbus5 libqt5network5 libqt5core5a pulseaudio-utils pavucontrol gnuradio
pip install construct requests
git clone https://github.com/daniestevez/gr-satellites
git clone https://github.com/daniestevez/gr-kiss
git clone https://github.com/daniestevez/libfec
git clone https://github.com/daniestevez/gr-csp
git clone https://github.com/bg2bhc/gr-lilacsat.git

cd ~/libfec
./configure
make
sudo make install
cd ~/gr-kiss
mkdir build
cd build
cmake ..
make
sudo make install
cd ~/gr-lilacsat
mkdir build
cd build
cmake ..
make
sudo make install
cd ~/gr-csp
mkdir build
cd build
cmake ..
make
sudo make install
cd ~/gr-satellites
mkdir build
cd build
cmake ..
make
sudo make install
sudo ldconfig
cd ..
./compile_hierarchical.sh

#Configure pulseaudio
#sudo echo "default-server = tcp:localhost" >>~/etc/pulse/client.conf





