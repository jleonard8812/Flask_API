from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from config import Config



db = SQLAlchemy()
login_manager = LoginManager()
bcrypt = Bcrypt()

def create_app(config_class):
    app = Flask(__name__, template_folder="API/app/templates")
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)

    # Register blueprints and routes
    from app.routes import auth
    from app.routes import main_
    app.register_blueprint(auth)
    app.register_blueprint(main_)
    

    @login_manager.user_loader
    def load_user(user_id):
        from app.models import User  # Import User model here
        return User.query.get(int(user_id))

    return app