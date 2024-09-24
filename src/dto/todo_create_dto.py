from pydantic import BaseModel


class ToDoCreateRequest(BaseModel):
    title: str
    description: str
