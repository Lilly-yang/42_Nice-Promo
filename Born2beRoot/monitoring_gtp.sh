#!/bin/bash

# Architecture

arch=$(uname -a)

# CPU

cpuf=$(grep "physical id" /proc/cpuinfo | sort -u | wc -l)
cpuv=$(grep "processor" /proc/cpuinfo | wc -l)

# RAM

ram_total=$(free -m | awk '$1 == "Mem:" {print $2}')
ram_use=$(free -m | awk '$1 == "Mem:" {print $3}')
ram_percent=$(free -m | awk '$1 == "Mem:" {printf("%.2f"), $3/$2*100}')

# Disk

disk_total=$(df -m | grep "^/dev/" | grep -v "/boot" | awk '{total += $2} END {printf("%.1fGb"), total/1024}')
disk_use=$(df -m | grep "^/dev/" | grep -v "/boot" | awk '{used += $3} END {print used}')
disk_percent=$(df -m | grep "^/dev/" | grep -v "/boot" | awk '{used += $3} {total += $2} END {printf("%d"), used/total*100}')

# CPU load

cpu_load=$(top -bn1 | grep "Cpu(s)" | awk '{print 100 - $8}')
cpu_fin=$(printf "%.1f" $cpu_load)

# Last boot

lb=$(who -b | awk '{print $3 " " $4}')

# LVM

lvmu=$(lsblk | grep -q "lvm" && echo yes || echo no)

# TCP

tcpc=$(ss -ta | grep ESTAB | wc -l)

# Users

ulog=$(users | wc -w)

# Network

ip=$(hostname -I | awk '{print $1}')
mac=$(ip link | grep "link/ether" | head -n 1 | awk '{print $2}')

# Sudo

cmnd=$(grep COMMAND /var/log/sudo/sudo.log | wc -l)

wall "Architecture: $arch
CPU physical: $cpuf
vCPU: $cpuv
Memory Usage: $ram_use/${ram_total}MB ($ram_percent%)
Disk Usage: $disk_use/${disk_total} ($disk_percent%)
CPU load: $cpu_fin%
Last boot: $lb
LVM use: $lvmu
Connections TCP: $tcpc ESTABLISHED
User log: $ulog
Network: IP $ip ($mac)
Sudo: $cmnd cmd"
