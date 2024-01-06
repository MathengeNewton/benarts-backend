from flask_login import UserMixin
from app.extensions import db, login_manager, bcrypt
import uuid
from sqlalchemy.dialects.postgresql import UUID


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

class Users(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True, unique=True)
    username = db.Column(db.String(64))
    email = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(128))
    created_at = db.Column(db.Date)
    updated_at = db.Column(db.Date, nullable=True)
    
    def __init__(self, username, password, email, created_at):
        self.username = username
        self.email = email
        self.password = password
        self.created_at = created_at

    def get_user_by_id(self):
        return str(self.id)

    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password)

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)
    
    @classmethod
    def get_user_by_email(cls, email):
        return cls.query.filter_by(email=email).first()