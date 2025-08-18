# PiTFT
https://www.adafruit.com/products/1601  

2.8" display with 320x240 16-bit color pixels and a resistive touch overlay.  
The plate uses the high speed SPI interface.  

This design uses the hardware SPI pins (SCK, MOSI, MISO, CE0, CE1) as well as GPIO #25 and #24.  
All other GPIO are unused.  
4 spots for optional slim tactile switches: GPIO #23, #22, #21, and #18  


## Assembly
https://learn.adafruit.com/adafruit-pitft-28-inch-resistive-touchscreen-display-raspberry-pi  


## Projects
https://learn.adafruit.com/diy-wifi-raspberry-pi-touch-cam  
https://github.com/notro/fbtft-spindle/wiki/FBTFT-image#adafruit-camera-app  
https://learn.adafruit.com/snappicam-raspberry-pi-camera  
https://learn.adafruit.com/touchscreen-pi-timelapse-controller  
https://learn.adafruit.com/cupcade-raspberry-pi-micro-mini-arcade-game-cabinet  


# FBTFT  
https://github.com/notro/fbtft/wiki  
https://github.com/notro/fbtft/wiki/Framebuffer-use  
https://github.com/notro/fbtft/wiki/LCD-Shields  
https://github.com/notro/fbtft-spindle/wiki/FBTFT-image  

 
## Calibration of Touch Screen  
https://github.com/notro/fbtft-spindle/wiki/FBTFT-image#touchpanel-calibration  
```
sudo ts_calibrate
# Test tslib
sudo ts_test
```

## Console  
Map console 1 to framebuffer 1, login screen will show up on the display  
```
con2fbmap 1 1
con2fbmap 1
$ console 1 is mapped to framebuffer 1

# Revert (to HDMI)
con2fbmap 1 0

# do it permanently: remove fbcon=map from /boot/cmdline.txt
```

## Framebuffer Mirroring (fbcp - Framebuffer copy)  
https://github.com/notro/fbtft/wiki/Framebuffer-use#framebuffer-mirroring  
https://github.com/notro/fbtft-spindle/wiki/FBTFT-image#fbcp---framebuffer-copy  
install fbcp  
load drivers  
We need to switch the console to fb0 first:  
```
con2fbmap 1 0

# start fbcp
fbcp &

# stop fbcp
killall fbcp

# syslog output
tail /var/log/messages

# start service
sudo service fbcp start

# stop service
sudo service fbcp stop

# Enable automatic startup
# remove from /boot/cmdline.txt: fbcon=map:10
sudo update-rc.d fbcp defaults

# Disable automatic startup
sudo update-rc.d fbcp remove
```

## X windows multiseat  
X windows on both HDMI and the LCD  
https://github.com/notro/fbtft-spindle/wiki/Appendix#x-windows-multiseat  
```
# Play Movies
omxplayer big_buck_bunny_480p_surround-fix.avi

mplayer -nolirc -vo fbdev2:/dev/fb1 -vf scale=320:-3 test.mpg

# Image Viewer
sudo fbi -d /dev/fb1 -T 1 -noverbose -a Mystery-100x100.jpg

sudo fbi -vt 2 -d /dev/fb1 -noverbose -autozoom adapiluv320x240.jpg
```

## INSTALL Adafruit PiTFT  
https://learn.adafruit.com/adafruit-pitft-28-inch-resistive-touchscreen-display-raspberry-pi/software-installation  
https://github.com/notro/fbtft/wiki/LCD-Shields  

Download Raspbian-Image first:  
http://adafruit-download.s3.amazonaws.com/2014-01-07-wheezy-raspbian-2014-03-12-fbtft-pitft.zip  

Wiki zum Image (Betriebssystem Raspbian mit integrierten Kernel Modulen):  
https://github.com/notro/fbtft-spindle/wiki/FBTFT-image  

