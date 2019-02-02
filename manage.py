from flask import current_app, Flask
import click
from flask.cli import with_appcontext


@click.command
@with_appcontext
def rprod():
    config = current_app.config
    click.echo(config["TEST_VARIABLE"])


def create_app():
    app = Flask(__name__)
    app.cli.add_command(rprod)
    return app
