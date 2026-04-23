sudo crontab -e # Edit the crontab file
# Add the following line to run check.sh every 5 minutes
# */5 * * * * sh check.sh
# Add the following line to run monitoring.sh every minute
# * * * * * /path/to/monitoring.sh
chmod +x monitoring.sh # Make the monitoring script executable
systemctl status cron # Check the status of the cron service
# is corn is not running, start it with the following command
sudo systemctl enable cron
sudo systemctl start cron
# test if the cron job is working by checking the output of check.sh and monitoring.sh after the scheduled time has passed
watch -n 1 cat /var/log/syslog | grep monitoring # Monitor the syslog for entries related to the monitoring script (adjust the path and grep pattern as needed)
journalctl -f # Follow the journal logs in real-time to see if the cron jobs are executing as expected (use Ctrl+C to stop following the logs)
# Check the output of check.sh and monitoring.sh to verify that they are running correctly and producing the expected results.
crontab -l
ls -l monitoring.sh

sudo ufw status # Check the status of the firewall

sudo service ssh status # Check the status of the SSH service
nano /etc/ssh/sshd_config # Check the SSH configuration file for any custom settings (e.g., port number, allowed users, etc.)
nano /etc/ssh/ssh_config # Check the SSH client configuration file for any custom settings (e.g., preferred authentication methods, etc.)
ssh lyang@localhost -p 4241 # Test SSH connection to localhost on port 4241 (replace with the appropriate username and port number if different)
ssh <user>@localhost -p 4241 # Test SSH connection to localhost on port 4241 (replace <user> with the appropriate username and port number if different)

uname -a # Check the system architecture

df -h --total | grep total | awk '{print $3 "/" $2}' # Check the used and total disk space

# to view the partitions for the VM
lsblk | grep "lvm" | wc -l # Check if LVM is used (returns 0 if not used, greater than 0 if used)

sudo -v # check if the user has sudo privileges


sudo adduser <username> # Add a new user (replace <username> with the desired username)
sudo addgroup <groupname> # Add a new group (replace <groupname> with the desired group name)
getent group <groupname> # Check the members of the new group (replace <groupname> with the name of the group you created)
sudo adduser <username> <groupname> # Add the user to the group (replace <username> and <groupname> with the appropriate names)
getent group <groupname> <groupname> # check users in groupname

# sudo policies
nano /etc/sudoers.d/sudo_config # Edit the sudoers file to give specific permissions to users or groups (be careful when editing this file, as incorrect configurations can lead to loss of sudo access)
Defaults  passwd_tries=3 # Set the number of password attempts before sudo gives up
Defaults  badpass_message="Mensaje de error personalizado" # Set a custom error message for failed sudo attempts
Defaults  logfile="/var/log/sudo/sudo_config" # Set a custom log file for sudo commands
Defaults  log_input, log_output # Enable logging of input and output for sudo commands
Defaults  iolog_dir="/var/log/sudo" # Set the directory for sudo I/O logs
Defaults  requiretty # Require a TTY(Teletypewriter) for sudo commands (can be disabled for certain users or groups if necessary)	
Defaults  secure_path="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/snap/bin" # Set a secure PATH for sudo commands

ls /var/log/sudo/ # Check the contents of the sudo log directory

# password policy
sudo nano /etc/pam.d/common-password # Edit the PAM password configuration to enforce password policies (e.g., minimum length, complexity requirements)
minlen=10 ➤ The minimum characters a password must contain.
ucredit=-1 ➤ The password must contain at least one capital letter. We must write it with a - sign, as this is how it knows that it refers to minimum characters; if we put a + sign it will refer to maximum characters.
dcredit=-1 ➤ The password must contain at least one digit.
lcredit=-1 ➤ The password must contain at least one lowercase letter.
maxrepeat=3 ➤ The password cannot have the same character repeated three consecutive times.
reject_username ➤ The password cannot contain the username within itself.
difok=7 ➤ The password must contain at least seven different characters from the last password used.
enforce_for_root ➤ We will implement this password policy for root.

sudo ufw allow 8080 # Allow incoming traffic on port 8080 (replace with the appropriate port number for your application)
sudo ufw status # Check the status of the firewall
# delete the rule if you want to remove it
sudo ufw delete allow 8080 # Remove the rule allowing traffic on port 8080

shasum machinename.vdi # Generate a SHA-1 checksum for the specified file (replace machinename.vdi with the actual file name)