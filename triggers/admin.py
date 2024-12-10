import time
from bottle import request, response
from config.settings import MEDIUM_LEVEL, STRONG_LEVEL
import math

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
    
    return _check_credentials(input)

def check_ban(ip):
    if ip in BANNED_IPS:
        # if withing the ban period, it's banned
        if time.time() < BANNED_IPS[ip]:
            return True
        else:
            # remove the ban after duration time
            del BANNED_IPS[ip]
            ATTEMPS[ip]['count'] = 1
    return False

def ban_ip(ip, duration=10):
    # sets ban duraion to 5 mins
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
        return f"Too many attempts. Try again after {TIME_PERIOD - remaining_time} secs"

    return _check_credentials(input)

def strong_admin(input):
    ip = request.remote_addr
    
    # check wether the ip is banned or unlock the ban
    if check_ban(ip):
        remaining_time = math.ceil((BANNED_IPS[ip] - time.time()) / 60) # blocked time in mins
        return f"Too many attempts. Try again after {remaining_time} mins"

    if check_brute_force(ip):
        current_time = time.time()
        remaining_time = math.ceil(current_time - ATTEMPS[ip]['first_req_time'])
        response.status = 429
        return f"Too many attempts. Try again after {TIME_PERIOD - remaining_time} secs"
    
    return _check_credentials(input)

def _check_credentials(input):
    if input['username'] == "admin" and input['password'] == "1234":
        return "Access Granted!"
    return "Access Denied!"