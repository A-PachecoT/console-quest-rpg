from pydantic import BaseModel, ConfigDict


class Entity(BaseModel):
    name: str

    level: int = 1

    current_hp: float = 100
    max_hp: int = 100

    current_mana: int = 100
    max_mana: int = 100

    attack: int = 10
    defense: float = 5

    is_defending: bool = False

    model_config = ConfigDict(
        json_schema_extra={
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
    )
