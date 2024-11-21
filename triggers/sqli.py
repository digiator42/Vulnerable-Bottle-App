from sqlite3 import Cursor

def trigger_sql_injection(user_input):
    query = f"SELECT * FROM users WHERE username = '{user_input}';"
    Cursor.execute(query)
