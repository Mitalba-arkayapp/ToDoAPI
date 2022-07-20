from fastapi  import Depends, FastAPI, HTTPException
from sqlalchemy.orm.session import Session

import crud,model,schemas
from database import SessionLocal,engine

model.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return{"hello":"wrold"}

@app.post("/todos/")
def create_todo(todos:schemas.ToDos,db:Session=Depends(get_db)):
    return crud.create_todo(db=db,todos=todos)
    

@app.get("/todos")
def read_todo(skip:int=0,limit:int=100,db:Session=Depends(get_db)):
    return crud.get_todos(db=db,skip=skip,limit=limit)

@app.get("/todos/{todo_id}")
def read_todo_by_id(todo_id:int,db:Session=Depends(get_db)):
    db_todo = crud.get_todo(todo_id=todo_id,db=db)
    if db_todo is None:
        raise HTTPException(status_code=404, detail="ToDo not found")
    return db_todo


@app.put("/todos/{todo_id}")
def update_todos(todo_id:int,todo:schemas.ToDoUpdate,db:Session=Depends(get_db)):
    return crud.update_todo(db=db,todo_id=todo_id,todo=todo)

@app.delete("/todos/{todo_id}")
def remove_todos(todo_id:int,db:Session=Depends(get_db)):
    return crud.remove_todo(db=db,todo_id=todo_id)

