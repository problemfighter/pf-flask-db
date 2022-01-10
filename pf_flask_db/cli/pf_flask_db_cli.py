import click
from flask.cli import AppGroup, with_appcontext

pf_flask_db_cli = AppGroup("db-cli", help="PF Flask Database Manipulation")
_pf_flask_db_cli_db = None
_DB_CONFIG_NOT_FOUND = 'Database Configuration Not Found'


@pf_flask_db_cli.command("init", help="Initialize database tables")
@with_appcontext
def initialize():
    if _pf_flask_db_cli_db:
        _pf_flask_db_cli_db.create_all()
        click.secho('Successfully Initialize Database Tables', fg="blue", bold=True)
    else:
        click.secho(_DB_CONFIG_NOT_FOUND, fg="blue", bold=True)


@pf_flask_db_cli.command("destroy", help="Delete database tables")
@with_appcontext
def destroy():
    if _pf_flask_db_cli_db:
        _pf_flask_db_cli_db.drop_all()
        click.secho('Successfully Delete Database Tables', fg="green", bold=True)
    else:
        click.secho(_DB_CONFIG_NOT_FOUND, fg="blue", bold=True)


def init_flask_db_cli(app, db):
    global _pf_flask_db_cli_db
    _pf_flask_db_cli_db = db
    if app:
        app.cli.add_command(pf_flask_db_cli)
