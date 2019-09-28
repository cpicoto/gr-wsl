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

* Enabling sound: follow these instructions
	* https://token2shell.com/howto/x410/enabling-sound-in-wsl-ubuntu-let-it-sing/
	* Use this version of pulseaudio http://bosmans.ch/pulseaudio/pulseaudio-1.1.zip
  * Make sure you have the pulseaudio daemon running and allowed on the firewall before attempting a connection from WSL
  * This will be attempted later using pavucontrol in the WSL 


* Launch Ubuntu app
  * Create your default username and password
	* First step upgrade to latest release
    * Check your release with: uname -a 
      * ex: 4.4.0-18362-Microsoft
		* Edit  /etc/update-manager/release-upgrades and change to Prompt=normal
		* Execute do-release-upgrade (this will upgrade to the latest normal release of your distro)

	* Edit /etc/pulse/client.conf
		Change the default-server line to: default-server = tcp:localhost

* Clone the gr-wsl repo and start the install script
  * cd ~
  * git clone https://github.com/cpicoto/gr-wsl
  * cd gr-wsl
  * ./install.sh  
  * Launch gnuradio-companion

* TODO
  * QTGui will fail without this:
    * /usr/lib/x86_64-linux-gnu$ ls -l libQt5Core.so.5
lrwxrwxrwx 1 root root 20 Jun 25 03:23 libQt5Core.so.5 -> libQt5Core.so.5.12.2
    * sudo strip --remove-section=.note.ABI-tag libQt5Core.so.5.12.2
    * Include a simple audio playback GRC to validate the setup

* Future Work
  * Considering publishing a dedicated gr-satellites distro with all this setup already done.



## Dependencies

You will need a Windows 10 PC including
  * Recommended Version 1903 (OS Build 18362.XXX)
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
