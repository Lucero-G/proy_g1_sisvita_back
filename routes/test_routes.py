from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from models.test import Test
from schemas.test_schema import test_schema

test_routes = Blueprint("test_routes", __name__)

@test_routes.route('/test', methods=['GET'])
def get_Test():
    all_test = Test.query.all()
    result = test_schema.dump(all_test)

    data = {
        'message': 'Todos los test',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)
