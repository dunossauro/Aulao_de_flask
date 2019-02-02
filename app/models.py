from app import db


class User(db.Model):
    """Modelo do usuário."""

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), index=True, unique=True)
    username = db.Column(db.String(60), index=True, unique=True)
    password = db.Column(db.String(60), index=True, unique=True)


def configure(app):
    app.db = db
