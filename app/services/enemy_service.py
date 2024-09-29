

from app.models.monster import Monster


class EnemyService:
	
	def GenerateEnemy(playerLevel: int) -> Monster:
		enemy = Monster()
		enemy.GenerateRandomStats(playerLevel);
		return enemy
