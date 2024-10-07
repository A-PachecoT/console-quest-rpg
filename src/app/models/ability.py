from pydantic import BaseModel


class Ability(BaseModel):
    id: int
    name: str
    description: str
    damage: int
    mana_cost: int

    class Config:
        schema_extra = {
            "example": {
                "name": "Fireball",
                "description": "A ball of fire",
                "damage": 10,
                "mana_cost": 10,
            }
        }
