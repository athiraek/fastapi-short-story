from pydantic import BaseModel

class CharacterBase(BaseModel):
    name: str
    description: str

class CharacterCreate(CharacterBase):
    pass

class Character(CharacterBase):
    id: int

    class Config:
        from_attributes = True  # Updated from `orm_mode` to `from_attributes`

class StoryRequest(BaseModel):
    character_id: int
