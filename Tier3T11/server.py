import http.server
import json
import sqlite3
from urllib.parse import urlparse, parse_qs

# Database initialization
conn = sqlite3.connect("notes.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY AUTOINCREMENT, content TEXT)")
conn.commit()
conn.close()

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        """Handles GET requests (Fetching notes or serving static files)."""
        if self.path == "/api/notes":
            conn = sqlite3.connect("notes.db")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM notes")
            notes = [{"id": row[0], "content": row[1]} for row in cursor.fetchall()]
            conn.close()

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(notes).encode())
        else:
            super().do_GET()  # Serve HTML, CSS, and JS files normally

    def do_POST(self):
        """Handles POST requests (Adding, Updating, Deleting notes)."""
        content_length = int(self.headers["Content-Length"])
        post_data = json.loads(self.rfile.read(content_length).decode())

        if self.path == "/api/add_note":
            self.add_note(post_data)
        elif self.path == "/api/update_note":
            self.update_note(post_data)
        elif self.path == "/api/delete_note":
            self.delete_note(post_data)

    def add_note(self, post_data):
        """Adds a new note to the database."""
        conn = sqlite3.connect("notes.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO notes (content) VALUES (?)", (post_data["content"],))
        conn.commit()
        conn.close()

        self.send_response(201)
        self.end_headers()

    def update_note(self, post_data):
        """Updates an existing note in the database."""
        conn = sqlite3.connect("notes.db")
        cursor = conn.cursor()
        cursor.execute("UPDATE notes SET content = ? WHERE id = ?", (post_data["content"], post_data["id"]))
        conn.commit()
        conn.close()

        self.send_response(200)
        self.end_headers()

    def delete_note(self, post_data):
        """Deletes a note from the database."""
        conn = sqlite3.connect("notes.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM notes WHERE id = ?", (post_data["id"],))
        conn.commit()
        conn.close()

        self.send_response(200)
        self.end_headers()

# Start the server
if __name__ == "__main__":
    PORT = 8080
    print(f"Server running on http://localhost:{PORT}")
    http.server.test(HandlerClass=MyHandler, port=PORT)
