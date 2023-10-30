from app import db
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()  # Initialize the Bcrypt object

class Bebeh(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    description = db.Column(db.String(300))

    def __repr__(self):
        return f"{self.name} - {self.description}"

class User(db.Model):
    username = db.Column(db.String(40), unique=True, primary_key=True)
    password = db.Column(db.String(60), nullable=False)  # Increased length to store the hashed password
    def get_id(self):
        return str(self.username) 

    def __init__(self, username, password):
        self.username = username
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)