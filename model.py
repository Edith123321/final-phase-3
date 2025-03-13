# This is the model file that defines the models, tables and relationships
# My project is a task management system that allows the users to track and update their tasks dynamically
# One user can have many task, one task can only belong to one category, one task can have many users

from sqlalchemy import Column, Integer, String, create_engine, Boolean, ForeignKey, Boolean, DateTime
from sqlalchemy.orm import  relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()


Base = declarative_base()
engine = create_engine("sqlite:///tasks.db")

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key = True)
    name = Column (String(50), nullable = False)
    email = Column(String(100), nullable = False, unique = True)

    tasks = relationship("Task", back_populates = "user")

class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key = True)
    name = Column(String(50), nullable = False, unique = True)

    tasks  = relationship("Task", back_populates = 'categories')

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    due_date = Column(DateTime, nullable=True)
    priority = Column(String, nullable=False, default="Medium")
    completed = Column(Boolean, default=False)

    user_id = Column(Integer, ForeignKey("users.id"))
    category_id = Column(Integer, ForeignKey("categories.id"))
    
    user = relationship("User", back_populates = "tasks")
    categories = relationship("Category", back_populates = "tasks")



Session = sessionmaker(bind=engine)
session = Session()

     






