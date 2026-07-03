from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Users(Base):
    __tablename__="Users"
    
    id = Column(Integer, primary_key=True, index=True)
    name=Column(String, nullable=False)
    email=Column(String)
    password=Column(String)
    
    notes = relationship("Notes", back_populates="owner")

    
class Notes(Base):
    __tablename__="Notes"
    
    id=Column(Integer, primary_key=True, index=True)
    title= Column(String)
    content=Column(String)
    owner_id = Column(Integer, ForeignKey("Users.id"))

    owner = relationship("Users", back_populates="notes")
    
    
    