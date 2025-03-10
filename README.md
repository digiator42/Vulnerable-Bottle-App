# Vulnerable Bottle App

Intentionally vulnerable web application built with the lightweight [Bottle framework](https://bottlepy.org/).   
It's designed for educational purposes to help learners (including me) understand and practice web application security concepts, including but not limited to OWASP Top 10 vulnerabilities.

**Disclaimer:**  
This application is **`intentionally insecure`**. It may also contain **`unintentional vulnerabilities`**. The author is not responsible for any misuse of this application. Use it only in a controlled environment for learning purposes.

## Features and Vulnerabilities

- **Injection Attacks**: SQL Injection, Command Injection
- **SSRF (Server-Side Request Forgery)**
- **XSRF (Cross-Site Request Forgery)**
- **SSTI (Server-Side Template Injection)**
- **XSS (Cross-Site Scripting)**
- **JWT Failure Verification**
- **Open Redirect**
- **Cryptographic Failures**
- **Insecure File Read**
- **Broken Authentication**
- **Insecure Deserialization**
- **File Upload Vulnerabilities**

## Login
  - **Login with username:test & password:test**
    - jwt and crypto vulnerabilities will not work though.

## App Routes
- You can find all app routes with possible methods -> http://localhost:8000/routes
- Each route accept both `GET` and `POST` requests for hands-on exploration, Except for root views only accept `GET` requests
- There is no restrictions on GET or POST requests, the data will be collected whether it's query or body data (exclude main login page)

### For Instance:

### Route: `/xss/xss`   

#### **Supported Methods**
- **GET**  
Query parameters   
  - URL: `http://localhost:8000/xss/xss?input=<script>alert(1)</script>`   
  - Also you can combine multi different query params:  
  `http://localhost:8000/xss/xss?level=medium&input=<script>alert(1)</script>`  
  this will change level to medium before making the request.   
  - you can also send payload with get request and it works, but let's keep it simple

- **POST**  
body data (Raw, Form-date & x-www-form-urlencoded)  
  - Body
    ```json
    {
      "input": "<script>alert(1)</script>"
    }
    ```

<br>
<br>

## Running the Application   

- Run the application:
    ```bash
    git clone https://github.com/digiator42/Vulnerable-Bottle-App
    cd ./Vulnerable-Bottle-App
    docker build -t vuln-app .
    docker run -p 8000:8000 vuln-app
    ```

- Browse http://localhost:8000

## Logs:
Input logs are included for educational purposes in **`./logs`** folder and can be displayed in frontend
