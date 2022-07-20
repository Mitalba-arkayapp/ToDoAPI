from sqlalchemy import  Boolean,Column,Integer,String
from database import Base

class ToDos(Base):
    __tablename__ = "ToDo"

    id = Column(Integer,primary_key = True,index=True)
    title = Column(String(20))
    complete = Column(Boolean,default=False)

