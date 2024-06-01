from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from models.tratamiento import Tratamiento
from schemas.tratamiento_schema import tratamiento_schema

tratamiento_routes = Blueprint("tratamiento_routes", __name__)

@tratamiento_routes.route('/tratamiento', methods=['GET'])
def get_Tratamiento():
    all_tratamiento = Tratamiento.query.all()
    result = tratamiento_schema.dump(all_tratamiento)

    data = {
        'message': 'Todos los tratamientos',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)
