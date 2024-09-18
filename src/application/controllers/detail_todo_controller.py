from src.infra.database.config.db_config import DBConnectionHandler
from src.infra.database.repository.todo_repository import ToDoRepository
from src.interfaces.todo_repository import ToDoRepositoryInterface
from src.use_case.detail_todo import DetailToDoUseCase


class DetailTodoController:

    def __init__(
            self, todo_repository: ToDoRepositoryInterface = ToDoRepository(DBConnectionHandler)
    ):
        self.use_case = DetailToDoUseCase(todo_repository)

    def execute(self, id: int):
        return self.use_case.execute(id)
