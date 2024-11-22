import os
import subprocess

def trigger_cmd(user_input):
    os.system(user_input)
    return {"output": "works"}

def trigger_subprocess_cmd(user_input):
    try:
        result = subprocess.run(user_input, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return {"output": result.stdout, "error": result.stderr}
    except subprocess.CalledProcessError as e:
        return {"output": e.stdout, "error": e.stderr}