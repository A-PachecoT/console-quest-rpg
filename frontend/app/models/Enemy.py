from .AbstractCharacter import AbstractCharacter

class Enemy(AbstractCharacter):
	
	def __init__(self, id, name, level, hp, maxHp) -> None:
		super().__init__(id, name, level, hp, maxHp)
	
	def Attack(self, target: AbstractCharacter) -> None:
		super().Attack(target)
		pass

