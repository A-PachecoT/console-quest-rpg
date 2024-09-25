from pydantic import Field
from .entity import Entity

class Monster(Entity):
    xp_reward: int = Field(default=4, ge=0)
    

    def GenerateRandomStats(self):
        pass

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "name": "Goblin",
                "current_hp": 50,
                "max_hp": 50,
                "attack": 5,
                "defense": 2,
                "xp_reward": 10
            }
        }