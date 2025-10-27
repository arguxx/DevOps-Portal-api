from flask import Blueprint

health_bp = Blueprint("healtz", __name__)

@health_bp.route('/api/healtz', methods=['GET'])
def healtz():
    return "OK", 200