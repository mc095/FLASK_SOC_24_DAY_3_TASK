from flask import Flask
import sqlite3

app = Flask(__name__)

# Create database and table
with sqlite3.connect('employee.db') as conn:
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS employee (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            address TEXT NOT NULL
        )
    ''')

    conn.commit()

print("Employee database and table created successfully.")
