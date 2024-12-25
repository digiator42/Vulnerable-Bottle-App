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
- **Description**: Removed basic dangerous characters like `;`, `&`, and `|`. However, it still executes user input with limited filtering.
- **Exploit Example**:
  ```
  ping nothing || ls
  ```

---

### 3. Strong Level
- **Description**: This level applies stricter sanitization, removing dangerous characters like `&&`, `||`, `$()` and more.
- **Exploit Example**:
  Attempting direct injection is highly unlikely to succeed. However, creative bypass methods might still exist.
---
