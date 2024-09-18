import json

from flask import Response
from flask_restx import Namespace, Resource
from src.application.status import STATUS_CODES

health = Namespace('healthcheck', description='Check status API')


@health.route('/', methods=['GET', ])
class HealthCheck(Resource):

    def get(self):
        return Response(
            json.dumps({'msg': 'Status OK'}),
            mimetype="application/json",
            status=STATUS_CODES['Success'],
        )
