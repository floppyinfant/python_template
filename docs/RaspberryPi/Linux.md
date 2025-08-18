# Linux
(A Short Primer)  

http://www.selflinux.org  
http://wiki.ubuntuusers.de
http://wiki.ubuntuusers.de/Shell/Befehls%C3%BCbersicht
http://wiki.ubuntuusers.de/Benutzer_und_Gruppen  
http://wiki.ubuntuusers.de/usermod  


Prompt:  
pi@raspberry ~ $  

Code completion:  
<Tab>  

History:  
Cursor_up/ -down  
```
history
```

Verzeichnisse:  
```
.               # current dir  
..              # parrent dir  
/               # root dir  
~, /home        # user dir  
$PATH  
set  
./befehl  
```

Ausgabe umlenken:  
```
|               # pipe output to another process
>               # redirect character stream to file
>>              # append character stream to file
```

```
sudo

# Anzeige von UID GID
id

# eigene Gruppenzugehörigkeit
groups
groups benutzer

# angemeldete Benutzer
w
who
whoami

# Benutzerverwaltung
useradd, usermod
groupadd, groupmod

# Debian spezifisch
adduser, deluser
addgroup, delgroup

# Bestehenden Benutzer einer weiteren Gruppe hinzufügen
sudo usermod -aG GRUPPENNAME BENUTZERNAME

# change owner
chown user.group file

chgrp group file

# Rechte setzen
chmod 755 *.txt
chmod a+x *.txt

# print working directory
pwd

# list files: -l as list, -a all (incl. hidden files)
ls -al

# disk free
df -h

# disk usage
du

# list open files
lsof

tar -xvzf *.tar.gz

# laufende prozesse(process status)
ps aux

top

htop

kill pid

killall

# X11 beenden
pkill x

# X11 starten (Desktop)
startx

hostname

ifconfig

uname -m

lscpu

free -h

cat /proc/meminfo

dmesg

tail -f /var/log/messages
```

```
# Raspbian (Debian Wheezy)
raspi-config

# rpi-update
sudo wget https://raw.github.com/Hexxeh/rpi-update/master/rpi-update -O /usr/bin/rpi-update
sudo chmod +x /usr/bin/rpi-update
sudo REPO_URI=https://github.com/notro/rpi-firmware rpi-update


# Boot...
sudo nano /boot/cmdline.txt
sudo nano /boot/config.txt
```

```
# System V init-Process
cat /etc/init.d/README | more

sudo nano /etc/default/<service>
sudo nano /etc/init.d/<service>

# service manuell starten
sudo /etc/init.d/<service> {status | start | stop}
sudo service <service> {start, restart}

# service als autostart
sudo update-rc.d <script> default
sudo update-rc.d <script> remove

# Prozess beenden
sudo killall <process>

# autostart
sudo nano /etc/rc.local

ls -l /etc/rc<x>.d

# /etc/inittab


# kernel module manuell laden
sudo modprobe spi-bcm2708

# kernel module automatisch laden
sudo nano /etc/modules
#ls -l /etc/modprobe.d
...

# kernel module ausschließen vom Laden
nano /etc/modprobe.d/raspi-blacklist.conf


# Bibliotheken in /usr/lib zum dynamischen linker hinzufügen
sudo ldconfig
```

---

# Shell  

In Linux ist alles eine Datei!  
(UNIX: everything is a file!)  
```
# root shell oder sudo benutzen, um GPIO zu nutzen!
sudo bash

# GPIO PIN
echo "25" > /sys/class/gpio/export
# Ausgabe
echo "out" > /sys/class/gpio/gpio25/direction
# Wert "0" oder "1" SENDEN
echo "1" > /sys/class/gpio/gpio25/value

sudo bash
echo "18" > /sys/class/gpio/export
# Eingabe
echo "in" > /sys/class/gpio/gpio18/direction
# Wert LESEN
cat /sys/class/gpio/gpio18/value

# Temperatur auslesen
cat /sys/class/thermal/thermal_zone0/temp
```

```
# Pi Cam
raspistill --help
raspivid --help
```
