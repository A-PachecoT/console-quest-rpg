from pydantic import BaseModel, Field
from typing import List

class Entity(BaseModel):
    id: int
    name: str

    level: int = Field(default=1, ge=1)

    current_hp: int = Field(default=100, ge=0)
    max_hp: int = Field(default=100, ge=0)

    attack: int = Field(default=10, ge=1)
    defense: int = Field(default=5, ge=0)

    def __init__(self, name: str):
        self.name = name

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "name": "Goblin",
                "level": 1,
                "current_hp": 100,
                "max_hp": 100,
                "attack": 10,
                "defense": 5,
            }
        }