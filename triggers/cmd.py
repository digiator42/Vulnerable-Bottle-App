import os
import subprocess

def trigger_cmd(user_input):
    os.system(user_input['input'])
    return user_input

def trigger_subprocess_cmd(user_input):
    try:
        result = subprocess.run(user_input['input'], shell=True, check=True, \
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout or result.stderr
    except subprocess.CalledProcessError as e:
        return e.stdout or e.stderr
    
def medium_cmd():
    """
    test code api
    """
    pass

def medium_subprocess_cmd():
    """
    test code api
    """
    pass