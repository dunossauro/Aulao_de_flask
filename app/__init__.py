from flask import Flask, current_app
from flask.cli import with_appcontext
import click
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from os import environ


db = SQLAlchemy()


class User(db.Model):
    """Modelo do usuário."""

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), index=True, unique=True)
    username = db.Column(db.String(60), index=True, unique=True)
    password = db.Column(db.String(60), index=True, unique=True)

    def __repr__(self):
        return f'User(email={self.email}, username={self.username}, password={self.password})'


@click.command()
@with_appcontext
def sconfig():
    from pprint import pprint
    pprint(current_app.config)


def create_app():
    app = Flask(__name__)

    db.init_app(app)
    migrate = Migrate(app, db)
    app.config.from_object(f"config.{environ.get('FLASK_ENV')}")
    app.cli.add_command(sconfig)
    app.user = User

    from app.api import api
    app.register_blueprint(api)

    return app
