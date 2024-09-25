from src.interfaces.todo_repository import ToDoRepositoryInterface
from src.response import ResponseFailure, ResponseSuccess, ResponseTypes


class ListToDoUseCase:
    def __init__(self, todo_repository: ToDoRepositoryInterface):
        self._todo_repository = todo_repository

    def execute(self):
        try:
            result = self._todo_repository.list_todos()
            if result is None:
                return ResponseFailure(ResponseTypes.PARAMETERS_ERROR, "Not Found")
            return ResponseSuccess(result)
        except Exception:
            return ResponseFailure(ResponseTypes.SYSTEM_ERROR, "System Error")
