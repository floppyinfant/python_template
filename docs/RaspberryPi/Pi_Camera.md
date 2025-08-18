# Camera Module

## Hardware  
Kamera Modul 5MP (27,99€)  
stills capture mode (2592×1944), aspect ratio 4:3  
video mode (1920x1080p), aspect ratio 16:9  
video mode (640×480 60.1-90fps), up to VGAp90 binned  
http://www.raspberrypi.org/new-camera-mode-released/  
5 megapixel native resolution sensor capable of 2592 x 1944 pixel static images.  
Supports 1080p30, 720p60 and 640X480p60/90 video.  
  
Kamera NoIR (33,90€)  
Adafruit PiTFT Mini Kit, 320x240 2,8" Touchscreen (45,95€)  


## Literatur  
Foto und Video mit Raspberry Pi: Gesichtserkennung, Focus Stacking, Zeitrafferaufnahmen, Highspeed-Fotos und selbst gebaute Digicam: 20 Projekte mit dem Camera Module  


## Projekte  
http://en.wikipedia.org/wiki/Category:Photographic_techniques  
http://en.wikipedia.org/wiki/Category:Animation_techniques  
http://en.wikipedia.org/wiki/Category:Stop_motion  

High-Speed-Video  

Timelapse | Zeitraffer  

Langzeitbelichtung  
http://en.wikipedia.org/wiki/Light_writing   
http://en.wikipedia.org/wiki/Persistence_of_vision  

Naturfotographie  

Foto-Falle  

Bewegungsmelder  

Nightwatch  

IR-Fotographie  

Makro-Fotographie  

Focus-Stacking  

High-Dynamic-Range (HDR)  

Panoramafotographie  

Landschaftsfotographie  

Portrait-Fotographie  

Gesichtserkennung  

Mustererkennung  

OpenCV  

Webcam mit Motorsteuerung  

Webcam streamen:  
fswebcam  
RPiWebCamInterface  


# RPi Camera | Kamera Modul 5MP  
http://www.raspberrypi.org/help/camera-module-setup/  
stills capture mode (2592×1944), aspect ratio 4:3  
video mode (1920x1080p), aspect ratio 16:9  
http://www.raspberrypi.org/new-camera-mode-released/  
video modes 1080p30, 720p60 and 640X480p60/90  
http://elinux.org/Rpi_Camera_Module  
```
sudo apt-get update
sudo apt-get dist-upgrade
sudo rpi-update                        # update firmware: installs the new modes
```

## ERRORS
Error:  
mmal_vc_component_enable  

http://www.gtkdb.de/index_36_2502.html  
https://github.com/raspberrypi/linux/issues/435  
(disable 1-wire in /etc/modules)  


Error:  
mmal: mmal_vc_component_create: failed to create component 'vc.ril.camera' (1:ENOMEM)  
mmal: mmal_component_create_core: could not create component 'vc.ril.camera' (1)  
mmal: Failed to create camera component  
mmal: main: Failed to create camera component  
mmal: Camera is not detected. Please check carefully the camera module is installed correctly  


## Bash  
http://www.raspberrypi.org/documentation/usage/camera/raspicam/README.md  

### Aufnahme  
```
raspivid -w 640 -h 480 -fps 90 -t 10000 -o test90fps.h264
raspistill -t 2000 -o image.jpg
raspistillyuv
```

### Wiedergabe von Videos  
```
omxplayer
```
```
sudo apt-get install  mplayer mencoder  ffmpeg
mplayer -vo fbdev2:/dev/fb1 -x 240 -y 320 -framedrop video.mp4
```
http://www.ffmpeg.org/  
http://www.mplayerhq.hu/  
http://www.mplayerhq.hu/DOCS/HTML/de/mencoder.html  

### Convert | Box in MP4-Container Format  
```
sudo apt-get install gpac
MP4Box -add filename.h264 filename.mp4
```

VLC Player, fswebcam, MJPEG-Streamer  
s.u.  

ALSA Audio:  
s. MediaCenter  

---

### Wiedergabe von Bildern  
```
sudo apt-get install fbi
sudo apt-get install  fim  
sudo apt-get install  pqiv  
sudo apt-get install  links2

# Usage of fbi (frame buffer image - works without X-Window):
sudo fbi -T 2 -d /dev/fb1 -noverbose -a image.jpg

# Usage of ...:
pquiv -f ...
links2 -g ...
```

---

### ImageMagick  
http://www.imagemagick.org/Usage/basics/  
```
sudo apt-get install imagemagick  

# Usage:
display
animate
convert :show
identify
mogrify
composite
montage
compare
stream
import
conjure
```

---

### Timelapse  
http://www.raspberrypi.org/documentation/usage/camera/raspicam/timelapse.md  


### Stop-Motion Video aus Einzelbildern erstellen  
```
sudo apt-get install libav-tools

avconv -i image_%04d.jpg -r 10 -vcodec libx264 -crf 20 -g 15 timelapse.mp4
```

### Slow-Motion (High-Speed Camera)  
```
raspivid -w 640 -h 480 -fps 90 -t 5000 -o slowmo.h264
```

---

### Python PiCamera
http://www.raspberrypi.org/documentation/usage/camera/python-picamera.md  
http://picamera.readthedocs.org/en/release-1.3/  
```
sudo apt-get install python-picamera
```

---

### RPi_Cam_Web_Interface (RaspiMJPEG)  
http://www.raspberrypi.org/forums/viewtopic.php?f=43&t=63276  

Installation  
```
git clone https://github.com/silvanmelchior/RPi_Cam_Web_Interface.git
cd RPi_Cam_Web_Interface
chmod u+x RPi_Cam_Web_Interface_Installer.sh
./RPi_Cam_Web_Interface_Installer.sh install
```
browse to the URL of your Pi  
needed to start apache2 and RPi_Cam manualy after install:  
```
sudo /etc/init.d/apache2 start
./RPi_Cam_Web_Interface_Installer.sh  start

# Camera freigeben für raspistill | raspivid
./RPi_Cam_Web_Interface_Installer.sh  autostart_no | autostart_yes
./RPi_Cam_Web_Interface_Installer.sh  start | stop
./RPi_Cam_Web_Interface_Installer.sh  remove  
#  Die folgenden Pakete werden ENTFERNT:
#   apache2 gpac libapache2-mod-php5 motion php5
# !!! Deinstalliert ALLE Dateien in /var/www !!!
```
```
sudo killall raspimjpeg     # stop
sudo /etc/rc.local          # start
```
```
# Updates
cd  RPi_Cam_Web_Interface
git pull origin master
./RPi_Cam_Web_Interface_Installer.sh  install
```

---

### MAKE Raspberry Eye (Remote Servo Cam)  
http://makezine.com/projects/raspberry-eye-remote-servo-cam/  
http://sourceforge.net/projects/mjpg-streamer/  

---

### fswebcam  
http://www.firestorm.cx/fswebcam/  

---

## Android Software  
Pi Sight (Android)  
RaspiCam Remote (Android)  
