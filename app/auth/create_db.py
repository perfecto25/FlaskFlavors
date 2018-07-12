from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine('sqlite:///users.db', echo=True)
Base = declarative_base()

class User(Base):
    
    __tablename__ = "users"

    id = Column(Integer, primary_key = True)
    username = Column(String(64), index = True, unique = True)
    password = Column(String(128))
    email = Column(String(120), index = True, unique = True)
    
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
Base.metadata.create_all(engine)