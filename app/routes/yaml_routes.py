from flask import Blueprint, request, Response, make_response
from app.services.yaml_service import generate_deployment, generate_service

yaml_bp = Blueprint("yaml", __name__)

@yaml_bp.route('/api/deployment/generate', methods=['POST'])
def deployment_generate():
    data = request.get_json()
    respon = generate_deployment(data)
    return Response(respon, mimetype='text/plain')

@yaml_bp.route('/api/service/generate', methods=['POST', 'OPTIONS'])
def service_generate():
    if request.method == 'OPTIONS':
        response = make_response()
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'POST, OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Accept'
        return response
        
    data = request.get_json()
    respon = generate_service(data)
    response = make_response(respon)
    response.headers['Content-Type'] = 'text/plain'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Accept'
    response.headers['Access-Control-Allow-Methods'] = 'POST, OPTIONS'
    return response