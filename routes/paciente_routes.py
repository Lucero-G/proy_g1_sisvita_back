from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from models.paciente import Paciente
from schemas.paciente_schema import paciente_schema

paciente_routes = Blueprint("paciente_routes", __name__)

@paciente_routes.route('/paciente', methods=['POST'])
def create_Paciente():
    descripcion = request.json.get('descripcion')


    new_paciente = Paciente(descripcion)

    db.session.add(new_paciente)
    db.session.commit()

    result = paciente_schema.dump(new_paciente)

    data = {
        'message': 'Nuevo Paciente creado!',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

@paciente_routes.route('/paciente', methods=['GET'])
def get_Paciente():
    all_paciente = Paciente.query.all()
    result = paciente_schema.dump(all_paciente)

    data = {
        'message': 'Todos los Pacientes',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)
