# C / C++
<src: BOL>  

```
sudo apt-get install make gcc g++ cmake libx11-dev libxtst-dev
```


# WiringPi
http://wiringpi.com/
https://projects.drogon.net/raspberry-pi/wiringpi/
https://github.com/WiringPi/
https://github.com/WiringPi/WiringPi2-Python
http://elinux.org/Rpi_Low-level_peripherals/

Arduino-like Library to adress GPIO in C with Wrappers for Python, ...
does not need sudo to access GPIO


## Installation
```
git clone git://git.drogon.net/wiringPi
cd wiringPi
git pull origin             # fetch an updated version
./build
```


## Usage (Shell)
```
gpio -v
gpio readall

gpio -g mode 23 out         # -g für BCM-numbering
gpio -g write 23 1          # einschalten
gpio -g write 23 0          # ausschalten

gpio -g unexport 23         # PIN freigeben
gpio unexportall
```
