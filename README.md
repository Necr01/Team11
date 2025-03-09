# Team11
**Overview of Database System Architectures**
1. Single Tier Architecture
Description: The application and database run on the same system.
Example: A local note-taking app using SQLite with a Python script.
Advantages: Simple to set up, quick data access, no reliance on a network.
Disadvantages: Limited scalability, not suitable for multi-user environments.

2. Two-Tier Architecture
Description: A client-server setup where the client communicates directly with a database hosted on a separate server.
Example: A Python application interacting with a MySQL database for CRUD operations.
Advantages: Supports multiple clients, improved scalability.
Disadvantages: More complex than single-tier, potential performance bottlenecks.

3. Three-Tier Architecture
Description: Incorporates an intermediary application server between the client and database to manage business logic.
Example: A web application using Flask for the backend, MySQL for data storage, and a browser-based frontend.
Advantages: Enhanced security, scalability, and flexibility.
Disadvantages: More complex to set up and maintain.

Steps to Run or Test Implementations
1. Single-Tier Architecture (SQLite + Python)
Prerequisites:

Install Python (if not already installed).
SQLite (pre-included with Python).
Setup & Execution:

Create an SQLite database (notes.db).
Write a Python script to handle database operations like adding, deleting, and retrieving notes.
Run the script with:

python script.py

Use Python queries or an SQLite viewer to confirm changes.

2. Two-Tier Architecture (SQLite + Python Client)

Prerequisites:

Install Python.

SQLite is already included with Python.

Setup & Execution:


Create an SQLite database (notes.db).

Develop a Python script to execute SQL queries and interact with the database.

Run the client script using:

python client.py

Verify database modifications through an SQLite viewer.

3. Three-Tier Architecture (SQLite + Python + Web Frontend)
   
Prerequisites:

Install Python.

SQLite (built into Python).

A web browser (e.g., Chrome, Firefox).

Setup & Execution:

Database: Create notes.db in SQLite.

Backend (Python): Develop a Python script to handle data interactions (add, delete, fetch notes).

Frontend (HTML, CSS, JavaScript): Create a web interface for user interaction. Use JavaScript (Fetch API) to communicate with the backend.

Running the Application:

Start the Python server:

python -m http.server 8000

Open a web browser and visit:

http://localhost:8000

Perform CRUD operations through the web interface, with the frontend interacting with the backend.

Summary
This project explores different database system architectures using SQLite, Python, HTML, CSS, and JavaScript:

Single-Tier: A standalone Python script communicates directly with SQLite.
Two-Tier: A separate Python client connects to an SQLite database, ensuring better separation of concerns.
Three-Tier: A web-based approach with a frontend (HTML, CSS, JavaScript), a backend (Python server), and an SQLite database for data management.
