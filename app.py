# # hero app.py
#
# # from flask import Flask, render_template, request, jsonify
# # from flask_cors import CORS
# # import mysql.connector
# #
# # app = Flask(__name__)
# # CORS(app)
# #
# # # Configure MySQL connection
# # db_config = {
# #     'host': 'localhost',
# #     'user': 'root',
# #     'password': 'root',  # Replace with your MySQL password
# #     'database': 'skilldev'
# # }
# # db = mysql.connector.connect(**db_config)
# # cursor = db.cursor()
# #
# # @app.route('/')
# # def index():
# #     return render_template('index.html')
# #
# # @app.route('/signup', methods=['POST'])
# # def signup():
# #     data = request.json
# #     try:
# #         cursor.execute("INSERT INTO users (name, email, password) VALUES (%s, %s, %s)",
# #                        (data['name'], data['email'], data['password']))
# #         db.commit()
# #         return jsonify({'message': 'User registered successfully!'})
# #     except Exception as e:
# #         return jsonify({'error': str(e)}), 400
# #
# # @app.route('/login', methods=['POST'])
# # def login():
# #     data = request.json
# #     cursor.execute("SELECT * FROM users WHERE email = %s AND password = %s",
# #                    (data['email'], data['password']))
# #     user = cursor.fetchone()
# #     if user:
# #         return jsonify({'message': 'Login successful!', 'user': user})
# #     return jsonify({'error': 'Invalid credentials'}), 401
# #
# # if __name__ == '__main__':
# #     app.run(debug=True)
#
# # hero + register app.py
# from flask import Flask, render_template, request, jsonify
# from flask_cors import CORS
# import mysql.connector
#
#
# app = Flask(__name__)
# # Allow requests from specific frontend URL
# CORS(app)
#
# # Configure MySQL connection
# db_config = {
#     'host': 'localhost',
#     'user': 'root',
#     'password': 'root',  # Replace with your MySQL password
#     'database': 'skilldev'
# }
# db = mysql.connector.connect(**db_config)
# cursor = db.cursor()
#
#
# @app.route('/')
# def index():
#     return render_template('index.html')
#
#
# @app.route('/signup', methods=['POST'])
# def signup():
#     data = request.json
#     name = data.get('name')
#     email = data.get('email')
#     password = data.get('password')
#
#     # Check if the email already exists
#     cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
#     existing_user = cursor.fetchone()
#
#     if existing_user:
#         return jsonify({'error': 'Email already exists!'}), 400
#
#     # Simple password check (length must be at least 6 characters)
#     if len(password) < 6:
#         return jsonify({'error': 'Password must be at least 6 characters long!'}), 400
#
#     try:
#         cursor.execute("INSERT INTO users (name, email, password) VALUES (%s, %s, %s)",
#                        (name, email, password))
#         db.commit()
#         return jsonify({'message': 'User registered successfully!'})
#     except Exception as e:
#         return jsonify({'error': str(e)}), 400
#
#
# @app.route('/login', methods=['POST'])
# def login():
#     data = request.json
#     email = data.get('email')
#     password = data.get('password')
#
#     cursor.execute("SELECT * FROM users WHERE email = %s AND password = %s",
#                    (email, password))
#     user = cursor.fetchone()
#
#     if user:
#         return jsonify({'message': 'Login successful!', 'user': user})
#     return jsonify({'error': 'Invalid credentials'}), 401
#
#
# if __name__ == '__main__':
#     app.run(debug=True)



# method not found error resolution code

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

# @app.route('/signup', methods=['GET', 'POST'])
# def signup():
#     if request.method == 'POST':
#         # Get data from the form
#         name = request.form.get('name')
#         email = request.form.get('email')
#         password = request.form.get('password')
#
#         # Check if the email already exists
#         cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
#         existing_user = cursor.fetchone()
#
#         if existing_user:
#             return jsonify({'error': 'Email already exists!'}), 400
#
#         # Simple password check (length must be at least 6 characters)
#         if len(password) < 6:
#             return jsonify({'error': 'Password must be at least 6 characters long!'}), 400
#
#         # Hash password
#         hashed_password = generate_password_hash(password)
#
#         try:
#             cursor.execute("INSERT INTO users (name, email, password) VALUES (%s, %s, %s)",
#                            (name, email, hashed_password))
#             db.commit()
#             return jsonify({'message': 'User registered successfully!'})
#         except Exception as e:
#             return jsonify({'error': str(e)}), 400
#
#     # For GET request, render the signup form
#     return render_template('register.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        try:
            # Get data from the form
            name = request.form.get('name')
            email = request.form.get('email')
            password = request.form.get('password')

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
            return jsonify({'message': 'User registered successfully!'})
        except Exception as e:
            # Log the actual error and traceback
            print(f"Error occurred: {e}")
            print(traceback.format_exc())  # This will print the full traceback
            return jsonify({'error': 'An error occurred. Please try again later.'}), 500

    # For GET request, render the signup form
    return render_template('register.html')
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
    user = cursor.fetchone()

    if user and check_password_hash(user[3], password):  # user[3] is the password field in the table
        return jsonify({'message': 'Login successful!', 'user': user})
    return jsonify({'error': 'Invalid credentials'}), 401

if __name__ == '__main__':
    app.run(debug=True)

