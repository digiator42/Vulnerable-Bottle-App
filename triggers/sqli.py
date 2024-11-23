import sqlite3

def check_sql_injection(user_input):
    if "'" in user_input:
        return True
    return False

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

def trigger_sql_injection(user_input):
    print('--------> ', user_input)
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()
    query = f"SELECT * FROM users WHERE username = '{user_input}';"
    cursor.execute(query)
    result = cursor.fetchone()
    connection.close()
    if result:
        return result[1], result[3]
    else:
        return None, None
