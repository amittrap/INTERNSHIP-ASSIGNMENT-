# 🔍 Basic Vulnerability Scan Using Nessus Essentials

This project is part of a Cyber Security Internship task to perform a basic vulnerability scan on a personal computer using **Nessus Essentials**.

## 📌 Objective

Use a free vulnerability scanning tool to identify security issues on your local machine, understand potential risks, and learn basic remediation techniques.

---

## 🧰 Tools Used

- **Nessus Essentials** – Free vulnerability scanner by Tenable  
  📎 [Download Link](https://www.tenable.com/products/nessus/nessus-essentials)

---

## ⚙️ Steps Followed

1. Installed **Nessus Essentials** and activated with free license.
2. Scanned the local machine (`127.0.0.1`) using the **Basic Network Scan** template.
3. Waited for the scan to complete (approx. 45 mins).
4. Reviewed the vulnerability report and noted the high/medium severity issues.
5. Took relevant screenshots and documented top findings and fixes.

---

## 🛡️ Key Vulnerabilities Found

| Vulnerability                        | Severity | Description                                                  | Suggested Fix |
|-------------------------------------|----------|--------------------------------------------------------------|---------------|
| SSL Certificate Cannot Be Trusted   | Medium   | SSL cert not trusted – risks MitM attacks                    | Use a valid certificate |
| SMB Signing Not Required            | Medium   | Leaves system open to SMB relay attacks                      | Enable SMB signing via registry |
| NetBIOS Name Disclosure             | Low      | Reveals system info useful in attacks                        | Disable NetBIOS over TCP/IP |
| OS Patch Status Not Detectable      | Info     | Nessus couldn’t verify Windows patch level                   | Run scan with credentials |
| Unknown Service Banners             | Info     | Detected unidentified services on uncommon ports             | Audit & disable unnecessary services |

---

## 🧩 How Attackers Could Exploit These

- **Man-in-the-Middle (MitM)**: Using self-signed SSL certs allows attackers to intercept encrypted communication.
- **SMB Relay Attacks**: Without SMB signing, credentials could be captured and reused by an attacker.
- **Reconnaissance**: NetBIOS and SMB disclosures help attackers map the internal network.

---

## 🩹 How to Patch / Fix

- Replace SSL certs with trusted CA-signed certificates.
- Enforce SMB signing through Windows Group Policy or Registry.
- Disable NetBIOS over TCP/IP if not required.
- Perform Windows updates and rerun Nessus with system credentials for accurate patch detection.

---

## 📁 Project Structure


