from datetime import date

from pydantic import BaseModel


class ToDoUpdateRequest(BaseModel):
    title: str
    description: str
    completed: bool
    start_date: date
    end_date: date