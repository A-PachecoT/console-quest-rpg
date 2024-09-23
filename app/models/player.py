from pydantic import Field
from .entity import Entity
from .monster import Monster

class Player(Entity):
    exp: int = Field(default=0)
    target_exp: int = Field(default=10)

    current_enemy: Monster = Field(default = None)

    def __init__(self, name: str):
        super().__init__(name)

    class Config:
        allow_population_by_field_name = True
        json_schema_extra = {
            "example": {
                "id": 1,
                "name": "Hero",
                "level": 1,
                "current_hp": 100,
                "max_hp": 100,
                "attack": 10,
                "defense": 5,
                "exp": 0,
                "target_exp": 10,
            }
        }
