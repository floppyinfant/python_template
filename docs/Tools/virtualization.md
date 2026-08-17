# Virtualization

- @see Google Docs: Administration
- https://en.wikipedia.org/wiki/Comparison_of_platform_virtualization_software
- https://en.wikipedia.org/wiki/List_of_emulators 


## Type-1 Hypervisors

Synonym: bare-metal hypervisors

nutzen Hardware-Virtualisierungsfunktionen (Intel VT-x oder AMD-V) der CPU

- Proxmox VE (Virtual Environment)
- Microsoft Hyper-V
- KVM (mit Qemu)
- VMware ESXi
- Broadcom vSphere Hypervisor

## Type-2 Hypervisors: Virtual Machines hosted on OS

- VMware (Player, Workstation Pro, Fusion on Mac)
- Virtual Box
- Qemu
- Parallels on Mac
- DOSBox
- DOSEMU
- Win4Lin

---

## Compatibility Layer

- https://en.wikipedia.org/wiki/Compatibility_layer 

### WSL2

Windows Subsystem for Linux

BIOS/UEFI Settings: Intel VT-x, VT-d, AMD-V

- @see docs/Tools/wsl.txt

```bash
# installation in Administrator PowerShell [?]
wsl --install -d Ubuntu
wsl --install Ubuntu-22.04 --web-download
wsl --distribution Ubuntu-22.04

# usage
wsl --list --online

wsl -l -v
wsl --list --verbose

wsl
sudo apt update
sudo apt install neofetch mc sl

# Programming with VScode Remote Development Extension
mkdir myproject
cd myproject
code .		# starts Windows VScode

# access windows filesystem
cd /mnt/c/

# access linux files in Windows Explorer
explorer.exe .

# access linux filesystem from Windows Powershell
cd \\wsl.localhost\Ubuntu
cd \\wsl$\docker-desktop-data\mnt\wsl\docker-desktop-data\data

# execute commands from Windows Powershell in WSL
wsl -d Ubuntu -e bash -c "cat /etc/os-release"

wsl --terminate
wsl --shutdown
wsl --update
wsl --export Ubuntu <pfad\ubuntu.tar.gz>
```

Linux Systeminformationen
- https://wiki.ubuntuusers.de/Systeminformationen_ermitteln/ 
- https://wiki.ubuntuusers.de/Skripte/Basheinzeiler/ 
- https://wiki.ubuntuusers.de/Shell/Befehls%C3%BCbersicht/ 
- https://wiki.ubuntuusers.de/Shell/ 
- https://wiki.ubuntuusers.de/Programmierung/ (awk, etc.)

```bash
neofetch
htop
sudo lshw -short
lscpu
cat /proc/cpuinfo
free -m		# RAM
cat /proc/meminfo
sudo dmidecode -t memory
sudo dmidecode -t bios
sudo dmidecode -t system
lsblk
df -h
sudo fdisk -l
mount
du -hs .		# belegter Festplattenplatz
du -hT		# freier Festplattenplatz
lspci			# sudo apt install pciutils
lspci -t		# tree view
lspci -v		# verbose
lspci -vv
lspci | grep -i 'eth'
ip addr
ethtool ens33
ifconfig -a
netstat -a
lsusb			# sudo apt install usbutils
lsusb -v
cat /etc/os-release
lsb_release -a
cat /etc/lsb-release 
cat /etc/issue
cat /proc/version
uname -a
uname -r
ps -ef
top
htop
sudo lshw
sudo lshw -short
sudo lshw -html > lshw-info.html
hostname
date
whoami
id -u			# user-id; default 1000
id -g			# group-id
# cat /sys/class/...
hwinfo
cpu-x			# GUI-Tool
lsmod			# geladene Kernel Module
sudo dmesg | tail 
watch 'sudo dmesg | tail'
sudo dmesg -w 
```

---

## Container

@see docs/Tools/docker.txt

Docker
- Docker Desktop (on Windows uses WSL2)
- Docker Engine
- Docker CLI
- Docker-compose (yaml)
- Dockerfile (image, container, build, volumes)
- Docker Hub
- Windows Containers vs. Linux Containers
- Portainer

Kubernetes

Podman

kasm

.env file for credentials (add to .gitignore)

Installation mit Docker Desktop oder Skript:

```bash
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh ./get-docker.sh

# aktuellen Benutzer berechtigen
sudo usermod -aG docker $USER
```

Usage:

```bash
# Docker
docker version

ls -l /var/lib/docker/volumes
ls -l /var/lib/docker-desktop/volumes

# alle laufenden Container auflisten
docker ps -a

# docker images auflisten
docker images

# Container ausführen:
# -d (detached),
# -p (port-mapping host:container),
# -e FOO=bar (env-vars),
# -v (volumes: bind mounts, $(pwd))
docker run -d –name webserver -p 3000:80 \
-v ./var:/var/share/nginx/html nginx

# interaktiv bash starten
docker run -it ubuntu:24:10 bash

# einen Container anhalten
docker stop <containername>
docker kill <containername>

# einen gestoppten Container endgültig löschen
docker rm <containername>
```

Docker Compose:

```bash
# Docker Compose
docker-compose up -d

# open a shell inside the container
docker compose exec webserver bash
```

---

More:

- vGPU
- VHD

Shells:
- Cygwin
- MinGW + MSYS2
- Git-Bash
- busybox

CachyOS (Arch Linux Distrubution)
- Steam
- Proton
- Protontricks
- Wine
- Winetricks
- (Crossover)
- WinBoat uses Dockur
- Dockur macOS

Vagrant
- https://www.vagrantup.com/

---

## Emulators

Qemu

Bochs

WinUAE, UAE4All (Commodore Amiga)

MAME (Arcade)

ScummVM

Dolphin (Wii)

RetroPie, Batocera, Recalbox, Lakka, ArkOS (R36S), ... using EmulationStation, RetroArch, LibRetro

Commodore OS Vision 3 (Linux Distribution)

CachyOS, Nobara, Bazzite, SteamOS Linux Distributions

---

