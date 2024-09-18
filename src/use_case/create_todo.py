from pydantic import ValidationError

from src.dto.todo_create_dto import ToDoCreateRequest
from src.exception.custom_errors import ParametersError
from src.interfaces.todo_repository import ToDoRepositoryInterface
from src.response import ResponseSuccess, ResponseFailure, ResponseTypes


class CreateToDoUseCase:
    def __init__(self, todo_repository: ToDoRepositoryInterface):
        self._todo_repository = todo_repository

    def execute(self, todo_data: dict):
        try:
            data = ToDoCreateRequest(**todo_data)
            result = self._todo_repository.insert(data.title, data.description, False)
            if not result:
                return ResponseFailure(ResponseTypes.PARAMETERS_ERROR, 'Not Found')
            return ResponseSuccess(result)
        except (ValidationError, ParametersError) as pe:
            return ResponseFailure(
                ResponseTypes.PARAMETERS_ERROR,
                'Fields Required: [{"title": "string", "description": "string"}]'
            )
        except Exception as ex:
            return ResponseFailure(ResponseTypes.SYSTEM_ERROR, 'System Error')
