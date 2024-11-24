import sqlite3

def create_admin_table():
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS admins (id INTEGER PRIMARY KEY, username TEXT, password TEXT)"
    )
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            is_admin BOOLEAN NOT NULL DEFAULT 0
        )
    ''')
    cursor.execute('''
        INSERT INTO users (username, password, is_admin) VALUES
        ('admin', 'admin', 1)
    ''')
    connection.commit()
    cursor.execute("SELECT * FROM users WHERE password = ?", ('admin',))
    result = cursor.fetchone()
    print('--------> ', result)
    connection.close()

def trigger_sql_injection(username):
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}';"
    cursor.execute(query)
    result = cursor.fetchall()
    connection.close()
    if result:
        return result[1], result[3]
    else:
        return None, None
    
def get_db_info():
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    cursor.execute("SELECT * FROM users;")
    users = cursor.fetchall()
    
    connection.close()
    print(tables, '\n', users)