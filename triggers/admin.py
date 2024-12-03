
def trigger_admin(input):
    if input['username'] == "admin" and input['password'] == "1234":
        return "Access Granted!"
    return "Access Denied!"