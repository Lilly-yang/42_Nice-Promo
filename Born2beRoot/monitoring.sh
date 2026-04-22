#!/bin/bash

## This script gathers various system information and sends it as a message to all logged-in users using the `wall` command. It collects data on system architecture, CPU, memory usage, disk usage, CPU load, last boot time, LVM usage, TCP connections, user logins, network information, and sudo command usage.
# CPU PHYSICAL
# Count the number of physical CPUs by counting unique "physical id" entries in /proc/cpuinfo
cpuf=$(grep "physical id" /proc/cpuinfo | wc -l) 

# CPU VIRTUAL
# Count the number of virtual CPUs by counting "processor" entries in /proc/cpuinfo
cpuv=$(grep "processor" /proc/cpuinfo | wc -l)

# RAM
# Get total RAM, used RAM, and calculate RAM usage percentage using the `free` command and `awk` for processing
ram_total=$(free --mega | awk '$1 == "Mem:" {print $2}')
# Get used RAM
ram_use=$(free --mega | awk '$1 == "Mem:" {print $3}')
# Calculate RAM usage percentage
ram_percent=$(free --mega | awk '$1 == "Mem:" {printf("%.2f"), $3/$2*100}')

# DISK
# Get total disk space, used disk space, and calculate disk usage percentage using the `df` command and `awk` for processing. It filters out the /boot partition and sums up the values for all other partitions.
disk_total=$(df -m | grep "/dev/" | grep -v "/boot" | awk '{disk_t += $2} END {printf ("%.1fGb\n"), disk_t/1024}')
# Get used disk space
disk_use=$(df -m | grep "/dev/" | grep -v "/boot" | awk '{disk_u += $3} END {print disk_u}')
# Calculate disk usage percentage
disk_percent=$(df -m | grep "/dev/" | grep -v "/boot" | awk '{disk_u += $3} {disk_t+= $2} END {printf("%d"), disk_u/disk_t*100}')

# CPU LOAD
# Get the percentage of CPU idle time using `vmstat` and calculate the CPU load percentage
cpul=$(vmstat 1 2 | tail -1 | awk '{printf $15}')
# Calculate CPU load percentage by subtracting idle time from 100
cpu_op=$(expr 100 - $cpul)
# Format the CPU load percentage to one decimal place
cpu_fin=$(printf "%.1f" $cpu_op)

# LAST BOOT
# Get the last boot time using the `who -b` command and format it to show only the date and time
lb=$(who -b | awk '$1 == "system" {print $3 " " $4}')

# LVM USE
# Check if LVM is in use by looking for "lvm" in the output of `lsblk`. If found, set lvmu to "yes", otherwise set it to "no".
lvmu=$(if [ $(lsblk | grep "lvm" | wc -l) -gt 0 ]; then echo yes; else echo no; fi)

# TCP CONNEXIONS
# Count the number of established TCP connections using the `ss` command and filtering for "ESTAB"
tcpc=$(ss -ta | grep ESTAB | wc -l)

# USER LOG
# Count the number of logged-in users by using the `users` command and counting the number of words in its output
ulog=$(users | wc -w)

# NETWORK
# Get the IP address of the host using `hostname -I` and the MAC address by parsing the output of `ip link` for "link/ether"
ip=$(hostname -I)
# Get the MAC address by looking for "link/ether" in the output of `ip link` and extracting the second field
mac=$(ip link | grep "link/ether" | awk '{print $2}')

# SUDO
# Count the number of sudo commands executed by filtering the journal for entries with _COMM=sudo, looking for "COMMAND" in the output, and counting the lines
cmnd=$(journalctl _COMM=sudo | grep COMMAND | wc -l)

wall "	Architecture: $arch
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