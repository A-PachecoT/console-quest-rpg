from pydantic import BaseModel, Field
from enum import Enum

class ItemType(str, Enum):
    WEAPON = "weapon"
    ARMOR = "armor"
    POTION = "potion"

class Item(BaseModel):
    id: int
    name: str
    type: ItemType
    value: int = Field(default=0, ge=0)
    description: str = ""

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "name": "Steel Sword",
                "type": "weapon",
                "value": 15,
                "description": "A sharp steel sword"
            }
        }