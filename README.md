# Vulnerable Bottle App

Intentionally vulnerable web application built with the lightweight [Bottle framework](https://bottlepy.org/).   
It's designed for educational purposes to help learners (including me) understand and practice web application security concepts, including but not limited to OWASP Top 10 vulnerabilities.

**Disclaimer:**  
This application is **`intentionally insecure`**. It may also contain **`unintentional vulnerabilities`**. The author is not responsible for any misuse of this application. Use it only in a controlled environment for learning purposes.

## Features and Vulnerabilities

- **Injection Attacks**: SQL Injection, Command Injection
- **Broken Authentication**: Weak password storage, exposed credentials & database
- **CSRF (Cross-Site Request Forgery)**: Missing CSRF protection
- **Sensitive Data Exposure**
- **XSS (Cross-Site Scripting)**
- **Insecure Deserialization**
- **SSRF (Server-Side Request Forgery)**
- **File Upload Vulnerabilities**


## App Routes

- Each route accept both `GET` and `POST` requests for hands-on exploration, Except for root views only GET
- There is no restrinctions on GET or POST requests, the data will be collected wether it's query or body data

### For Instance:

### Route: `/xss/xss`

This route demonstrates Cross-Site Scripting (XSS) vulnerabilities.

#### **Supported Methods**
- **GET**  
Query parameters   
Acually you can send payload with get request and it works, but let's keep it simple
  - URL: `http://localhost:8000/xss/xss?input=<script>alert(1)</script>`

- **POST**  
body data (Raw, Form-date & x-www-form-urlencoded)  
  - Body
    ```json
    {
      "input": "<script>alert(1)</script>"
    }
    ```

## Running the Application

- Run the application:
    ```bash
    cd /Vulnerable-Bottle-App
    docker build -t vuln-app .
    docker run -p 8000:8000 vuln-app
    ```

- Browse http://localhost:8000
- It can be run with development server instead of gunicorn. **`python3 app.py`**

## Logs:
Input logs are included for educational purposes in **`./logs`** folder and can be displayed in frontend
