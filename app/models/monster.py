import random
from pydantic import Field, ConfigDict
from .entity import Entity
from app.utils.logger import monster_logger


class Monster(Entity):
    xp_reward: int = Field(default=4, ge=0)

    def GenerateRandomStats(self, playerLevel: int):
        minLevel = 1 if playerLevel < 2 else playerLevel - 1
        self.level = random.randint(minLevel, playerLevel + 1)
        self.max_hp = random.randint(50, 100) * self.level
        self.current_hp = self.max_hp
        self.attack = random.randint(3, 6) * self.level
        self.defense = (random.random() * 1.5 + 0.5) * self.level
        self.xp_reward = self.level * 4
        monster_logger.info(f"Generated monster: {self.name} (Level {self.level})")
        monster_logger.info(f"  HP: {self.current_hp}/{self.max_hp}")
        monster_logger.info(f"  Attack: {self.attack}")
        monster_logger.info(f"  Defense: {self.defense}")
        monster_logger.info(f"  XP Reward: {self.xp_reward}")

    model_config = ConfigDict(
        json_schema_extra={
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
    )
