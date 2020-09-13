#!/bin/bash
cd ~
mkdir ~/runtime-xdg
echo "export DISPLAY=$(cat /etc/resolv.conf | grep nameserver | awk '{print $2; exit;}'):0.0" >>~/.bashrc
echo "export PULSE_SERVER=$(cat /etc/resolv.conf | grep nameserver | awk '{print $2; exit;}')" >>~/.bashrc
echo "export XDG_RUNTIME_DIR=~/runtime-xdg" >>~/.bashrc
echo Installing gnuradio on WSL2
echo Enter your user password to execute sudo command:
sudo apt update
sudo apt upgrade 
sudo apt -y install make cmake git xterm python-pip synaptic swig doxygen gr-osmosdr pkg-config libpulse-dev qt5-default libqt5svg5-dev sudo apt install direwolf libboost-all-dev libqt5widgets5 libqt5gui5 libqt5dbus5 libqt5network5 libqt5core5a pulseaudio-utils pavucontrol liborc-0.4-dev
pip3 install construct requests
git clone https://github.com/daniestevez/gr-satellites
git clone https://github.com/daniestevez/gr-kiss
git clone https://github.com/daniestevez/libfec
git clone https://github.com/daniestevez/gr-csp
git clone https://github.com/bg2bhc/gr-lilacsat.git
#git clone https://github.com/csete/gqrx.git

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
#cd ~/gqrx
#mkdir build
#cd build
#cmake ..
#make
#sudo make install


#Graphics QT won't work in WSL if the next line fails
#sudo strip --remove-section=.note.ABI-tag /usr/lib/x86_64-linux-gnu/libQt5Core.so.5.1*

#Configure pulseaudio
#sudo echo "default-server = tcp:localhost" >>~/etc/pulse/client.conf





