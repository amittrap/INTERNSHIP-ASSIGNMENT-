# 🔐 Cyber Security Internship – Task 4

## ✅ Firewall Setup and Configuration on Linux (UFW)

### 🎯 Objective
Configure and test basic firewall rules using **UFW (Uncomplicated Firewall)** on Linux to allow or block traffic on specific ports.

---

## 🛠 Tools Used
- **Operating System:** Ubuntu/Linux
- **Firewall Tool:** UFW (Uncomplicated Firewall)
- **Terminal**

---

## 📋 Steps Performed

```bash
# 1. Update and install UFW
sudo apt update
sudo apt install ufw -y

# 2. Check UFW status
sudo ufw status

# 3. Enable UFW
sudo ufw enable

# 4. Allow SSH (to prevent lockout)
sudo ufw allow 22

# 5. Deny Telnet (port 23)
sudo ufw deny 23

# 6. Verify allowed/denied services
sudo ufw status
sudo ufw status numbered

# 7. Delete a rule by number (e.g., rule #2)
sudo ufw delete 2

# 8. Show rules in command format
sudo ufw show added

# 9. List predefined app profiles and view info
sudo ufw app list
sudo ufw app info OpenSSH

# 10. Test port block
telnet localhost 23
```

---

## 📸 Screenshot Checklist

- [ ] `sudo ufw status` (before enabling)
- [ ] `sudo ufw enable`
- [ ] `sudo ufw allow 22`
- [ ] `sudo ufw deny 23`
- [ ] `sudo ufw status` (after rules)
- [ ] `sudo ufw status numbered`
- [ ] `sudo ufw show added`
- [ ] `telnet localhost 23` (should fail)
- [ ] `sudo ufw delete 2` (remove rule)

---

## 🔍 UFW vs iptables

| Feature                  | UFW (Uncomplicated Firewall)               | iptables                                  |
|--------------------------|--------------------------------------------|--------------------------------------------|
| Ease of Use              | Beginner-friendly, simple commands         | Complex syntax, manual configuration       |
| Interface Type           | Frontend for iptables                      | Core firewall utility                      |
| Rule Configuration       | Simplified                                 | Highly customizable                        |
| Use Case                 | Quick setups and learning                  | Advanced, detailed network rules           |
| Logging                  | Basic                                      | Advanced                                   |

---

## 📚 Interview Questions

1. What is a firewall?
2. Difference between stateful and stateless firewall?
3. What are inbound and outbound rules?
4. How does UFW simplify firewall management?
5. Why block port 23 (Telnet)?
6. What are common firewall mistakes?
7. How does a firewall improve network security?
8. What is NAT in firewalls?

---

