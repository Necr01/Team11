import sqlite3

# Connect to SQLite database (creates a new one if not exists)
conn = sqlite3.connect("notes.db")
cursor = conn.cursor()

# Create a table for storing notes
cursor.execute('''
    CREATE TABLE IF NOT EXISTS notes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        content TEXT NOT NULL
    )
''')

# Commit and close connection
conn.commit()
conn.close()

print("Database and table created successfully.")

def add_note(title, content):
    conn = sqlite3.connect("notes.db")
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO notes (title, content) VALUES (?, ?)", (title, content))
    
    conn.commit()
    conn.close()
    print("Note added successfully.")

def view_notes():
    conn = sqlite3.connect("notes.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM notes")
    notes = cursor.fetchall()
    
    conn.close()
    
    for note in notes:
        print(f"ID: {note[0]}, Title: {note[1]}\nContent: {note[2]}\n{'-'*30}")

def update_note(note_id, new_title, new_content):
    conn = sqlite3.connect("notes.db")
    cursor = conn.cursor()
    
    cursor.execute("UPDATE notes SET title = ?, content = ? WHERE id = ?", (new_title, new_content, note_id))
    
    conn.commit()
    conn.close()
    print("Note updated successfully.")

def delete_note(note_id):
    conn = sqlite3.connect("notes.db")
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM notes WHERE id = ?", (note_id,))
    
    conn.commit()
    conn.close()
    print("Note deleted successfully.")

def main():
    while True:
        print("\nPersonal Notes App")
        print("1. Add Note")
        print("2. View Notes")
        print("3. Update Note")
        print("4. Delete Note")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter note title: ")
            content = input("Enter note content: ")
            add_note(title, content)

        elif choice == "2":
            view_notes()

        elif choice == "3":
            note_id = int(input("Enter note ID to update: "))
            new_title = input("Enter new title: ")
            new_content = input("Enter new content: ")
            update_note(note_id, new_title, new_content)

        elif choice == "4":
            note_id = int(input("Enter note ID to delete: "))
            delete_note(note_id)

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
