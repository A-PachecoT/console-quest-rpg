from .entity import Entity
from .monster import Monster
from typing import Optional


class Player(Entity):
    exp: int = 0
    target_exp: int = 10
    password: str

    current_enemy: Optional[Monster] = None

    class Config:
        allow_population_by_field_name = True
        json_schema_extra = {
            "example": {
                "id": 1,
                "name": "Hero",
                "password": "123456",
                "level": 1,
                "current_hp": 100,
                "max_hp": 100,
                "attack": 10,
                "defense": 5,
                "exp": 0,
                "target_exp": 10,
            }
        }
