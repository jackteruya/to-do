from unittest import mock

from src.dto.todo_create_dto import ToDoCreateRequest
from src.exception.custom_errors import ParametersError
from src.infra.database.repository.todo_repository import ToDoRepository
from src.serializers.todo import ToDoJsonEncoder


def test_healthcheck_todo(client):
    result = client.get(
        f"api/v1/healthcheck/"
    )
    assert result.status_code == 200