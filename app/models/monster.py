import random
from pydantic import Field
from .entity import Entity


class Monster(Entity):
    xp_reward: int = Field(default=4, ge=0)

    def GenerateRandomStats(self, playerLevel: int):
        minLevel = 1 if playerLevel < 2 else playerLevel - 1
        self.level = random.randint(minLevel, playerLevel + 1)
        self.max_hp = random.randint(50, 100) * self.level
        self.current_hp = self.max_hp
        self.attack = random.randint(5, 10) * self.level
        self.defense = random.randint(1, 3) * self.level
        self.xp_reward = self.level * 4

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "name": "Goblin",
                "current_hp": 50,
                "max_hp": 50,
                "attack": 5,
                "defense": 2,
                "xp_reward": 10,
            }
        }
