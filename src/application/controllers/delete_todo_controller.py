from src.infra.database.config.db_config import DBConnectionHandler
from src.infra.database.repository.todo_repository import ToDoRepository
from src.interfaces.todo_repository import ToDoRepositoryInterface
from src.use_case.delete_todo import DeleteToDoUseCase


class DeleteTodoController:

    def __init__(
            self, todo_repository: ToDoRepositoryInterface = ToDoRepository(DBConnectionHandler)
    ):
        self.use_case = DeleteToDoUseCase(todo_repository)

    def execute(self, id: int):
        return self.use_case.execute(id)
