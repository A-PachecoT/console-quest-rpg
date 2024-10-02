from app.models.monster import Monster


class EnemyService:
    def GenerateEnemy(self, playerLevel: int) -> Monster:
        enemy = Monster(name="Goblin")
        enemy.GenerateRandomStats(playerLevel)
        return enemy

    def die(self, player: dict) -> dict:
        player["current_enemy"] = None
        return player
