# Weak Crypto / Hash

The app is divided into three levels: Weak, Medium, and Strong. Each level introduces progressively stronger input sanitization, making it harder to exploit.

## Weak Crypto / Hash Levels
Let's get into cryptograph & hashing world
### 1. Weak Level
- **Description**: This level simulates weak md5 hashing algorithm.
- **Exploit Example**:
  ```
  check the code, you will find md5 hashing, go to online website and decrypt (not really, means compare exploited stored hashed) the md5 to get the very easy password
  ```

---

### 2. Medium Level
- **Description**: sha256.
- **Exploit Example**:
  ```
  The sequence of hashing md5 then sha256 means that you need to do more work, get a list of weak passwords and use the same hashing sequence to exploit it.
  ```

---

### 3. Strong Level
- **Description**: Salting, encrpted hash, bcrypt, hashpw, fernet
- **Exploit Example**:
```
```
---
