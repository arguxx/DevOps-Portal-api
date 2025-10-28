from flask_sqlalchemy import SQLAlchemy

# Initialize SQLAlchemy instance
db = SQLAlchemy()

# Import models to register them with SQLAlchemy
from .user_model import User
from .deployment_model import Deployment, Service

__all__ = ['db', 'User', 'Deployment', 'Service']