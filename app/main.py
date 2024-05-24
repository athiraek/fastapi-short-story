from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas, openai_client
from .database import SessionLocal, engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Short Story API"}

@app.post("/characters/", response_model=schemas.Character)
def create_character(character: schemas.CharacterCreate, db: Session = Depends(get_db)):
    return crud.create_character(db=db, character=character)

@app.get("/characters/", response_model=list[schemas.Character])
def read_characters(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_characters(db=db, skip=skip, limit=limit)

@app.get("/characters/{character_id}", response_model=schemas.Character)
def read_character(character_id: int, db: Session = Depends(get_db)):
    db_character = crud.get_character(db=db, character_id=character_id)
    if db_character is None:
        raise HTTPException(status_code=404, detail="Character not found")
    return db_character

@app.post("/generate_story/")
def generate_story(story_request: schemas.StoryRequest, db: Session = Depends(get_db)):
    db_character = crud.get_character(db=db, character_id=story_request.character_id)
    if db_character is None:
        raise HTTPException(status_code=404, detail="Character not found")
    story = openai_client.generate_story(db_character.name, db_character.description)
    return {"story": story}