```
cd ~
wget http://adafruit-download.s3.amazonaws.com/libraspberrypi-bin-adafruit.deb 
wget http://adafruit-download.s3.amazonaws.com/libraspberrypi-dev-adafruit.deb 
wget http://adafruit-download.s3.amazonaws.com/libraspberrypi-doc-adafruit.deb 
wget http://adafruit-download.s3.amazonaws.com/libraspberrypi0-adafruit.deb 
wget http://adafruit-download.s3.amazonaws.com/raspberrypi-bootloader-adafruit-112613.deb
# optional DMA-enabled-kernel (beta release)
wget http://adafruit-download.s3.amazonaws.com/raspberrypi-bootloader-adafruit-20140421-3.deb

sudo dpkg -i -B *.deb
```

If you have a version of Raspbian more recent than Sept. 2013, you'll need to turn off the accelerated X framebuffer here, run  
```
sudo mv /usr/share/X11/xorg.conf.d/99-fbturbo.conf ~
```
to remove the accelerated X buffer and save it in your home directory  

```
sudo shutdown -h now
```
(if you don't have the TFT installed, shutdown, place the TFT on the Pi and re-power)  


## Test
```
sudo modprobe spi-bcm2708
sudo modprobe fbtft_device name=adafruitts rotate=90
export FRAMEBUFFER=/dev/fb1 
startx
```
Hit Control-C in the console to quit the X server.  


## Autostart
We'll now make the modules auto-load. Lets edit the /etc/modules list with  
```
sudo nano /etc/modules
```
add two lines:  
```
spi-bcm2708
fbtft_device
```

```
sudo nano /etc/modprobe.d/adafruit.conf
```
add the following line:  
```
options fbtft_device name=adafruitts rotate=90 frequency=32000000
```

```
sudo reboot
```
and look at the console output (or run dmesg in the console window after logging in)  
you will see the modules install.  
Look in particular for the STMPE610 detection and the ILI9340 screen frequency.  


set up the touchscreen for rotate=90 configuration:  
```
sudo mkdir /etc/X11/xorg.conf.d
sudo nano /etc/X11/xorg.conf.d/99-calibration.conf
```
add lines:  
```
Section "InputClass"
        Identifier      "calibration"
        MatchProduct    "stmpe-ts"
        Option  "Calibration"   "3800 200 200 3800"
        Option  "SwapAxes"      "1"
EndSection
```

## Test
```
FRAMEBUFFER=/dev/fb1 startx
# Type Control-C to quit X
```
If you don't ever want to have to type FRAMEBUFFER=/dev/fb1 before startx, you can make it a default state by editing your profile file:  
```
sudo nano ~/.profile
# add line near the top
export FRAMEBUFFER=/dev/fb1
```

NEXT is touch screen calibration  
https://learn.adafruit.com/adafruit-pitft-28-inch-resistive-touchscreen-display-raspberry-pi/touchscreen-install-and-calibrate  

---

http://www.freetronics.com/pages/oled128-quickstart-guide-raspberry-pi#.U4JmFJ_elD  
(This is a simplified version of the Install steps on the fbtft wiki.)  

```
sudo wget https://raw.github.com/Hexxeh/rpi-update/master/rpi-update -O /usr/bin/rpi-update
sudo chmod +x /usr/bin/rpi-update
sudo REPO_URI=https://github.com/notro/rpi-firmware rpi-update

sudo reboot

sudo REPO_URI=https://github.com/notro/rpi-firmware rpi-update

sudo modprobe spi-bcm2708
sudo modprobe fbtft_device name=freetronicsoled128

FRAMEBUFFER=/dev/fb1 startx

# Use Ctrl-C from the console you loaded startx from in order to close the X session.
```

Create a file .xinitrc in our home directory containing only one line of content: the one x-application you want to start  
```
/usr/bin/xeyes
```
Then “startx” will display the xeyes app full screen and nothing else (note that this applies to -all- X sessions, including any on /dev/fb0 ie the main TV output!)  

```
mencoder big_buck_bunny_480p_stereo.ogg -vf scale=-3:128,crop=128:128 -ovc x264 -nosound -o big_buck_bunny_128.avi

mplayer -nolirc -vo fbdev2:/dev/fb1 big_buck_bunny_128x128.avi

fbi -d /dev/fb1 -T 1 -noverbose -a Mystery-100x100.jpg

con2fbmap 1 1
```

Choosing a smaller font:  
```
sudo setfont -C /dev/console Uni3-Terminus12x6.psf
```

If you want your console output back on the main output fb0, run  
```
con2fbmap 1 0
```
