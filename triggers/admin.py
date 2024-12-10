import time
from bottle import request, response
from config.settings import MEDIUM_LEVEL, STRONG_LEVEL


BANNED_IPS = {}
ATTEMPS = {}
TIME_PERIOD = 60
MAX_ATTEMPTS = 5

def trigger_admin(input):
    session = request.environ.get('beaker.session')
    level = session['level']
    
    if level == MEDIUM_LEVEL:
        return medium_admin(input)
    
    elif level == STRONG_LEVEL:
        return strong_admin(input)
    
    if input['username'] == "admin" and input['password'] == "1234":
        return "Access Granted!"
    return "Access Denied!"

def check_ban(ip):
    if ip in BANNED_IPS:
        if time.time() < BANNED_IPS[ip]:
            return True
        else:
            del BANNED_IPS[ip]
    return False

def ban_ip(ip, duration=60):
    BANNED_IPS[ip] = time.time() + duration

def check_brute_force(ip):
    current_time = time.time()

    if ip in ATTEMPS:
        ATTEMPS[ip]['count'] += 1
        
        if ATTEMPS[ip]['count'] > (MAX_ATTEMPTS * 2):
            ban_ip(ip)
        
        # allowing ip request again after 60 secs
        if current_time - ATTEMPS[ip]['first_req_time'] > TIME_PERIOD:
            # reset tries
            ATTEMPS[ip]['count'] = 1
            ATTEMPS[ip]['first_req_time'] = current_time
        # if more than 5 attempts are made within 60 seconds, then it's brute force
        if ATTEMPS[ip]['count'] > MAX_ATTEMPTS:
            return True
    else:
        ATTEMPS[ip] = {'count': 1, 'first_req_time': current_time}

    return False

def medium_admin(input):
    ip = request.remote_addr

    if check_brute_force(ip):
        current_time = time.time()
        remaining_time = round(current_time - ATTEMPS[ip]['first_req_time'])
        response.status = 429
        return f"Too many attempts. Try again later. {TIME_PERIOD - remaining_time} secs"
    if input['username'] == "admin" and input['password'] == "1234":
        return "Access Granted!"
    return "Access Denied!"

def strong_admin(input):
    ip = request.remote_addr
    if check_ban(ip):
        remaining_time = int((BANNED_IPS[ip] - time.time()) / 60) # blocked time in mins
        return f"Too many attempts. Try again later. {remaining_time} mins"

    if check_brute_force(ip):
        current_time = time.time()
        remaining_time = round(current_time - ATTEMPS[ip]['first_req_time'])
        response.status = 429
        return f"Too many attempts. Try again later. {TIME_PERIOD - remaining_time} secs"
    
    if input['username'] == "admin" and input['password'] == "1234":
        return "Access Granted!"
    return "Access Denied!"