from .health_check import health_bp
from .yaml_routes import yaml_bp

def register_routes(app):
    app.register_blueprint(health_bp)
    app.register_blueprint(yaml_bp)