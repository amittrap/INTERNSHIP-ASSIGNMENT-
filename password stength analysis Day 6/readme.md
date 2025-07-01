# 🔐 Cyber Security Internship: Task 6 - Password Strength Evaluation

## 📌 Objective
The purpose of this task is to understand what makes a password strong and how to test password strength using online password strength checkers. The task also explores common password attack methods and best practices for creating secure passwords.

---

## 📂 Deliverables
- Password strength evaluation report
- Detailed explanation of common password attacks
- Summary of best practices for password security

---

## 🛠️ Tools Used
- [PasswordMeter.com](http://www.passwordmeter.com/) - Password Strength Checker

---

## 🔑 Passwords Created and Evaluated

| Password            | Complexity Elements                        | Password Strength Result |
|---------------------|--------------------------------------------|--------------------------|
| password123         | Lowercase, Numbers                         | Very Weak                |
| Pass@2024           | Uppercase, Lowercase, Numbers, Symbol       | Moderate                 |
| X!v9@qT7#bL2        | Uppercase, Lowercase, Numbers, Multiple Symbols | Strong              |
| Hello@world2024     | Uppercase, Lowercase, Numbers, Symbol       | Strong                   |
| G#7hX$k&9Lp@2b!3    | Uppercase, Lowercase, Numbers, Multiple Symbols | Very Strong          |

---

## 🛡️ Common Password Attacks

### 1. Brute Force Attack
- Attackers try **every possible combination** until the correct password is found.
- **Prevention:** Use long, complex passwords; enable MFA; implement account lockout policies.

### 2. Dictionary Attack
- Attackers use **precompiled lists of common words and passwords** to guess user passwords.
- **Prevention:** Avoid using common words or predictable sequences in passwords.

### 3. Credential Stuffing
- Attackers use **previously leaked username-password pairs** to try to log into other accounts.
- **Prevention:** Use unique passwords for each account; enable MFA.

### 4. Phishing
- Attackers trick users into **revealing passwords via fake websites or emails**.
- **Prevention:** Always verify links and sources; use email security filters; conduct security awareness training.

### 5. Rainbow Table Attack
- Attackers use **precomputed tables of hashed passwords** to reverse password hashes.
- **Prevention:** Salt all passwords; use strong, modern hashing algorithms like bcrypt, scrypt, or Argon2.

---

## 🔍 Summary Table

| Attack Type           | Method                            | Prevention                                   |
|----------------------|-----------------------------------|----------------------------------------------|
| Brute Force          | Tries all combinations            | Complex passwords, MFA, rate-limiting        |
| Dictionary Attack    | Tries common words/passwords       | Unique, unpredictable passwords              |
| Credential Stuffing  | Uses leaked credentials            | Unique passwords per site, MFA               |
| Phishing             | Tricks users to reveal passwords   | Awareness, source verification, email filters |
| Rainbow Table Attack | Uses precomputed hash tables       | Salting, modern hashing algorithms           |

---

## ✅ Key Learnings
- Password length and complexity significantly improve security.
- Passphrases offer a good balance between strength and memorability.
- Multi-factor authentication (MFA) adds an essential layer of security.
- Password managers help generate and store complex, unique passwords safely.

---

## 📚 References
- PasswordMeter.com: [http://www.passwordmeter.com/](http://www.passwordmeter.com/)
- OWASP Authentication Cheat Sheet: [https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)

---

