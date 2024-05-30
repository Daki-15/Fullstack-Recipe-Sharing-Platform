from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from models import User, db
import os

# Get the current directory
basedir = os.path.abspath(os.path.dirname(__file__))

# Set the database file path
db_path = os.path.join(basedir, 'DB', 'test.db')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path # Set the SQLALCHEMY_DATABASE_URI configuration
app.config['SECRET_KEY'] = 'your-secret-key'  # Replace with your secret key

db.init_app(app)
with app.app_context():
    db.create_all() # This line creates the tables in the database

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Import routes
from routes import *

if __name__ == "__main__":
    app.run(debug=True)
