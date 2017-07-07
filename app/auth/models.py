from flask_login import UserMixin

from app import db, bcrypt


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(
        db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)

    @staticmethod
    def hash_password(password):
        return bcrypt.generate_password_hash(password)

    def __repr__(self):
        return '<User {}>'.format(self.username)
