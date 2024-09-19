from unittest import mock

from src.dto.todo_update_dto import ToDoUpdateRequest
from src.exception.custom_errors import ParametersError
from src.infra.database.repository.todo_repository import ToDoRepository
from src.serializers.todo import ToDoJsonEncoder


def test_partial_update_todo(create_todo_tester, client):
    data = ToDoJsonEncoder().default(create_todo_tester)
    data['completed'] = True
    data['start_date'] = '2024-09-18'
    data['end_date'] = '2024-09-18'
    result = client.patch(
        f"api/v1/todo/{create_todo_tester.id}/",
        json=data
    )
    assert result.status_code == 200
    assert result.json == data
    assert result.json['end_date'] == '2024-09-18'


def test_partial_update_todo_validation_error(create_todo_tester, client):
    data = ToDoJsonEncoder().default(create_todo_tester)
    data['completed'] = '2024-09-18'
    result = client.patch(
        f"api/v1/todo/{create_todo_tester.id}/",
        json=data
    )
    assert result.status_code == 400


def test_partial_update_todo_validation_error_data(create_todo_tester, client):
    data = ToDoJsonEncoder().default(create_todo_tester)
    data['end_date'] = True
    result = client.patch(
        f"api/v1/todo/{create_todo_tester.id}/",
        json=data
    )
    assert result.status_code == 400


def test_partial_update_todo_not_found(create_todo_tester, client):
    data = ToDoJsonEncoder().default(create_todo_tester)
    data['start_date'] = '2024-09-18'
    data['end_date'] = '2024-09-18'
    result = client.patch(
        f"api/v1/todo/90/",
        json=data
    )
    assert result.status_code == 404


@mock.patch.object(ToDoRepository, "edit_partial_todo", side_effect=Exception())
def test_partial_update_todo_system_error(mock_get_by_id, create_todo_tester, client):
    data = ToDoJsonEncoder().default(create_todo_tester)
    data['start_date'] = '2024-09-18'
    data['end_date'] = '2024-09-18'
    result = client.patch(
        f"api/v1/todo/90/",
        json=data
    )
    assert result.status_code == 500