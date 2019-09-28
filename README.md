# gr-wsl
GNU Radio Setup for WSL (Windows Subsystem for Linux)

This is a collection of installation scripts and instructions to run GNU Radio based applications for Linux 
inside WSL.

After a successful setup you will be able to use gr-satellites to decode satellite telemetry and contribute to the Satnogs database.

## Installation

### How to setup gr-satellites to decode telemetry from SatnogsTracker using Windows Subsystem for Linux (WSL)


* Configure WSL following these instructions https://docs.microsoft.com/en-us/windows/wsl/install-win10
  * Basically says to enable the feature from a Powershell Windows as Administrator
      Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux

* If you want to use graphical based features from GNU radio you need an X Server application running on your Windows PC
  This is an optional requirment if you only need to use command line. 
  * I use X410 (https://token2shell.com/x410/) from the Microsoft Store
        https://www.microsoft.com/en-us/p/x410/9nlp712zmn9q?activetab=pivot:overviewtab
  * Launch X410 from your Start Menu or type X410 on the Search Box
  
* On Windows 10, go the Microsoft Store and download a Linux distribution 
  * I am using Ubuntu for this install 
        https://www.microsoft.com/en-us/p/ubuntu/9nblggh4msv6?activetab=pivot:overviewtab

* 
* Launch Debian after configuring WSL
	* Edit /etc/apt/sources.list
	* Insert this new line at the top ```deb http://ftp.us.debian.org/debian sid main```
	* ```
		sudo apt update
		sudo apt upgrade  --> This will take sometime
	    sudo apt install make cmake git xterm python-pip synaptic swig doxygen direwolf
		pip install construct requests
	    sudo synaptic```
	* Select gnuradio and gnuradio-dev >= 3.7.13.4 and apply changes to Install
	```
	cd ~
	git clone https://github.com/daniestevez/gr-satellites
	git clone https://github.com/daniestevez/gr-kiss
	git clone https://github.com/daniestevez/libfec
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
	```



## Dependencies

You will need a Windows 10 PC including
  * Recommended Version 1903 (OS Build 18362.356)
  * PC should have Soundcard and Internet Connection
  * It will use Windows Subsystem for Linux (WSL)
  * X Server application for Windows 
      (there are multiple free versions but X410 from the Windows Store is recommended)
  * pulseaudio for windows to play back audio comming from wsl
  * An SDR receiver for decoding realtime transmitions or IQ files.
  * An SDR Application for Windows that can transmit demodulated audio over UDP
    * I use SDR# v1.0.0.1715 with the SatNogs Tracker Plugin
    * https://github.com/cpicoto/SatNogsTracker
  

## Credits and References

* gr-satellites by Dani Estevez available at https://github.com/daniestevez/gr-satellites
* Scott Chapman @scott23192 (K4KDR) his twitter feed and GRC files at https://www.qsl.net/k/k4kdr//grc/
* Microsoft for WSL https://docs.microsoft.com/en-us/windows/wsl/install-win10

## About the author
* Carlos Picoto (cpicoto@hotmail.com) is an Ham Radio enthusiast and Software Engineer with the callsigns AD7NP and CT1DYE.
