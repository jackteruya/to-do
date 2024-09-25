from unittest import mock

from src.infra.database.repository.todo_repository import ToDoRepository


def test_list_todo(create_todo_tester, client):
    result = client.get("api/v1/todo/")
    assert result.status_code == 200


@mock.patch.object(ToDoRepository, "list_todos", return_value=None)
def test_list_todo_not_found(mock_list_todos, client):
    result = client.get("api/v1/todo/")
    assert result.status_code == 400


@mock.patch.object(ToDoRepository, "list_todos", side_effect=Exception())
def test_list_todo_system_error(mock_list_todos, client):
    result = client.get("api/v1/todo/")
    assert result.status_code == 500
