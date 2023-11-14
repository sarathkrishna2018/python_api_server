from werkzeug.security import generate_password_hash, check_password_hash
from app import db


class User(db.Model):
    """
    User model for storing user-related data.
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        """
        Create a hashed password.
        """
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """
        Verify if the provided password matches the stored hash.
        """
        return check_password_hash(self.password_hash, password)
