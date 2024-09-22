import AbstractCharacter
from pydantic import BaseModel, Field

class Enemy(AbstractCharacter, BaseModel):
	
	def __init__(self, id, name, level, hp, maxHp) -> None:
		super().__init__(id, name, level, hp, maxHp)
	
	def Attack(self, target: AbstractCharacter) -> None:
		super().Attack(target)
		pass

