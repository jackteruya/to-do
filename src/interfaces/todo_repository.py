from abc import ABC, abstractmethod
from datetime import date


class ToDoRepositoryInterface(ABC):
    """ToDo_ Repository Interface"""

    @abstractmethod
    async def get_by_id(self, id: int):
        """abstractmethod"""
        raise Exception("Method not implemented")

    @abstractmethod
    async def list_todos(self):
        """abstractmethod"""
        raise Exception("Method not implemented")

    @abstractmethod
    async def insert(self, title: str, description: str, completed: bool):
        """abstractmethod"""
        raise Exception("Method not implemented")

    @abstractmethod
    async def edit_todo(
        self,
        id: int,
        title: str,
        description: str,
        completed: bool,
        start_date: date,
        end_date: date,
    ):
        """abstractmethod"""
        raise Exception("Method not implemented")

    @abstractmethod
    async def edit_partial_todo(self, id: int, data: dict):
        """abstractmethod"""
        raise Exception("Method not implemented")

    @abstractmethod
    async def delete(self, id: int):
        """abstractmethod"""
        raise Exception("Method not implemented")
