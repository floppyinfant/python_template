# Media Center
HTPC (Home Theather Personal Computer), Wohnzimmer Computer  
http://de.wikipedia.org/wiki/Mediacenter  

# Kodi (ehemals XBMC)
http://kodi.wiki/view/Raspberry_Pi  

# XBMC
http://wiki.xbmc.org  
http://wiki.xbmc.org/index.php?title=Raspberry_Pi/FAQ#Installing_XBMC_on_the_Raspberry_Pi  
http://www.raspbian.org/RaspbianXBMC  


# Installation unter Raspbian
http://michael.gorven.za.net/raspberrypi/xbmc  
Add repository  
```
sudo nano /etc/apt/sources.list.d/mene.list
# deb http://archive.mene.za.net/raspbian wheezy contrib

# Import signing-key
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-key 5243CDED

# Install
sudo apt-get update
sudo apt-get install kodi

# Add user to groups: audio video input dialout plugdev tty
# Gruppenzugehörigkeit anzeigen
id
groups
# Create group, if it does not exist
addgroup --system input
# Bestehenden Benutzer einer weiteren Gruppe hinzufügen (mehrere Gruppen mit Komma, aber ohne Leerzeichen trennen); Option '-aG' ist wichtig, sonst werden alle bestehenden Gruppenzugehörigkeiten gelöscht und alleine durch die angegebenen ersetzt!
# sudo usermod -aG GRUPPENNAME BENUTZERNAME
sudo usermod -aG   audio,video,input,dialout,plugdev,tty pi

# grant ownership to input devices
sudo nano /etc/udev/rules.d/99-input.rules
# SUBSYSTEM=="input", GROUP="input", MODE="0660"
# KERNEL=="tty[0-9]*", GROUP="tty", MODE="0660"

# set gpu-memory split: GPU >96MB RAM
sudo nano /boot/config.txt
# gpu_mem=128
```

```
# Run Kodi
kodi-standalone

# enable autostart
sudo nano   /etc/default/kodi
#   ENABLED=1

# Test autostart
sudo service kodi start

# Usage
# Taste 'c' für Context-Menu
```


# OpenELEC
http://www.openelec.tv  
name: root  
pass: openelec  

Es gibt kein 'apt-get'; System ist klein und schnell - es läßt nur innerhalb Kodi verändern!  


Configuration:  
System > Dateimanager > Quelle hinzufügen  
"SuperRepo", http://srp.nu  

System > Addons > weitere Addons > OpenELEC Mediacenter OS-Addons > Addon Verzeichnis > Unofficial OpenELEC Mediacenter Addons  
aktivieren  

System > Addons > weitere Addons > OpenELEC Mediacenter OS-Addons > Dienste  
boblightd, sundtek-mediatv, vdr-addon  

System > Addons > weitere Addons > Unofficial OpenELEC Addons > Dienste  
tvheadend, mpd, vnc, ftp  

System > Addons > weitere Addons > Unofficial OpenELEC Addons >   Addon Bibliotheken  
RPi.GPIO, picamera  

System > Addons > weitere Addons > Unofficial OpenELEC Addons >   Programm Addons  
w_scan  

System > Addons > weitere Addons > Kodi Addon Repository > Dienste  
XBMC Boblight  

System > Addons > weitere Addons > Kodi Addon Repository > Programm Addons  
X-Note (Evernote)  


# RaspBMC
http://www.raspbmc.com  
```
sudo initctl stop xbmc  
sudo initctl start xbmc  

sudo initctl enable xbmc  
sudo initctl disable xbmc  
```
Server   aktivieren unter Menü:  
Programme > RaspBMC Settings > System Configuration > Service Management  

