#!/bin/bash

arch=$(uname -a)
cpu=$(nproc)
mem=$(free -m | awk '/Mem:/ {print $3 "/" $2}')
disk=$(df -h --total | grep total | awk '{print $3 "/" $2}')
boot=$(who -b | awk '{print $3 " " $4}')
ip=$(hostname -I)

wall "Architecture: $arch
CPU: $cpu
Memory: $mem
Disk: $disk
Last boot: $boot
IP: $ip"