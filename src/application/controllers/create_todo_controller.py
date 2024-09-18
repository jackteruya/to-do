from src.infra.database.config.db_config import DBConnectionHandler
from src.infra.database.repository.todo_repository import ToDoRepository
from src.interfaces.todo_repository import ToDoRepositoryInterface
from src.use_case.create_todo import CreateToDoUseCase


class CreateTodoController:

    def __init__(
            self,
            todo_repository: ToDoRepositoryInterface = ToDoRepository(DBConnectionHandler)
    ):
        self.use_case = CreateToDoUseCase(todo_repository)

    def execute(self, todo_data: dict):
        return self.use_case.execute(todo_data)

