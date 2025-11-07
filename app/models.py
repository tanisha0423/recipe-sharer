from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    
    recipes = relationship("Recipe", back_populates="owner")

class Recipe(Base):
    __tablename__ = "recipes"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(Text)
    ingredients = Column(Text)
    instructions = Column(Text)
    user_id = Column(Integer, ForeignKey("users.id"))
    
    owner = relationship("User", back_populates="recipes")
