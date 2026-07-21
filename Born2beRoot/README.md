*This project has been created as part of the 42 curriculum by <login>.*

## Description

**Born2beRoot** is a systems administration project that requires setting up a secure virtual machine from scratch. The goal is to create a functional, hardened virtual machine running either Debian or Rocky Linux with strict security policies, proper partitioning, user management, and a monitoring system.

This project emphasizes understanding:
- Operating system installation and configuration
- Secure partitioning strategies using LVM and disk encryption
- Firewall configuration and SSH hardening
- Password and sudo policies
- Automated system monitoring via cron jobs

The deliverable is a fully configured virtual machine that meets the 42 subject requirements, with a signature file containing the SHA1 hash of the VM disk.

## Instructions

### Prerequisites
- VirtualBox hypervisor
- The chosen Linux distribution ISO (Debian or Rocky Linux)
- Sufficient disk space (at least 30GB recommended)

### Installation & Execution

1. **Create Virtual Machine**
   - Set up a new VM with at least 2 CPU cores and 2GB RAM
   - Create a new virtual disk (30GB+)

2. **Install Operating System**
   - Boot from the Linux ISO
   - Partition the disk according to the subject requirements:
     - Separate partitions for `/`, `/boot`, `/home`, `/var`, `/var/log`, `/tmp`, `/srv`
     - Use LVM for partitioning
     - Enable LUKS encryption on all partitions except `/boot`

3. **Initial Configuration**
   - Set hostname to `<login>42` (or as specified)
   - Create a user with sudo privileges
   - Configure sudo group restrictions
   - Install required packages (ssh, ufw, etc.)

4. **Security Hardening**
   - Configure UFW firewall (or firewalld)
   - Restrict SSH access to a specific port
   - Set password policy via `login.defs` and PAM
   - Disable root login

5. **Monitoring Setup**
   - Create `monitoring.sh` script
   - Set up cron job to run every 10 minutes
   - Ensure the script displays system stats on every terminal login

6. **Generate Signature**
   ```bash
   # On host machine, compute hash of VM disk
   sha1sum "Born2beRoot.vdi"
   ```
   - Copy the hash to `signature.txt`

### Verification Commands

```bash
# System information
hostnamectl
lsblk
df -h

# Security and services
sudo ufw status
sudo systemctl status ssh
sudo -l
cat /etc/login.defs | grep PASS
cat /etc/pam.d/common-password
crontab -l
```

## Resources

