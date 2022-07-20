from pydantic import BaseModel

class ToDos(BaseModel):
    id : int
    title : str
    complete : bool

class ToDoUpdate(BaseModel):
    title : str
    complete : bool



