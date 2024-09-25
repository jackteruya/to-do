from src.infra.database.config.db_config import DBConnectionHandler
from src.infra.database.repository.todo_repository import ToDoRepository
from src.interfaces.todo_repository import ToDoRepositoryInterface
from src.use_case.partial_update_todo import PartialUpdateToDoUseCase


class PartialUpdateTodoController:

    def __init__(
        self,
        todo_repository: ToDoRepositoryInterface = ToDoRepository(DBConnectionHandler),
    ):
        self.use_case = PartialUpdateToDoUseCase(todo_repository)

    def execute(self, id, todo_data):
        return self.use_case.execute(id, todo_data)
