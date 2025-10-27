# from app import create_app
from app.routes import register_routes
from flask import Flask

app = Flask(__name__)

register_routes(app)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
