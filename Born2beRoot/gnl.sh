#!/bin/bash

arch=$(uname -a) # Get the system architecture
cpu=$(nproc) # Get the number of CPU cores
mem=$(free -m | awk '/Mem:/ {print $3 "/" $2}') # Get the used and total memory in MB
disk=$(df -h --total | grep total | awk '{print $3 "/" $2}') # Get the used and total disk space
boot=$(who -b | awk '{print $3 " " $4}') # Get the last boot time
ip=$(hostname -I) # Get the IP address(es)

# Display the information in a formatted way
wall "Architecture: $arch
CPU: $cpu
Memory: $mem
Disk: $disk
Last boot: $boot
IP: $ip"