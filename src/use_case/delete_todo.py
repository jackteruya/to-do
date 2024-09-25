from src.interfaces.todo_repository import ToDoRepositoryInterface
from src.response import ResponseDelete, ResponseFailure, ResponseTypes


class DeleteToDoUseCase:
    def __init__(self, todo_repository: ToDoRepositoryInterface):
        self._todo_repository = todo_repository

    def execute(self, id: int):
        try:
            result = self._todo_repository.delete(id)
            if not result:
                return ResponseFailure(ResponseTypes.NOT_FOUND_ERROR, "Not Found")
            return ResponseDelete()
        except Exception:
            return ResponseFailure(ResponseTypes.SYSTEM_ERROR, "System Error")
