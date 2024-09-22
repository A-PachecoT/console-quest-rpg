from pydantic import BaseModel, Field
from typing import List

class Character(BaseModel):
    id: int
    name: str
    level: int = Field(default=1, ge=1)
    hp: int = Field(default=100, ge=0)
    max_hp: int = Field(default=100, ge=0)
    attack: int = Field(default=10, ge=1)
    defense: int = Field(default=5, ge=0)
    experience: int = Field(default=0, ge=0)
    inventory: List[str] = Field(default_factory=list)

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "name": "Hero",
                "level": 1,
                "hp": 100,
                "max_hp": 100,
                "attack": 10,
                "defense": 5,
                "experience": 0,
                "inventory": ["Potion", "Sword"]
            }
        }