### Documentation
- [Debian Installation Guide](https://www.debian.org/doc/manuals/debian-installation-guide/)
- [Rocky Linux Documentation](https://docs.rockylinux.org/)
- [LVM Administration Guide](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/logical_volume_manager_administration/)
- [Linux Unified Key Setup (LUKS)](https://gitlab.com/cryptsetup/cryptsetup/-/wikis/home)
- [OpenSSH Manual](https://man.openbsd.org/ssh_config)
- [UFW Firewall Guide](https://wiki.ubuntu.com/UncomplicatedFirewall)
- [Cron Job Documentation](https://linux.die.net/man/5/crontab)

### AI Usage

AI was used to assist with:
- **Script optimization**: Generating efficient bash scripts for system monitoring and configuration
- **Security policy documentation**: Explaining PAM rules and password policy configurations
- **Troubleshooting**: Debugging firewall rules, LVM configuration, and SSH access issues
- **Comparison analysis**: Clarifying differences between OS and tool choices

## Project Description

### Operating System Choice: Debian vs Rocky Linux

#### Debian
**Advantages:**
- Excellent documentation and community support
- Stable, well-tested releases
- Simpler package management with apt
- Lightweight on system resources
- Better suited for beginners and rapid deployment

**Disadvantages:**
- Release cycle is slower (every ~2 years)
- Less focus on enterprise features
- Fewer built-in security tools compared to Rocky

#### Rocky Linux
**Advantages:**
- Enterprise-grade stability and support
- Regular security updates with extended support windows
- Strong focus on compliance and hardening
- Binary compatible with RHEL
- Better suited for production environments

**Disadvantages:**
- Steeper learning curve (yum/dnf package management)
- Heavier on system resources
- Smaller community compared to Debian
- More complex configuration for some features

**Choice for this project**: This project uses **[Debian/Rocky - specify based on your choice]** because [provide your reasoning based on the advantages above].

### Design Choices & Architecture

#### 1. Partitioning Strategy

**Chosen Scheme**: LVM with LUKS Encryption
```
/boot                 500MB   (unencrypted - required for bootloader)
/                     10GB    (encrypted logical volume)
/home                 5GB     (encrypted logical volume)
/var                  3GB     (encrypted logical volume)
/var/log              2GB     (encrypted logical volume)
/tmp                  1GB     (encrypted logical volume)
/srv                  2GB     (encrypted logical volume)
swap                  1-2GB   (encrypted for security)
```

**Rationale:**
- LVM provides flexibility to resize partitions without reinstalling
- Separate partitions contain attack surface per component
- LUKS encryption protects data at rest
- Unencrypted `/boot` is necessary for bootloader to function

#### 2. Security Policies

**Password Policy** (via `login.defs` and PAM):
- Minimum length: 10 characters
- Must contain uppercase, lowercase, digits, and special characters
- Password aging: Maximum 30 days, minimum 2 days, warning 7 days
- Lock account after 3 failed login attempts

**sudo Configuration:**
- `sudo` group created with minimal privileges
- Restricted to specific commands where possible
- Session logging enabled
- Root login disabled in favor of sudo

**Rationale:**
- Strong password policy prevents brute force attacks
- Restricted sudo access limits privilege escalation
- Logging provides audit trail for security investigations

#### 3. Service Hardening

**SSH Configuration:**
- Non-standard port (e.g., 4242) to reduce automated attacks
- Root login disabled
- Password authentication disabled (key-based only, if possible)
- Allow specific users only

**Firewall (UFW)**:
- Default deny incoming, allow outgoing
- Allow only SSH and other essential services
- Log denied connections for monitoring

#### 4. Monitoring System

**monitoring.sh Script**:
Displays key system metrics every 10 minutes via cron:
- Architecture and kernel info
- CPU, memory, and disk usage
- Connected users
- Network statistics
- Uptime and boot messages

**Rationale:**
- Automated monitoring detects system issues early
- Persistent logging aids in troubleshooting and forensics

### Tool Comparisons

#### AppArmor vs SELinux

| Feature | AppArmor | SELinux |
|---------|----------|---------|
| **Approach** | Path-based access control | Label-based access control |
| **Complexity** | Simpler to configure | More granular but complex |
| **Learning Curve** | Beginner-friendly | Steep for beginners |
| **Performance** | Lower overhead | Higher overhead |
| **Default in Debian** | Yes | No (must install) |
| **Default in Rocky** | No | Yes |
| **Use Case** | Good for general hardening | Better for high-security environments |

**Recommendation**: Use AppArmor for Debian, SELinux for Rocky Linux (default setup).

#### UFW vs firewalld

| Feature | UFW | firewalld |
|---------|-----|-----------|
| **Purpose** | Simplified iptables frontend | Dynamic firewall manager |
| **Complexity** | Very simple syntax | More complex configuration |
| **Zone Support** | Not available | Yes (predefined profiles) |
| **Reload Behavior** | Requires reload | Hot reload without service interruption |
| **Default in Debian** | Available | Not default |
| **Default in Rocky** | Not default | Yes |
| **Best For** | Simple setups, learning | Enterprise environments |

**Recommendation**: Use UFW for Debian, firewalld for Rocky Linux.

#### VirtualBox

VirtualBox is a powerful open-source hypervisor that supports Windows, macOS, and Linux. It provides:
- Excellent cross-platform compatibility
- User-friendly interface for VM management
- Strong community support and documentation
- Free and open-source (GPL license)
- Reliable virtualization across different host architectures

### Security Considerations

- All partitions except `/boot` are encrypted with LUKS
- Firewall blocks all unsolicited incoming traffic
- SSH hardened with non-standard port and key-based auth
- Password policy enforces strong credentials
- Monitoring alerts to potential issues via cron
- Sudo access tightly controlled with logging
- No graphical interface reduces attack surface

## Files Included

- `signature.txt`: SHA1 hash of the VM disk (required submission)
- `monitoring.sh`: System monitoring script
