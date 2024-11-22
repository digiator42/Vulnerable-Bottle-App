import hashlib

def trigger_crypto(data):
    return hashlib.md5(data.encode()).hexdigest()
