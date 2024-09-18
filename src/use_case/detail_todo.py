from src.interfaces.todo_repository import ToDoRepositoryInterface
from src.response import ResponseFailure, ResponseSuccess, ResponseTypes


class DetailToDoUseCase:
    def __init__(self, todo_repository: ToDoRepositoryInterface):
        self._todo_repository = todo_repository

    def execute(self, id: int):
        try:
            result = self._todo_repository.get_by_id(id)
            if not result:
                return ResponseFailure(ResponseTypes.NOT_FOUND_ERROR, 'Not Found')
            return ResponseSuccess(result)
        except Exception as ex:
            return ResponseFailure(ResponseTypes.SYSTEM_ERROR, 'System Error')
