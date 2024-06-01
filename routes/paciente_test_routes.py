from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from models.paciente_test import PacienteTest
from schemas.paciente_test_schema import paciente_test_schema

paciente_test_routes = Blueprint("paciente_test_routes", __name__)

@paciente_test_routes.route('/paciente_test', methods=['GET'])
def get_PacienteTest():
    all_aciente_test = PacienteTest.query.all()
    result = paciente_test_schema.dump(all_aciente_test)

    data = {
        'message': 'Todos los Pacientes y su respectivos Test',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)
