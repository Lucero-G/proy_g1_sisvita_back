from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from models.especialista import Especialista
from schemas.especialista_schema import especialista_schema

especialista_routes = Blueprint("especialista_routes", __name__)

@especialista_routes.route('/especialista', methods=['POST'])
def create_Especialista():
    descripcion = request.json.get('descripcion')


    new_especialista = Especialista(descripcion)

    db.session.add(new_especialista)
    db.session.commit()

    result = especialista_schema.dump(new_especialista)

    data = {
        'message': 'Nuevo Especialista creado!',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

@especialista_routes.route('/predio', methods=['GET'])
def get_Especialista():
    all_predios = Especialista.query.all()
    result = especialista_schema.dump(all_predios)

    data = {
        'message': 'Todos los Especialistas',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)
