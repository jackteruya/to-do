import re
from datetime import date, datetime

from src.interfaces.todo_repository import ToDoRepositoryInterface
from src.response import ResponseFailure, ResponseTypes, ResponseSuccess


class PartialUpdateToDoUseCase:
    def __init__(self, todo_repository: ToDoRepositoryInterface):
        self._todo_repository = todo_repository

    def execute(self, id: int, data: dict):
        try:
            update_data = self.validate_data(data)
            if self._todo_repository.edit_partial_todo(id, update_data):
                result = self._todo_repository.get_by_id(id)
                if not result:
                    return ResponseFailure(ResponseTypes.NOT_FOUND_ERROR, 'Not Found')
                return ResponseSuccess(result)
            return ResponseFailure(ResponseTypes.NOT_FOUND_ERROR, 'Not Found')
        except Exception as ex:
            return ResponseFailure(ResponseTypes.SYSTEM_ERROR, 'System Error')

    @staticmethod
    def validate_data(data: dict):
        update_data = dict()
        for k, v in data.items():
            if v is not None:
                if isinstance(v, str) and re.match(r"(\d{4}-\d{2}-\d{2})", v):
                    v = datetime.strptime(v, '%Y-%m-%d')
                update_data[k] = v
        return update_data
