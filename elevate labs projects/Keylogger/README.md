
# 🛡️ Python Keylogger Project

## 📌 Overview

This project is a **Python-based Keylogger** that captures and logs keyboard input. It includes additional features like GUI interface, logging configuration, and email functionality to send logs. It is designed **strictly for educational and ethical testing purposes**.

---

## 📁 Project Structure

| File/Folder           | Description |
|------------------------|-------------|
| `keylogger.py`         | Main keylogger logic (records keystrokes) |
| `email_sender.py`      | Sends logs via email using SMTP |
| `gui.py`               | Basic GUI for user interaction or control panel |
| `test.py`              | Script for testing components of the keylogger |
| `config.json`          | Configuration settings (e.g., email, timer) |
| `logger_config.json`   | Custom logging configuration |
| `requirements.txt`     | Lists required Python packages |
| `.pyc` files           | Compiled Python files (auto-generated) |
| `README.md`            | Project documentation (this file) |

---

## 🚀 Features

- ✅ Stealth keylogging
- ✅ Cross-platform (Windows/Linux)
- ✅ Email log delivery
- ✅ Logging via `logging` module
- ✅ GUI for user control
- ✅ Modular code design

---

## ⚙️ Installation & Setup

### 1. 🔁 Clone the Repository
```bash
git clone https://github.com/your-username/keylogger-project.git
cd keylogger-project
```

### 2. 🐍 Create & Activate Virtual Environment
```bash
# Create
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# OR Activate (Linux/macOS)
source venv/bin/activate
```

### 3. 📦 Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🔧 Configuration

### Edit the `config.json` file:
```json
{
  "email": "your_email@example.com",
  "password": "your_app_password",
  "to_email": "receiver_email@example.com",
  "interval": 300
}
```

- `email`: Sender's email address  
- `password`: App password or sender's email password  
- `to_email`: Receiver's email for logs  
- `interval`: Interval in seconds to send logs via email  

---

## 💻 Running the Program

### Run the keylogger:
```bash
python keylogger.py
```

### To run with GUI:
```bash
python gui.py
```

---

## 📬 Email Functionality

The `email_sender.py` handles automatic email delivery of logs using SMTP.

**Note:** Enable **"Less secure apps"** or use **App Passwords** for Gmail/O365 accounts.

---

## 🧪 Testing

Run the test script:
```bash
python test.py
```

This runs unit/integration tests to ensure components work properly.

---

## 🔐 Ethical Use Notice

This project is for:

- Ethical hacking
- Cybersecurity education
- Parental/school monitoring (with consent)

⚠️ **Unauthorized or malicious use is strictly prohibited. The developer is not responsible for misuse.**

---

## 🧾 License

MIT License

---

## 🙋‍♂️ Author

Developed by AMIT MAURYA  
Cybersecurity & Python Automation Project
