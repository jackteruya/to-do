import json

from flask import Response
from flask_restx import Resource, Namespace, fields

from src.application.controllers.create_todo_controller import CreateTodoController
from src.application.controllers.detail_todo_controller import DetailTodoController
from src.application.controllers.list_todo_controller import ListTodoController
from src.application.controllers.partial_update_todo_controller import PartialUpdateTodoController
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
    def get(self, controller = ListTodoController()):
        result = controller.execute()
        if not result:
            Response(
                json.dumps(result.value),
                mimetype="application/json",
                status=STATUS_CODES[result.type],
            )
        return Response(
            json.dumps(result.value, cls=ToDoJsonEncoder),
            mimetype="application/json",
            status=STATUS_CODES[result.type],
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


resource_fields_patch = todo_api.model('ToDo', {
    'title': fields.String,
    'description': fields.String,
    'completed': fields.Boolean,
    'start_date': fields.Date,
    'end_date': fields.Date,
})

resource_fields_put = todo_api.model('ToDo', {
    'title': fields.String(required=True),
    'description': fields.String(required=True),
    'completed': fields.Boolean(required=True),
    'start_date': fields.Date(required=True),
    'end_date': fields.Date(required=True),
})


@todo_api.route('/<int:id>/', methods=['GET', 'PUT', 'PATCH', 'DELETE'])
class DeleteDetailUpdateToDoApi(Resource):

    @todo_api.doc('detail todo')
    def get(self, id: int, controller = DetailTodoController()):
        result = controller.execute(id)
        return Response(
            json.dumps(result.value, cls=ToDoJsonEncoder),
            mimetype="application/json",
            status=STATUS_CODES[result.type],
        )

    @todo_api.expect(resource_fields_put)
    @todo_api.doc('update todo')
    def put(self, id: int):
        return Response(
            json.dumps({'msg': [{'d': 1}, {'d': 2}, {'d': 3}]}),
            mimetype="application/json",
            status=STATUS_CODES['Create'],
        )

    @todo_api.expect(resource_fields_patch)
    @todo_api.doc('partial update todo')
    def patch(self, id: int, controller = PartialUpdateTodoController()):
        result = controller.execute(id, todo_api.payload)

        if not result:
            json_data = json.dumps(result.value)
        else:
            json_data = json.dumps(result.value, cls=ToDoJsonEncoder)

        return Response(
            json_data,
            mimetype="application/json",
            status=STATUS_CODES[result.type],
        )

    @todo_api.doc('delete todo')
    def delete(self, id: int):
        return Response(
            json.dumps({'msg': [{'d': 1}, {'d': 2}, {'d': 3}]}),
            mimetype="application/json",
            status=STATUS_CODES['Create'],
        )