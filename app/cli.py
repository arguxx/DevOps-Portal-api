"""
Flask CLI commands for database management
"""
import click
from flask.cli import with_appcontext
from app.model import db, User

@click.command('init-db')
@with_appcontext
def init_db_command():
    """Initialize the database."""
    db.create_all()
    click.echo('Initialized the database.')

@click.command('create-admin')
@click.option('--email', prompt=True, help='Admin email address')
@click.option('--password', prompt=True, hide_input=True, confirmation_prompt=True, help='Admin password')
@click.option('--name', prompt=True, help='Admin name')
@with_appcontext
def create_admin_command(email, password, name):
    """Create an admin user."""
    user = User.query.filter_by(email=email).first()
    if user:
        click.echo(f'User with email {email} already exists.')
        return
    
    user = User(email=email, name=name)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    click.echo(f'Admin user {email} created successfully.')

def init_app(app):
    """Register CLI commands with the Flask app."""
    app.cli.add_command(init_db_command)
    app.cli.add_command(create_admin_command)
