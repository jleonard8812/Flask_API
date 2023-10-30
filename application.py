
# from flask import Flask
# app = Flask(__name__)
# from flask_sqlalchemy import SQLAlchemy
# from flask_login import LoginManager
# from flask_bcrypt import Bcrypt
# from flask import render_template, request, flash, redirect, url_for
# from app.models import User
# from flask_login import login_user

# # set up some app variable stuff
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
# db = SQLAlchemy(app)
# login_manager = LoginManager(app)
# bcrypt = Bcrypt(app)

# # Create API routes
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form.get('username')
#         password = request.form.get('password')

#         user = User.query.filter_by(username=username).first()

#         if user and user.check_password(password):
#             login_user(user)
#             return redirect(url_for('protected_route'))
#         else:
#             flash('Login failed. Please check your credentials.', 'danger')

#     return render_template('login.html')



# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         username = request.form.get('username')
#         password = request.form.get('password')

#         # Check if the username already exists
#         existing_user = User.query.filter_by(username=username).first()
#         if existing_user:
#             flash('Username already exists', 'danger')
#         else:
#             new_user = User(username=username, password=password)
#             db.session.add(new_user)
#             db.session.commit()
#             flash('Registration successful. You can now log in.', 'success')
#             return redirect(url_for('login'))

#     return render_template('register.html')  # Replace with your actual template name


# @app.route('/')
# def index():
#     return('Hello!')


# @app.route('/bebehs')
# def get_bebehs():
#     from app.models import Bebeh
#     bebehs = Bebeh.query.all()
#     output = []
#     for bebeh in bebehs:
#         bebeh_data = {'name': bebeh.name, 'description': bebeh.description}

#         output.append(bebeh_data)
#     return {'bebehs': output}

# # @app.route('/bebehs', methods= ['POST'])
# # def add_bebeh:
# #     bebeh = 

# application.py
from app import create_app
from config import Config

app = create_app(Config)
if __name__ == '__main__':
    app.run()