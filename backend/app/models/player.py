from pydantic import BaseModel, Field
from typing import Optional

class Player(BaseModel):
    id: Optional[str] = Field(default=None, alias="_id")
    name: str
    level: int = Field(default=1)
    hp: int = Field(default=100)
    max_hp: int = Field(default=100)
    exp: int = Field(default=0)
    target_exp: int = Field(default=10)
    gold: int = Field(default=0)

    class Config:
        allow_population_by_field_name = True
        json_schema_extra = {
            "example": {
                "name": "Hero",
                "level": 1,
                "hp": 100,
                "max_hp": 100,
                "exp": 0,
                "target_exp": 10,
                "gold": 0
            }
        }
