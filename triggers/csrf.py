from typing import Dict
import sqlite3
from bottle import request

def trigger_csrf(input: Dict):
    amount = input['amount']
    recipient = input['recipient']
    
    session = request.environ.get('beaker.session')
    
    with sqlite3.connect('data.db') as conn:
        cursor = conn.cursor()
        
        cursor.execute("SELECT balance FROM users WHERE username = ? ", (session['username'],))
        
        balance = cursor.fetchone()
        new_balance = balance[0] - int(amount)
        
        cursor.execute("UPDATE users SET balance = ? WHERE username = ?", (new_balance, session['username']))
        
    return f'Transferred {amount} to {recipient}, balance {new_balance}'