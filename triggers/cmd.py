import os

def trigger_cmd_injection(user_input):
    os.system(user_input)