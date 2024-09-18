from src.infra.database.config.db_config import DBConnectionHandler
from src.infra.database.repository.todo_repository import ToDoRepository
from src.interfaces.todo_repository import ToDoRepositoryInterface
from src.use_case.list_todo import ListToDoUseCase


class ListTodoController:

    def __init__(self, todo_repository: ToDoRepositoryInterface = ToDoRepository(DBConnectionHandler)):
        self._use_case = ListToDoUseCase(todo_repository)

    def execute(self):
        return self._use_case.execute()
