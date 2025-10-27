from flask import Blueprint, jsonify


health_bp = Blueprint("health", __name__)

@health_bp.route('/api/healtz', methods=['GET'])
def healtz():
    return "OK", 200

@health_bp.route('/api/live', methods=['GET'])
def live():
    return jsonify({"status": "alive"}), 200
