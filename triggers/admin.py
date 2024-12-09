import time
from bottle import request, response
from config.settings import MEDIUM_LEVEL, STRONG_LEVEL

def trigger_admin(input):
    session = request.environ.get('beaker.session')
    level = session['level']
    
    if level == MEDIUM_LEVEL:
        return medium_admin(input)
    
    if input['username'] == "admin" and input['password'] == "1234":
        return "Access Granted!"
    return "Access Denied!"
    
ATTEMPS = {}
TIME_PERIOD = 60

def check_brute_force(ip):
    current_time = time.time()

    if ip in ATTEMPS:
        # allowing ip request again after 60 secs
        if current_time - ATTEMPS[ip]['first_req_time'] > TIME_PERIOD:
            # allowing 2 attempts in a minute
            ATTEMPS[ip]['count'] -= 2
            ATTEMPS[ip]['first_req_time'] = current_time
        # if more than 5 attempts are made within 60 seconds, then it's brute force
        if ATTEMPS[ip]['count'] > 5:
            return True
        ATTEMPS[ip]['count'] += 1
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