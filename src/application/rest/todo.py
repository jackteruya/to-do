import json

from dulwich.porcelain import status
from flask import Response
from flask_restx import Resource, Namespace, fields

from src.application.controllers.create_todo_controller import CreateTodoController
from src.application.status import STATUS_CODES
from src.serializers.todo import ToDoJsonEncoder

todo_api = Namespace('todo', description='Check status API')


resource_fields = todo_api.model('ToDo', {
    'title': fields.String(required=True),
    'description': fields.String(required=True)
})


@todo_api.route('/', methods=['GET', 'POST'])
class ListCreateToDoApi(Resource):

    @todo_api.doc('list todo')
    def get(self):
        return Response(
            json.dumps({'msg': [{'d': 1}, {'d': 2}, {'d': 3}]}),
            mimetype="application/json",
            status=STATUS_CODES['Success'],
        )

    @todo_api.expect(resource_fields)
    @todo_api.doc('create todo', code=201)
    def post(self, controller = CreateTodoController()):
        result = controller.execute(todo_api.payload)
        return Response(
            json.dumps(result.value, cls=ToDoJsonEncoder),
            mimetype="application/json",
            status=STATUS_CODES[result.type],
        )


@todo_api.route('/<int:id>/', methods=['GET', 'PUT', 'PATCH', 'DELETE'])
class DeleteDetailUpdateToDoApi(Resource):

    @todo_api.doc('detail todo')
    def get(self, id: int):
        return Response(
            json.dumps({'msg': [{'d': 1}, {'d': 2}, {'d': 3}]}),
            mimetype="application/json",
            status=STATUS_CODES['Success'],
        )

    @todo_api.doc('update todo')
    def put(self, id: int):
        return Response(
            json.dumps({'msg': [{'d': 1}, {'d': 2}, {'d': 3}]}),
            mimetype="application/json",
            status=STATUS_CODES['Create'],
        )

    @todo_api.doc('partial update todo')
    def patch(self, id: int):
        return Response(
            json.dumps({'msg': [{'d': 1}, {'d': 2}, {'d': 3}]}),
            mimetype="application/json",
            status=STATUS_CODES['Create'],
        )

    @todo_api.doc('delete todo')
    def delete(self, id: int):
        return Response(
            json.dumps({'msg': [{'d': 1}, {'d': 2}, {'d': 3}]}),
            mimetype="application/json",
            status=STATUS_CODES['Create'],
        )