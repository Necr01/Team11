import sqlite3

# Connect to SQLite database (creates a new one if it doesn't exist)
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Create a table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL
    )
""")
print("Table created successfully.")

# Commit changes and close the connection
conn.commit()
conn.close()

def insert_user(name, age):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
    conn.commit()
    conn.close()
    print(f"User '{name}' added successfully.")

insert_user("Glenn", 25)
insert_user("Alexa", 30)
insert_user("Mark", 30)

def get_users():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    conn.close()
    for row in rows:
        print(row)

get_users()

def update_user(user_id, new_name, new_age):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET name = ?, age = ? WHERE id = ?", (new_name, new_age, user_id))
    conn.commit()
    conn.close()
    print(f"User ID {user_id} updated successfully.")

update_user(1, "Glenn Galvo", 26)

def delete_user(user_id):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    conn.close()
    print(f"User ID {user_id} deleted successfully.")

delete_user(2)
