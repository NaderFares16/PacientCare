from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Database Connection
conn = sqlite3.connect('hospital_management.db')
cursor = conn.cursor()

# Entity Creation
cursor.execute('''
  CREATE TABLE IF NOT EXISTS patients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    gender TEXT,
    document TEXT UNIQUE,
    address TEXT,
    phone TEXT       
  )
''')

conn.commit()
conn.close()

@app.route('/')
def index():
  conn = sqlite3.connect('hospital_management.db')
  cursor = conn.cursor()
  cursor.execute('SELECT * FROM patients')
  patients = cursor.fetchall()
  conn.close()
  return render_template('index.html', patients=patients)