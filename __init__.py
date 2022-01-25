# import packages
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# init SQLAlchemy to use later in models.py
db = SQLAlchemy()

def create_app():
    # create the Flask instance; __name__ is the name of the current Python module
    app = Flask(__name__) 
    app.config['SECRET_KEY'] = 'secret-key-goes-here' # used by Flask and extensions to keep data safe
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite' # the path where the SQLite database file will be saved
    # deactivate Flask-SQLAlchemy track modifications
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
    
    # initialize the SQLite database
    db.init_app(app) 

    # the login manager contains the code that lets the application and Flask-Login work together
    # create a Login Manager instance
    login_manager = LoginManager() 
    # define the redirection when login is required and user attempts to access without being logged in
    login_manager.login_view = 'auth.login' 
    # configure it for login
    login_manager.init_app(app) 

    from models import User
    @login_manager.user_loader
    def load_user(user_id): #reload user object from the user ID stored in the session
                            # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(user_id))

    # blueprint for auth routes in our app
    # blueprint allows you to organize your flask app
    from auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    # blueprint for non-auth parts of app
    from main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    return app
