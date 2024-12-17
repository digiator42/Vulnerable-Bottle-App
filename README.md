# Vulnerable Bottle App

intentionally vulnerable web application built with the lightweight [Bottle framework](https://bottlepy.org/). This project is designed for educational purposes to help learners understand and practice web application security concepts, including but not limited to OWASP Top 10 vulnerabilities.

**Disclaimer:**  
This application is intentionally insecure. It may also contain **`unintentional vulnerabilities`**. The author is not responsible for any misuse of this application. Use it only in a controlled environment for learning purposes.
---

## Features and Vulnerabilities

- **Injection Attacks**: SQL Injection, Command Injection
- **Broken Authentication**: Weak password storage, exposed credentials & database
- **CSRF (Cross-Site Request Forgery)**: Missing CSRF protection
- **Sensitive Data Exposure**
- **XSS (Cross-Site Scripting)**
- **Insecure Deserialization**
- **SSRF (Server-Side Request Forgery)**
- **File Upload Vulnerabilities**

---

## App Routes

- Each route accept both `GET` and `POST` requests for hands-on exploration, Except for root views only GET
- There is no restrinctions on GET or POST requests, the data will be collected wether it's query or body data

### For Instance:

**`/xss/xss`**
- **GET**: Query parameters, body data (Raw, Form-date & x-www-form-urlencoded).
    - http://localhost:8000/xss/xss?input=\<script>alert(1)\</script>
    - data = {'input': '\<script>alert(1)\</script>'}
- **POST**: Query parameters, body data (Raw, Form-date & x-www-form-urlencoded).
    - same as GET
---
