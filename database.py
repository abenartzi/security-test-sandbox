import sqlite3

def get_user_profile(user_id):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # Intentionally unsafe: Vulnerable to SQL Injection
    # Inputting "1 OR 1=1" bypasses standard logic
    query = f"SELECT * FROM profiles WHERE id = '{user_id}'"
    
    cursor.execute(query)
    return cursor.fetchall()
