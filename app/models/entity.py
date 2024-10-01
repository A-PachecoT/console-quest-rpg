from pydantic import BaseModel


class Entity(BaseModel):
    name: str

    level: int = 1

    current_hp: int = 100
    max_hp: int = 100

    attack: int = 10
    defense: int = 5

    is_defendig: bool = False

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
