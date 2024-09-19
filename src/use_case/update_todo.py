import re
from datetime import datetime

from pydantic import ValidationError

from src.dto.todo_update_dto import ToDoUpdateRequest
from src.exception.custom_errors import ParametersError
from src.interfaces.todo_repository import ToDoRepositoryInterface
from src.response import ResponseFailure, ResponseTypes, ResponseSuccess


class UpdateToDoUseCase:
    def __init__(self, todo_repository: ToDoRepositoryInterface):
        self._todo_repository = todo_repository

    def execute(self, id: int, todo_data: dict):
        try:
            data = ToDoUpdateRequest(**todo_data)
            if self._todo_repository.edit_todo(id, data.title, data.description, data.completed, data.start_date, data.end_date):
                result = self._todo_repository.get_by_id(id)
                if result:
                    return ResponseSuccess(result)
            return ResponseFailure(ResponseTypes.NOT_FOUND_ERROR, 'Not Found')
        except (ValidationError, ParametersError) as pe:
            return ResponseFailure(
                ResponseTypes.PARAMETERS_ERROR,
                'Fields Required: ['
                '{"title": "string", '
                '"description": "string", '
                '"completed": "boolean", '
                '"start_date": "date", '
                '"end_date": "date"}]'
            )
        except Exception as ex:
            return ResponseFailure(ResponseTypes.SYSTEM_ERROR, 'System Error')
