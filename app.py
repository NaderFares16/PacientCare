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

@app.route('/newPatient', methods=['GET', 'POST'])
def newPatient():
  if request.method == 'POST':
    name = request.form['name']
    age = request.form['age']
    gender = request.form['gender']
    document = request.form['document']
    address = request.form['address']
    phone = request.form['phone']

    conn = sqlite3.connect('hospital_management.db')
    cursor = conn.cursor()
    cursor.execute('''
      INSERT INTO patients (
        name,
        age,
        gender,
        document,
        address,
        phone
      ) VALUES (
        ?,
        ?,
        ?,
        ?,
        ?,
        ?
      )
    ''', (name, age, gender, document, address, phone))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))
  return render_template('newPatient.html')

@app.route('/eraseHistory')
def eraseHistory():
  conn = sqlite3.connect('hospital_management.db')
  cursor = conn.cursor()
  cursor.execute('DELETE FROM patients')
  conn.commit()
  conn.close()
  return redirect(url_for('index'))

if __name__ == '__main__':
  app.run(debug=True)