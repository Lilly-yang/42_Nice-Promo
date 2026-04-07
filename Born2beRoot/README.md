# Born2beRoot

This folder contains the submission/support files for the 42 project **Born2beRoot**.

## Files

- `signature.txt`: VM disk signature hash (required by subject).
- `README.md`: setup notes and defense checklist (supporting document).

---

## 1) What to submit

For Born2beRoot, the required deliverable is usually:

- `signature.txt`

`signature.txt` must contain only the signature hash of your virtual machine disk.

---

## 2) How to generate `signature.txt`

### If you use VirtualBox

On your host machine, run:

```bash
sha1sum "Born2beRoot.vdi"
```

Copy only the hash (first field), for example:

```text
0123456789abcdef0123456789abcdef01234567
```

Put that exact hash into `signature.txt`.

### If your disk filename is different

Use the real disk filename:

```bash
sha1sum "<your_disk_name>.vdi"
```

---

## 3) Defense checklist (quick)

- Debian or Rocky setup completed.
- No graphical interface installed.
- At least 2 encrypted partitions (LVM + encryption as required).
- SSH service running and restricted to configured port.
- UFW/Firewall active with required rules.
- Password policy configured (`login.defs`, `pam` rules).
- `sudo` group and policy configured.
- Monitoring script (`monitoring.sh`) running via `cron` every 10 min.
- Hostname and user/group rules follow subject.
- `signature.txt` contains only one hash line.

---

## 4) Useful verification commands (inside VM)

```bash
hostnamectl
lsblk
sudo ufw status
sudo systemctl status ssh
sudo -l
cat /etc/login.defs
cat /etc/pam.d/common-password
crontab -l
```

---

## 5) Notes

- Do not add extra text in `signature.txt`.
- If you regenerate/recreate the VM disk, the hash changes and must be updated.
