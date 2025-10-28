from flask import Blueprint, jsonify, request

health_bp = Blueprint("health", __name__)

@health_bp.route('/api/healtz', methods=['GET'])
def healtz():
    return "OK", 200

@health_bp.route('/api/live', methods=['GET'])
def live():
    return jsonify({"status": "alive"}), 200

@health_bp.route("/api/hello", methods=["GET"])
def hello():
    name = request.args.get("name", "World")
    return jsonify({"message": f"Hello, {name}!"}), 200

@health_bp.route("/api/hello", methods=["POST"])
def hello_post():
    data = request.get_json()
    name = data.get("name", "World")
    return jsonify({"message": f"Hello (POST), {name}!"}), 200