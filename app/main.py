from flask import Blueprint, render_template
from flask_login import current_user
from flask_login import login_required
from app.models import Bebeh

main = Blueprint('main', __name__)

@main.route('/')
def home():
    bebehs = Bebeh.query.all()
    return render_template('main/home.html', bebehs=bebehs)

@main.route('/protected')
@login_required
def protected_route():
    return "This is a protected route. You are logged in as " + current_user.username