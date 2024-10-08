from .entity import Entity
from .monster import Monster
from .ability import Ability
from typing import Optional


class Player(Entity):
    xp: int = 0
    target_xp: int = 10
    password: Optional[str] = None

    current_enemy: Optional[Monster] = None

    abilities: Optional[list[Ability]] = []

    class Config:
        allow_population_by_field_name = True
        json_schema_extra = {
            "example": {
                "name": "Hero",
                "password": "123456",
                "level": 1,
                "current_hp": 100,
                "max_hp": 100,
                "attack": 10,
                "defense": 3.5,
                "xp": 0,
                "target_xp": 10,
            }
        }
