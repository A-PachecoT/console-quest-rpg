from pydantic import BaseModel, Field

class Monster(BaseModel):
    id: int
    name: str
    current_hp: int = Field(default=50, ge=0)
    max_hp: int = Field(default=50, ge=0)
    attack: int = Field(default=5, ge=1)
    defense: int = Field(default=2, ge=0)
    xp_reward: int = Field(default=10, ge=0)
    gold_reward: int = Field(default=5, ge=0)

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "name": "Goblin",
                "current_hp": 50,
                "attack": 5,
                "defense": 2,
                "xp_reward": 10,
                "gold_reward": 5
            }
        }