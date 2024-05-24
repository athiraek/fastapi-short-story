from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from supabase import create_client, Client
import openai
import os
from dotenv import load_dotenv

load_dotenv()

# Supabase configuration
supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(supabase_url, supabase_key)

# OpenAI configuration
openai.api_key = os.getenv("OPENAI_API_KEY")

# FastAPI app
app = FastAPI()

# Pydantic models
class CharacterCreate(BaseModel):
    name: str
    description: str

class StoryRequest(BaseModel):
    character_id: int

@app.post("/api/create_character", status_code=201)
def create_character(character: CharacterCreate):
    response = supabase.table('characters').insert({
        "name": character.name,
        "description": character.description
    }).execute()
    
    if response.status_code != 201:
        raise HTTPException(status_code=400, detail="Failed to create character")
    
    return response.data[0]

@app.post("/api/generate_story", status_code=201)
def generate_story(story_request: StoryRequest):
    response = supabase.table('characters').select("*").eq("id", story_request.character_id).execute()
    if response.status_code != 200 or not response.data:
        raise HTTPException(status_code=404, detail="Character not found")
    
    character = response.data[0]
    story = openai.Completion.create(
        engine="davinci",
        prompt=f"Write a short story (4 to 5 sentences) about {character['name']}. {character['description']}",
        max_tokens=100
    ).choices[0].text.strip()
    
    return {"story": story}
