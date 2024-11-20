from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash
import traceback

app = Flask(__name__)
CORS(app)

# Configure MySQL connection
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',  # Replace with your MySQL password
    'database': 'skilldev'
}
db = mysql.connector.connect(**db_config)
cursor = db.cursor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():

            # Get data from the form
            name = request.form.get('name')
            email = request.form.get('email')
            password = request.form.get('password')
            confirm_password = request.form.get('confirm-password')

            if password != confirm_password:
                return jsonify({'error': 'Password do not match!'}),400


            print(f"Name: {name}, Email: {email}, Password: {password}")  # Debug print

            # Check if the email already exists
            cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
            existing_user = cursor.fetchone()

            if existing_user:
                return jsonify({'error': 'Email already exists!'}), 400

            # Simple password check (length must be at least 6 characters)
            if len(password) < 6:
                return jsonify({'error': 'Password must be at least 6 characters long!'}), 400

            # Hash password
            hashed_password = generate_password_hash(password)

            # Insert into the database
            cursor.execute("INSERT INTO users (name, email, password) VALUES (%s, %s, %s)",
                           (name, email, hashed_password))
            db.commit()
            return render_template('login.html')

@app.route('/checklogin', methods=['GET', 'POST'])
def checklogin():
    data = request.form
    email = data.get('email')
    password = data.get('password')

    print(f"Email: {email}, Password: {password}")  # Debug print

    cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
    user = cursor.fetchone()

    if user and check_password_hash(user[3], password):  # user[3] is the password field in the table
        return jsonify({'message': 'Login successful!', 'user': user})
    return jsonify({'error': 'Invalid credentials'}), 401

if __name__ == '__main__':
    app.run(debug=True)

