# 📧 Phishing Email Analysis Report

This repository contains a detailed analysis of a **phishing email** targeting users through a spoofed domain: `weeblysite.com`. The report was generated as part of a cybersecurity task focused on identifying email-based threats.

---

## 🧠 Objective

To investigate and document the characteristics of a phishing email using:
- Email header analysis
- URL inspection
- Content analysis (language, formatting, urgency)
- Threat intelligence tools like [PhishTank](https://www.phishtank.com/)

---

## 🔍 Email Traits Identified

| Category              | Indicator                                  | Description                                              |
|-----------------------|---------------------------------------------|----------------------------------------------------------|
| **Sender Spoofing**   | `support@weeblysite.com`                    | Fake sender address pretending to be Weebly              |
| **Header Issues**     | SPF/DKIM failed, return-path mismatch       | Email failed authentication checks                       |
| **Malicious URL**     | `weeblysite.com/login/validate.php`         | Redirects to phishing page, flagged on PhishTank         |
| **Urgent Language**   | "Verify now or account suspended"           | Common fear tactic in phishing emails                    |
| **Grammar Issues**    | Spelling and sentence errors                | Often seen in large-scale phishing campaigns             |
| **No Personalization**| Generic greeting like “Dear User”           | Indicates a mass phishing email                          |

---

## 🛠 Tools Used

- [PhishTank](https://www.phishtank.com/)
- [Google Header Analyzer](https://toolbox.googleapps.com/apps/messageheader/)
- [MXToolbox](https://mxtoolbox.com/EmailHeaders.aspx)
- [VirusTotal](https://www.virustotal.com/)
- Manual inspection and reporting

---

## 📄 Report Access

You can download or view the full PDF report here:

📥 **[Download Report (PDF)](https://github.com/amittrap/INTERNSHIP-ASSIGNMENT-/edit/main/phishing_scan_day2)
📄 **[View Report in GitHub](https://github.com/amittrap/INTERNSHIP-ASSIGNMENT-/edit/main/phishing_scan_day2)**

---

## ✅ Conclusion

This project highlights key phishing indicators and demonstrates how to analyze suspicious emails using both manual techniques and automated tools. It serves as a practical example of basic threat detection in email-based attacks.

---

## 📚 License

This project is provided for educational and training purposes only. Do not attempt to replicate phishing attacks or misuse the analysis methods described.

---

