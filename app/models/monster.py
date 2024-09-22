from pydantic import BaseModel, Field

class Monster(BaseModel):
    id: int
    name: str
    hp: int = Field(default=50, ge=0)
    attack: int = Field(default=5, ge=1)
    defense: int = Field(default=2, ge=0)
    experience_reward: int = Field(default=10, ge=0)

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "name": "Goblin",
                "hp": 50,
                "attack": 5,
                "defense": 2,
                "experience_reward": 10
            }
        }