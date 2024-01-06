from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_login import login_required
import os

# def create_database():
#     if not os.path.exists("nation.db"):
#         db.create_all()
#         print("Database 'nation' created successfully.")


login_manager = LoginManager()
db = SQLAlchemy()
bcrypt = Bcrypt()