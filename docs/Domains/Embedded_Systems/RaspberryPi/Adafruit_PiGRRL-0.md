# Adafruit PiGRRL-zero 
<src: BOL>  

https://learn.adafruit.com/pigrrl-zero/overview  
https://learn.adafruit.com/pigrrl-zero/software-manual-1  

- Pi0  
- TFT-Display  
- D-Pad + Shoulder-Buttons  
- LiPo-Accu + Charging-Device  
- 3D-printed case  

### Mods  
- Pi Zero W (with Wifi and Bluetooth)
- HDMI-Output  
- Pi Camera 5MP  
- Sound: i2S and 3W Amp + 0,8W Speaker  
- UART or MIDI 3,5mm Jack  
- Patchbox OS with RT-Kernel, (pd, MODEP, Jack), Hotspot / Wifi-Access-Point (AP)  
- Keyboard via Bluetooth (Rii-Clever) setup with Desktop Tools (Toolbar)  


## Basic Setup  

Get Patchbox OS  
https://blokas.io/patchbox-os/  

connect  
- via Ethernet
- USB-to-TTL-Serial-Cable
- WLAN (wpa_supplicant.conf needed)  
- use scp (WinSCP) to copy files
- Putty as a terminal for **SSH**

```
ssh patch@retropie.local

passwd
# change default passwords

sudo raspi-config
# Raspbian | Raspberry Pi OS config-tool:
# /boot/config.txt
# overclock
# camera, audio, ...

sudo patchbox
# Blokas Patchbox OS config-tool:
# audio, RT-Kernel
```

## Desktop
```
startx
# Desktop "PIXEL" >> Einstellungen, Taskbar, Toolbar (Wifi-Symbol, Audio)
# X11 beenden über Menü oder via SSH | Alt+F1-6: ... kill <seat> ... ???
```

## Network  
```
ifconfig
ifconfig wlan0
sudo iwlist wlan0 scan
# /dev/eth0
# Hotspot
# /dev/wlan0
# /etc/wpa_supplicant/wpa_supplicant.conf
wpa_passphrase "testing" < file_where_password_is_stored
wpa_passphrase "ssid" >> /etc/wpa_supplicant/wpa_supplicant.conf
wpa_cli -i wlan0 reconfigure
```

## Bluetooth for QWERTY-Keyboard  
```
# use the tools on the Desktop Toolbar
```

## Manual Setup  
use a USB-Hub with Ethernet and a PC with Putty, WinSCP (to copy Scripts, ROMs) or use Samba (ROMs only)  

manual installation:  
https://learn.adafruit.com/pigrrl-zero/software-manual-1  

download:  
https://github.com/adafruit/Raspberry-Pi-Installer-Scripts  

Install RetroPie  
https://retropie.org.uk/download/  

## Adafruit PiTFT  
```
sudo bash pitft-fbcp.sh
```

## Overclock  
```
sudo nano /boot/config.txt
# insert at end of file:
gpu_mem=44
disable_audio_dither=1
overscan_scale=1
#gpu_mem_256=128
#gpu_mem_512=256
#gpu_mem_1024=256
dtoverlay=pitft22,rotate=270,speed=60000000,fps=40
display_rotate=0
hdmi_cvt=320 240 60 1 0 0 0
arm_freq=1000
core_freq=500
sdram_freq=450
over_voltage=6
```

## Adafruit Retrogame (Button support)  
```
sudo bash retrogame.sh
# edit the file /boot/retrogame.cfg to match the PINs used
# (the wiring changed to preserve the I2S-Pins for audio)
```

## Configure Controller (RetroPie)  
Emulationstation  
```
# press whatever key was assigned to the “Start” button to access the main menu. You’ll find an option here for “CONFIGURE INPUT”
```

