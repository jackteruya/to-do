from unittest import mock

from src.dto.todo_create_dto import ToDoCreateRequest
from src.exception.custom_errors import ParametersError
from src.infra.database.repository.todo_repository import ToDoRepository
from src.serializers.todo import ToDoJsonEncoder


def test_create_todo(client):
    data = {
        "title": "string",
        "description": "string"
    }
    result = client.post(
        f"api/v1/todo/",
        json=data
    )
    assert result.status_code == 201


@mock.patch.object(ToDoCreateRequest, "__init__", side_effect=ParametersError(message='error'))
def test_update_todo_validation_error(mock___init__, client):
    data = {
        "title": "string",
        "description": "string"
    }
    result = client.post(
        f"api/v1/todo/",
        json=data
    )
    assert result.status_code == 400


@mock.patch.object(ToDoRepository, "insert", return_value=None)
def test_detail_todo_not_found(mock_insert, client):
    data = {
        "title": "string",
        "description": "string"
    }
    result = client.post(
        f"api/v1/todo/",
        json=data
    )
    assert result.status_code == 400


@mock.patch.object(ToDoRepository, "insert", side_effect=Exception())
def test_detail_todo_system_error(mock_insert, client):
    data = {
        "title": "string",
        "description": "string"
    }
    result = client.post(
        f"api/v1/todo/",
        json=data
    )
    assert result.status_code == 500