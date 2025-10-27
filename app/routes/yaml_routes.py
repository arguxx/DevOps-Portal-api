from flask import Blueprint, request, Response
from app.services.yaml_service import generate_deployment
from app.services.yaml_service import generate_service


yaml_bp = Blueprint("yaml", __name__)

@yaml_bp.route('/api/deployment/generate', methods=['POST'])
def deployment_generate():
    data = request.get_json()
    respon = generate_deployment(data)
    return Response(respon, mimetype='text/plain')


@yaml_bp.route('/api/service/generate', methods=['POST'])
def service_generate():
    data = request.get_json()
    respon = generate_service(data)
    return Response(respon, mimetype='text/plain')

