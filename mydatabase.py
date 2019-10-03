import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class USER(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True, nullable=False )
    name = Column(String(250), nullable=False, unique = True)
    email = Column(String(250), nullable=False, unique = True)
    password = Column(String(250), nullable=False)

class SESSIONS(Base):
    __tablename__ = 'sessions'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    logintime = Column(String(250))
    logouttime = Column(String(250))
    user_id = Column(Integer, ForeignKey('user.id'))
    DATA = relationship(USER)

# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
engine = create_engine('sqlite:///sqlalchemy_example.db')

# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)
