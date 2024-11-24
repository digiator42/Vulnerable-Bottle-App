from bottle import request

def trigger_admin(username):
    password = request.GET.get('password') or request.POST.get('password')
    if username == "admin" and password == "1234":
        return "Access Granted!"
    return "Access Denied!"