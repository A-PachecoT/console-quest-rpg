import AbstractCharacter
from pydantic import BaseModel, Field

class Player(AbstractCharacter, BaseModel):
	
	_id: int

	_exp: int = Field(default=0, ge=0)
	_targetExp: int = Field(default=100, ge=0)
	_gold: int = Field(default=0, ge=0)

	def __init__(self, id, name, level, hp, maxHp, exp, targetExp, gold) -> None:
		super().__init__(id, name, level, hp, maxHp)
		self._exp = exp
		self._targetExp = targetExp
		self._gold = gold

	def LevelUp(self) -> None:
		self._level += 1
		self._maxHp += 10
		self._hp = self._maxHp
		self._targetExp *= 0.1 
	
	def GainExp(self, exp: int) -> None:
		self._exp += exp
		if self._exp >= self._targetExp:
			self.LevelUp()
			self._exp = 0
	
	def Attack(self, target: AbstractCharacter) -> None:
		pass

	def GetId(self) -> int:
		return self._id
	def GetExp(self) -> int:
		return self._exp
	def GetTargetExp(self) -> int:
		return self._targetExp
	def GetGold(self) -> int:
		return self._gold



