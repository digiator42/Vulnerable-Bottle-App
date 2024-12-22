# Brute Force

The app is divided into three levels: Weak, Medium, and Strong. Each level introduces progressively stronger input sanitization, making it harder to exploit.

## Brute Force Levels

### 1. Weak Level
- **Description**: This level has no restrictions of any kind. 
- **Exploit Example**:
  ```python
  # only use this for educational purposes
  for req in range(100):
    response = requests.post('url', data=data)
    # useful to alert you upon success
    print(response.content_length)
  ```

---

### 2. Medium Level
- **Description**: stricter.
- **Exploit Example**:
  ```
  check the code, next to help button
  ```

---

### 3. Strong Level
- **Description**: This level applies stricter method.
- **Exploit Example**:
  More than 10 reqs in a sec, means 5 mins block
---
