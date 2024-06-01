from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from models.pregunta import Pregunta
from schemas.pregunta_schema import pregunta_schema

pregunta_routes = Blueprint("pregunta_routes", __name__)

@pregunta_routes.route('/pregunta', methods=['GET'])
def get_Pregunta():
    all_pregunta = Pregunta.query.all()
    result = pregunta_schema.dump(all_pregunta)

    data = {
        'message': 'Todas las Preguntas',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)
