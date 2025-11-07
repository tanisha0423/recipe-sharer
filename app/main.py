from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import SessionLocal, engine
from . import models, schemas, crud
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Recipe Sharing Platform")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React app URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency for DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/", response_model=schemas.User)
def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)

@app.get("/users/", response_model=list[schemas.User])
def list_users(db: Session = Depends(get_db)):
    return crud.get_users(db)

@app.post("/recipes/", response_model=schemas.Recipe)
def create_recipe(recipe: schemas.RecipeCreate, user_id: int, db: Session = Depends(get_db)):
    return crud.create_recipe(db, recipe, user_id)

@app.get("/recipes/", response_model=list[schemas.Recipe])
def list_recipes(db: Session = Depends(get_db)):
    return crud.get_recipes(db)

@app.put("/recipes/{recipe_id}", response_model=schemas.Recipe)
def update_recipe(recipe_id: int, recipe: schemas.RecipeCreate, db: Session = Depends(get_db)):
    return crud.update_recipe(db, recipe_id, recipe)

@app.delete("/recipes/{recipe_id}")
def delete_recipe(recipe_id: int, db: Session = Depends(get_db)):
    crud.delete_recipe(db, recipe_id)
    return {"message": "Recipe deleted successfully"}
