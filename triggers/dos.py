import requests
from config.settings import HOST, PORT

def trigger_dos(user_input):
    url = f"http://{HOST}:{PORT}/"
    print(f"Sending {user_input} requests to {url}")
    if user_input and user_input.isdigit():
        for i in range(int(user_input)):
            print(f"Sending request {i}")
            try:
                response = requests.get(url, timeout=5)
                print(f"Response {i}: {response.status_code}")
            except requests.exceptions.RequestException as e:
                print(f"Request {i} failed: {e}")
        return "Requests sent"
    return "Invalid input"