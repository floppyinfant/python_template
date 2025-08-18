# Python
```
sudo apt-get install python-dev python-setuptools python-pip
```

Adafruit Python Code
```
git clone http://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code.git
```

Adafruit WebIDE
http://learn.adafruit.com/webide/
```
sudo service adafruit-webide.sh {start,stop,restart}
```

iPython
```
sudo apt-get install ipython-notebook
```

Stani's Python Editor (SPE)
```
sudo apt-get install spe
```


## Modules (Library)
```
import sys
import time
import os
import os.path
import argparse
import webbrowser

from mcpi import minecraft

import pygame
from pygame.locals import *
import pygame.midi
#import pygame.mixer_music

import cwiid

import RPi.GPIO as GPIO
import wiringpi2

import picamera
from PIL import Image


with picamera.PiCamera() as camera:
    pass

wii = cwiid.Wiimote()

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)
GPIO.output(23, GPIO.HIGH)

mc = minecraft.Minecraft.create()
```

## RPi.GPIO
https://pypi.python.org/pypi/RPi.GPIO
sudo apt-get install python-rpi.gpio
sudo apt-get install python-dev

```
# Example: GPIO LED
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)          # GPIO-Bezeichnung verwenden, z.B. 'GPIO14'
# GPIO.setmode(GPIO.BOARD)      # PIN Nr. verwenden, z.B. '8'
GPIO.setup(23, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
try:
while(True):
    ### continous code here ###

    GPIO.output(23, True)       # True oder GPIO.HIGH
    GPIO.output(25, True)
    time.sleep(2)               # seconds
    GPIO.output(23, False)      # False oder GPIO.LOW
    GPIO.output(25, False)
    time.sleep(2)               # seconds

except KeyboardInterrupt:
    GPIO.cleanup()
```


## WiringPi-Wrapper
https://github.com/WiringPi/WiringPi2-Python
```
git clone https://github.com/Gadgetoid/WiringPi2-Python.git
cd WiringPi2-Python/
sudo python setup.py install
```

WiringPi Python Module
```
import wiringpi2

# For sequential pin numbering, one of these MUST be called before using IO functions
wiringpi2.wiringPiSetup() 
# OR
wiringpi2.wiringPiSetupSys() # For /sys/class/gpio with GPIO pin numbering
# OR
wiringpi2.wiringPiSetupGpio() # For GPIO pin numbering

wiringpi2.pinMode(6,1) # Set pin 6 to 1 ( OUTPUT )
wiringpi2.digitalWrite(6,1) # Write 1 ( HIGH ) to pin 6
wiringpi2.digitalRead(6) # Read pin 6
```

## Pygame
http://inventwithpython.com
https://github.com/notro/fbtft/wiki/Pygame


## Python Imaging Library (PIL)
sudo apt-get install python-imaging
sudo apt-get install python-imaging-tk


## PiCamera
http://picamera.readthedocs.org/en/release-1.3/
http://picamera.readthedocs.org/en/release-1.3/recipes1.html

```
import picamera

with picamera.PiCamera() as camera:
    camera.start_preview()
    time.sleep(2)               # Camera warm-up time
    camera.capture('foo.jpg')
```


## Py-SPIdev
```
git clone git://github.com/doceme/py-spidev
cd py-spidev
sudo python setup.py install
```


## cwiid - Wiimote Interface
http://www.theraspberrypiguy.com/raspberry-pi-how-to-use-a-wiimote/
https://github.com/abstrakraft/cwiid

The CWiid package contains the following parts:
1.libcwiid - wiimote API.
2.cwiid module - python interface to libcwiid
3.wmgui - GTK gui to the wiimote.
4.wminput - an event/joystick/mouse driver for the wiimote.
5.lswm - list wiimote devices (in the spirit of ls{,pci,usb}, etc.
6.wmdemo - a minimal demonstration of the libwiimote API. (not installed)

Requirements:
awk, bison, flex, bluez-libs, gtk+-2 dev libs, python 2.4 or greater, python dev for python module, uinput kernel support, kernel sources

Execution:
```
wmgui [-h] [bdaddr]
wminput [-h] [-c config] [bdaddr]
```

Python:
```
import cwiid
wii = cwiid.Wiimote()
```


## Minecraft
```
from mcpi import minecraft

mc = minecraft.Minecraft.create()
mc.postToChat("Hello world")
```
