# Wireshark Network Traffic Capture and Protocol Analysis

## 📄 Assignment Overview
This project is part of the Cybersecurity Internship where the task is to capture live network traffic using Wireshark and analyze it by filtering specific protocols: IP source addresses, DNS, HTTP, ICMP, TCP, and UDP.

---

## 🎯 Objective
- Capture live network packets using Wireshark.
- Identify and analyze basic protocols and traffic types.
- Summarize key findings from the packet capture.

---

## 🛠 Tools Used
- **Wireshark** (Packet Capture and Analysis Tool)

---


---

## 🔍 Protocols Analyzed

| Protocol | Packet Count | Observations |
|----------|--------------|--------------|
| IPv6     | 16 packets   | UDP, MDNS, DNS traffic |
| IPv4     | 53 packets   | UDP, SSDP, MDNS, DNS traffic |
| UDP      | 41 packets   | Major protocol used; includes SSDP, MDNS, DNS |
| TCP      | Not significant | Very minimal or no TCP traffic observed |
| DNS      | 8 packets    | Domain queries like Grammarly services |
| HTTP     | Not observed | No HTTP traffic detected |
| ICMP     | Not observed | No ICMP (ping) traffic detected |

---

## 📊 Key Observations
- **Dominant Traffic:** UDP-based traffic, primarily for service discovery and DNS queries.
- **DNS Traffic:** Communication with domains like `treatment.grammarly.com` and `capi.grammarly.com`.
- **HTTP Traffic:** No HTTP traffic detected, browsing likely occurred over HTTPS (TLS encryption).
- **ICMP Traffic:** No ping or traceroute traffic was captured.

---

## 📸 Included Screenshots
- **Protocol Hierarchy**: Packet distribution among protocols.
- **Endpoints**: Active IP sources.
- **Conversations**: Network conversations between devices.
- **UDP Filter View**: Detailed view of captured UDP traffic.

---

## ✅ Conclusion
The captured traffic mainly involved **local network service discovery and DNS resolution.** No significant HTTP or ICMP traffic was observed, and the primary protocol used was UDP.

---

## 🔗 Submission
The `.pcapng` file, analysis report (README.md), and all screenshots have been included in this repository as required.