## Audio (I2S)  
https://learn.adafruit.com/adafruit-max98357-i2s-class-d-mono-amp  
```
# Adafruit Setup-Script:
sudo bash i2samp.sh
reboot 			# reboot twice!
alsamixer

# manual detailed installation:
sudo nano /etc/modprobe.d/raspi-blacklist.conf
# comment out:
#blacklist i2c-bcm2708
#blacklist snd-soc-pcm512x
#blacklist snd-soc-wm8804

# Disable headphone audio (if it's set)
sudo nano /etc/modules
# comment out:
#snd_bcm2835

# Add Device Tree Overlay
sudo nano /boot/config.txt
# comment out:
#dtparam=audio=on
# add:
dtoverlay=hifiberry-dac
dtoverlay=i2s-mmap

# Create asound.conf file
sudo nano /etc/asound.conf
```
```
pcm.speakerbonnet {
   type hw card 0
}
pcm.dmixer {
   type dmix
   ipc_key 1024
   ipc_perm 0666
   slave {
     pcm "speakerbonnet"
     period_time 0
     period_size 1024
     buffer_size 8192
     rate 44100
     channels 2
   }
}
ctl.dmixer {
    type hw card 0
}
pcm.softvol {
    type softvol
    slave.pcm "dmixer"
    control.name "PCM"
    control.card 0
}
ctl.softvol {
    type hw card 0
}
pcm.!default {
    type             plug
    slave.pcm       "softvol"
}
```
```
# Speaker Tests
# noise Test
speaker-test -c2
# Wav Test
speaker-test -c2 --test=wav -w /usr/share/sounds/alsa/Front_Center.wav
# mp3 Test
sudo apt-get install -y mpg123
mpg123 http://ice1.somafm.com/u80s-128-mp3


# Reducing popping:
sudo nano /boot/config.txt
# add (done @see above):
dtoverlay=i2s-mmap

sudo nano /etc/asound.conf
# @see: https://learn.adafruit.com/adafruit-max98357-i2s-class-d-mono-amp/pi-i2s-tweaks
# https://alsa.opensrc.org/How_to_use_softvol_to_control_the_master_volume
# Add software volume control:
nano ~/.asoundrc
# @see <link above>
reboot
speaker-test -c2 --test=wav -w /usr/share/sounds/alsa/Front_Center.wav
reboot
alsamixer
# Just press the up and down arrows to set the volume, and ESC to quit

# Hardware: If SD is connected to ground directly (voltage is under 0.16V) then the amp is shut down
```

## HDMI-Output  
using Adapter-cable from Mini-HDMI to HDMI  

## Camera  
Pi Camera (5MP) with Adapter-Cable for Pi0 (smaller pitch)  


# References  
https://learn.adafruit.com/pigrrl-zero/software-manual-1  

Pi0  
https://learn.adafruit.com/adafruits-raspberry-pi-lesson-5-using-a-console-cable/overview  
https://www.adafruit.com/product/3400  
https://de.pinout.xyz/pinout/pin7_gpio4  

PiGRRL-zero Advance  
https://www.threedprintspace.com/software  
https://www.thingiverse.com/thing:2126383  
https://www.stuffaboutcode.com/2016/01/pocket-pigrrl-battery-monitor.html  

GPi-case (safe-shutdown script)  
https://support.retroflag.com/  
https://github.com/RetroFlag/retroflag-picase  
https://recalbox.gitbook.io/documentation/basic-manual/getting-started/preparation-and-installation-of-recalbox/retroflag-gpi-case  

PiBoy DMG  
https://www.experimentalpi.com/  

Adafruit  
https://learn.adafruit.com/running-opengl-based-games-and-emulators-on-adafruit-pitft-displays  
https://github.com/adafruit/Adafruit-Retrogame/blob/master/configs/retrogame.cfg.zero  
https://learn.adafruit.com/adafruit-max98357-i2s-class-d-mono-amp  

Patchbox OS (RT-Kernel)  
https://blokas.io/patchbox-os/docs/first-run-options/  

Retro Gaming / RetroPie Distro  
https://retropie.org.uk/  

Edit /boot/config.txt  
https://www.raspberrypi.org/documentation/computers/configuration.html  

Wifi: wpa_supplicant.conf  
https://manpages.debian.org/testing/wpasupplicant/wpa_supplicant.conf.5.en.html  
https://www.linuxbabe.com/ubuntu/connect-to-wi-fi-from-terminal-on-ubuntu-18-04-19-04-with-wpa-supplicant  

Camera (5MP)  
https://www.adafruit.com/product/1367  
https://picamera.readthedocs.io/en/release-1.13/  
