from unittest import mock

from src.infra.database.repository.todo_repository import ToDoRepository
from src.serializers.todo import ToDoJsonEncoder


def test_detail_todo(create_todo_tester, client):
    data = ToDoJsonEncoder().default(create_todo_tester)
    result = client.get(f"api/v1/todo/{create_todo_tester.id}/")
    assert result.status_code == 200
    assert result.json == data


def test_detail_todo_not_found(client):
    result = client.get("api/v1/todo/90/")
    assert result.status_code == 404


@mock.patch.object(ToDoRepository, "get_by_id", side_effect=Exception())
def test_detail_todo_system_error(mock_get_by_id, client):
    result = client.get("api/v1/todo/90/")
    assert result.status_code == 500
