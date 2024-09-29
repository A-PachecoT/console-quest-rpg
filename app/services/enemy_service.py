from app.models.monster import Monster


class EnemyService:
    def GenerateEnemy(self, playerLevel: int) -> Monster:
        enemy = Monster(name="Goblin")
        enemy.GenerateRandomStats(playerLevel)
        return enemy
