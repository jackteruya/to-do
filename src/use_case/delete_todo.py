from src.interfaces.todo_repository import ToDoRepositoryInterface
from src.response import ResponseFailure, ResponseTypes, ResponseSuccess, ResponseDelete


class DeleteToDoUseCase:
    def __init__(self, todo_repository: ToDoRepositoryInterface):
        self._todo_repository = todo_repository

    def execute(self, id: int):
        try:
            result = self._todo_repository.delete(id)
            if not result:
                return ResponseFailure(ResponseTypes.NOT_FOUND_ERROR, 'Not Found')
            return ResponseDelete()
        except Exception as ex:
            return ResponseFailure(ResponseTypes.SYSTEM_ERROR, 'System Error')
