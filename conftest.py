
from pytest import fixture

from src.application import server
from src.infra.database.config import DBConnectionHandler
from src.infra.database.repository.todo_repository import ToDoRepository


@fixture
def application():
    server.app.config["TESTING"] = True
    server.app.testing = True
    return server.app


@fixture
def client(application):
    with application.test_client() as client:
        yield client


@fixture(scope='session')
def create_todo_tester():
    db = ToDoRepository(DBConnectionHandler)
    todo = db.insert(
        title='Teste ToDO',
        description='Criando teste',
        completed=False
    )

    yield todo

    db.delete(todo.id)


@fixture(scope='function')
def create_todo_tester_delete():
    db = ToDoRepository(DBConnectionHandler)
    todo = db.insert(
        title='Teste ToDO',
        description='Criando teste',
        completed=False
    )

    yield todo

    db.delete(todo.id)
