from datetime import date

from sqlalchemy import select, update, delete

from src.infra.database.entities import ToDo
from src.interfaces.todo_repository import ToDoRepositoryInterface


class ToDoRepository(ToDoRepositoryInterface):
    """ToDo_ Repository"""

    def __init__(self, db_connection):
        self.__db_connection = db_connection

    def get_by_id(self, id: int):
        try:
            with self.__db_connection() as db_connection:
                todo = db_connection.session.query(ToDo).filter_by(id=id).first()
                return todo
        except Exception as ex:
            return None

    def list_todos(self):
        try:
            with self.__db_connection() as db_connection:
                todo = db_connection.session.scalars(
                    select(ToDo).order_by(ToDo.id)
                )
                return todo.all()
        except Exception as ex:
            return None

    def insert(self, title: str, description: str, completed: bool):
        try:
            with self.__db_connection() as db_connection:
                new_todo = ToDo(
                    title=title,
                    description=description,
                    completed=completed
                )
                db_connection.session.add(new_todo)
                db_connection.session.commit()
                db_connection.session.refresh(new_todo)
            return new_todo
        except Exception as ex:
            return None

    def edit_todo(self, id: int, title: str, description: str, completed: bool, start_date: date, end_date: date):
        try:
            with self.__db_connection() as db_connection:
                todo = update(ToDo).where(ToDo.id == id).values(
                    title=title,
                    description=description,
                    completed=completed,
                    start_date=start_date,
                    end_date=end_date
                )
                db_connection.session.execute(todo)
                db_connection.session.commit()
                return True
        except Exception as ex:
            return None

    def edit_partial_todo(self, id: int, data: dict):
        try:
            with self.__db_connection() as db_connection:
                todo = update(ToDo).where(ToDo.id == id).values(
                    **data
                )
                db_connection.session.execute(todo)
                db_connection.session.commit()
            return True
        except Exception as ex:
            return None

    def delete(self, id: int):
        try:
            with self.__db_connection() as db_connection:
                todo = delete(ToDo).where(ToDo.id == id)
                db_connection.session.execute(todo)
                db_connection.session.commit()
        except Exception as ex:
            return None
