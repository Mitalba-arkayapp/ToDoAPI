from ast import In
from sre_constants import IN
from sqlalchemy.orm.session import Session
from fastapi import HTTPException, status

import model,schemas

def get_todo(db:Session,todo_id:int):
    return db.query(model.ToDos).filter(model.ToDos.id==todo_id).first()

def get_todos(db : Session,skip:int=0,limit:int=100):
    return db.query(model.ToDos).offset(skip).limit(limit).all()

def  create_todo(db:Session , todos : schemas.ToDos):
    db_todo = model.ToDos(id=todos.id,title=todos.title)
    if db_todo == db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="use another id."
        )
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

def update_todo(db:Session,todo_id:int, todo: schemas.ToDoUpdate):
    db_todo = get_todo(db, todo_id = todo_id)
    if db_todo is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Todo is not found."
        )
    # db_todo.id = todo.id
    db_todo.title = todo.title
    db_todo.complete = todo.complete
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo
"""
def remove_todo(db:Session,todo_id:int):
    db_todo = get_todo(db, todo_id = todo_id)
    if db_todo is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Todo is not found."
        )
    #db_todo
    db.delete(db_todo)
    db.commit()
    db.refresh(db_todo)
    return 
    # HTTPResponse(status_code=status.HTTP_200_OK,detail="deleted")
"""
    
    
    
def remove_todo(db: Session, todo_id: int):
   todo = db.query(model.ToDos).filter(model.ToDos.id == todo_id).first()
   if todo is None:
    raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Todo is not found."
        )

   db.delete(todo)
   db.commit()
   return {"detail": "TODO Deleted"}