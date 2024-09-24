from unittest import mock

from src.infra.database.repository.todo_repository import ToDoRepository


def test_delete_todo(create_todo_tester_delete, client):
    result = client.delete(f"api/v1/todo/{create_todo_tester_delete.id}/")
    assert result.status_code == 204


@mock.patch.object(ToDoRepository, "delete", return_value=None)
def test_delete_todo_not_found(mock_delete, client):
    result = client.delete("api/v1/todo/90/")
    assert result.status_code == 404


@mock.patch.object(ToDoRepository, "delete", side_effect=Exception())
def test_delete_todo_system_error(mock_delete, client):
    result = client.delete("api/v1/todo/90/")
    assert result.status_code == 500