SSH  
FTP  
Samba (Windows Freigabe '\\RASPBMC\', Linux 'smb://')  
VNC (raspbmc:0)  
Remote Control  
TVHeadend (Port 9981)  
SABnzbd (Port 8088)  
Deluge client (Port 8112)  
Boblight Support  
Cronjob Scheduler  


# OSMC - Open Source Media Center
(ehemals RaspBMC)  
https://osmc.tv/   
```
sudo systemctl start mediacenter
sudo systemctl stop mediacenter
```
prevent kodi from starting on boot  
```
sudo systemctl disable mediacenter
sudo systemctl enable mediacenter
```


# Xbian
http://www.xbian.org/  

based on Debian  
SSH standardmäßig aktiviert:  
Config startet automatisch bei login  

user:   xbian  
passwd: raspberry  


# Alternative Distributionen:

LinuxMCE, MythBuntu (jeweils mit MythTV)  
MediaPortal (win32)  
Apple Front Row  
Microsoft Windows XP Media Center Edition (MCE)  
Windows Media Center (WMC) in   Windows 7  

---

# Remote Controls
HDMI-CEC  
Android YATSE  
Android XBMC Remote  
GPIO IR-Receiver  

# Bilder

# Diashows

# Bonjour/ Avahi/ Zeroconf
```
sudo apt-get install avahi-daemon
```
Domain:  
raspberrypi.local  

# NAS
http://kodi.wiki/view/File_sharing  

Samba: SMB (Server Message Block), CIFS (Common Internet File System) (Windows File Sharing)  
AFP (Apple Filing Protocol)  
NFS (UNIX Network File System)  
FTP  
SFTP (SSH FileTransfer Protocol)  
iSCSI  
WebDAV  
UPnP, DLNA  

# FreeNAS
http://www.freenas.org/  

mount  
http://wiki.ubuntuusers.de/mount  
usage:  
```
sudo mount -t <type> -o <options> <file-system> <mount-point>
sudo mount -t ntfs -o uid=1000,gid=046,umask=0027,nls=utf8,auto,users /dev/sda1 /media/MYBOOK
```

parameter 'type':  
ext, ext2, ext3, ext4, reiserfs  
nfs  
iso9660 (für CDs), udf (für DVDs)  
vfat (=FAT32), NTFS  


alle Geräte der Datei /etc/fstab ohne die Option 'noauto' einhängen  
```
mount -a
```

# fstab
http://wiki.ubuntuusers.de/fstab  

UUID anzeigen  
```
sudo blkid
# /dev/sda1: LABEL="MYBOOK" UUID="206A63706A634220" TYPE="ntfs"

sudo nano /etc/fstab
# <file system> <mount point> <type> <options> <dump> <pass>
# UUID=206A63706A634220   /media/MYBOOK ntfs   defaults
# ,username=pi,password=raspberry

# Beispiele von ubuntuusers:
# /dev/sdb1           /media/exthdd ntfs     rw,user,noauto,uid=0,gid=46,umask=007,nls=utf8 0 0
# /dev/sda5           /media/daten    vfat     rw,auto,user,umask=0000                            0             0

# fstab erneut einlesen
sudo mount -a
```

# NTFS-3G
FUSE  
http://wiki.ubuntuusers.de/Windows-Partitionen_einbinden/NTFS-3G?redirect=no  
http://www.tuxera.com/community/ntfs-3g-manual  

# Samba
SMB, CIFS  
https://www.samba.org/  
http://kodi.wiki/view/Samba  
http://wiki.ubuntuusers.de/Samba  
http://www.openframeworks.cc/setup/raspberrypi/Raspberry-Pi-SMB.html  

Installation:  
```
sudo apt-get install samba samba-common-bin
```

Configuration:  
```
sudo smbpasswd -a pi # set passwd 'raspberry'

sudo nano /etc/samba/smb.conf
```

Restart Samba-Server:  
```
sudo /etc/init.d/samba restart
# or
sudo service smdb restart
# or
sudo smbd restart
```
mount using 'smb://raspberrypi.local/Data'  
Windows Freigabe: '\\RASPBMC\'  

# Video Library
http://kodi.wiki/view/Adding_videos_to_the_library  
http://kodi.wiki/view/Media_sources  
http://kodi.wiki/view/Types_of_Media_Sources  

---

# PVR (Persönlicher Video Recorder)
DVR (Digital Video Recorder)  
Festplattenrekorder  
http://en.wikipedia.org/wiki/Comparison_of_PVR_software_packages  

Features:  
EPG (Electronic Programe Guide), Elektronische Programm-Zeitschrift  
XMLTV  
Timeshifting, zeitversetztes Fernsehen  

Standards:  
DVB-T (Terrestrian)  
DVB-S (Satellite)  
DVB-S2  
DVB-C (Cable)  
HD+  
V4L (Analog Video)  


# MPEG-2 Lizenz zur Wiedergabe von DVB-Streams
Seriennummer auslesen:  
```
cat /proc/cpuinfo | grep Serial
# Serial                    : 00000000c4adb50b
```
Lizenzen kaufen (ca. 5€):  
http://www.raspberrypi.com/mpeg-2-license-key/  

Lizenzen eintragen in /flash/config.txt (FAT-Partition)  
decode_MPG2=0x2b28fe11  
decode_WVC1=  

Pruefen, ob das Decoding aktiv ist  
```
vcgencmd codec_enabled MPG2
vcgencmd codec_enabled WVC1
```

---

# MythTV
Digital Video Recorder (DVR)  

# TVHeadend
TV Streaming Client zum Aufzeichnen  
https://tvheadend.org/projects/tvheadend/wiki/download  
https://tvheadend.org/projects/tvheadend/wiki  
http://kodi.wiki/view/HTS_Tvheadend  
http://wiki.ubuntuusers.de/Tvheadend  

Installation:  
```
sudo nano   /etc/apt/sources.list
# add repository:
#   deb http://apt.tvheadend.org/stable wheezy main

# import GPG signing key
curl http://apt.tvheadend.org/repo.gpg.key | sudo apt-key add -

sudo apt-get update
sudo apt-get install tvheadend

# Benutzer hts genügend Rechte zuweisen, um auf die TV-Karte zugreifen zu können
sudo adduser hts video

# PVR add-on in Kodi installieren
sudo apt-get install   kodi-pvr-tvheadend-hts
```

Administration über Browser:  
http://raspbmc:9981  

Streaming Protokoll  
Port 9982 - HTSP server (Streaming protocol)  
```
sudo service tvheadend stop
```

Clients  
https://tvheadend.org/projects/tvheadend/wiki/Clients  

XBMC  
Showtime  
TVHGuide (Android)  
TvhClient (iPhone)  
pidvbip (Raspberry Pi)  
VLC HTSP Plugin  
Linux VDR  
Kaffein  

---

# DVB-S/ S2
## Sundtek SkyTV Ultimate IV 2014 (DVB-S/ S2)

benötigt eine MPEG-2 Lizenz zur Wiedergabe des DVB-Streams!  
http://sundtek.com/shop/Digital-TV-Sticks/Sundtek-SkyTV-Ultimate-IV-2015-DVB-S/S2.html  
http://support.sundtek.com/index.php/topic,341.0.html  
http://support.sundtek.com/index.php/board,21.0.html  

Linux Installation  
http://support.sundtek.com/index.php/topic,341.msg1670.html  
Treiber Download und News  
http://support.sundtek.com/index.php/topic,1573.0.html  
Treiber Board  
http://support.sundtek.com/index.php/board,6.0.html  

Installation:  
```
wget http://www.sundtek.de/media/sundtek_netinst.sh
chmod 777 sundtek_netinst.sh
sudo ./sundtek_netinst.sh
```

Configuration for Raspberry Pi:  
```
sudo nano /etc/sundtek.conf
# ir_disabled=1
# use_hwpidfilter=on

# Disable Remote control polling:
/opt/bin/mediaclient --disablerc=/dev/mediainput0

# Hardware PID-Filter einschalten:
/opt/bin/mediaclient -P on -d /dev/dvb/adapter0/frontend0
# Die PID Filter übernehmen die Demux Filter
# welche man in /opt/bin/mediaclient --lc bei den Applikationen sieht.
# Dadurch wird der CPU Verbrauch gesenkt.
# Besonders geeignet für Raspberry PI und andere schwächere Systeme.
# Unter Linux profitiert vor allem VDR von den Filtern.
```

Usage:  
```
# list media hardware devices
/opt/bin/mediaclient -e
#   
# Anzeigen welche Applikationen mit dem Treiber verbunden sind: list media clients
/opt/bin/mediaclient --lc

# DVB-S(2) via Netzwerk:
/opt/bin/mediaclient --enablenetwork=on
/opt/bin/mediaclient --scan-network
/opt/bin/mediaclient --mount=127.0.0.1:0

# channels.conf für Linux VDR erstellen:
w_scan -f s -s S19E2 -o 7

# channels.conf für VLC erstellen:
w_scan -X -c DE -f s -s S19E2 >> channels.conf.vlc
```

Programme:  
Kaffeine  
Linux VDR  
tvtime  
```
tvtime -d /dev/video1   
```
mplayer  
XawTV  

Clients für Smartphone:  
TVHclient  
XBMC  

VLC (über Browser aufrufbar mit Mozilla plugin)  


# Online TV Recorder (OTR)
Internet Videorecorder  

---

# IPTV
multicast UDP/RTP  
unicast HTTP MPEG1/2 transport streams  
HTTP with h264 video stream  

Dt. Telekom Entertain (40€ - 50€)  
Vodafone TV (40€ - 45€)  


# WebTV
Zatoo  

# Video-On-Demand (VoD)

# Podcasts
http://de.wikipedia.org/wiki/Kategorie:Video-on-Demand  
http://de.wikipedia.org/wiki/Kategorie:Internetfernsehen  


# Online Videotheken
Maxdome  
Videoload  
Watchever  
Lovefilm  

Amazon Prime, Amazon instant video  
iTunes  


# Video-Portale
YouTube  
Vimeo  
MyVideo  

---

# Sat>IP
Sat-over-IP  

# HbbTV
Red-Button  

# Media Server
Streaming  

Protokolle:  
RTSP  
UDP  
HTTP  

# DLNA
UPnP (Universal Plug and Play)  
upnp://  

# AirPlay

# Miracast (ab Android 4.2)

# AppleTV (ATV2)

# WiDi (Intel)

---

# Mediathek
Internet-TV  

# Podcasts

# Audio Streaming
iTunes (AirPlay, Bonjour = Zeroconf/ Avahi-Daemon)  

Clouds:  
Spotify  
Google Play Music  
SoundCloud  

# Internet-Radio
Radio-Streams:  
Last.fm  
tunein.com  

---

# Mopidy
includes Mpd  

Pi MusicBox  
Distribution basiert auf Mopidy mit Mpd  

load the IPv6 kernel module now  
```
sudo modprobe ipv6
# add ipv6 to /etc/modules to ensure the IPv6 kernel module is loaded on boot
echo ipv6 | sudo tee -a /etc/modules
```

since I have a HDMI cable connected, but want the sound on the analog sound connector, I have to run  
```
sudo amixer cset numid=3 1
```
to force it to use analog output. 1 means analog, 0 means auto, and is the default, while 2 means HDMI.  

you can test sound output independent of Mopidy by running  
```
aplay /usr/share/sounds/alsa/Front_Center.wav
```
to make the change to analog output stick, you can add the amixer command to e.g. /etc/rc.local, which will be executed when the system is booting  


Installation  
https://docs.mopidy.com/en/latest/installation/debian/#debian-install  
```
wget -q -O - https://apt.mopidy.com/mopidy.gpg | sudo apt-key add -
sudo nano   /etc/apt/sources.list.d/mopidy.list
#   # Mopidy APT archive
# deb http://apt.mopidy.com/ stable main contrib non-free
# deb-src http://apt.mopidy.com/ stable main contrib non-free
sudo apt-get update
sudo apt-get install mopidy
```

Extensions  
https://docs.mopidy.com/en/latest/#ext  

To list all the extensions available from apt.mopidy.com, you can run:  
```
apt-cache search mopidy

sudo apt-get install mopidy-spotify
```
or install from PyPI:  
```
pip search mopidy
```

Configuration  
https://docs.mopidy.com/en/latest/config/  

print out configuration values  
```
mopidy config
```
diable extension without uninstalling:  
mopidy.conf  
```
[spotify]
enabled = false
```
```
nano   ~/.config/mopidy/mopidy.conf
```
mopidy.conf  
```
[mpd]
hostname = ::

[spotify]
username = alice
password = mysecret
```

run Mopidy:  
https://docs.mopidy.com/en/latest/running/  
https://docs.mopidy.com/en/latest/command/#mopidy-cmd  
```
mopidy
```
run Mopidy as a system service, automatically starting at boot:  
https://docs.mopidy.com/en/latest/debian/  

stop Mopidy:  
Ctrl + c  
or:  
```
pkill mopidy
```

plugins:  
SpotiMC  


# Mpd (Music Player Daemon)
ct 14 (16.06.2014), "Hier spielt die Musik", S. 154  
http://www.musicpd.org/doc/user/  
```
man mpd.conf
```

Mpd installieren  
```
sudo apt-get install mpd mpc
# weitere tools installieren
# sudo apt-get install alsa-base alsa-utils lame mplayer

# Audio Treiber laden (RPi1):
sudo modprobe snd_bcm2835

# Permanente Aktivierung des Treibers
sudo nano /etc/modules
#   snd_bcm2835

# Audio-Ausgang auswählen: '1' für Klinkenbuchse, '0' für HDMI
sudo amixer cset numid=3 1
# Einstellung dauerhaft speichern
sudo alsactl store


# Konfigurationsdatei
sudo nano /etc/mpd.conf

music_directory    "/home/pi/music"
bind_to_adress     "any"
audio_output {
        type "httpd"
        ...
}

# Mpd nach Änderung der Konfiguration neu starten
sudo /etc/init.d/mpd restart


# Frontend für die Kommandozeile
sudo apt-get install mpc

# Songdatenbank neu aufbauen
mpc update

# alle Songs der Musikbibliothek ausgeben
mpc listall

# Playlist erstellen: use grep u.a.
mpc ls | mpc add

# Abspielen
mpc play

# Hilfe
mpc <tab>
```

GUI Frontends:  
Gmpc (Gnome Music Player Client)  
MPDroid (Streaming Client für Android)  
mpd.wikia.com/wiki/Clients  


# Mopidy/ MPD clients

Console:  
mpc  

GUI:  
GMPC  
http://gmpc.wikia.com/  
Sonata  
http://sonata.berlios.de/  

Web:  
Rompr  
http://sourceforge.net/projects/rompr/  
http://sourceforge.net/p/rompr/wiki/Installation/  

Android:  
MPDroid  

---

# ALSA
Audio Treiber installieren (Alternativen: PulseAudio, Jack)  
```
sudo apt-get install alsa-base alsa-utils
#
# Treiber laden
sudo modprobe snd_bcm2835
#
Treiber beim Systemstart automatisch laden
sudo nano /etc/modules
# snd_bcm2835 # in neue Zeile hinzufügen
#
# Audio-Ausgabe über die Klinkenbuchse
sudo amixer cset numid=3 1 # 1: Klinkenbuchse; 0: HDMI
sudo alsactl store
```

# PulseAudio
http://dbader.org/blog/crackle-free-audio-on-the-raspberry-pi-with-mpd-and-pulseaudio  

# JACK

# OSS

---

# Wetter
# Clock
# Calendar

# PIM
# Social Networks

---

# Boblight
Adalight  
Ambilight (Philips)  
AtmoLight (VLC Filter)  
Insanelight (RPi)  
AmbiTV  

LPD8806 LED-Strips  
@see Raspberry Pi LED  


Boblight  
https://code.google.com/p/boblight/  
http://wiki.xbmc.org/index.php?title=Add-on:XBMC_Boblight  
http://www.forum-raspberrypi.de/Thread-ambilight-fuer-xbmc-nachruesten  

Adalight  
http://www.adafruit.com/products/461  

Sedu Ambilight  
http://www.sedu-board.de/  
http://www.sedu-board.de/sedu-ambilight/vorstellung-sedu-ambilight-mit-sedustripes/  

Insanelight  
http://www.insanelight.de/  

AmbiTV  
https://github.com/gkaindl/ambi-tv  

---

# Spiele, Games
Arcade, Retro  

Spiele (ROMs):  
Atari | Activision:  
Pitfall, Donkey Kong, Frogger, Space Invaders  

Amiga:  
Lucas Arts: Monkey Island  

GameBoy:  
Tetris, Gargoyles Quest  


# PiPlay | PiMAME
http://pimame.org/  


# RetroPie
http://blog.petrockblock.com/retropie/  

Setup  
http://blog.petrockblock.com/2012/07/22/retropie-setup-an-initialization-script-for-retroarch-on-the-raspberry-pi/  
https://github.com/petrockblog/RetroPie-Setup  
```
sudo apt-get update
sudo apt-get install -y git dialog
#
git clone git://github.com/petrockblog/RetroPie-Setup.git
#
cd RetroPie-Setup
chmod +x retropie_setup.sh
sudo ./retropie_setup.sh
```

get ROMs from Internet:  
MAME Roms must be in a ZIP Archive, names all lower case, chmod a+rw  
copy ROMs to ~/RetroPie/roms/...  
copy Amiga kick.rom to /opt/retropie/emulators/uae4all/  
copy NeoGeo BIOS to   /opt/retropie/emulators/gngeo-0.7/neogeo-bios/  
copy Intellivision BIOS files to /usr/local/share/jzintv/rom  

Start RetroPie  
```
emulationstation
```

# Minecraft
http://www.raspberrypi.org/learning/getting-started-with-minecraft-pi/  
http://pi.minecraft.net/  
http://www.stuffaboutcode.com/p/minecraft.html  
https://github.com/brooksc/mcpipy  
```
sudo apt-get install minecraft-pi
```
start minecraft from Desktop  
release Mouse with Tab-key  
open IDLE (not IDLE3)  

Display a message inside the running minecraft game  
```
from mcpi import minecraft
mc = minecraft.Minecraft.create()
mc.postToChat("Hello world")
```

Usage of game  
Use the mouse to look around and use the following keys on the keyboard:  

Key                       Action  
W                         Forward  
A                         Left  
S                         Down  
D                         Right  
E                         Inventory  
Space                     Jump  
Double Space              Fly / Fall  
Esc                       Pause / Game menu  
Tab                       Release mouse cursor  

You can select an item from the quick draw panel with the mouse's scroll wheel (or use the numbers on your keyboard), or press E and select something from the inventory.  

# MAME
https://code.google.com/p/mame4all-pi/  
http://mamedev.org/  
https://github.com/notro/fbtft/wiki/MAME  
https://learn.adafruit.com/cupcade-raspberry-pi-micro-mini-arcade-game-cabinet/overview  

Setup:  
get 'ClrMAME Pro' to convert romsets to MAME 0.37b5 from   http://mamedev.emulab.it/clrmamepro/   using 'clrmame.dat' file  
get sound samples from      http://dl.openhandhelds.org/cgi-bin/gp2x.cgi?0,0,0,0,5,2511  
copy sound samples to ...  
get artwork from   http://dl.openhandhelds.org/cgi-bin/gp2x.cgi?0,0,0,0,5,2512  
copy art to ...  

KEYBOARD  
Keys LControl, LAlt, Space, LShift are the fire buttons  
Cursors Keys for up, down, left and right  
Keys 1 & 2 to start 1 or 2 player games  
Keys 5 & 6 Insert credits for 1P or 2P  
Key Escape to quit  
Key TAB to bring up the MAME menu  
Function Keys: F11 show fps, F10 toggle throttle, F5 cheats, Shift F11 show profiler  
Key P to pause  
NOTE: To type OK when MAME requires it with the joystick, press LEFT and then RIGHT  
 
# ScummVM

Emulator für Lucas Arts Adventures wie Monkey Island, Indianer Jones, Maniac Manson etc.  

Installieren:  
```
sudo apt-get install scummvm
```

Ausführen:  
```
/usr/games/scummvm
```

Infos  
http://www.scummvm.org   > Documentation > Game datafiles  
#kostenlose Spiele unter > Games  


# Stella
ATARI 2600 VCS  
http://stella.sourceforge.net/  

ROMs  
https://atariage.com/2600/emulation/index.php?SystemID=2600  

# WinUAE
Amiga Forever  


# FastDOSBox
MS-DOS Emulator  
Download kostenpflichtig über Pi-Store  

Grafische Oberfläche beenden  
```
pkill x
```

Ausführen  
```
/usr/local/bin/indiecity/InstalledApps/fastdosbox/Full/fastdosbox-1.5/fastdosbox <dir_with_exe-files>
```
---

# Wiimote
http://www.theraspberrypiguy.com/raspberry-pi-how-to-use-a-wiimote/  
https://github.com/petrockblog/RetroPie-Setup/wiki/Wiimotes-with-classic-controllers  

Installation:  
```
sudo apt-get install bluetooth python-cwiid wminput   bluez-utils blueman   vorbis-tools

sudo service bluetooth status

git clone https://github.com/the-raspberry-pi-guy/Wiimote.git
cd Wiimote/Example
# Testprogramm
python wiimote.py
# Home-Button gedrückt halten, um 3D-Koordinaten anzuzeigen
Strg+c
```

Das Programm wminput  
```
sudo apt-get install wminput
sudo modprobe uinput
sudo wminput
# Maus läßt sich mit der Wiimote bedienen
```

# RetroPie GPIO-Adapter
http://blog.petrockblock.com/2012/10/21/the-retropie-gpio-adapter/  

