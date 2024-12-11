import sqlite3
from typing import Dict
from config.settings import database_users

def create_admin_table():
    with sqlite3.connect("data.db") as connection:
        cursor = connection.cursor()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS admins (id INTEGER PRIMARY KEY, username TEXT, password TEXT)"
        )
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                password TEXT NOT NULL,
                role TEXT NOT NULL
            )
        ''')

        cursor.execute("SELECT * FROM users WHERE username = 'admin'")
        
        if cursor.fetchone() is None:
            for name, data in database_users.items():
                cursor.execute(
                    "INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
                    (name, data['password'], data['role'])
                )

        connection.commit()

def trigger_sqli(input: Dict):
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()
    query = f"SELECT * FROM users WHERE username = '{input['username']}';"
    try:
        cursor.execute(query)
    except sqlite3.OperationalError as e:
        return str(e)
    result = cursor.fetchall()
    connection.close()
    if result:
        return result
    
    return ''
    
def get_db_info():
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    cursor.execute("SELECT * FROM users;")
    users = cursor.fetchall()
    
    connection.close()
    print(tables, '\n', users)