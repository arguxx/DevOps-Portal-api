import os
from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from .config import config
from .model import db

migrate = Migrate()

def create_app(config_name=None):
    """Application factory pattern"""
    if config_name is None:
        config_name = os.getenv('FLASK_ENV', 'development')
    
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_object(config.get(config_name, config['default']))
    
    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    CORS(app)
    
    # Register blueprints
    from .routes import register_routes
    register_routes(app)
    
    # Register CLI commands
    from . import cli
    cli.init_app(app)
    
    # Create database tables
    with app.app_context():
        db.create_all()
    
    return app