# Buffer overflow

The app is divided into three levels: Weak, Medium, and Strong. Each level introduces progressively stronger input sanitization, making it harder to exploit.

## Buffer overflow Levels
Memory is dynamically managed in python, this is just a simulation.
### 1. Weak Level
- **Description**: This level has no input checking.
- **Exploit Example**:
  ```
  Change form input max length to something greater that 15 chars
  ```