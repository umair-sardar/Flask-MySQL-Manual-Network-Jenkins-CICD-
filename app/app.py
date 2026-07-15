import os
import time
from flask import Flask, render_template, request, redirect  # <--- Galti yahan thi, 'url_parser' ko hata diya hai
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# Database Configuration
DB_HOST = os.environ.get('DB_HOST', 'mysql-container')
DB_USER = os.environ.get('DB_USER', 'root')
DB_PASSWORD = os.environ.get('DB_PASSWORD', 'rootpassword')
DB_NAME = os.environ.get('DB_NAME', 'mydb')

def get_db_connection():
    connection = None
    for i in range(5):
        try:
            connection = mysql.connector.connect(
                host=DB_HOST,
                user=DB_USER,
                password=DB_PASSWORD,
                database=DB_NAME
            )
            if connection.is_connected():
                return connection
        except Error as e:
            print(f"Database connection failed (attempt {i+1}/5): {e}")
            time.sleep(3)
    return None

@app.route('/')
def index():
    conn = get_db_connection()
    if not conn:
        return "Database Connection Error!", 500
    
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', users=users)

@app.route('/add', methods=['POST'])
def add_user():
    name = request.form.get('name')
    email = request.form.get('email')
    
    if name and email:
        conn = get_db_connection()
        if conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
            conn.commit()
            cursor.close()
            conn.close()
            
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
