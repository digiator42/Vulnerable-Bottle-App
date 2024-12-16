import hashlib
from typing import Dict
from config.settings import MEDIUM_LEVEL, STRONG_LEVEL, KEY
import hashlib
from bottle import request
from bcrypt import checkpw
import sqlite3
from cryptography.fernet import Fernet


def trigger_crypto(data: Dict):
    level = request.environ.get('beaker.session')['level']
    
    if level == MEDIUM_LEVEL:
        return medium_crypto(data)
    elif level == STRONG_LEVEL:
        return strong_crypto(data)
    else:
        return weak_crypto(data)
    
def weak_crypto(data: Dict):
    password_hash = hashlib.md5(data['password'].encode()).hexdigest()
    
    stored_password_hash = "5f4dcc3b5aa765d61d8327deb882cf99"
    
    if password_hash == stored_password_hash:
        return "Authentication successful!"
    else:
        return "Authentication failed!"
    
def medium_crypto(data: Dict):

    password_hash = hashlib.md5(data['password'].encode()).hexdigest()
    password_hash = hashlib.sha256(password_hash.encode()).hexdigest()
    
    stored_password_hash = "a8d025f2cf6c4d28b4ea8e2e3612b8ffbe25547b19be9edbbb2eef8d983fe49a"
        
    if password_hash == stored_password_hash:
        return "Authentication successful!"
    else:
        return "Authentication failed!"

def strong_crypto(data: Dict):
    username = request.environ.get('beaker.session')['username']
    
    with sqlite3.connect("data.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT encrypted_password_hash FROM users_hashed_pass WHERE username = ?", (username,))
        result = cursor.fetchone()

        if not result:
            return "User not found!"

        encrypted_password_hash: bytes = result[0].encode()

    cipher_suite = Fernet(KEY)
    # Decrypt the bcrypt hash
    stored_password_hash: bytes = cipher_suite.decrypt(encrypted_password_hash)
    
    # is it the same stored password
    if checkpw(data['password'].encode(), stored_password_hash):
        return "Authentication successful!"
    else:
        return "Authentication failed!"