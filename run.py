import os
import time
import subprocess

if __name__ == "__main__":
    while True:
        try:
            result = subprocess.run(["python3", "app.py"], check=True)
            print(result)
        except subprocess.CalledProcessError as e:
            print(f"Subprocess error: {e}")
            time.sleep(3)
