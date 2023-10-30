from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, current_user, login_required
from app.models import User, Bebeh
from app import db

auth = Blueprint('auth', __name__)
main_ = Blueprint('main_', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    # Your login route code here
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()

        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('main_.home'))  # Use 'main_' to access routes in the 'main_' blueprint
        else:
            flash('Login failed. Please check your credentials.', 'danger')

    return render_template('login.html')

@auth.route('/register', methods=['GET', 'POST'])
def register():
    # Your registration route code here
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Check if the username already exists
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash('Username already exists', 'danger')
        else:
            new_user = User(username=username, password=password)
            db.session.add(new_user)
            db.session.commit()
            flash('Registration successful. You can now log in.', 'success')
            return redirect(url_for('auth.login'))

    return render_template('register.html')

@main_.route('/')
# @login_required  # Use the login_required decorator to protect this route
def home():
    return render_template('home.html')

@main_.route('/bebehs')
@login_required  # Use the login_required decorator to protect this route
def get_bebehs():
    bebehs = Bebeh.query.all()
    output = []
    for bebeh in bebehs:
        bebeh_data = {'name': bebeh.name, 'description': bebeh.description}
        output.append(bebeh_data)
    return {'bebehs': output}