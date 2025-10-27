from flask import Flask
from flask_cors import CORS
from .config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Aktifkan CORS biar bisa diakses dari Angular nanti
    CORS(app)
    
    # Import dan daftarkan blueprint
    from .routes.yaml_routes import yaml_bp
    app.register_blueprint(yaml_bp, url_prefix="/api/yaml")
    
    return app
