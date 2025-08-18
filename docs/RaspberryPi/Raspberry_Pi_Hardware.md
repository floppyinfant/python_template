# Raspberry Pi Hardware

## Raspberry Pi Model A

1x USB 2.0
256 MB SDRAM
Leistungsaufnahme max. 500mAh (2,5W)


## Raspberry Pi Model B Rev. 2

Architektur: ARMv6 (ARM11-Familie)
CPU: 700 MHz
GPU: Broadcom Dual Core VideoCore IV, OpenGL-ES 1.1/2.0, Full HD 1080p60
RAM: 512 MB
System-on-a-Chip (SoC): Broadcom BCM2835
SD-Card Reader
Konektivität: HDMI, RCA | FBAS | composite, analog Audio (3,5mm klinke), 2x USB 2.0, Ethernet
Leistungsaufnahme max. 700mAh (3,5 W) bei 5V
GPIO: 26 PIN


## Raspberry Pi 1 Model B+

Architektur: ARMv6 (ARM11-Familie)
CPU: 700 MHz
GPU: Broadcom Dual Core VideoCore IV, OpenGL-ES 1.1/2.0, Full HD 1080p60
RAM: 512 MB
SoC: Broadcom BCM2835
4x USB 2.0
Micro-SD-Card
GPIO: 40 PIN


## Raspberry Pi 2 Model B

Architektur: ARMv7 (32 Bit), Familie ARM-Cortex-A, Typ ARM-Cortex-A7
CPU: 4 Kerne 900 MHz
RAM: 1 GB
SoC: Broadcom BCM2836
4x USB 2.0
Leistungsaufnahme idle: 1,4 W
Leistungsaufnahme Last: 2,4 W
Leistungsaufnahme max. 800mAh (4W) bei 5V
Micro-SD-Card
GPIO: 40 PIN



## Raspberry Pi 3 Model B

Architektur: ARMv8 (64 Bit), Familie ARM-Cortex-A, Typ ARM-Cortex-A53
CPU: 4 Kerne 1200 MHz
RAM: 1 GB
SoC: Broadcom BCM2837
Broadcom BCM43143
2,4GHz WLAN b/g/n,
Bluetooth 4.1 Low Energy
4x USB 2.0
Leistungsaufnahme max. 800mAh (4W) bei 5V
Micro-SD-Card
GPIO: 40 PIN


## Raspberry Pi 4 Model B
## Raspberry Pi 5 Model B
## Raspberry Pi 0
## Raspberry Pi 0 Version 2

---

# Interfaces

P1 GPIO (General Purpose Input Output), 26 PINs, 17 I/O-PINs total
http://de.wikipedia.org/wiki/GPIO
8 digital I/O-PINs, one as PWM out
2 I2C
5 SPI (mit 1,8 kOhm Pull-up Widerstand auf 3,3V)
2 serial UART
3.3V, max. 50mAh (in Summe aller GPIO-PINs)
5V-PIN ist direkt mit dem USB-Port verbunden: liefert ca. 300mAh bei Verwendung eines 1A Netzteils (-700mAh Stromverbrauch des RPi; 3,5 Watt)


UART (Universal Asynchronous Receiver Transmitter), 2-wire
RS-232Serielle Schnittstelle
FTDITTLUSB-RS232-Serial Adapter
http://de.wikipedia.org/wiki/UART
http://de.wikipedia.org/wiki/Logikpegel
Rx
Tx


I2C (Inter Integrated Circuits), 2-wire, TWI (Two-wire-interface)
http://de.wikipedia.org/wiki/I%C2%B2C
SCL (Takt)
SDA (Datenleitung)


SPI (Serial Peripheral Interface), 4-wire with 2nd select line (total 5 PINs)
http://de.wikipedia.org/wiki/Serial_Peripheral_Interface
MOSI (Master Out Slave In) = SDO (Serial Data Out)
MISO (Master In Slave Out) = SDI (Serial Data In)
SCLK (Serial Clock)
CE0
CE1


1-Wire
http://de.wikipedia.org/wiki/1-Wire


PWM (Pulse Width Modulation)
http://de.wikipedia.org/wiki/Pulsweitenmodulation
PPM (Pulse Position Modulation) for controlling servo motors


DAC (Digital Analaog Converter)
ADC (Analog Digital Converter)


DSI (DisplaySerial Interface)
CSI (Camera Serial Interface)


CAN
Automobilindustrie
http://de.wikipedia.org/wiki/Controller_Area_Network


P5 auxilliary GPIO connector on Rev. 2 Boards (muss selbst gelötet werden), 8 PINs


General Purpose Input Output (GPIO)
http://elinux.org/Rpi_Low-level_peripherals
http://de.wikipedia.org/wiki/Raspberry_Pi#GPIO


Case
Netzteil 5V, 1A (micro-USB)
USB-Lade-Kabel Handy mit Netzstecker
Transcend SDHC 16GB (class-10), 20MB/s read, 11MB/s write
Edimax WLAN USB-Adapter 150MBit/s IEEE802.11b/g/n

Rii Keyboard Bluetooth (25€)
Logitec K400 Keyboard, Funk (30€)

Sundtek USB DVB-T Receiver | SkyTV Ultimate DVB-S/S2-Receiver


Kamera Modul 5MP (27,99€)
stills capture mode (2592×1944), aspect ratio 4:3
video mode (1920x1080p), aspect ratio 16:9
video mode (640×480 60.1-90fps), up to VGAp90 binned
@see 
5 megapixel native resolution sensor capable of 2592 x 1944 pixel static images.
Supports 1080p30, 720p60 and 640X480p60/90 video.

Kamera NoIR (33,90€)
Adafruit PiTFT Mini Kit, 320x240 2,8" Touchscreen (45,95€)
LCD-Touch-Display 2,8" 320x240 (QVGA) (53€)


Adafruit
Pi T Cobbler Breakout Kit (11,95€)
Breadboard Steckbrett Experimentierboard 830 Kontakte (7,95€)
Drahtbrücken 65 Stk. (3,15€)
Widerstandsset (4,59€)
LED kreativ-Set (8,43€)

USB-TTL-Kabel für Debugging

---

