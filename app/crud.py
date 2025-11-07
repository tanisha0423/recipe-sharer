from sqlalchemy.orm import Session
from . import models, schemas
from fastapi import HTTPException

# ------------------ User Operations ------------------

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(username=user.username, email=user.email, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db: Session):
    return db.query(models.User).all()

# ------------------ Recipe Operations ------------------

def create_recipe(db: Session, recipe: schemas.RecipeCreate, user_id: int):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    db_recipe = models.Recipe(**recipe.dict(), user_id=user_id)
    db.add(db_recipe)
    db.commit()
    db.refresh(db_recipe)
    return db_recipe

def get_recipes(db: Session):
    return db.query(models.Recipe).all()

def update_recipe(db: Session, recipe_id: int, recipe: schemas.RecipeCreate):
    db_recipe = db.query(models.Recipe).filter(models.Recipe.id == recipe_id).first()
    if not db_recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")
    for key, value in recipe.dict().items():
        setattr(db_recipe, key, value)
    db.commit()
    db.refresh(db_recipe)
    return db_recipe

def delete_recipe(db: Session, recipe_id: int):
    db_recipe = db.query(models.Recipe).filter(models.Recipe.id == recipe_id).first()
    if not db_recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")
    db.delete(db_recipe)
    db.commit()
